# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = 'LABsystem'
copyright = '2025, Giuseppe Iuliano'
author = 'Giuseppe Iuliano'
release = '1.0.0'
version = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',
]

# Support for Markdown files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
# html_logo = '_static/logo.png'  # ← Logo commentato/rimosso
html_favicon = None

# Theme options
html_theme_options = {
    'logo_only': False,  # ← Rimesso a False dato che non c'è più il logo
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 3,
    'includehidden': True,
    'titles_only': False
}

# MyST parser settings
myst_enable_extensions = [
    "colon_fence",
]
