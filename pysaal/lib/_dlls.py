from ctypes import Array, c_char, c_int, create_string_buffer
from pathlib import Path

from pysaal.lib._astro_func import get_astro_func_dll
from pysaal.lib._el_ops import get_el_ops_dll
from pysaal.lib._env_const import get_env_const_dll
from pysaal.lib._ext_ephem import get_ext_ephem_dll
from pysaal.lib._main_dll import FILEPATHLEN, GETSETSTRLEN, INFOSTRLEN, LOGMSGLEN, get_main_dll
from pysaal.lib._sgp4_prop import get_sgp4_prop_dll
from pysaal.lib._sp_vec import get_sp_vec_dll
from pysaal.lib._time_func import get_time_func_dll
from pysaal.lib._tle import get_tle_dll
from pysaal.lib._vcm import get_vcm_dll


class DLLs:

    FILE_PATH_LENGTH = FILEPATHLEN
    GET_SET_STRING_LENGTH = GETSETSTRLEN
    INFO_STRING_LENGTH = INFOSTRLEN
    LOG_MESSAGE_LENGTH = LOGMSGLEN

    main = get_main_dll()
    env_const = get_env_const_dll()
    time_func = get_time_func_dll()
    astro_func = get_astro_func_dll()
    tle = get_tle_dll()
    sgp4_prop = get_sgp4_prop_dll()
    vcm = get_vcm_dll()
    sp_vec = get_sp_vec_dll()
    ext_ephem = get_ext_ephem_dll()
    el_ops = get_el_ops_dll()

    @staticmethod
    def get_null_string() -> Array[c_char]:
        return create_string_buffer(DLLs.GET_SET_STRING_LENGTH + 1)

    @staticmethod
    def get_last_error_message() -> str:
        stbuf = create_string_buffer(DLLs.GET_SET_STRING_LENGTH + 1)
        DLLs.main.GetLastErrMsg(stbuf)
        return stbuf.value.decode("utf-8").strip()

    @staticmethod
    def get_last_info_message() -> str:
        stbuf = create_string_buffer(DLLs.LOG_MESSAGE_LENGTH + 1)
        DLLs.main.GetLastInfoMsg(stbuf)
        return stbuf.value.decode("utf-8").strip()

    @staticmethod
    def open_log_file(log_path: Path) -> None:
        """Opens a log file for writing.

        .. notes::
            * The log file will be created if it does not exist.
            * If the log file exists, it will be overwritten.
            * close_log_file() should be called when finished with the log.
            * Due to memory usage, the log should only be used for debugging purposes.

        :param filename: Path to the log file.
        """
        DLLs.main.OpenLogFile(log_path.as_posix().encode())

    @staticmethod
    def close_log_file() -> None:
        DLLs.main.CloseLogFile()

    @staticmethod
    def log_message(msg: str) -> None:
        DLLs.main.LogMessage(msg.encode())

    @staticmethod
    def allow_duplicate_keys(allow: bool) -> None:
        DLLs.main.SetAllKeyMode(c_int(allow))
