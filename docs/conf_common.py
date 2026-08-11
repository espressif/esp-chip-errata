# The content below is copied from the esp-hdg repo and modified acc to the esp-chip-errata repo

from esp_docs.conf_docs import *  # noqa: F403,F401
import yaml

languages = ['en', 'zh_CN']

idf_targets = ['esp32s2', 'esp32s3', 'esp32c3', 'esp32c6', 'esp32h2', 'esp32c2', 'esp32', 'esp32p4', 'esp32c5', 'esp32c61', 'esp32s31']

# Map idf_target to chip_series in lbcf.yml
idf_target_to_chip_series = {
    "esp32": "ESP32",
    "esp32s2": "ESP32-S2",
    "esp32c2": "ESP8684",
    "esp32s3": "ESP32-S3",
    "esp32c3": "ESP32-C3",
    "esp32c6": "ESP32-C6",
    "esp32h2": "ESP32-H2",
    "esp32p4": "ESP32-P4",
    "esp32c5": "ESP32-C5",
    "esp32c61": "ESP32-C61",
    "esp32s31": "ESP32-S31",
}

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
                '03-errata-description/shared/rmt-idle-level-cannot-be-controlled.rst',
                '03-errata-description/shared/i2c-fail-in-multiple-reads-operation.rst',
                '03-errata-description/shared/cpu-load-store.rst',
                '03-errata-description/shared/ecdsa-invalid-r-and-s-signature-accepted.rst',
                '03-errata-description/shared/ecdsa-invalid-s-signature-accepted.rst',
                'revision-history/esp32h2-revision-history.rst',
                ]
ESP32_DOCS = ['01-chip-identification/esp32/*.rst',
              '02-errata-summary/esp32-errata-summary.rst',
              '03-errata-description/esp32/*.rst',
              '03-errata-description/shared/rtc-reg-read-error-from-light-sleep.rst',
              'revision-history/esp32-revision-history.rst',
              ]
ESP32P4_DOCS = ['01-chip-identification/esp32p4/*.rst',
                '02-errata-summary/esp32p4-errata-summary.rst',
                '03-errata-description/esp32p4/*.rst',
                '03-errata-description/shared/rmt-idle-level-cannot-be-controlled.rst',
                '03-errata-description/shared/i2c-fail-in-multiple-reads-operation.rst',
                '03-errata-description/shared/ecdsa-invalid-r-and-s-signature-accepted.rst',
                '03-errata-description/shared/ecdsa-invalid-s-signature-accepted.rst',
                'revision-history/esp32p4-revision-history.rst',
              ]
ESP32C5_DOCS = ['01-chip-identification/esp32c5/*.rst',
                '02-errata-summary/esp32c5-errata-summary.rst',
                '03-errata-description/esp32c5/*.rst',
                '03-errata-description/shared/psram-read-after-write-consistency.rst',
                'revision-history/esp32c5-revision-history.rst',
                ]

ESP32C61_DOCS = ['01-chip-identification/esp32c61/*.rst',
                '02-errata-summary/esp32c61-errata-summary.rst',
                '03-errata-description/esp32c61/*.rst',
                '03-errata-description/shared/psram-read-after-write-consistency.rst',
                'revision-history/esp32c61-revision-history.rst',
              ]

ESP32S31_DOCS = ['01-chip-identification/esp32s31/*.rst',
                '02-errata-summary/esp32s31-errata-summary.rst',
                '03-errata-description/esp32s31/*.rst',
                '03-errata-description/shared/ecdsa-invalid-r-and-s-signature-accepted.rst',
                'revision-history/esp32s31-revision-history.rst',
              ]

conditional_include_dict = {'esp32c2':ESP32C2_DOCS,
                            'esp32c3':ESP32C3_DOCS,
                            'esp32c6':ESP32C6_DOCS,
                            'esp32s2':ESP32S2_DOCS,
                            'esp32s3':ESP32S3_DOCS,
                            'esp32h2':ESP32H2_DOCS,
                            'esp32':ESP32_DOCS,
                            'esp32p4':ESP32P4_DOCS,
                            'esp32c5':ESP32C5_DOCS,
                            'esp32c61':ESP32C61_DOCS,
                            'esp32s31':ESP32S31_DOCS,
                            }

# link roles config
github_repo = 'espressif/esp-chip-errata'

# context used by sphinx_idf_theme
html_context['github_user'] = 'espressif'
html_context['github_repo'] = 'esp-chip-errata'

html_static_path = ['../_static']

# Custom css files to prevent break at hyphens
html_css_files = ['prevent_break_at_hyphen.css']

# Set column width for the errata summary table with merged cells
html_css_files += ['table.css']

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

% Fallback for CJK characters
\usepackage{xeCJK}
\setCJKmainfont{Noto Serif CJK SC}
\setCJKsansfont{Noto Sans CJK SC}
\setCJKmonofont{Noto Sans Mono CJK SC}

% Font settings
\setmainfont {MaisonNeue-Light}[
  UprightFont = MaisonNeue-Light,
  ItalicFont = MaisonNeue-LightItalic,
  BoldFont = MaisonNeue-Medium,
]

\setmonofont{MaisonNeueMono-Regular}

\setsansfont{MaisonNeue-Light}

% Minimum table column width
\setlength{\tymin}{20em}
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

# Use xindy to prepare index
latex_use_xindy = True

# Set the path of the logo \sphinxlogo used in the titlepage
latex_logo = '../_static/esp-logo-standard-vertical.pdf'

# Get doc version from lbcf.yml and add to PDF
def load_chip_series_version(idf_target):
    chip_series = idf_target_to_chip_series.get(idf_target.lower())
    if not chip_series:
        return 'Unknown Version'

    yml_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".lbcf.yml"))
    with open(yml_path, 'r', encoding='utf-8') as f:
        yml = yaml.safe_load(f)

    for entry in yml.get("documents", []):  # get the list under the 'documents' key
        if entry.get("chip_series") == chip_series and "version" in entry:
            return entry["version"]

    return "Unknown Version"

def conf_setup(app, config):
    print("Current target:", config.idf_target)

    doc_version = load_chip_series_version(config.idf_target)
    print("Doc version:", doc_version)

    doc_version_config = '''
    %% Version number
    \\newcommand{{\\docversion}}{{{}}}
    '''.format(doc_version)

    config.latex_elements['preamble'] += doc_version_config

user_setup_callback = conf_setup
