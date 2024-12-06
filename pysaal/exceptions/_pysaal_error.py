from pysaal.enums._pysaal_error_code import PySAALErrorCode


class PySAALError(Exception):
    def __init__(self, code: PySAALErrorCode):
        if code == PySAALErrorCode.UNKNOWN:
            super().__init__("Unknown error")
        elif code == PySAALErrorCode.DUPLICATE_KEY:
            super().__init__("Duplicate key")
        elif code == PySAALErrorCode.BAD_KEY:
            super().__init__("Bad key")
