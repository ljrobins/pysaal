from enum import Enum

from pysaal.lib._main_dll import BADKEY, DUPKEY


class PySAALKeyErrorCode(Enum):
    DUPLICATE_KEY = DUPKEY
    BAD_KEY = BADKEY
