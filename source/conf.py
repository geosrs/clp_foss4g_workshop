# -*- coding: utf-8 -*-
#
# sphinx_essc_geo documentation build configuration file, created by
# sphinx-quickstart on Tue May 18 09:01:35 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.intersphinx', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.pngmath', 'sphinx.ext.ifconfig', 'rst2pdf.pdfbuilder', 'sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'CLP-FFI-ESSC FOSS-Geo Materials 2013'
copyright = u'2013, http://www.essc.org.ph license under GNU Free Document License'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%B %d %Y %H:%M:%S'

# List of documents that shouldn't be included in the build.
#unused_docs = ['intro.rst', 'chapter1.rst']

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# TODO:check for duplicate entries
rst_epilog = """
.. |ftools_buffer| image:: images/ftools/buffer.png
                   :width: 20 pt
.. |ftools_clip| image:: images/ftools/clip.png
                 :width: 20 pt
.. |ftools_geoprocessing| image:: images/ftools/geoprocessing.png
                          :width: 20 pt
.. |ftools_intersect| image:: images/ftools/intersect.png
                      :width: 20 pt
.. |mActionAddBasicShape| image:: images/qgis_icons/mActionAddBasicShape.png
                          :width: 20 pt
.. |mActionAddImage| image:: images/qgis_icons/mActionAddImage.png
                     :width: 20 pt
.. |mActionAddLegend| image:: images/qgis_icons/mActionAddLegend.png
                      :width: 20 pt
.. |mActionAddMap| image:: images/qgis_icons/mActionAddMap.png
                   :width: 20 pt
.. |mActionAddOgrLayer| image:: images/qgis_icons/mActionAddOgrLayer.png
                        :width: 20 pt
.. |mActionAddRasterLayer| image:: images/qgis_icons/mActionAddRasterLayer.png
                           :width: 20 pt
.. |mActionAddWmsLayer| image:: images/qgis_icons/mActionAddWmsLayer.png
                        :width: 20 pt
.. |mActionAlignLeft| image:: images/qgis_icons/mActionAlignLeft.png
                      :width: 20 pt
.. |mActionCalculateField| image:: images/qgis_icons/mActionCalculateField.png
                           :width: 20 pt
.. |mActionAddFeatureLine| image:: images/qgis_icons/mActionAddFeatureLine.png
                        :width: 20 pt
.. |mActionAddFeaturePoint| image:: images/qgis_icons/mActionAddFeaturePoint.png
                         :width: 20 pt
.. |mActionAddFeaturePolygon| image:: images/qgis_icons/mActionAddFeaturePolygon.png
                           :width: 20 pt
.. |mActionCopySelected| image:: images/qgis_icons/mActionCopySelected.png
                         :width: 20 pt
.. |mActionDeleteAttribute| image:: images/qgis_icons/mActionDeleteAttribute.png
                            :width: 20 pt
.. |mActionDeleteSelected| image:: images/qgis_icons/mActionDeleteSelected.png
                           :width: 20 pt
.. |mActionDraw| image:: images/qgis_icons/mActionDraw.png
                 :width: 20 pt
.. |mActionEditCopy| image:: images/qgis_icons/mActionEditCopy.png
                     :width: 20 pt
.. |mActionEditCut| image:: images/qgis_icons/mActionEditCut.png
                    :width: 20 pt
.. |mActionEditPaste| image:: images/qgis_icons/mActionEditPaste.png
                      :width: 20 pt
.. |mActionFileNew| image:: images/qgis_icons/mActionFileNew.png
                    :width: 20 pt
.. |mActionFilePrint| image:: images/qgis_icons/mActionFilePrint.png
                      :width: 20 pt
.. |mActionFileSave| image:: images/qgis_icons/mActionFileSave.png
                     :width: 20 pt
.. |mActionGroupItems| image:: images/qgis_icons/mActionGroupItems.png
                       :width: 20 pt
.. |mActionIdentify| image:: images/qgis_icons/mActionIdentify.png
                     :width: 20 pt
.. |mActionInvertSelection| image:: images/qgis_icons/mActionInvertSelection.png
                            :width: 20 pt
.. |mActionLabel| image:: images/qgis_icons/mActionLabel.png
                  :width: 20 pt
.. |mActionMeasureArea| image:: images/qgis_icons/mActionMeasureArea.png
                        :width: 20 pt
.. |mActionMeasure| image:: images/qgis_icons/mActionMeasure.png
                    :width: 20 pt
.. |mActionMoveFeature| image:: images/qgis_icons/mActionMoveFeature.png
                        :width: 20 pt
.. |mActionNewAttribute| image:: images/qgis_icons/mActionNewAttribute.png
                         :width: 20 pt
.. |mActionNewComposer| image:: images/qgis_icons/mActionNewComposer.png
                        :width: 20 pt
.. |mActionNewVectorLayer| image:: images/qgis_icons/mActionNewVectorLayer.png
                           :width: 20 pt
.. |mActionNodeTool| image:: images/qgis_icons/mActionNodeTool.png
                     :width: 20 pt
.. |mActionOptions| image:: images/qgis_icons/mActionOptions.png
                    :width: 20 pt
.. |mActionPan| image:: images/qgis_icons/mActionPan.png
                :width: 20 pt
.. |mActionRaiseItems| image:: images/qgis_icons/mActionRaiseItems.png
                       :width: 20 pt
.. |mActionSaveAsPDF| image:: images/qgis_icons/mActionSaveAsPDF.png
                      :width: 20 pt
.. |mActionSaveMapAsImage| image:: images/qgis_icons/mActionSaveMapAsImage.png
                           :width: 20 pt
.. |mActionScaleBar| image:: images/qgis_icons/mActionScaleBar.png
                     :width: 20 pt
.. |mActionSelectPan| image:: images/qgis_icons/mActionSelectPan.png
                      :width: 20 pt
.. |mActionSelectedToTop| image:: images/qgis_icons/mActionSelectedToTop.png
                          :width: 20 pt
.. |mActionShowPluginManager| image:: images/qgis_icons/mActionShowPluginManager.png
                              :width: 20 pt
.. |mActionToggleEditing| image:: images/qgis_icons/mActionToggleEditing.png
                          :width: 20 pt
.. |mActionUngroupItems| image:: images/qgis_icons/mActionUngroupItems.png
                         :width: 20 pt
.. |mActionUnselectAttributes| image:: images/qgis_icons/mActionUnselectAttributes.png
                               :width: 20 pt
.. |mActionZoomFullExtent| image:: images/qgis_icons/mActionZoomFullExtent.png
                           :width: 20 pt
.. |mActionZoomIn| image:: images/qgis_icons/mActionZoomIn.png
                   :width: 20 pt
.. |mActionZoomLast| image:: images/qgis_icons/mActionZoomLast.png
                     :width: 20 pt
.. |mActionZoomOut| image:: images/qgis_icons/mActionZoomOut.png
                    :width: 20 pt
.. |mActionZoomToLayer| image:: images/qgis_icons/mActionZoomToLayer.png
                        :width: 20 pt
.. |mActionZoomToSelected| image:: images/qgis_icons/mActionZoomToSelected.png
                           :width: 20 pt
.. |plugin_installer| image:: images/qgis_icons/plugin_installer.png
                      :width: 20 pt
.. |adddelimitedtext| image:: images/qgis_icons/adddelimitedtext.png
                      :width: 20 pt
.. |mActionGPSTools| image:: images/qgis_icons/mActionGPSTools.png
                         :width: 20pt
.. |mActionAddBingLayer| image:: images/qgis_icons/mActionAddBingLayer.png
                         :width: 20pt
"""

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'nature'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'ESSC'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'ESSC FOSS-Geo'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'essclogotrace_thumbnail.jpg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
html_use_modindex = False

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'sphinx_essc_geodoc'

