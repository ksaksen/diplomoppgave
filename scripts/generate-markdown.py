# ==========================================================
# CELLE 2: STREAMING / SIDE-FOR-SIDE PROSESSERING FOR STORE FILER
# ==========================================================
import os
import time
import warnings
from pdf2image import convert_from_path, pdfinfo_from_path
from google.genai import Client

# Importer alle variablene direkte fra config.py
from config import API_NOEKKEL, pdf_sti, lagrings_sti, START_SIDE

warnings.filterwarnings("ignore", category=SyntaxWarning)

if 'API_NOEKKEL' not in locals() or 'pdf_sti' not in locals():
    raise NameError("FEIL: Du må kjøre den øverste konfigurasjonscellen (Celle 1) først!")

client = Client(api_key=API_NOEKKEL)

try:
    # 1. Finn ut hvor mange sider filen har
    info = pdfinfo_from_path(pdf_sti)
    totalt_antall_sider = info["Pages"]

    print(f"-> Fant en stor fil: {os.path.basename(pdf_sti)}")
    print(f"-> Totalt antall sider i filen: {totalt_antall_sider}")
    print(f"-> Skipper frem og starter fra side {START_SIDE}...")
    print(f"-> Skriver til/oppdaterer fil på Drive: {os.path.basename(lagrings_sti)}")

    if START_SIDE == 1 or not os.path.exists(lagrings_sti):
        with open(lagrings_sti, 'w', encoding='utf-8') as f:
            f.write(f"# Transkripsjon av {os.path.basename(pdf_sti)}\n\n")

    # 2. Gå gjennom sidene i en løkke fra START_SIDE
    for side_nr in range(START_SIDE, totalt_antall_sider + 1):
        print(f"\n[Side {side_nr} av {totalt_antall_sider}] Konverterer til bilde...")

        side_bilde = convert_from_path(pdf_sti, first_page=side_nr, last_page=side_nr)[0]

        midlertidig_bilde_sti = f"./tmp_side_{side_nr}.jpg"
        side_bilde.save(midlertidig_bilde_sti, 'JPEG')

        print(f"[Side {side_nr}] Sender bilde til Gemini...")
        bilde_fil = client.files.upload(file=midlertidig_bilde_sti)

        # Bruker raw-string (r) og doble krøllparenteser for å unngå LaTeX-krash i Python-strengformatering
        instruksjon = rf"""
        Du er en ekspert på halvlederfysikk, kvantemekanikk, Docusaurus MDX og LaTeX/KaTeX-formatering.
        Dette bildet er SIDE {side_nr} fra en diplomoppgave.
        Din jobb er å transkribere siden til helt ren, feilfri Docusaurus-kompatibel Markdown (.md).

        FØLG DISSE REGLENE STRENGT SÅ DOCUSAURUS MDX / KATEX IKKE KRASJER COMPILEREN:

        1. DOCUSAURUS MDX SIKKERHET (KRITISK):
           - Siden Docusaurus bruker MDX, blir rå krøllparenteser '{{' og '}}' i vanlig tekst tolket som JavaScript. Hvis siden inneholder krøllparenteser i vanlig tekst eller kodeeksempler, MÅ de escapes slik: '\{{' og '\}}'. (Unntak: Inni matte-modus som $\vec{{r}}$ skal de IKKE escapes).
           - Mindre-enn og større-enn-tegn ('<' og '>') i vanlig tekst blir tolket som HTML-tags og vil krasje Docusaurus! Du MÅ enten bruke matematiske tegn i dollartegn ($<$ eller $>$) eller erstatte dem med &lt; og &gt; i ren tekst.

        2. MATEMATIKK & FORMELER (KATEX):
           - Bruk ETT enkelt dollartegn ($...$) for inline-matematikk, f.eks. $E_k$, $\epsilon_0$, $m_0$. ALDRI bruk \\( eller \\)!
           - Bruk DOBLE dollartegn ($$...$$) for stående formler (display math).
           - VIKTIG FOR DOCUSAURUS: Det MÅ være en helt TOM LINJE før og etter en $$...$$ blokk. Eksempel:
             
             Teksten her.
             
             $$
             H\\Psi = E\\Psi
             $$
             
             Neste tekstblokk.
           - ALDRI ha mellomrom mellom dollartegnene og innholdet. Skriv $E=mc^2$, IKKE $ E=mc^2 $.
           - Kvantemekanikk (Bra-Ket): Bruk \\langle m | og | j \\rangle. ALDRI bruk uformaterte tegn som |m> eller <m| da '>' og '<' krasjer MDX-parseren fullstendig.

        3. REN TEKST OG STRUKTUR:
           - Rett opp skrivefeil i maskinskriften, men bevar alt faglig innhold nøyaktig.
           - Tekst som "and therefore," skal formateres som vanlig tekst (*and therefore,*), IKKE som en LaTeX-formel ($and therefore,$).

        4. OUTPUT-FORMAT:
           - Pass på at alle $$...$$ blokker er LUKKET før siden slutter.
           - Svar KUN med den rene Markdown-teksten for denne siden. IKKE pakk svaret inn i ```markdown ... ``` kodeblokker.
        """



        # --- RETRY-LOGIKK MOT 503 / NETWORK TIMEOUTS ---
        maks_forsoek = 3
        respons = None

        for forsoek in range(1, maks_forsoek + 1):
            try:
                respons = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=[bilde_fil, instruksjon]
                )
                break  # Vellykket kall, hopp ut av retry-løkken
            except Exception as e:
                print(f"  [Advarsel] Feil på forsøk {forsoek}/{maks_forsoek} for Side {side_nr}: {e}")
                if forsoek < maks_forsoek:
                    ventetid = forsoek * 5  # Venter 5 sek på 1. feil, 10 sek på 2. feil
                    print(f"  Venter {ventetid} sekunder før nytt forsøk...")
                    time.sleep(ventetid)
                else:
                    raise e  # Kast feilen videre dersom alle 3 forsøk feiler

        side_markdown = respons.text.strip()

        if side_markdown.startswith("```markdown"): side_markdown = side_markdown[11:].strip()
        elif side_markdown.startswith("```"): side_markdown = side_markdown[3:].strip()
        if side_markdown.endswith("```"): side_markdown = side_markdown[:-3].strip()

        with open(lagrings_sti, 'a', encoding='utf-8') as f:
            f.write(f"\n\n<!-- START SIDE {side_nr} -->\n")
            f.write(side_markdown)
            f.write(f"\n<!-- SLUTT SIDE {side_nr} -->\n")

        if os.path.exists(midlertidig_bilde_sti):
            os.remove(midlertidig_bilde_sti)

        print(f"[Side {side_nr}] Suksess! Lagt til i filen.")

        # Liten pause på 1 sekund for å unngå å presse rate limits
        time.sleep(1)

    print(f"\n SUKSESS! Sider fra {START_SIDE} til {totalt_antall_sider} er ferdig konvertert og lagret i:\n {lagrings_sti}")

except Exception as e:
    print(f"\n FEIL under prosessering: {str(e)}")