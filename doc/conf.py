# -*- coding: utf-8 -*-
#
# hidimstat documentation build configuration file, created by
# sphinx-quickstart on Thu Jun  1 00:35:01 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys
import warnings
import sphinx_gallery
import sphinx_bootstrap_theme
from distutils.version import LooseVersion
import matplotlib

# Disable agg warnings in doc
warnings.filterwarnings("ignore", category=UserWarning,
                        message='Matplotlib is currently using agg, which is a'
                                ' non-GUI backend, so cannot show the figure.')

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx_gallery.gen_gallery',
    'numpydoc',
]

if LooseVersion(sphinx_gallery.__version__) < LooseVersion('0.2'):
    raise ImportError('Must have at least version 0.2 of sphinx-gallery, got '
                      '%s' % (sphinx_gallery.__version__,))

matplotlib.use('agg')


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'hidimstat'
copyright = u'2020, Jerome-Alexis Chevalier & Binh Nguyen'
author = u'Jerome-Alexis Chevalier & Binh Nguyen'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
from hidimstat import __version__ as version  # noqa
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# generate autosummary even if no references
autosummary_generate = True

# remove warnings: "toctree contains reference to nonexisting document"
numpydoc_show_class_members = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'bootstrap'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'navbar_sidebarrel': False,
    'navbar_pagenav': False,
    'source_link_position': "",
    'navbar_links': [
        ("Examples", "auto_examples/index"),
        ("API", "api"),
        ("GitHub", "https://github.com/ja-che/hidimstat", True)
    ],
    'bootswatch_theme': "flatly",
    'bootstrap_version': "3",
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'hidimstat_doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'hidimstat.tex', u'hidimstat Documentation',
     u'Jerome-Alexis Chevalier', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'hidimstat', u'Hidimstat Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'hidimstat', u'hidimstat Documentation',
     author, 'hidimstat', 'One line description of project.',
     'Miscellaneous'),
]

# -- Intersphinx configuration -----------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/devdocs', None),
    'scipy': ('https://scipy.github.io/devdocs', None),
    'matplotlib': ('https://matplotlib.org', None),
    'sklearn': ('https://scikit-learn.org/stable', None),
    'numba': ('https://numba.pydata.org/numba-doc/latest', None),
    'joblib': ('https://joblib.readthedocs.io/en/latest', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable', None),
    'seaborn': ('https://seaborn.pydata.org/', None),
    'mayavi': ('http://docs.enthought.com/mayavi/mayavi', None),
    'pyvista': ('https://docs.pyvista.org', None),
}

examples_dirs = ['../examples']
gallery_dirs = ['auto_examples']
import mne

scrapers = ('matplotlib',)
try:
    mlab = mne.utils._import_mlab()
    # Do not pop up any mayavi windows while running the
    # examples. These are very annoying since they steal the focus.
    mlab.options.offscreen = True
    # hack to initialize the Mayavi Engine
    mlab.test_plot3d()
    mlab.close()
except Exception:
    pass
else:
    scrapers += ('mayavi',)
try:
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        import pyvista
    pyvista.OFF_SCREEN = False
except Exception:
    pass
else:
    scrapers += ('pyvista',)
if any(x in scrapers for x in ('pyvista', 'mayavi')):
    from traits.api import push_exception_handler
    push_exception_handler(reraise_exceptions=True)
    report_scraper = mne.report._ReportScraper()
    scrapers += (report_scraper,)
else:
    report_scraper = None

sphinx_gallery_conf = {
    'doc_module': 'groupmne',
    'reference_url': dict(groupmne=None),
    'examples_dirs': examples_dirs,
    'gallery_dirs': gallery_dirs,
    'plot_gallery': 'True',
    'thumbnail_size': (160, 112),
    'min_reported_time': 1.,
    'backreferences_dir': os.path.join('generated'),
    'abort_on_example_error': False,
    'image_scrapers': scrapers,
    'show_memory': True,
    # 'reference_url': {
    #     'numpy': 'http://docs.scipy.org/doc/numpy-1.9.1',
    #     'scipy': 'http://docs.scipy.org/doc/scipy-0.17.0/reference',
    # }
}


def setup(app):
    app.add_stylesheet('style.css')
