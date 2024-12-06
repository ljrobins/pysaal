from ctypes import Array, c_char, c_double

from pysaal.enums import PySAALErrorCode, TLEClassification, TLEType
from pysaal.exceptions import PySAALError
from pysaal.lib import DLLs
from pysaal.lib._tle import (
    XA_TLE_AGOMGP,
    XA_TLE_BSTAR,
    XA_TLE_BTERM,
    XA_TLE_ECCEN,
    XA_TLE_ELSETNUM,
    XA_TLE_EPHTYPE,
    XA_TLE_EPOCH,
    XA_TLE_INCLI,
    XA_TLE_MNANOM,
    XA_TLE_MNMOTN,
    XA_TLE_NDOT,
    XA_TLE_NDOTDOT,
    XA_TLE_NODE,
    XA_TLE_OMEGA,
    XA_TLE_REVNUM,
    XA_TLE_SATNUM,
    XA_TLE_SIZE,
    XA_TLE_SP_AGOM,
    XA_TLE_SP_BTERM,
    XA_TLE_SP_OGPARM,
    XS_TLE_SATNAME_1_12,
    XS_TLE_SECCLASS_0_1,
    XS_TLE_SIZE,
)
from pysaal.math.constants import B_STAR_TO_B_TERM_COEFFICIENT
from pysaal.time import Epoch


