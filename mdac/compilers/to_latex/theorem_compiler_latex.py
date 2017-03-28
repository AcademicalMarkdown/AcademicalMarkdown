from mdac.compilers.base_compiler import BaseCompiler
from mdac.helpers.constants import LATEX_THEOREM_FORMAT_STR
from mdac.models.theorem_model import TheoremModel
from mdac.registers.common_register import CommonRegister
from mdac.registers.latex_register import LatexRegister


class TheoremCompilerLatex(TheoremModel, BaseCompiler):
    def load_dict(self, input_dict: dict):
        """
        call the super method (defined in BaseModel),
        then register label and theorem
        :param input_dict: the input dict
        """
        # call the original load dict
        super().load_dict(input_dict)

        # register the theorem type to register (for latex header)
        LatexRegister.register_theorem_type(self.theorem_type)
        CommonRegister.register_new_label(self.label)

    def compile(self) -> str:
        """
        return a pure latex theorem block
        :return: a pure latex syntax theorem
        """

        return LATEX_THEOREM_FORMAT_STR.format(
            theorem_type=self.theorem_type,
            label=self.label,
            content=self.content
        )