# -- Options for rst2pdf output --------------------------------------------------
# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\.
# For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
# The options element is a dictionary that lets you override
# this config per-document.
# For example,
# ('index', u'MyProject', u'My Project', u'Author Name',
#  dict(pdf_compressed = True))
# would mean that specific document would be compressed
# regardless of the global pdf_compressed setting.

#pdf_documents = [
#        ('index', u'MyProject', u'My Project', u'Author Name'),
#    ]

# A comma-separated list of custom stylesheets. Example:
#pdf_stylesheets = ['sphinx','kerning','a4']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
#pdf_compressed = False

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']

# Language to be used for hyphenation support
#pdf_language = "en_US"

# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
#pdf_fit_mode = "shrink"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
#pdf_break_level = 0

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
#pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
#pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
#pdf_verbosity = 0

# If false, no index is generated.
#pdf_use_index = True

# If false, no modindex is generated.
#pdf_use_modindex = True

# If false, no coverpage is generated.
#pdf_use_coverpage = True

# Name of the cover page template to use
#pdf_cover_template = 'sphinxcover.tmpl'

# Documents to append as an appendix to all manuals.
#pdf_appendices = []

# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
#pdf_splittables = False

# Set the default DPI for images
#pdf_default_dpi = 72

# Enable rst2pdf extension modules (default is only vectorpdf)
# you need vectorpdf if you want to use sphinx's graphviz support
#pdf_extensions = ['vectorpdf']

# Page template name for "regular" pages
#pdf_page_template = 'cutePage'

# Show Table Of Contents at the beginning?
#pdf_use_toc = True

# How many levels deep should the table of contents be?
#pdf_toc_depth = 9999

# Add section number to section references
#pdf_use_numbered_links = False

# Background images fitting mode
#pdf_fit_background_mode = 'scale'

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'ESSCQuiapo.tex', u'Quiapo Church DMM - ESSC FOSS-Geo Materials 2013',
   u'ESSC', 'manual', 'False'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'essclogotrace_thumbnail.jpg'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# Additional stuff for the LaTeX preamble.

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

#If true, add page references after internal references. This is very useful for printed copies of the manual. Default is False.
latex_show_pageref = True

#Control whether to display URL addresses. This is very useful for printed copies of the manual. The setting can have the following values:  'no' – do not display URLs (default); 'footnote' – display URLs in footnotes; 'inline' – display URLs inline in parentheses
latex_show_urls = True

latex_elements = {
     'classoptions': 
     ',openany,oneside', 
     'babel' : '\\usepackage[english]{babel}'
    }


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}


#edit checks
todo_include_todos = True
