from src.compilers.to_latex.code_compiler_latex import CodeCompilerLatex
from src.compilers.to_latex.figure_compiler_latex import FigureCompilerLatex
from unit_test.helpers.constants_for_test import *

code_latex_compiler = CodeCompilerLatex()
fig_latex_compiler = FigureCompilerLatex()


class TestLatexCodeCompiler:
    def test_code_with_file(self):
        code_latex_compiler.load_dict(
            input_dict=code_test_dict_with_file
        )
        exp_res = '''
~~~~{.python caption="this is a test code" label=test_code}
def resource():
    return "this file is used for testing"


print(resource())

~~~~
'''

        assert code_latex_compiler.compile() == exp_res


class TestLatexFigCompiler:
