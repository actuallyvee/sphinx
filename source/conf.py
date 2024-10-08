# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import pathlib
import sys
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Documentation'
copyright = '2024, Nhi Pham, Victoria Pham, Jenny Spicer'
author = 'Nhi Pham, Victoria Pham, Jenny Spicer'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


#  add in the extension names to the empty list variable 'extensions'
extensions = [
      'sphinx.ext.autodoc', 
      'sphinx.ext.doctest',
      'sphinx.ext.napoleon', 
      'sphinx.ext.coverage'
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme' # read the docs theme. 
html_static_path = ['_static']
