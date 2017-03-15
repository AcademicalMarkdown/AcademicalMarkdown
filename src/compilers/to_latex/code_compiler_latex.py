import codecs

from src.compilers.base_compiler import BaseCompiler
from src.helpers.constants import LATEX_CODE_FORMAT_STR, LEFT_BRACKET, \
    RIGHT_BRACKET
from src.models.code_model import CodeModel


class CodeCompilerLatex(CodeModel, BaseCompiler):
    def compile(self) -> str:
        """
        this function returns a string as the compiled result as
        current yaml block
        :return: the compiled result (valid pandoc code to convert to latex)
        """

        # if specified a file
        if self.file:
            with codecs.open(self.file, 'r', encoding='utf-8') as f:
                self.content = f.read()

        # return the pandoc code that can be convert to latex
        return LATEX_CODE_FORMAT_STR.format(
            syntax=self.syntax,
            caption=self.caption,
            label=self.label,
            content=self.content,
            left_bracket=LEFT_BRACKET,
            right_bracket=RIGHT_BRACKET
        )
