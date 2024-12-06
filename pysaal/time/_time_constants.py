from ctypes import c_double, c_int
from pathlib import Path

from pysaal.lib import DLLs
from pysaal.time._epoch import Epoch
from pysaal.time._time_span import TimeSpan


class TimeConstants:
    def __init__(self, epoch: Epoch, tai_utc: float, ut1_utc: float, ut1_rate: float, polar_x: float, polar_y: float):
        self.epoch = epoch
        self.tai_minus_utc = tai_utc  # TAI minus UTC offset at requested time (seconds)
        self.ut1_minus_utc = ut1_utc  # UT1 minus UTC offset at requested time (seconds)
        self.ut1_rate = ut1_rate  # UT1 rate of change versus UTC at Reference time (msec/day)
        self.polar_x = polar_x  # Interpolated polar wander (X direction) at requested time (arc-seconds)
        self.polar_y = polar_y  # Interpolated polar wander (Y direction) at requested time (arc-seconds)

    @classmethod
    def from_epoch(cls, epoch: Epoch) -> "TimeConstants":
        tai_minus_utc = c_double()
        ut1_minus_utc = c_double()
        ut1_rate = c_double()
        polar_x = c_double()
        polar_y = c_double()
        DLLs.time_func.UTCToTConRec(epoch.utc_ds50, tai_minus_utc, ut1_minus_utc, ut1_rate, polar_x, polar_y)
        return cls(epoch, tai_minus_utc.value, ut1_minus_utc.value, ut1_rate.value, polar_x.value, polar_y.value)

    @staticmethod
    def is_file_loaded() -> bool:
        return DLLs.time_func.IsTConFileLoaded()

    @staticmethod
    def load_file(file_path: Path) -> None:
        DLLs.time_func.TConLoadFile(file_path.as_posix().encode())

    @staticmethod
    def get_loaded_time_span() -> TimeSpan:
        num_loaded = c_int()
        start = c_double()
        end = c_double()
        DLLs.time_func.TConTimeSpan(num_loaded, start, end)
        return TimeSpan(Epoch(start.value), Epoch(end.value))
