# constants are invariant outside of this file.

# this is used for formatting due to python formatting will have an error
# when you try to format "{{a}, {b}}" because of the outer brackets
LEFT_BRACKET = '{'
RIGHT_BRACKET = '}'


LATEX_CODE_FORMAT_STR = '''
~~~~{left_bracket}.{syntax} caption="{caption}" label="{label}"{right_bracket}
{content}
~~~~
'''

