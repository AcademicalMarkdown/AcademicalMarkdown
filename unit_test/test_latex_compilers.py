from src.compilers.to_latex.code_compiler_latex import CodeCompilerLatex
from src.compilers.to_latex.figure_compiler_latex import FigureCompilerLatex
from src.compilers.to_latex.table_compiler_latex import TableCompilerLatex
from src.compilers.to_latex.theorem_compiler_latex import TheoremCompilerLatex
from src.registers.latex_register import global_latex_register
from unit_test.helpers.constants_for_test import *

code_latex_compiler = CodeCompilerLatex()
fig_latex_compiler = FigureCompilerLatex()
table_latex_compiler = TableCompilerLatex()
theorem_compiler = TheoremCompilerLatex()


class TestLatexCodeCompiler:
    def test_code_with_file(self):
        code_latex_compiler.load_dict(
            input_dict=code_test_dict_with_file
        )
        exp_res = '''
~~~~{ .python caption="this is a test code" label=test_code }
def resource():
    return "this file is used for testing"


print(resource())

~~~~
'''

        assert code_latex_compiler.compile() == exp_res


class TestLatexFigCompiler:
    def test_figure_with_everything(self):
        fig_latex_compiler.load_dict(
            input_dict=figure_test_dict
        )
        exp_res = "![this is a image](./image/git.png)" \
                  "{ #fig:figid width=30 height=20 }"
        assert fig_latex_compiler.compile() == exp_res


class TestTableCompilerLatex:
    def test_table_with_file(self):
        table_latex_compiler.load_dict(
            input_dict=table_test_dict_with_file
        )
        exp_res = '''
Hello     World
-------  --------
'quote   good
lala     "haha"
testing  2

: this is a table \label{tbl: testTable}'''

        assert table_latex_compiler.compile() == exp_res


class TestLatexTheoremCompiler:
    def test_theorem(self):
        theorem_compiler.load_dict(
            input_dict=theorem_test_dict
        )
        exp_res = '''
\\begin{Lemma}
\\label{thm:maxwell eq}
great theorem
\\end{Lemma}'''

        assert theorem_compiler.compile() == exp_res
        assert global_latex_register.theorem_types == {'Lemma'}
