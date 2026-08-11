import sys
import os
import re

def fix_markdown_math(file_path):
    if not os.path.exists(file_path):
        print(f"FEIL: Filen '{file_path}' finnes ikke.")
        sys.exit(1)
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normaliser linjeskift til standard unix \n for pålitelig regex-matching
    content = content.replace("\r\n", "\n")

    # =========================================================================
    # NYTT TRINN: STRUKTURELL RENSING (FØR MATEMATIKK-PROSESSERING)
    # =========================================================================
    
    # 1. Erstatt HTML-entiteter som &amp; inni formler med ekte tegn
    content = content.replace("&amp;", "&")

    # 2. Fiks den ødelagte "s^_" og "s^_a" syntaksen til korrekt s-stjerne LaTeX
    content = content.replace("s^_-", "s^*")
    content = content.replace("s^_", "s^*")
    content = content.replace("s^*_a", "s^*_a") # Bevarer indeks om nødvendig

    # 3. Fiks feilformaterte orbitalnavn i ren tekst (f.eks. sp3s* eller s p 3 s *)
    # Endrer "sp3s*" eller "sp3s^*" til pen inline LaTeX: $sp^3s^*$
    content = re.sub(r'\bsp3s\s*\*+', r'$sp^3s^*$', content)
    content = re.sub(r'\bsp3s\s*\^\*', r'$sp^3s^*$', content)
    content = re.sub(r'\bs\s+p\s+3\s+s\s*\*+', r'$sp^3s^*$', content)

    # =========================================================================
    # TRADISJONELLE TRINN (OPPDATERT)
    # =========================================================================

    # Trinn 1: Erstatt \tag{x} med \quad (x) for Docusaurus-kompatibilitet
    content = re.sub(r'\s*\\tag\{([^}]+)\}', r' \\quad (\1)', content)

    # Trinn 2: Erstatt naken ^* med ^{*} overalt i all matematikk ($...$ og $$...$$)
    def fix_caret_star(math_content):
        # Beskytt allerede innpakkede ^{\ast} med en placeholder
        protected = math_content.replace('^{\\ast}', '\x00CARET_STAR\x00')
        # Erstatt alle gjenværende nakne ^* og ^{*} med ^{\ast}
        fixed = protected.replace('^{*}', '^{\\ast}').replace('^*', '^{\\ast}')
        # Gjenopprett placeholder
        return fixed.replace('\x00CARET_STAR\x00', '^{\\ast}')

    # Fiks i inline $...$ (ikke $$) — negativ lookbehind/ahead for å unngå $$
    content = re.sub(
        r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)',
        lambda m: '$' + fix_caret_star(m.group(1)) + '$',
        content,
        flags=re.DOTALL
    )

    # Trinn 2b: Splitt enkeltlinje-blokkformler ($$ formel $$) til flerlinje-formler
    pattern_single_line = r'(?m)^\s*\$\$(.+?)\$\$\s*$'

    def split_single_line(match):
        eq = match.group(1).strip()
        return f"$$\n{eq}\n$$"

    content_fixed_lines = re.sub(pattern_single_line, split_single_line, content)

    # Trinn 2c: Finn alle $$ ... $$ blokker, pakk dem inn i aligned-miljøet om nødvendig,
    # og sørg for at de er polstret med tomme linjer før og etter seg.
    pattern_block = r'(?s)\$\$(.*?)\$\$'
    
    def process_block(match):
        block_content = match.group(1).strip()
        
        # Sjekk om det er et linjeskift (\\) i formelen
        has_line_break = '\\\\' in block_content
        
        # Sjekk om formelen allerede er pakket inn i et flerlinje-miljø
        environments = [
            'aligned', 'align', 'matrix', 'pmatrix', 'bmatrix', 
            'cases', 'array', 'gather', 'split', 'equation'
        ]
        has_env = any(f'\\begin{{{env}}}' in block_content for env in environments)
        
        if has_line_break and not has_env:
            lines = block_content.split('\n')
            # Pakk inn innholdet i aligned-miljøet
            wrapped = ["\\begin{aligned}"] + lines + ["\\end{aligned}"]
            block_content = "\n".join(wrapped)

        # Pakk inn naken ^* i klammeparenteser (^{*}) for KaTeX/Docusaurus
        block_content = fix_caret_star(block_content)

        # Returner formelen omgitt av doble linjeskift (som blir komprimert senere)
        return f"\n\n$$\n{block_content}\n$$\n\n"

    final_content = re.sub(pattern_block, process_block, content_fixed_lines)

    # Trinn 3: Komprimer alle sekvenser av 3 eller flere påfølgende linjeskift 
    # til nøyaktig 2 linjeskift (som representerer nøyaktig én blank linje).
    final_content = re.sub(r'\n{3,}', '\n\n', final_content)
    
    # Fjern eventuelle ledende/trailende linjeskift i hele dokumentet
    final_content = final_content.strip() + '\n'

    # Skriv oppdatert innhold tilbake til filen
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print(f"Suksess! Korrigerte matematikk-formateringen og linjeavstand i: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Bruk: python3 korriger-markdown-math.py <sti_til_markdown_fil>")
        sys.exit(1)
        
    fix_markdown_math(sys.argv[1])
