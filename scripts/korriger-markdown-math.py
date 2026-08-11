import sys
import os
import re

def parse_and_format_raw_data(content):
    """
    Fanger opp de vertikalt eller horisontalt ødelagte datablokkene med fysikk-parametere
    og gjør dem om til ekte, to-kolonners Markdown-tabeller.
    """
    # Regex som ser etter det første desimaltallet, fulgt av tegn frem til bondlength-strengen.
    # [re.DOTALL] sikrer at den leser på tvers av alle merkelige linjeskift.
    pattern = r'(-?\d+\.\d+.*?d\s*=\s*bondlength\s+in\s+Angstrom)'
    
    def replacer(match):
        raw_block = match.group(1)
        
        # TRINN A: Normaliser blokken til én lang linje ved å kollapse alle linjeskift
        clean_block = re.sub(r'\s+', ' ', raw_block)
        
        # TRINN B: Fjern alle uønskede mellomrom inni E( ... ) og V( ... )
        # Dette fikser de loddrette 'E \n ( \n s ...' splitte-feilene fra AI-en!
        clean_block = re.sub(r'([EV])\s*\(\s*([^)]+?)\s*\)', lambda m: m.group(1) + "(" + m.group(2).replace(" ", "") + ")", clean_block)
        
        # Splitt ut alle tokens (ord og tall)
        tokens = clean_block.replace("in Angstrom", "").replace("d=bondlength", "").split()
        
        pairs = []
        val_pattern = r'^-?\d+\.\d+$'
        bond_val = None
        
        j = 0
        while j < len(tokens):
            token = tokens[j]
            
            # Hvis vi finner et desimaltall
            if re.match(val_pattern, token):
                # Sjekk om neste token er et gyldig renset matriseelement
                if j + 1 < len(tokens) and ('E(' in tokens[j+1] or 'V(' in tokens[j+1]):
                    verdi = token
                    symbol = tokens[j+1]
                    
                    # Sikre vakker LaTeX-formatering for Docusaurus/GitHub ($s^*$)
                    symbol = symbol.replace("s*", "s^*").replace("s*a", "s^*_a").replace("s*c", "s^*_c")
                    symbol = symbol.replace("∗", "^*") # Fanger opp spesielle stjerne-tegn
                    pairs.append((f"${symbol}$", verdi))
                    j += 2
                    continue
                else:
                    # Hvis tallet står alene til slutt, er det bondlength-verdien
                    bond_val = token
            j += 1
            
        if not pairs:
            return raw_block # Returner uendret hvis ingen struktur ble funnet
            
        # Bestem tabelltittel dynamisk basert på kontekst i rådataen
        tittel = "Matriseelementer"
        if "InAs" in raw_block:
            tittel = "InAs Matriseelementer"
        elif "GaSb" in raw_block:
            tittel = "GaSb Matriseelementer"
            
        # Bygg opp den endelige Markdown-tabellen
        table_md = [
            f"\n### {tittel}",
            "| Element / Parameter | Verdi (eV) |",
            "| :--- | :--- |"
        ]
        for sym, val in pairs:
            table_md.append(f"| {sym} | {val} |")
        if bond_val:
            table_md.append(f"| $d$ (bond length) | {bond_val} Å |")
        table_md.append("\n")
        
        return "\n".join(table_md)

    return re.sub(pattern, replacer, content, flags=re.DOTALL)

def fix_markdown_math(file_path):
    if not os.path.exists(file_path):
        print(f"FEIL: Filen '{file_path}' finnes ikke.")
        sys.exit(1)
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normaliser alle linjeskift til standard Unix \n
    content = content.replace("\r\n", "\n")

    # 1. Kjør den globale restruktureringen av rådatablokkene
    content = parse_and_format_raw_data(content)

    # 2. Generelle KaTeX-sikkerhetsjusteringer
    content = content.replace("&amp;", "&")
    content = re.sub(r'\bsp3s\s*\*+', r'$sp^3s^*$', content)
    content = re.sub(r'\bsp3s\s*\^\*', r'$sp^3s^*$', content)
    content = re.sub(r'(?m)^\s*\$\$(.+?)\$\$\s*$', r"$$\n\1\n$$", content)

    # 3. Fjern unødvendig store mengder tomme linjer
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = content.strip() + '\n'

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Suksess! Genererte ekte tabeller ut av rådatastringene i: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Bruk: python3 korriger-markdown-math.py <sti_til_markdown_fil>")
        sys.exit(1)
        
    # Hent KUN argument nummer 1 (den spesifikke filbanen du oppgir) for å unngå cover.md-feil!
    target_file = sys.argv[1]
    fix_markdown_math(target_file)
