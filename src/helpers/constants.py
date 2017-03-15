# constants are invariant outside of this file.

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

: {caption} \label{{ {label} }}"""
