import re

from src.helpers.constants import MDAC_BLOCK_REGEX
from src.helpers.general_function import load_yaml
from src.models.block_model import BlockModel


class BlockParser(BlockModel):
    def __init__(self):
        super().__init__()
        self.meta_dict = {}  # the dict converted by meta_block

    def load_mdac_block(self, block_str: str):
        """
        this function load the mdac block into the current object
        :param block_str: the string that we want to load
        """
        match = re.match(pattern=MDAC_BLOCK_REGEX,
                         string=block_str)

        # extract data from match,
        # see constant -> MDAC_BLOCK_REGEX for more info
        block_type = match.group(2).strip().lower()
        content_block = match.group(3)
        meta_block = match.group(4)

        # construct the object
        self.__construct__(block_type=block_type,
                           content_block=content_block,
                           meta_block=meta_block)

    def convert_to_dict(self):
        """
        this method converts the current meta block into a dict
        """
        if self.meta_block:
            # attempting to load meta block
            self.meta_dict = load_yaml(self.meta_block)

    def parse(self, block_str: str):
        """
        parse the block that is send in
        :param block_str: the block sent in to parse
        """
        self.load_mdac_block(block_str)
        self.convert_to_dict()
