import codecs
import csv

from tabulate import tabulate
from typing import List

from src.compilers.base_compiler import BaseCompiler
from src.helpers.constants import LATEX_TABLE_FORMAT_STR, CSV_DELIMINATOR, \
    DECODE_ERROR_MESSAGE_FORMAT
from src.models.table_model import TableModel
from src.registers.common_register import CommonRegister


class TableCompilerLatex(TableModel, BaseCompiler):
    def load_dict(self, input_dict: dict):
        """
        call the super method (defined in BaseModel), then register the label
        :param input_dict: the input dict
        """
        # call the original load dict
        super().load_dict(input_dict)

        # register the label
        CommonRegister.register_new_label(self.label)

    @staticmethod
    def __get_csv_content__(file_name: str) -> List[List[str]]:
        """
        get the content of csv file, returns a list of list (iterable)
        :param file_name: the name of the csv file
                        Notice the CSV file is read via python default setting
        :return: the content of the csv file in list of list format
        """
        try:
            with codecs.open(file_name, encoding='utf-8') as f:
                # read the csv file
                content = csv.reader(f, delimiter=CSV_DELIMINATOR)

                # cast content to list (extract the content)
                # to prevent file close out side of with block
                content = list(content)
        except UnicodeDecodeError:
            raise UnicodeDecodeError(
                DECODE_ERROR_MESSAGE_FORMAT.format(filename=file_name)
            )

        return content

    def compile(self) -> str:
        """
        compile the class into pandoc table (simple table)
        :return: a simple table with caption and label
        """

        # put the file content into self.content
        if self.file:
            csv_matrix = self.__get_csv_content__(self.file)

            # assign headers
            if self.top_header:
                self.content = tabulate(csv_matrix, headers='firstrow')
            else:
                self.content = tabulate(csv_matrix)

        # return format
        return LATEX_TABLE_FORMAT_STR.format(
            content=self.content, caption=self.caption, label=self.label
        )
