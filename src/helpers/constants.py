# constants are invariant outside of this file.
import re

CSV_DELIMINATOR = ","

# ======================== code compile section ==========================
LATEX_CODE_FORMAT_STR = '''
~~~~{{ .{syntax} caption="{caption}" {label} }}
{content}
~~~~
'''
LATEX_CODE_LABEL_FORMAT = "label={label}"

# ======================= figure compile section =========================

LATEX_FIGURE_FORMAT_STR = \
    "![{caption}]({source})" \
    "{{ {label} {width} {height} }}"

LATEX_FIG_WIDTH_FORMAT = "width={width}"
LATEX_FIG_HEIGHT_FORMAT = "height={height}"
LATEX_FIG_LABEL_FORMAT = "#{label}"

# ======================== table compile section ==========================

LATEX_TABLE_FORMAT_STR = """
{content}

: {caption} \label{{{label}}}"""

# ======================== theorem compile section ========================

LATEX_THEOREM_FORMAT_STR = '''
\\begin{{{theorem_type}}}
\\label{{{label}}}
{content}
\\end{{{theorem_type}}}'''

THEOREM_HEADER_FORMAT_STR = '''
\\newtheorem{{{theorem_type}}}{{{theorem_type}}}'''

# ======================== ref compile section ===========================
ORIG_REF_REGEX_FORMAT = r"(?<!\\)(\\\\)*?\[@{label}\]"
COMPILED_REF_REGEX_FORMAT = r"\1\\ref{{{label}}}"
ORIG_PAGE_REF_REGEX_FORMAT = r"(?<!\\)(\\\\)*?\[p@{label}\]"
COMPILED_PAGE_REF_REGEX_FORMAT = r"\1\\pageref{{{label}}}"

# ======================== constants compile section ====================
ORIG_CONST_REGEX_FORMAT = r"(?<!\\)(\\\\)*?\[@{label}\]"

# ======================== main compiler section =========================
YAML_HEADER_REGEX = re.compile(r"\A---(.*)^[-.]{3}", re.MULTILINE | re.DOTALL)

YAML_BLOCK_REGEX = re.compile(r"""
                    ^           # match beginning of a line
                    %---        # match %--- literally (beginning of a block)
                    [\s\S]*?    # matches everything lazily (content of block)
                    (?<!\\)     # exclude one single escape character (\)
                    (?:\\\\)*   # match any number of escaped \ (\\)
                    ---%        # match ---% literally (ending of a block)
                    """, re.VERBOSE | re.MULTILINE)

YAML_BLOCK_STRIP_REGEX = re.compile(r"""
                    ^           # match beginning of a line
                    %---        # match %--- literally (beginning of a block)
                    ([\s\S]*?    # matches everything lazily (content of block)
                    (?<!\\)     # exclude one single escape character (\)
                    (?:\\\\)*)   # match any number of escaped \ (\\)
                    ---%        # match ---% literally (ending of a block)
                    """, re.VERBOSE | re.MULTILINE)

YAML_BLOCK_STRIP_REPLACE_REGEX = "\\1"

UNESCAPED_REGEX_SUB_LIST = [
    (r'(\\\\)*\\%---', r'\1%---'),  # escaped beginning block
    (r'(\\\\)*\\---%', r'\1---%'),  # escaped ending block
    (r'(?:\\)(\\\\)*?\[@', r'\1[@'),  # escaped ref labels beginning
    (r'(?:\\)(\\\\)*?\[p@', r'\1[p@'),  # escaped page ref labels
    (r'\\]', r']'),  # escaped ref & page ref labels beginning
    (r'\\\\', r'\\'),
]

# ======================= Error message Section ===========================
DECODE_ERROR_MESSAGE_FORMAT = \
    "cannot decode {filename} with utf-8 encodings"
YAML_PARSE_ERROR_FORMAT = \
    'following error encountered while parsing {yaml_block}:\n{error_message}'
COMPILER_LOAD_ERROR_FORMAT = \
    'following error encountered while interpreting {yaml_block}:' \
    '\n{error_message}'
RESET_YAML_HEADER_ERROR = \
    'there can be only one yaml header exists in document, ' \
    'you cannot set yaml header twice'
