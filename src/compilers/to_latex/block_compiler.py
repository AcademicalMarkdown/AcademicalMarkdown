from src.compilers.base_compiler import BaseCompiler
from src.compilers.block_parser import BlockParser
from src.compilers.to_latex.code_compiler_latex import CodeCompilerLatex
from src.compilers.to_latex.figure_compiler_latex import FigureCompilerLatex
from src.compilers.to_latex.include_compiler_latex import IncludeCompilerLatex
from src.compilers.to_latex.table_compiler_latex import TableCompilerLatex
from src.compilers.to_latex.theorem_compiler_latex import TheoremCompilerLatex


class BlockCompiler(BlockParser, BaseCompiler):
    def __init__(self):
        super().__init__()
        self.compiler = BaseCompiler()
        self.compiler_dict = {}
        self.type_to_compiler_dict = {
            'code': CodeCompilerLatex(),
            'figure': FigureCompilerLatex(),
            'include': IncludeCompilerLatex(),
            'table': TableCompilerLatex(),
            'theorem': TheoremCompilerLatex()
        }

    @property
    def use_raw_data(self) -> bool:
        """
        the does current block need to use raw data
        current method need to invoke after compile method
        :return: whether self.compiler uses raw_data
        """
        self.__find_compiler__()
        return self.compiler.use_raw_data()

    def __find_compiler__(self):
        """
        a helper to compile method, to find the compiler correspond to current
        block_type
        """
        try:
            # attempt to find the compiler
            self.compiler = self.type_to_compiler_dict[self.block_type]

        except KeyError:
            # find the match
            matches = [key for key in self.type_to_compiler_dict.keys()
                       if key.startswith(self.block_type)]
            # see if there is only one
            if len(matches) == 1:
                self.compiler = self.type_to_compiler_dict[matches[0]]
            # nothing matches the type you give
            if len(matches) == 0:
                raise KeyError
            # more than one thing matches the type you give
            else:
                raise KeyError

    def __get_compiler_dict__(self):
        """
        construct a dict that the can be send into the compiler
        """
        # add the get the para name of the content block
        content_para = self.compiler.get_content_data_name()

        # add the content block to meta dict
        self.compiler_dict = self.meta_dict.update(
            {content_para, self.content_block}
        )

    def compile(self) -> str:
        """
        return the compile result of current block
        :return: the compiled result of current block
        """
        # init
        self.__find_compiler__()
        self.__get_compiler_dict__()

        # compile
        self.compiler.load_dict(self.compiler_dict)
        return self.compiler.compile()
