from ctypes import c_char, c_double, c_int
from datetime import datetime, timezone

from pysaal.lib import DLLs


class Epoch:
    """Class used to represent an epoch in DS50 format for use with the SAAL library"""

    def __init__(self, epoch: float):
        """Basic constructor

        :param epoch: The epoch in DS50 format
        """

        #: The epoch in UTC days since 1950
        self.utc_ds50 = epoch

    def __add__(self, other: float) -> "Epoch":
        return Epoch(self.utc_ds50 + other)

    def __sub__(self, other: float) -> "Epoch":
        return Epoch(self.utc_ds50 - other)

    def __lt__(self, other: "Epoch") -> bool:
        return self.utc_ds50 < other.utc_ds50

    def __le__(self, other: "Epoch") -> bool:
        return self.utc_ds50 <= other.utc_ds50

    def __gt__(self, other: "Epoch") -> bool:
        return self.utc_ds50 > other.utc_ds50

    def __ge__(self, other: "Epoch") -> bool:
        return self.utc_ds50 >= other.utc_ds50

    def __eq__(self, other) -> bool:
        if not isinstance(other, Epoch):
            return False
        return self.utc_ds50 == other.utc_ds50

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.utc_ds50)

    @property
    def greenwich_angle(self) -> float:
        """Return the Greenwich angle in radians using the FK theory loaded to the environment constants."""
        return DLLs.time_func.ThetaGrnwch(self.utc_ds50, DLLs.env_const.EnvGetFkPtr())

    @property
    def fk4_greenwich_angle(self) -> float:
        """Return the Greenwich angle using the Fourth Fundamental Catalog (FK4) in radians."""
        return DLLs.time_func.ThetaGrnwchFK4(self.utc_ds50)

    @property
    def fk5_greenwich_angle(self) -> float:
        """Return the Greenwich angle using the Fifth Fundamental Catalog (FK5) in radians."""
        return DLLs.time_func.ThetaGrnwchFK5(self.utc_ds50)

    @property
    def datetime(self) -> datetime:
        """Return the Epoch as a datetime object."""
        year = c_int()
        month = c_int()
        day = c_int()
        hour = c_int()
        minute = c_int()
        sec = c_double()
        DLLs.time_func.UTCToTimeComps2(self.utc_ds50, year, month, day, hour, minute, sec)
        tz = timezone.utc
        return datetime(year.value, month.value, day.value, hour.value, minute.value, int(sec.value), tzinfo=tz)

    @property
    def year(self) -> int:
        """Return the year of the Epoch."""
        year = c_int()
        DLLs.time_func.UTCToTimeComps2(self.utc_ds50, year, c_int(), c_int(), c_int(), c_int(), c_double())
        return year.value

    @property
    def month(self) -> int:
        """Return the month of the Epoch."""
        month = c_int()
        DLLs.time_func.UTCToTimeComps2(self.utc_ds50, c_int(), month, c_int(), c_int(), c_int(), c_double())
        return month.value

    @property
    def day(self) -> int:
        """Return the day of the Epoch."""
        day = c_int()
        DLLs.time_func.UTCToTimeComps2(self.utc_ds50, c_int(), c_int(), day, c_int(), c_int(), c_double())
        return day.value

    @property
    def hour(self) -> int:
        """Return the hour of the Epoch."""
        hour = c_int()
        DLLs.time_func.UTCToTimeComps2(self.utc_ds50, c_int(), c_int(), c_int(), hour, c_int(), c_double())
        return hour.value

    @property
    def minute(self) -> int:
        """Return the minute of the Epoch."""
        minute = c_int()
        DLLs.time_func.UTCToTimeComps2(self.utc_ds50, c_int(), c_int(), c_int(), c_int(), minute, c_double())
        return minute.value

    @property
    def second(self) -> float:
        """Return the second of the Epoch."""
        sec = c_double()
        DLLs.time_func.UTCToTimeComps2(self.utc_ds50, c_int(), c_int(), c_int(), c_int(), c_int(), sec)
        return sec.value

    @property
    def day_of_year(self) -> int:
        """Return the day of year of the Epoch."""
        day_of_year = c_int()
        DLLs.time_func.UTCToTimeComps1(self.utc_ds50, c_int(), day_of_year, c_int(), c_int(), c_double())
        return day_of_year.value

    @property
    def tai_ds50(self) -> float:
        """Return the TAI time in DS50 format."""
        return DLLs.time_func.UTCToTAI(self.utc_ds50)

    @property
    def ut1_ds50(self) -> float:
        """Return the UT1 time in DS50 format."""
        return DLLs.time_func.UTCToUT1(self.utc_ds50)

    @property
    def tt_ds50(self) -> float:
        """Return the TT time in DS50 format."""
        return DLLs.time_func.UTCToET(self.utc_ds50)

    @property
    def dtg_20(self) -> str:
        """Convert the Epoch to a DTG20 string in YYYY/DOY HHMM SS.SSS format."""
        dtg20 = (c_char * 20)()
        DLLs.time_func.UTCToDTG20(self.utc_ds50, dtg20)
        return dtg20.value.decode()

    @property
    def dtg_19(self) -> str:
        """Convert the Epoch to a DTG19 string in YYYYMonDDHHMMSS.SSS format."""
        dtg19 = (c_char * 19)()
        DLLs.time_func.UTCToDTG19(self.utc_ds50, dtg19)
        return dtg19.value.decode()

    @property
    def dtg_17(self) -> str:
        """Convert the Epoch to a DTG17 string in YYYY/DOY.DDDDDDDD format."""
        dtg17 = (c_char * 17)()
        DLLs.time_func.UTCToDTG17(self.utc_ds50, dtg17)
        return dtg17.value.decode()

    @property
    def dtg_15(self) -> str:
        """Convert the Epoch to a DTG15 string in YYDOYHHMMSS.SSS format."""
        dtg15 = (c_char * 15)()
        DLLs.time_func.UTCToDTG15(self.utc_ds50, dtg15)
        return dtg15.value.decode()

    @classmethod
    def from_year_and_days(cls, year: int, days: float) -> "Epoch":
        """Instantiate an Epoch from a year and days.

        :param year: year
        :param days: days
        """
        return cls(DLLs.time_func.YrDaysToUTC(c_int(year), c_double(days)))

    @classmethod
    def from_dtg(cls, dtg: str) -> "Epoch":
        """Instantiate an Epoch from a DTG string.

        .. note::

            Supported formats:

            * "YYYY/DOY HHMM SS.SSS"
            * "YYYYMonDDHHMMSS.SSS"
            * "YYYY/DOY.DDDDDDDD"
            * "YYDOYHHMMSS.SSS"

        :param dtg: DTG string in any of the supported formats
        """
        return cls(DLLs.time_func.DTGToUTC(dtg.encode()))

    @classmethod
    def from_components(cls, yr: int, mon: int, day: int, hr: int, minute: int, sec: float) -> "Epoch":
        """Instantiate an Epoch from traditional date and time components.

        :param yr: year
        :param mon: month
        :param day: day
        :param hr: hour
        :param minute: minute
        :param sec: second
        """
        c_year = c_int(yr)
        c_mon = c_int(mon)
        c_day = c_int(day)
        c_hr = c_int(hr)
        c_min = c_int(minute)
        c_sec = c_double(sec)
        return cls(DLLs.time_func.TimeComps2ToUTC(c_year, c_mon, c_day, c_hr, c_min, c_sec))

    @staticmethod
    def time_constants_loaded() -> bool:
        """Check to see if a time constants file has been loaded.

        :return: True if a time constants file has been loaded, False otherwise
        """
        return bool(DLLs.time_func.IsTConFileLoaded())
