from src.compilers.common_compilers.base_compiler import BaseCompiler
from src.helpers.constants import LATEX_FIG_HEIGHT_FORMAT, \
    LATEX_FIG_WIDTH_FORMAT, LATEX_FIG_LABEL_FORMAT, LATEX_FIGURE_FORMAT_STR
from src.models.figure_model import FigureModel
from src.registers.common_register import CommonRegister


class FigureCompilerLatex(FigureModel, BaseCompiler):
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
        this function compile the class into string format
        :return: a pandoc image string (something like this `![]()`)
        """

        # add data to key words, to make them valid parameters
        # see constants for more
        width_str = LATEX_FIG_WIDTH_FORMAT.format(width=self.width) \
            if self.width else ""
        height_str = LATEX_FIG_HEIGHT_FORMAT.format(height=self.height) \
            if self.height else ""
        label_str = LATEX_FIG_LABEL_FORMAT.format(label=self.label) \
            if self.label else ""

        # valid pandoc figure syntax, see constants for more
        return LATEX_FIGURE_FORMAT_STR.format(
            caption=self.caption,
            source=self.source,
            label=label_str,
            width=width_str,
            height=height_str
        )
