# constants are invariant outside of this file.

CSV_DELIMINATOR = ","
# this is used for formatting due to python formatting will have an error
# when you try to format "{{a}, {b}}" because of the outer brackets
LEFT_BRACKET = '{'
RIGHT_BRACKET = '}'

# ======================== code compile section ==========================
LATEX_CODE_FORMAT_STR = '''
~~~~{left_bracket}.{syntax} caption="{caption}" {label}{right_bracket}
{content}
~~~~
'''
LATEX_CODE_LABEL_FORMAT = "label={label}"

# ======================= figure compile section =========================

LATEX_FIGURE_FORMAT_STR = \
    "![{caption}]({source})" \
    "{left_bracket}{label} {width} {height}{right_bracket}"

LATEX_FIG_WIDTH_FORMAT = "width={width}"
LATEX_FIG_HEIGHT_FORMAT = "height={height}"
LATEX_FIG_LABEL_FORMAT = "#{label}"

# ======================== table compile section ==========================

LATEX_TABLE_FORMAT_STR = """
{content}

: {caption} \label{{ {label} }}"""
