import os, sys
sys.path.insert(0, os.path.abspath(".."))
project = "Your Project"
author = "Your Name"
release = "0.1.0"
extensions = ["sphinx.ext.autodoc","sphinx.ext.napoleon","sphinx.ext.viewcode"]
templates_path = ["_templates"]
exclude_patterns = []
html_theme = "sphinx_rtd_theme"
