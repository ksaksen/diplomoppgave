import sys
import os
import re

def split_matrix_block(content):
    """
    Finner lange tabeller/matriser i teksten og splitter dem 
    på midten til to uavhengige, kortere tabeller under hverandre.
    """
    # Fanger opp innholdet mellom \begin{array}... og \end{array} eller \begin{aligned}... og \end{aligned}
    pattern = r'\\begin\{(array|aligned)\}(.*?)\\end\{\1\}'
    
    def replacer(match):
        block_inner = match.group(2).strip()
        
        # Finn alle linjer basert på enten doble backslasher (\\) eller rene linjeskift
        # Fjerner tomme linjer
        raw_lines = [line.strip() for line in block_inner.split('\\\\') if line.strip()]
        if not raw_lines:
            # Prøv vanlig linjeskift hvis \\ ikke ble brukt mellom radene
            raw_lines = [line.strip() for line in block_inner.split('\n') if line.strip()]

        clean_lines = []
        for line in raw_lines:
            # Rens unna HTML-entiteter her også for sikkerhets skyld
            cleaned = line.replace("&amp;", "&")
            clean_lines.append(cleaned)

        totalt_antall_rader = len(clean_lines)
        
        # Hvis tabellen har mindre enn 4 rader totalt, er det ingen vits i å splitte den
        if totalt_antall_rader < 4:
            return match.group(0)
            
        # Finn midtpunktet for splittingen
        midtpunkt = (totalt_antall_rader + 1) // 2
        
        tabell1_rader = clean_lines[:midtpunkt]
        tabell2_rader = clean_lines[midtpunkt:]
        
        # Bygg opp de to nye adskilte tabellene med Docusaurus-kompatibel $$ \begin{aligned}
        output = []
        
        output.append("$$\n\\begin{aligned}")
        output.append(" \\\\\n".join(tabell1_rader))
        output.append("\n\\end{aligned}\n$$\n")
        
        output.append("$$\n\\begin{aligned}")
        output.append(" \\\\\n".join(tabell2_rader))
        output.append("\n\\end{aligned}\n$$")
        
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
