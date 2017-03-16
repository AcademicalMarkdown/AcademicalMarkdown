from src.compilers.base_compiler import BaseCompiler
from src.helpers.constants import LATEX_THEOREM_FORMAT_STR
from src.models.theorem_model import TheoremModel
from src.registers.common_register import global_common_register
from src.registers.latex_register import global_latex_register


class TheoremCompilerLatex(TheoremModel, BaseCompiler):
    def compile(self) -> str:
        """
        return a pure latex theorem block
        :return: a pure latex syntax theorem
        """

        # register the theorem type to register (for latex header)
        global_latex_register.register_theorem_type(self.theorem_type)
        global_common_register.register_new_label(self.label)

        return LATEX_THEOREM_FORMAT_STR.format(
            theorem_type=self.theorem_type,
            label=self.label,
            content=self.content
        )
