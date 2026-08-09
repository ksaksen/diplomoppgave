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

    # Trinn 1: Erstatt \tag{x} med \quad (x) for Docusaurus-kompatibilitet
    content = re.sub(r'\s*\\tag\{([^}]+)\}', r' \\quad (\1)', content)

    # Trinn 2: Splitt enkeltlinje-blokkformler ($$ formel $$) til flerlinje-formler
    # Slik at åpnings- og lukkemarkørene ($$) står på egne linjer for GitHub
    pattern_single_line = r'(?m)^\s*\$\$(.+?)\$\$\s*$'

    def split_single_line(match):
        eq = match.group(1).strip()
        return f"$$\n{eq}\n$$"

    content_fixed_lines = re.sub(pattern_single_line, split_single_line, content)

    # Trinn 2: Finn alle $$ ... $$ blokker, pakk dem inn i aligned-miljøet om nødvendig,
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
