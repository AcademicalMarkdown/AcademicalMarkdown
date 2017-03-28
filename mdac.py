import sys

from fire import Fire

from info import PROJECT_ROOT_PATH
from mdac.__main__ import main

if __name__ == '__main__':
    sys.path.append(PROJECT_ROOT_PATH)
    Fire(main)
