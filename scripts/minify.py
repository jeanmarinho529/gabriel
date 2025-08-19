import os
from css_html_js_minify import css_minify, js_minify


def combine_files(files: list):
    combined = ''
    for fname in files:
        if os.path.exists(fname):
            with open(fname, 'r', encoding='utf-8') as infile:
                combined += f'/* {fname} */\n'  # Identification comment
                combined += infile.read() + '\n'
        else:
            print(f'[WARNING] File not found: {fname}')
    
    return combined

def minify_files_css(files: list, output_min_file: str = "styles.min.css", output_file: str = ""):
    minified = css_minify(combine_files(files))

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(minified)
    
    with open(output_min_file, "w", encoding="utf-8") as f:
        f.write(minified)

    print("✅ CSS combined and minified successfully!")


def minify_files_js(files: list, output_min_file: str = "scripts.min.js", output_file: str = ""):
    minified = js_minify(combine_files(files))

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(minified)
    
    with open(output_min_file, "w", encoding="utf-8") as f:
        f.write(minified)

    print("✅ JS combined and minified successfully!")
