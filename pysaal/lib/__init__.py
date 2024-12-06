from pathlib import Path
from ctypes import c_double, c_int

from pysaal.lib._dlls import DLLs

# Generate the SGP4 license file if it does not exist.
SGP4_LICENSE_PATH = Path.cwd() / "SGP4_Open_License.txt"
if not SGP4_LICENSE_PATH.exists():
    _res_lic_path = Path(__file__).parent / "SGP4_Open_License.txt"
    SGP4_LICENSE_PATH.write_bytes(_res_lic_path.read_bytes())


# Load the time constants for accurate time conversions.
TIME_CONSTANTS_PATH = Path(__file__).parent / "time_constants.dat"
DLLs.time_func.TConLoadFile(TIME_CONSTANTS_PATH.as_posix().encode())

# Load the JPL DE405 ephemeris data for accurate planetary positions.
JPL_DE405_PATH = Path(__file__).parent / "JPLcon_1950_2050.405"
_jpl_start = c_double(DLLs.time_func.YrDaysToUTC(c_int(1960), c_double(1.0)))
_jpl_end = c_double(DLLs.time_func.YrDaysToUTC(c_int(2050), c_double(1.0)))
DLLs.astro_func.JplSetParameters(JPL_DE405_PATH.as_posix().encode(), _jpl_start, _jpl_end)

__all__ = ["DLLs"]
