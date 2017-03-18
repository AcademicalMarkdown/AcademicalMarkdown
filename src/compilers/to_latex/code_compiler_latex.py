import codecs

from src.compilers.common_compilers.base_compiler import BaseCompiler
from src.helpers.constants import LATEX_CODE_FORMAT_STR, \
    LATEX_CODE_LABEL_FORMAT
from src.models.code_model import CodeModel
from src.registers.common_register import CommonRegister


class CodeCompilerLatex(CodeModel, BaseCompiler):
    def load_dict(self, input_dict: dict):
        """
        call the super method (defined in BaseModel), then register the label
        :param input_dict: the input dict
        """
        # call the original load dict
        super().load_dict(input_dict)

        # register the label
        CommonRegister.register_new_label(self.label)

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

        # construct parameters
        label_str = LATEX_CODE_LABEL_FORMAT.format(label=self.label) \
            if self.label else ""

        # return the pandoc code that can be convert to latex
        return LATEX_CODE_FORMAT_STR.format(
            syntax=self.syntax,
            caption=self.caption,
            label=label_str,
            content=self.content
        )
