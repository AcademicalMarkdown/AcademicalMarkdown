import yaml

from src.compilers.common_compilers.base_compiler import BaseCompiler
from src.helpers.constants import YAML_PARSE_ERROR_FORMAT
from src.models.header_model import HeaderModel


class HeaderCompiler(HeaderModel, BaseCompiler):
    def load_header(self, header_yaml: str):
        """
        this function loads a yaml header into the object
        :param header_yaml: the header yaml text
        """
        # pyYaml do not accept yaml end with '---'
        if header_yaml.endswith('---'):
            header_yaml = header_yaml.strip('---')

        # try to parse the header yaml
        try:
            header_yaml_dict = yaml.safe_load(header_yaml)
        except yaml.YAMLError as error:
            raise yaml.YAMLError(
                YAML_PARSE_ERROR_FORMAT.format(error_message=str(error))
            )

        # load the dict
        self.load_dict(header_yaml_dict)

    def compile(self) -> str:
        """
        this function returns a yaml header that pandoc is happy about
        :return: a header with all the mdac content deleted
        """
        # try to delete constants
        try:
            del self.__header_dict__['constants']
        except KeyError:
            pass
        # try to delete output
        try:
            del self.__header_dict__['output']
        except KeyError:
            pass

        return yaml.safe_dump(self.__header_dict__,
                              explicit_start=True,
                              explicit_end=True)
