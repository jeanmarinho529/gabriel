import os
from css_html_js_minify import css_minify

# List of CSS files in the correct order
CSS_FILES = [
    '.assets/css/custom-bootstrap.css',
    '.assets/css/style.css'
]

# Output files
OUTPUT_CSS = "all-styles.css"
OUTPUT_MIN_CSS = "styles.min.css"

# Combine CSS files in order
combined_css = ''
for fname in CSS_FILES:
    if os.path.exists(fname):
        with open(fname, 'r', encoding='utf-8') as infile:
            combined_css += f'/* {fname} */\n'  # Identification comment
            combined_css += infile.read() + '\n'
    else:
        print(f'[WARNING] File not found: {fname}')

# Optionally, save combined CSS (currently commented out)
# with open(OUTPUT_CSS, "w", encoding="utf-8") as f:
#     f.write(combined_css)

# Minify combined CSS
minified = css_minify(combined_css)

# Save minified CSS
with open(OUTPUT_MIN_CSS, "w", encoding="utf-8") as f:
    f.write(minified)

print("✅ CSS combined and minified successfully!")
