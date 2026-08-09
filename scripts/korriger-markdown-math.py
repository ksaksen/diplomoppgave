import sys
import os
import re

def fix_markdown_math(file_path):
    if not os.path.exists(file_path):
        print(f"FEIL: Filen '{file_path}' finnes ikke.")
        sys.exit(1)
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trinn 1: Splitt enkeltlinje-blokkformler ($$ formel $$) til flerlinje-formler
    # Slik at åpnings- og lukkemarkørene ($$) står på egne linjer for GitHub
    pattern_single_line = r'(?m)^\s*\$\$(.+?)\$\$\s*$'
    
    def split_single_line(match):
        eq = match.group(1).strip()
        return f"$$\n{eq}\n$$"
        
    content_fixed_lines = re.sub(pattern_single_line, split_single_line, content)

    # Trinn 2: Finn alle $$ ... $$ blokker og pakk dem inn i \begin{aligned} ... \end{aligned}
    # dersom de inneholder linjeskift (\\) og ikke allerede har et flerlinje-miljø.
    pattern_block = r'(?s)\$\$(.*?)\$\$'
    
    def process_block(match):
        block_content = match.group(1)
        
        # Sjekk om det er et linjeskift (\\) i formelen
        has_line_break = '\\\\' in block_content
        
        # Sjekk om formelen allerede er pakket inn i et flerlinje-miljø
        environments = [
            'aligned', 'align', 'matrix', 'pmatrix', 'bmatrix', 
            'cases', 'array', 'gather', 'split', 'equation'
        ]
        has_env = any(f'\\begin{{{env}}}' in block_content for env in environments)
        
        if has_line_break and not has_env:
            lines = block_content.strip().split('\n')
            # Pakk inn innholdet i aligned-miljøet
            wrapped = ["\\begin{aligned}"] + lines + ["\\end{aligned}"]
            return f"$$\n" + "\n".join(wrapped) + "\n$$"
        else:
            # Returner uforandret (men med normaliserte linjeskift rundt $$)
            return f"$$\n{block_content.strip()}\n$$"

    final_content = re.sub(pattern_block, process_block, content_fixed_lines)

    # Skriv oppdatert innhold tilbake til filen
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print(f"Suksess! Korrigerte matematikk-formateringen i: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Bruk: python3 korriger-markdown-math.py <sti_til_markdown_fil>")
        sys.exit(1)
        
    fix_markdown_math(sys.argv[1])
