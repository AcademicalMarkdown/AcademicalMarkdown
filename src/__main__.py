import logging

import pypandoc
from typing import Tuple, Union

from src.compilers.to_latex.main_latex_compiler import \
    compile_to_pandoc_for_latex, pre_compile
from src.helpers.constants import PANDOC_CONFIG_DEFAULTS, \
    DEFAULT_FILE_NAME_FORMAT_DICT
from src.registers.common_register import CommonRegister


def __validate_pandoc__():
    """
    validate whether pandoc exists
    """
    try:
        pypandoc.get_pandoc_version()
    except OSError:
        option = input(
            "pandoc not found, do you want to install? enter [Y/N]: ")
        if option.lower().startswith('y'):
            pypandoc.download_pandoc()
        else:
            raise OSError('pandoc requirement not found in path')


def __invoke_pandoc__(input_content: str, output_format: str,
                      extra_args: dict, output_file: str, default: dict):
    """
    invoke pandoc via pypandoc.
    :param output_file: the file name of the output file 
    :param default: the default argument dict.
                    the key is long name of the para, the 
    :param input_content: the markdown content ready to be compiled
    :param output_format: a string indicate the output format of the file
                            like 'beamer', 'pdf', 'html')
    :param extra_args: all the other argument that pandoc accepts
    """

    def __convert_arg(arg: Tuple[str, Union[str, bool, list]]):
        """
        a helper that converts the a arg tuple into regular command line arg
        :param arg: a tuple, where the first is the long name of the argument
                    the second is the value of the argument
        :return: if the second one is a bool, 
        """
        # extract info from arg
        arg_name = arg[0]
        val = arg[1]

        # if the value is true
        # if the second element is false it should be filtered out by
        # the parent function
        if val is True:
            return '--{arg}'.format(arg=arg_name)

        # if the value is a list
        # gives the
        elif isinstance(val, list):
            return ' '.join("--{arg}={val}".format(arg=arg_name, val=element)
                            for element in val)

        # if the val is a string
        else:
            return "--{arg}={val}".format(arg=arg_name, val=val)

    # merge the two dict
    arg_dict = default.copy()
    arg_dict.update(extra_args)  # default will be overloaded via extra_args

    # convert extra args to list
    # exclude where the second one is false
    converted_args = [__convert_arg(arg) for arg in arg_dict.items()
                      if arg[1] is not False]

    # invoke pandoc
    pypandoc.convert_text(source=input_content, format='md',
                          to=output_format, outputfile=output_file,
                          extra_args=converted_args)


def __load_default__(output_format: str) -> dict:
    """
    return the default configuration of current output format
    :param output_format: a string representing the output format
    :return: a dict which key is the parameter long name, the value is the 
                value of the parameter
    """
    # get the default config dict
    try:
        res_dict = PANDOC_CONFIG_DEFAULTS[output_format]
    except KeyError:
        res_dict = {}

    return res_dict


def __get_output_format__(config):
    """
    extract the output format from the configs
    :param config: a dict of configs that represents the pandoc cli args
    :return: get the output format from the config files.
                if there is no format, then raise an error
    """
    output_format = ''  # set default output format

    # try to get output format
    try:
        output_format = config['to']
        del config['to']
    except KeyError:
        pass
    try:
        output_format = config['write']
        del config['write']
    except KeyError:
        pass
    try:
        output_format = config['format']
        del config['format']
    except KeyError:
        pass

    # raise error when there is no output format provided
    if not output_format:
        raise IOError

    return output_format


def __get_output_filename__(input_file: str, config, output_format):
    """
    return the output file name extracted from config
    :param input_file: the input file's name
    :param config: the config dict, representing the cli args of pandoc
    :param output_format: the output format, like 'html'
    :return: if there is a output file specified in config, then use that.
                if none specified, then get a file name from input file and
                            output format
    """
    # find the output file name
    # remove the extension and to find the file name
    file_name = '.'.join(input_file.split('.')[:-1])
    # construct the default filename
    output_file = DEFAULT_FILE_NAME_FORMAT_DICT[
        output_format].format(
        file_name=file_name
    )
    try:
        output_file = config['output']
        del config['output']
    except KeyError:
        pass

    return output_file


def __get_compile_function__(output_format: str):
    FORMAT_TO_COMPILER_FUNCTION_DICT = {
        'pdf': compile_to_pandoc_for_latex,
        'latex': compile_to_pandoc_for_latex,
        'beamer': compile_to_pandoc_for_latex
    }

    return FORMAT_TO_COMPILER_FUNCTION_DICT[output_format]


def __compile_with_reg_data__(mdac_file: str):
    """
    compile the mdac document using information about the output config in the 
    common register
    :param mdac_file: the md file that needed to be converted by pandoc
    """
    # get the content of the mdac file
    with open(mdac_file, 'r', encoding='utf-8') as f:
        mdac_content = f.read()

    # pre compile to load the data
    pre_compile_res = pre_compile(mdac_content)

    # get the output config
    output_configs = CommonRegister.get_output_configs()

    # invoke pandoc from all the configs
    for config in output_configs:
        # get the output format
        output_format = __get_output_format__(config)

        # load the default of the current output format
        default_config = __load_default__(output_format=output_format)

        # get the output filename
        output_file = __get_output_filename__(input_file=mdac_file,
                                              config=config,
                                              output_format=output_format)

        # compile the file to pandoc markdown
        compile_function = __get_compile_function__(output_format)
        compile_res = compile_function(pre_compile_res=pre_compile_res)

        # check if pandoc exists
        __validate_pandoc__()

        # invoke the pandoc
        __invoke_pandoc__(input_content=compile_res,
                          output_file=output_file,
                          output_format=output_format,
                          extra_args=config, default=default_config)


def main(input_file, output_file='', output_format='', extra_args=None):
    """
    the main process
    :param input_file: the path of input mdac file 
    :param output_file: the output file full path
    :param output_format: the output format of the file
    :param extra_args: a list of extra arguments provided to pandoc
    """
    if output_format:
        logging.warning('it is recommend to include command line arguments in'
                        'your mdac file meta')

        # get the file name if no file name is specified
        if not output_file:
            output_file = __get_output_filename__(input_file=input_file,
                                                  config={},
                                                  output_format=output_format)

        compile_function = __get_compile_function__(output_format)

        with open(input_file, 'r', encoding='utf-8') as f:
            input_content = f.read()

        pre_compile_res = pre_compile(input_content)

        compile_res = compile_function(pre_compile_res)

        pypandoc.convert_text(source=compile_res,
                              outputfile=output_file,
                              format='md',
                              to=output_format,
                              extra_args=extra_args)

    else:
        __compile_with_reg_data__(input_file)
