from enum import Enum

from pysaal.lib._main_dll import BADKEY, DUPKEY


class PySAALErrorCode(Enum):
    DUPLICATE_KEY = DUPKEY
    BAD_KEY = BADKEY
    UNKNOWN = 1
    SEG_FAULT = 2
