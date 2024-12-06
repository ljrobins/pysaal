from pysaal.enums._pysaal_error_code import PySAALErrorCode
from pysaal.lib import DLLs


class PySAALError(Exception):

    SUCCESS_CODE = 0

    def __init__(self, code: PySAALErrorCode):
        if code == PySAALErrorCode.DUPLICATE_KEY:
            super().__init__("Duplicate key")
        elif code == PySAALErrorCode.BAD_KEY:
            super().__init__("Bad key")
        else:
            super().__init__(DLLs.get_last_error_message())
