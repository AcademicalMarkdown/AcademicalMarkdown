from typing import Tuple

from src.helpers.general_function import load_yaml
from src.models.block_model import BlockModel


class BlockParser(BlockModel):
    def __init__(self):
        super().__init__()
        self.meta_dict = {}  # the dict converted by meta_block

    def load_match_obj(self, match_obj: Tuple[str]):
        # extract data from match,
        # see constant -> MDAC_BLOCK_REGEX for more info
        block_type = match_obj[1].strip().lower()
        content_block = match_obj[2].strip()
        try:
            meta_block = match_obj[3]
        except IndexError:
            meta_block = ''

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

    def parse(self, match_ob: tuple):
        """
        parse the block that is send in
        :param match_ob: the block sent in to parse
        """
        self.load_match_obj(match_ob)
        self.convert_to_dict()
