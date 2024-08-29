# The content below is copied from the esp-hdg repo and modified acc to the esp-chip-errata repo

from esp_docs.conf_docs import *  # noqa: F403,F401

languages = ['en', 'zh_CN']
idf_targets = ['esp32s2', 'esp32s3', 'esp32c3', 'esp32c6', 'esp32h2', 'esp32c2']
extensions += ['sphinx_copybutton',
               # Note: order is important here, events must
               # be registered by one extension before they can be
               # connected to another extension
               'esp_docs.esp_extensions.dummy_build_system',
               'linuxdoc.rstFlatTable', #https://return42.github.io/linuxdoc/linuxdoc-howto/table-markup.html#flat-table
               'sphinx-tags', # Fine-tuned for this project based on https://sphinx-tags.readthedocs.io/en/latest/quickstart.html
               'sphinx_design', #https://sphinx-design.readthedocs.io/en/latest/get_started.html
               ]

ESP32C3_DOCS = ['01-chip-identification/esp32c3/*.rst',
                '02-errata-summary/esp32c3-errata-summary.rst',
                '03-errata-description/esp32c3/*.rst',
                '03-errata-description/shared/sar-adc-adc2-not-work.rst',
                'revision-history/esp32c3-revision-history.rst',
                ]
ESP32C2_DOCS = ['01-chip-identification/esp32c2/*.rst',
                '02-errata-summary/esp32c2-errata-summary.rst',
                '03-errata-description/esp32c2/*.rst',
                'revision-history/esp32c2-revision-history.rst',
                ]
ESP32S3_DOCS = ['01-chip-identification/esp32s3/*.rst',
                '02-errata-summary/esp32s3-errata-summary.rst',
                '03-errata-description/esp32s3/*.rst',
                '03-errata-description/shared/sar-adc-adc2-not-work.rst',
                '03-errata-description/shared/rmt-idle-level-cannot-be-controlled.rst',
                '03-errata-description/shared/tchsen-scan-done-int-raw-data-undefined.rst',
                '03-errata-description/shared/rtc-reg-read-error-from-light-sleep.rst',
                'revision-history/esp32s3-revision-history.rst',
                ]
ESP32C6_DOCS = ['01-chip-identification/esp32c6/*.rst',
                '02-errata-summary/esp32c6-errata-summary.rst',
                '03-errata-description/esp32c6/*.rst',
                '03-errata-description/shared/clock-rc-fast-clk-inaccurate.rst',
                '03-errata-description/shared/cpu-load-store.rst',
                '03-errata-description/shared/rmt-idle-level-cannot-be-controlled.rst',
                'revision-history/esp32c6-revision-history.rst',
                ]
ESP32S2_DOCS = ['01-chip-identification/esp32s2/*.rst',
                '02-errata-summary/esp32s2-errata-summary.rst',
                '03-errata-description/esp32s2/*.rst',
                '03-errata-description/shared/tchsen-scan-done-int-raw-data-undefined.rst',
                '03-errata-description/shared/rtc-reg-read-error-from-light-sleep.rst',
                'revision-history/esp32s2-revision-history.rst',
                ]
ESP32H2_DOCS = ['01-chip-identification/esp32h2/*.rst',
                '02-errata-summary/esp32h2-errata-summary.rst',
                '03-errata-description/esp32h2/*.rst',
                '03-errata-description/shared/clock-rc-fast-clk-inaccurate.rst',
                '03-errata-description/shared/cpu-load-store.rst',
                'revision-history/esp32h2-revision-history.rst',
                ]

conditional_include_dict = {'esp32c2':ESP32C2_DOCS,
                            'esp32c3':ESP32C3_DOCS,
                            'esp32c6':ESP32C6_DOCS,
                            'esp32s2':ESP32S2_DOCS,
                            'esp32s3':ESP32S3_DOCS,
                            'esp32h2':ESP32H2_DOCS}

# link roles config
github_repo = 'espressif/esp-chip-errata'

# context used by sphinx_idf_theme
html_context['github_user'] = 'espressif'
html_context['github_repo'] = 'esp-chip-errata'

html_static_path = ['../_static']

# Extra options required by sphinx_idf_theme
project_slug = 'esp-chip-errata'

# Contains info used for constructing target and version selector
# Can also be hosted externally, see esp-idf for example
versions_url = './_static/docs_version.js'

# Final PDF filename will contains target and version
pdf_file_prefix = u'esp-chip-errata'

# disable the check for link anchors
linkcheck_anchors = False

# Tracing ID for Google Analytics
google_analytics_id = 'G-EEZFY8D6CS'

# Configuration for sphinx_tags
tags_create_tags = True
tags_extension = ["rst"]
tags_create_badges = True
tags_badge_colors = {
    "*": "secondary",
}

# Table, figure, and section numbering configurations
numfig = True

# --- Customized LaTeX configurations ----------------

# Customized titlepage
titlepage = ''
with open('../_static/titlepage.tex') as f:
    titlepage = f.read()

# Additional configurations added to the preamble
# Add the following code to 'preamble_extra' if you want to add watermark to the PDF
# \definecolor{watermark}{rgb}{0.83, 0.83, 0.83}
# \usepackage{draftwatermark}
# \SetWatermarkAngle{45}
# \SetWatermarkColor{watermark}
# \SetWatermarkFontSize{3.5cm}
# \SetWatermarkText{CONFIDENTIAL}
preamble_extra = r'''
% ToC
\makeatletter
\renewcommand{\l@section}[2]{\vspace{14pt}\@dottedtocline{2}{0pt}{30pt}{\LARGE\bfseries\textcolor{LochmaraColor}{#1}}{#2}}
\renewcommand{\l@subsection}[2]{\@dottedtocline{2}{0pt}{30pt}{\textcolor{LochmaraColor}{#1}}{#2}}
\renewcommand{\@dotsep}{10000}
\makeatother

% Line spacing
\linespread{1.3}

% Make text left-aligned
\raggedright
'''

# LaTeX Figure alignment
latex_elements['figure_align'] = 'H'

# Remove empty pages after ToC and end of chapter
latex_elements['extraclassoptions'] = 'openany,oneside'

# Set table header and tiplisting color
latex_elements['sphinxsetup'] = r'''
TableMergeColorHeader={gray!25},
TableRowColorHeader={gray!25},
TableRowColorOdd={white!0},
TableRowColorEven={white!0},
TableMergeColorOdd={white!0},
TableMergeColorEven={white!0},
noteBorderColor={RGB}{16, 32, 160},
'''

# Use customized titlepage with version number
latex_elements['maketitle'] = titlepage

# Set document class
latex_docclass = {
    'howto': 'article',
    'manual': 'article',
}

# Start a document from Section instead of Chapter
latex_toplevel_sectioning = 'section'

# Configure latex table style
latex_table_style = ['colorrows']

# Set the path of the logo \sphinxlogo used in the titlepage
latex_logo = '../_static/esp-logo-standard-vertical.pdf'
