project = 'Tax Documentation'
extensions = []
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

def setup(app):
    app.add_css_file('custom.css')
