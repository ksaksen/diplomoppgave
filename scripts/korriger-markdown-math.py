import sys
import os
import re

def split_matrix_block(content):
    """
    Finner tabeller/matriser i teksten og splitter rader som har 
    mange elementer inn i to adskilte, renere tabeller.
    """
    # Regex som fanger opp innholdet mellom \begin{array}... og \end{array} 
    # eller \begin{aligned}... og \end{aligned}
    pattern = r'\\begin\{(array|aligned)\}(.*?)\\end\{\1\}'
    
    def replacer(match):
        env_type = match.group(1)
        block_inner = match.group(2).strip()
        
        # Splitter innholdet inn i enkeltlinjer
        lines = [line.strip() for line in block_inner.split('\\\\') if line.strip()]
        
        tabell1_rader = []
        tabell2_rader = []
        
        for line in lines:
            # Fjern eventuelle HTML-entiteter som har overlevd
            line = line.replace('&amp;', '&')
            
            # Splitter linjen på '&' tegnene for å isolere elementene
            # En typisk ødelagt linje ser ut som: E(s, b) & = verdi1 & E(p, b) & = verdi2
            parts = [p.strip() for p in line.split('&') if p.strip()]
            
            # Hvis linjen inneholder nok elementer til å splittes i to par (f.eks. symbol1, verdi1, symbol2, verdi2)
            if len(parts) >= 4:
                # Første tabell får de to første elementene (f.eks. "E(s, b)" og "= verdi1")
                tabell1_rader.append(f"{parts[0]} & {parts[1]}")
                # Andre tabell får de to neste elementene (f.eks. "E(p, b)" og "= verdi2")
                tabell2_rader.append(f"{parts[2]} & {parts[3]}")
            elif len(parts) >= 2:
                # Hvis linjen er kort, legger vi den bare i den første tabellen
                tabell1_rader.append(f"{parts[0]} & {parts[1]}")
        
        # Hvis vi ikke klarte å splitte noen rader, returnerer vi bare originalen uforandret
        if not tabell2_rader:
            return match.group(0)
            
        # Konstruer to adskilte, pene aligned-tabeller for Docusaurus
        output = []
        output.append("$$\n\\begin{aligned}")
        output.append(" \\\\\n".join(tabell1_rader))
        output.append("\\end{aligned}\n$$\n")
        
        output.append("$$\n\\begin{aligned}")
        output.append(" \\\\\n".join(tabell2_rader))
        output.append("\\end{aligned}\n$$")
        
        return "\n".join(output)

    return re.sub(pattern, replacer, content, flags=re.DOTALL)

def fix_markdown_math(file_path):
    if not os.path.exists(file_path):
        print(f"FEIL: Filen '{file_path}' finnes ikke.")
        sys.exit(1)
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Normaliser linjeskift til standard unix \n for pålitelig regex-matching
    content = content.replace("\r\n", "\n")

    # =========================================================================
    # TRINN 1: RESTRUKTURERING AV TABELLER (NY)
    # =========================================================================
    content = split_matrix_block(content)

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
        
    print(f"Suksess! Korrigerte matematikk-formateringen og delte matrisene i: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Bruk: python3 korriger-markdown-math.py <sti_til_markdown_fil>")
        sys.exit(1)
        
    fix_markdown_math(sys.argv[1])
