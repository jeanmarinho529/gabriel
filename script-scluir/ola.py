import os

from css_html_js_minify import css_minify

# Lista de arquivos CSS na ordem correta
CSS_FILES = [
    'assets/css/custom-bootstrap.css',
    'assets/css/style.css'
]

# Arquivos de saída
OUTPUT_CSS = "all-styles.css"
OUTPUT_MIN_CSS = "styles.min.css"

# Junta os arquivos CSS na ordem
combined_css = ''
for fname in CSS_FILES:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as infile:
            combined_css += f'/* {fname} */\n'  # Comentário de identificação
            combined_css += infile.read() + '\n'
    else:
        print(f'[AVISO] Arquivo não encontrado: {fname}')

# with open(OUTPUT_CSS, "w", encoding="utf-8") as f:
#     f.write(combined_css)

minified = css_minify(combined_css)

with open(OUTPUT_MIN_CSS, "w", encoding="utf-8") as f:
    f.write(minified)

print("✅ CSS combinado e minificado com sucesso!")