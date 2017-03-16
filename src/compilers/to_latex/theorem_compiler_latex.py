from src.compilers.base_compiler import BaseCompiler
from src.helpers.constants import LATEX_THEOREM_FORMAT_STR
from src.models.theorem_model import TheoremModel
from src.registers.latex_register import global_latex_register


class TheoremCompiler(TheoremModel, BaseCompiler):
    def compile(self) -> str:
        """
        return a pure latex theorem block
        :return: a pure latex syntax theorem
        """

        # register the theorem type to register (for latex header)
        global_latex_register.register_theorem_type(
            new_theorem_type=self.theorem_type
        )

        return LATEX_THEOREM_FORMAT_STR.format(
            theorem_type=self.theorem_type,
            label=self.label,
            content=self.content
        )
