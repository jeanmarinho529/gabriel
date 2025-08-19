import os
from css_html_js_minify import css_minify

# List of CSS files in the correct order
CSS_FILES = [
    'assets/css/custom-bootstrap.css',
    'assets/css/style.css'
]

# Output files
OUTPUT_CSS = "all-styles.css"
OUTPUT_MIN_CSS = "styles.min.css"

def combine_files(files: list):
    combined = ''
    for fname in CSS_FILES:
        if os.path.exists(fname):
            with open(fname, 'r', encoding='utf-8') as infile:
                combined += f'/* {fname} */\n'  # Identification comment
                combined += infile.read() + '\n'
        else:
            print(f'[WARNING] File not found: {fname}')
    
    return combined

def minify_files_css(files: list, output_min_file: str = "styles.min.css", output_file: str = ""):
    minified = css_minify(combine_files(CSS_FILES))

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(minified)
    
    with open(output_min_file, "w", encoding="utf-8") as f:
        f.write(minified)

    print("✅ CSS combined and minified successfully!")


def minify_files_js(files: list, output_min_file: str = "styles.min.css", output_file: str = ""):
    minified = css_minify(combine_files(CSS_FILES))

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(minified)
    
    with open(output_min_file, "w", encoding="utf-8") as f:
        f.write(minified)

    print("✅ JS combined and minified successfully!")

minify_files_css(CSS_FILES)