class TLE:

    MAX_SATELLITE_ID = 339999
    MAX_DESIGNATOR_LENGTH = 8

    def __init__(self, line_1: str, line_2: str):

        self.c_double_array, self.c_char_array = TLE.get_null_pointers()
        DLLs.tle.TleLinesToArray(line_1.encode(), line_2.encode(), self.c_double_array, self.c_char_array)
        self.loaded = False
        self.key = None
        self.name = self.designator

    @staticmethod
    def get_null_pointers() -> tuple[Array[c_double], Array[c_char]]:
        xa_tle = (c_double * XA_TLE_SIZE)()
        xs_tle = (c_char * XS_TLE_SIZE)()
        return xa_tle, xs_tle

    @staticmethod
    def get_number_in_memory() -> int:
        return DLLs.tle.TleGetCount()

    def update(self) -> None:
        if self.loaded and self.key is not None:
            DLLs.tle.TleUpdateSatFrArray(self.key, self.c_double_array, self.c_char_array)

    def destroy(self) -> None:
        if self.loaded and self.key is not None:
            DLLs.tle.TleRemoveSat(self.key)
            self.key = None
            self.loaded = False

    def load(self) -> None:
        key = DLLs.tle.TleAddSatFrArray(self.c_double_array, self.c_char_array)
        if key in PySAALErrorCode:
            raise PySAALError(PySAALErrorCode(key))
        self.key = key
        self.loaded = True

    @property
    def classification(self) -> TLEClassification:
        return TLEClassification(self.c_char_array.value.decode()[XS_TLE_SECCLASS_0_1])

    @classification.setter
    def classification(self, value: TLEClassification):
        self.c_char_array[XS_TLE_SECCLASS_0_1] = value.value.encode()
        self.update()

    @property
    def designator(self) -> str:
        idx_start = XS_TLE_SATNAME_1_12
        idx_end = idx_start + TLE.MAX_DESIGNATOR_LENGTH
        return self.c_char_array.value.decode()[idx_start:idx_end].strip()

    @designator.setter
    def designator(self, value: str):
        if len(value) > self.MAX_DESIGNATOR_LENGTH:
            raise ValueError(f"Name exceeds maximum length of {self.MAX_DESIGNATOR_LENGTH}")

        idx_start = XS_TLE_SATNAME_1_12
        idx_end = idx_start + TLE.MAX_DESIGNATOR_LENGTH
        self.c_char_array[idx_start:idx_end] = f"{value: <{TLE.MAX_DESIGNATOR_LENGTH}}".encode()  # type: ignore
        self.update()

    @property
    def lines(self) -> tuple[str, str]:
        line_1 = (c_char * XS_TLE_SIZE)()
        line_2 = (c_char * XS_TLE_SIZE)()
        DLLs.tle.TleGPArrayToLines(self.c_double_array, self.c_char_array, line_1, line_2)
        return line_1.value.decode().strip(), line_2.value.decode().strip()

    @property
    def line_1(self) -> str:
        return self.lines[0]

    @property
    def line_2(self) -> str:
        return self.lines[1]

    @property
    def satellite_id(self) -> int:
        return int(self.c_double_array[XA_TLE_SATNUM])

    @satellite_id.setter
    def satellite_id(self, value: int):
        if value > self.MAX_SATELLITE_ID:
            raise ValueError(f"Satellite ID exceeds maximum value of {self.MAX_SATELLITE_ID}")
        self.c_double_array[XA_TLE_SATNUM] = float(value)
        self.update()

    @property
    def epoch(self) -> Epoch:
        return Epoch(self.c_double_array[XA_TLE_EPOCH])

    @epoch.setter
    def epoch(self, value: Epoch):
        self.c_double_array[XA_TLE_EPOCH] = value.utc_ds50
        self.update()

    @property
    def ndot(self) -> float:
        """Mean motion derivative (rev/day /2)"""
        return self.c_double_array[XA_TLE_NDOT]

    @property
    def ndotdot(self) -> float:
        """Mean motion second derivative (rev/day**2 /6)"""
        return self.c_double_array[XA_TLE_NDOTDOT]

    @property
    def b_star(self) -> float:
        """B* drag term (1/er)"""
        return self.c_double_array[XA_TLE_BSTAR]

    @property
    def ephemeris_type(self) -> TLEType:
        return TLEType(self.c_double_array[XA_TLE_EPHTYPE])

    @property
    def inclination(self) -> float:
        """Orbit inclination (deg)"""
        return self.c_double_array[XA_TLE_INCLI]

    @property
    def raan(self) -> float:
        """Right ascension of ascending node (deg)"""
        return self.c_double_array[XA_TLE_NODE]

    @property
    def eccentricity(self) -> float:
        return self.c_double_array[XA_TLE_ECCEN]

    @property
    def argument_of_perigee(self) -> float:
        """Argument of perigee (deg)"""
        return self.c_double_array[XA_TLE_OMEGA]

    @property
    def mean_anomaly(self) -> float:
        """Mean anomaly (deg)"""
        return self.c_double_array[XA_TLE_MNANOM]

    @property
    def mean_motion(self) -> float:
        """Mean motion (rev/day)"""
        return self.c_double_array[XA_TLE_MNMOTN]

    @property
    def revolution_number(self) -> int:
        return int(self.c_double_array[XA_TLE_REVNUM])

    @property
    def element_set_number(self) -> int:
        return int(self.c_double_array[XA_TLE_ELSETNUM])

    @property
    def ballistic_coefficient(self) -> float:
        """Ballistic coefficient (m2/kg)"""
        if self.ephemeris_type == TLEType.SP:
            bc = self.c_double_array[XA_TLE_SP_BTERM]
        elif self.ephemeris_type == TLEType.XP:
            bc = self.c_double_array[XA_TLE_BTERM]
        else:
            bc = B_STAR_TO_B_TERM_COEFFICIENT * self.c_double_array[XA_TLE_BSTAR]
        return bc

    @property
    def agom(self) -> float:
        """Solar radiation pressure (m2/kg)"""
        if self.ephemeris_type == TLEType.SP:
            agom = self.c_double_array[XA_TLE_SP_AGOM]
        elif self.ephemeris_type == TLEType.XP:
            agom = self.c_double_array[XA_TLE_AGOMGP]
        else:
            agom = 0.0
        return agom

    @property
    def outgassing_parameter(self) -> float:
        """Outgassing parameter (km/s2)"""
        if self.ephemeris_type == TLEType.SP:
            ogparm = self.c_double_array[XA_TLE_SP_OGPARM]
        else:
            ogparm = 0.0
        return ogparm
