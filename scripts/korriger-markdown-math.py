import sys
import os
import re

def parse_and_format_raw_data(content):
    """
    Fanger opp de lange, horisontale rådatastringene med fysikk-parametere
    og gjør dem om til ekte, strukturerte Markdown-tabeller med to kolonner.
    """
    # Regex som finner linjer som starter med et tall, inneholder "E(s,c)" og slutter med "in Angstrom"
    # Dette matcher de lange rådatastringene dine uansett om det er rotete linjeskift i dem fra før.
    pattern = r'(-?\d+\.\d+\s+E\(s\s*,\s*c\).*?d=bondlength in Angstrom)'
    
    matches = re.findall(pattern, content, re.DOTALL)
    if not matches:
        return content

    for i, match in enumerate(matches):
        # Rens teksten og lag en ren liste med ord/tall
        tokens = match.replace("\n", " ").split()
        
        # Vi skal parre sammen tallene og symbolene
        # Eksempel på par: ["E(s,c)", "-2.7219"]
        pairs = []
        
        # Gå gjennom tokens for å finne verdi + symbol par
        j = 0
        while j < len(tokens):
            token = tokens[j]
            
            # Sjekk om det er et tall (verdi)
            if re.match(r'^-?\d+\.\d+$', token):
                verdi = token
                # Sjekk om neste token er et symbol (f.eks. E(s,c) eller V(s,s))
                if j + 1 < len(tokens) and ('E(' in tokens[j+1] or 'V(' in tokens[j+1]):
                    symbol = tokens[j+1]
                    # Normaliser s* og sp3s* så det blir pen inline LaTeX
                    symbol = symbol.replace("s*", "s^*").replace("s^*a", "s^*_a").replace("s^*c", "s^*_c")
                    pairs.append((f"${symbol}$", verdi))
                    j += 2
                    continue
            # Fang opp bondlength til slutt
            if token == "d=bondlength":
                # Finn verdien som kom rett før (f.eks. 2.62)
                if pairs:
                    last_val = tokens[j-1]
                    # Hvis forrige token var et rent tall, var det sannsynligvis bondlength-verdien
                    if re.match(r'^\d+\.\d+$', last_val):
                        # Fjern den feilaktige forrige parringen hvis den tok verdien til bondlength
                        if pairs[-1][1] == last_val:
                            pairs.pop()
                        pairs.append(("$d$ (bond length)", f"{last_val} Å"))
            j += 1

        if not pairs:
            continue

        # Bygg en kjempefin Markdown-tabell for Docusaurus
        tittel = "**InAs Matriseelementer**" if i == 0 else "**GaSb Matriseelementer**"
        
        table_md = []
        table_md.append(f"\n### {tittel}\n")
        table_md.append("| Element / Parameter | Verdi (eV) |")
        table_md.append("| :--- | :--- |")
        for sym, val in pairs:
            table_md.append(f"| {sym} | {val} |")
        table_md.append("\n")
        
        formatted_table = "\n".join(table_md)
        content = content.replace(match, formatted_table)

    return content

def fix_markdown_math(file_path):
    if not os.path.exists(file_path):
        print(f"FEIL: Filen '{file_path}' finnes ikke.")
        sys.exit(1)
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normaliser linjeskift til standard unix \n for pålitelig regex-matching
    content = content.replace("\r\n", "\n")

    # =========================================================================
    # TRINN 1: RESTRUKTURERING AV RÅDATA TIL EKTE TABELLER (NY)
    # =========================================================================
    content = parse_and_format_raw_data(content)

    # 1. Erstatt HTML-entiteter som &amp; inni formler med ekte tegn
    content = content.replace("&amp;", "&")

    # 2. Fiks den ødelagte "s^_" og "s^_a" syntaksen til korrekt s-stjerne LaTeX
    content = content.replace("s^_-", "s^*")
    content = content.replace("s^_", "s^*")
    content = content.replace("s^*_a", "s^*_a")

    # 3. Fiks feilformaterte orbitalnavn i ren tekst (f.eks. sp3s* eller s p 3 s *)
    content = re.sub(r'\bsp3s\s*\*+', r'$sp^3s^*$', content)
    content = re.sub(r'\bsp3s\s*\^\*', r'$sp^3s^*$', content)
    content = re.sub(r'\bs\s+p\s+3\s+s\s*\*+', r'$sp^3s^*$', content)

    # =========================================================================
    # TRADISJONELLE TRINN
    # =========================================================================
    content = re.sub(r'\s*\\tag\{([^}]+)\}', r' \\quad (\1)', content)

    def fix_caret_star(math_content):
        protected = math_content.replace('^{\\ast}', '\x00CARET_STAR\x00')
        fixed = protected.replace('^{*}', '^{\\ast}').replace('^*', '^{\\ast}')
        return fixed.replace('\x00CARET_STAR\x00', '^{\\ast}')

    content = re.sub(
        r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)',
        lambda m: '$' + fix_caret_star(m.group(1)) + '$',
        content,
        flags=re.DOTALL
    )

    pattern_single_line = r'(?m)^\s*\$\$(.+?)\$\$\s*$'
    def split_single_line(match):
        eq = match.group(1).strip()
        return f"$$\n{eq}\n$$"

    content_fixed_lines = re.sub(pattern_single_line, split_single_line, content)

    pattern_block = r'(?s)\$\$(.*?)\$\$'
    def process_block(match):
        block_content = match.group(1).strip()
        has_line_break = '\\\\' in block_content
        environments = [
            'aligned', 'align', 'matrix', 'pmatrix', 'bmatrix', 
            'cases', 'array', 'gather', 'split', 'equation'
        ]
        has_env = any(f'\\begin{{{env}}}' in block_content for env in environments)
        
        if has_line_break and not has_env:
            lines = block_content.split('\n')
            wrapped = ["\\begin{aligned}"] + lines + ["\\end{aligned}"]
            block_content = "\n".join(wrapped)

        block_content = fix_caret_star(block_content)
        return f"\n\n$$\n{block_content}\n$$\n\n"

    final_content = re.sub(pattern_block, process_block, content_fixed_lines)

    final_content = re.sub(r'\n{3,}', '\n\n', final_content)
    final_content = final_content.strip() + '\n'

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print(f"Suksess! Genererte ekte tabeller ut av rådatablokkene i: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Bruk: python3 korriger-markdown-math.py <sti_til_markdown_fil>")
        sys.exit(1)
        
    fix_markdown_math(sys.argv[1])
