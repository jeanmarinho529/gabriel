import os
from scripts.minify import minify_files_css, minify_files_js
from scripts.release import new_release, delete_files

# List of CSS files in the correct order
FILES_CSS = [
    "./assets/css/custom-bootstrap.css",
    "./assets/css/style.css"
]

OUTPUT_CSS = "./assets/css/all-styles.css"
OUTPUT_MIN_CSS = "./assets/css/styles.min.css"

minify_files_css(FILES_CSS, OUTPUT_MIN_CSS)


# List of JS files in the correct order
FILES_JS = [
    "./assets/js/script.js",
]

OUTPUT_JS = "./assets/js/all-script.js"
OUTPUT_MIN_JS = "./assets/js/script.min.js"

# minify_files_js(FILES_CSS, OUTPUT_MIN_CSS)


IGNORE_TO_COPY = [
    "dev",
    "scripts",
    "excluir",
    ".git",
    ".gitkeep",
    ".gitignore",
    "Makefile",
]

DELETE_FILES = [
    "/poetry.lock",
    "/pyproject.toml",
    "/assets/css/bootstrap.css",
    "/assets/css/custom-bootstrap.css",
    "/assets/css/style.css",
    "/assets/js/script.js",
    "/assets/videos/.gitkeep",
    "/assets/fonts/.gitkeep",
    "/assets/icons/.gitkeep",
    "/assets/images/.gitkeep",
    "/assets/videos/.gitkeep",
]

PATH = os.path.dirname(os.path.abspath(__file__))

RELEASE_PATH = "release"

new_release(
    os.path.dirname(os.path.abspath(__file__)), 
    IGNORE_TO_COPY,
)

delete_files(
    PATH,
    RELEASE_PATH,
    DELETE_FILES
)