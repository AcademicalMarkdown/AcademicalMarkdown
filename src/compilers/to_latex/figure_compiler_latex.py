from src.compilers.base_compiler import BaseCompiler
from src.helpers.constants import LATEX_FIG_HEIGHT_FORMAT, \
    LATEX_FIG_WIDTH_FORMAT, LATEX_FIG_LABEL_FORMAT, LATEX_FIGURE_FORMAT_STR, \
    LEFT_BRACKET, RIGHT_BRACKET
from src.models.figure_model import FigureModel


class FigureCompilerLatex(FigureModel, BaseCompiler):
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
            left_bracket=LEFT_BRACKET,
            right_bracket=RIGHT_BRACKET,
            label=label_str,
            width=width_str,
            height=height_str
        )
