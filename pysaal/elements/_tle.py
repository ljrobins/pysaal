from ctypes import Array, c_char, c_double, c_longlong
from pathlib import Path

from pysaal.elements._cartesian_elements import CartesianElements
from pysaal.elements._lla import LLA
from pysaal.elements._propagated_tle import PropagatedTLE
from pysaal.enums import Classification, PySAALKeyErrorCode, SGP4EpochType, SGP4ErrorCode, TLEType
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
from pysaal.math.linalg import Vector3D
from pysaal.time import Epoch


class TLE:

    MAX_SATELLITE_ID = 339999
    MAX_DESIGNATOR_LENGTH = 8

    def __init__(self):

        self.c_double_array, self.c_char_array = TLE.get_null_pointers()
        self.loaded = False
        self.key = None
        self.name = self.designator

    @classmethod
    def from_lines(cls, line_1: str, line_2: str) -> "TLE":
        tle = cls()
        DLLs.tle.TleLinesToArray(line_1.encode(), line_2.encode(), tle.c_double_array, tle.c_char_array)
        tle.name = tle.designator
        return tle

    @classmethod
    def from_key(cls, key: c_longlong) -> "TLE":
        line_1 = (c_char * XS_TLE_SIZE)()
        line_2 = (c_char * XS_TLE_SIZE)()
        status = DLLs.tle.TleGetLines(key, line_1, line_2)
        if status != SGP4ErrorCode.NONE.value:
            raise PySAALError
        tle = cls.from_lines(line_1.value.decode().strip(), line_2.value.decode().strip())
        tle.loaded = True
        tle.key = key
        return tle

    @classmethod
    def from_c_arrays(cls, c_double_array: Array[c_double], c_char_array: Array[c_char]) -> "TLE":
        line_1 = (c_char * XS_TLE_SIZE)()
        line_2 = (c_char * XS_TLE_SIZE)()
        DLLs.tle.TleGPArrayToLines(c_double_array, c_char_array, line_1, line_2)
        return cls.from_lines(line_1.value.decode().strip(), line_2.value.decode().strip())

    @staticmethod
    def write_loaded_tles_to_file(file_path: Path) -> None:
        DLLs.tle.TleSaveFile(file_path.as_posix().encode(), 0, 0)

    @staticmethod
    def get_null_pointers() -> tuple[Array[c_double], Array[c_char]]:
        xa_tle = (c_double * XA_TLE_SIZE)()
        xs_tle = (c_char * XS_TLE_SIZE)()
        return xa_tle, xs_tle

    @staticmethod
    def destroy_all() -> None:
        DLLs.tle.TleRemoveAllSats()
        DLLs.sgp4_prop.Sgp4RemoveAllSats()

    @staticmethod
    def get_number_in_memory() -> int:
        return DLLs.tle.TleGetCount()

    @property
    def cartesian_elements(self) -> CartesianElements:
        return self.get_state_at_epoch(Epoch(self.epoch.utc_ds50)).cartesian_elements

    @property
    def lla(self) -> LLA:
        return self.get_state_at_epoch(Epoch(self.epoch.utc_ds50)).lla

    @property
    def position(self) -> Vector3D:
        return self.cartesian_elements.position

    @property
    def velocity(self) -> Vector3D:
        return self.cartesian_elements.velocity

    @property
    def longitude(self) -> float:
        return self.lla.longitude

    @property
    def latitude(self) -> float:
        return self.lla.latitude

    @property
    def altitude(self) -> float:
        return self.lla.altitude

    def update(self) -> None:
        if self.loaded and self.key is not None:
            DLLs.tle.TleUpdateSatFrArray(self.key, self.c_double_array, self.c_char_array)

    def get_range_at_epoch(self, epoch: Epoch, other: "TLE") -> float:
        pri_state = self.get_state_at_epoch(epoch)
        sec_state = other.get_state_at_epoch(epoch)
        return (pri_state.position - sec_state.position).magnitude

    def destroy(self) -> None:
        if self.loaded and self.key is not None:
            DLLs.tle.TleRemoveSat(self.key)
            DLLs.sgp4_prop.Sgp4RemoveSat(self.key)
            self.key = None
            self.loaded = False

    def load(self) -> None:
        if not self.loaded:
            key = DLLs.tle.TleAddSatFrArray(self.c_double_array, self.c_char_array)
            if key in PySAALKeyErrorCode:
                raise PySAALError
            status = DLLs.sgp4_prop.Sgp4InitSat(key)
            if status != SGP4ErrorCode.NONE.value:
                raise PySAALError
            self.key = key
            self.loaded = True

    def get_state_at_epoch(self, epoch: Epoch) -> PropagatedTLE:
        if not self.loaded:
            self.load()
        pos, vel = CartesianElements.get_null_pointers()
        llh = LLA.get_null_pointer()
        error = DLLs.sgp4_prop.Sgp4PropDs50UTC(self.key, epoch.utc_ds50, c_double(), pos, vel, llh)
        if error:
            raise PySAALError
        xa_sgp4_out = PropagatedTLE.null_pointer()
        error = DLLs.sgp4_prop.Sgp4PropAll(self.key, SGP4EpochType.UTC.value, epoch.utc_ds50, xa_sgp4_out)
        if error:
            raise PySAALError
        return PropagatedTLE.from_c_array(xa_sgp4_out)

    @staticmethod
    def get_loaded_keys() -> Array[c_longlong]:
        keys = (c_longlong * TLE.get_number_in_memory())()
        DLLs.tle.TleGetLoaded(9, keys)
        return keys

    @property
    def classification(self) -> Classification:
        return Classification(self.c_char_array.value.decode()[XS_TLE_SECCLASS_0_1])

    @classification.setter
    def classification(self, value: Classification):
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
    def n_dot(self) -> float:
        """Mean motion derivative (rev/day /2)"""
        return self.c_double_array[XA_TLE_NDOT]

    @n_dot.setter
    def n_dot(self, value: float):
        self.c_double_array[XA_TLE_NDOT] = value
        self.update()

    @property
    def n_dot_dot(self) -> float:
        """Mean motion second derivative (rev/day**2 /6)"""
        return self.c_double_array[XA_TLE_NDOTDOT]

    @n_dot_dot.setter
    def n_dot_dot(self, value: float):
        self.c_double_array[XA_TLE_NDOTDOT] = value
        self.update()

    @property
    def b_star(self) -> float:
        """B* drag term (1/er)"""
        if self.ephemeris_type == TLEType.SGP or self.ephemeris_type == TLEType.SGP4:
            b_star = self.c_double_array[XA_TLE_BSTAR]
        elif self.ephemeris_type == TLEType.SP:
            b_star = self.c_double_array[XA_TLE_SP_BTERM] / B_STAR_TO_B_TERM_COEFFICIENT
        elif self.ephemeris_type == TLEType.XP:
            b_star = self.c_double_array[XA_TLE_BTERM] / B_STAR_TO_B_TERM_COEFFICIENT
        return b_star

    @b_star.setter
    def b_star(self, value: float):
        if self.ephemeris_type == TLEType.SGP or self.ephemeris_type == TLEType.SGP4:
            self.c_double_array[XA_TLE_BSTAR] = value
        elif self.ephemeris_type == TLEType.SP:
            self.c_double_array[XA_TLE_SP_BTERM] = value * B_STAR_TO_B_TERM_COEFFICIENT
        elif self.ephemeris_type == TLEType.XP:
            self.c_double_array[XA_TLE_BTERM] = value * B_STAR_TO_B_TERM_COEFFICIENT
        self.update()

    @property
    def ephemeris_type(self) -> TLEType:
        return TLEType(self.c_double_array[XA_TLE_EPHTYPE])

    @ephemeris_type.setter
    def ephemeris_type(self, value: TLEType):
        self.c_double_array[XA_TLE_EPHTYPE] = value.value
        self.update()

    @property
    def inclination(self) -> float:
        """Orbit inclination (deg)"""
        return self.c_double_array[XA_TLE_INCLI]

    @inclination.setter
    def inclination(self, value: float):
        self.c_double_array[XA_TLE_INCLI] = value
        self.update()

    @property
    def raan(self) -> float:
        """Right ascension of ascending node (deg)"""
        return self.c_double_array[XA_TLE_NODE]

    @raan.setter
    def raan(self, value: float):
        self.c_double_array[XA_TLE_NODE] = value
        self.update()

    @property
    def eccentricity(self) -> float:
        return self.c_double_array[XA_TLE_ECCEN]

    @eccentricity.setter
    def eccentricity(self, value: float):
        self.c_double_array[XA_TLE_ECCEN] = value
        self.update()

    @property
    def argument_of_perigee(self) -> float:
        """Argument of perigee (deg)"""
        return self.c_double_array[XA_TLE_OMEGA]

    @argument_of_perigee.setter
    def argument_of_perigee(self, value: float):
        self.c_double_array[XA_TLE_OMEGA] = value
        self.update()

    @property
    def mean_anomaly(self) -> float:
        """Mean anomaly (deg)"""
        return self.c_double_array[XA_TLE_MNANOM]

    @mean_anomaly.setter
    def mean_anomaly(self, value: float):
        self.c_double_array[XA_TLE_MNANOM] = value
        self.update()

    @property
    def mean_motion(self) -> float:
        """Mean motion (rev/day)"""
        return self.c_double_array[XA_TLE_MNMOTN]

    @mean_motion.setter
    def mean_motion(self, value: float):
        self.c_double_array[XA_TLE_MNMOTN] = value
        self.update()

    @property
    def revolution_number(self) -> int:
        return int(self.c_double_array[XA_TLE_REVNUM])

    @revolution_number.setter
    def revolution_number(self, value: int):
        self.c_double_array[XA_TLE_REVNUM] = value
        self.update()

    @property
    def element_set_number(self) -> int:
        return int(self.c_double_array[XA_TLE_ELSETNUM])

    @element_set_number.setter
    def element_set_number(self, value: int):
        self.c_double_array[XA_TLE_ELSETNUM] = value
        self.update()

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

    @ballistic_coefficient.setter
    def ballistic_coefficient(self, value: float):
        if self.ephemeris_type == TLEType.SP:
            self.c_double_array[XA_TLE_SP_BTERM] = value
        elif self.ephemeris_type == TLEType.XP:
            self.c_double_array[XA_TLE_BTERM] = value
        else:
            self.c_double_array[XA_TLE_BSTAR] = value / B_STAR_TO_B_TERM_COEFFICIENT
        self.update()

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

    @agom.setter
    def agom(self, value: float):
        if self.ephemeris_type == TLEType.SP:
            self.c_double_array[XA_TLE_SP_AGOM] = value
        elif self.ephemeris_type == TLEType.XP:
            self.c_double_array[XA_TLE_AGOMGP] = value
        self.update()

    @property
    def outgassing_parameter(self) -> float:
        """Outgassing parameter (km/s2)"""
        if self.ephemeris_type == TLEType.SP:
            ogparm = self.c_double_array[XA_TLE_SP_OGPARM]
        else:
            ogparm = 0.0
        return ogparm

    @outgassing_parameter.setter
    def outgassing_parameter(self, value: float):
        if self.ephemeris_type == TLEType.SP:
            self.c_double_array[XA_TLE_SP_OGPARM] = value
        self.update()
