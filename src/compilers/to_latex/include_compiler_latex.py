import codecs

from src.compilers.base_compiler import BaseCompiler
from src.helpers.constants import DECODE_ERROR_MESSAGE_FORMAT
from src.models.include_model import IncludeModel


class IncludeCompilerLatex(IncludeModel, BaseCompiler):
    def compile(self) -> str:
        """
        find the file and copy the content of the file into current file
        :return: the content of the file to include
        """
        try:
            with codecs.open(self.file, 'r', encoding='utf-8') as f:
                content = f.read()

        except UnicodeDecodeError:
            raise UnicodeDecodeError(
                DECODE_ERROR_MESSAGE_FORMAT.format(filename=self.file)
            )

        return content
