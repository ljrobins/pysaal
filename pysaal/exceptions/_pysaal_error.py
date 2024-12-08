from pysaal.lib import DLLs


class PySAALError(Exception):
    def __init__(self):
        super().__init__(DLLs.get_last_error_message())
