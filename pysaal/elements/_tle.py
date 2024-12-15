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
    """Class for Two-Line Element Sets (TLEs)."""

    #: Numbers above this value will not parse in accordance with the alpha-5 format.
    MAX_SATELLITE_ID = 339999

    #: Designators longer than this will not fit entirely in the allocated space for a TLE.
    MAX_DESIGNATOR_LENGTH = 8

    def __init__(self):

        self.c_double_array, self.c_char_array = TLE.get_null_pointers()

        #: Flag indicating if the TLE is loaded into memory
        self.loaded = False

        #: The key used to reference the TLE in memory
        self.key = None

        #: The name associated with the TLE
        self.name = self.designator

    @classmethod
    def from_lines(cls, line_1: str, line_2: str) -> "TLE":
        """Create a TLE object from two TLE lines.

        :param line_1: The first line of the TLE.
        :param line_2: The second line of the TLE.

        .. note::

            This is the preferred method for creating a TLE object.

        :example:

        .. code-block:: python

            from pysaal.elements import TLE

            line_1 = "1 25544U 98067A   24340.99323416 +.00018216  00000 0  32316-3 0 0999"
            line_2 = "2 25544  51.6388 184.2057 0007028 306.7642 201.1123 15.5026597648519"

            tle = TLE.from_lines(line_1, line_2)

            print(tle.satellite_id)

        """
        tle = cls()
        DLLs.tle.TleLinesToArray(line_1.encode(), line_2.encode(), tle.c_double_array, tle.c_char_array)
        tle.name = tle.designator
        return tle

    @classmethod
    def from_key(cls, key: c_longlong) -> "TLE":
        """Instantiate a TLE from a known key in memory

        :param key: The key associated with the TLE in memory
        """
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
        """Instantiate a TLE from c arrays that correspond to the required arguments for the SAAL functions

        :param c_double_array: The c_double array containing the TLE numeric fields
        :param c_char_array: The c_char array containing the TLE string fields

        .. note::

            This method is primarily for internal use.
        """
        line_1 = (c_char * XS_TLE_SIZE)()
        line_2 = (c_char * XS_TLE_SIZE)()
        DLLs.tle.TleGPArrayToLines(c_double_array, c_char_array, line_1, line_2)
        return cls.from_lines(line_1.value.decode().strip(), line_2.value.decode().strip())

    @staticmethod
    def write_loaded_tles_to_file(file_path: Path) -> None:
        """Write all files in memory to a file.

        :param file_path: The path to the file to write.
        """
        DLLs.tle.TleSaveFile(file_path.as_posix().encode(), 0, 0)

    @staticmethod
    def get_null_pointers() -> tuple[Array[c_double], Array[c_char]]:
        """Get null pointers for the c_double and c_char arrays used in the SAAL functions"""
        xa_tle = (c_double * XA_TLE_SIZE)()
        xs_tle = (c_char * XS_TLE_SIZE)()
        return xa_tle, xs_tle

    @staticmethod
    def destroy_all() -> None:
        """Remove all TLEs from memory"""
        DLLs.tle.TleRemoveAllSats()
        DLLs.sgp4_prop.Sgp4RemoveAllSats()

    @staticmethod
    def get_number_in_memory() -> int:
        """Get the number of TLEs in memory"""
        return DLLs.tle.TleGetCount()

    @property
    def state(self) -> PropagatedTLE:
        """Full orbit state at the current epoch.  See :ref:`propagated_tle` for details."""
        return self.get_state_at_epoch(self.epoch)

    @property
    def cartesian_elements(self) -> CartesianElements:
        r"""TEME position and velocity elements in :math:`km` and :math:`\frac{km}{s}`."""
        return self.state.cartesian_elements

    @property
    def lla(self) -> LLA:
        """Latitude, longitude, and altitude of the satellite"""
        return self.state.lla

    @property
    def position(self) -> Vector3D:
        """Position of the satellite in :math:`km`"""
        return self.cartesian_elements.position

    @property
    def velocity(self) -> Vector3D:
        r"""Velocity of the satellite in :math:`\frac{km}{s}`"""
        return self.cartesian_elements.velocity

    @property
    def longitude(self) -> float:
        """Longitude of the satellite in :math:`degrees`"""
        return self.lla.longitude

    @property
    def latitude(self) -> float:
        """Latitude of the satellite in :math:`degrees`"""
        return self.lla.latitude

    @property
    def altitude(self) -> float:
        """Altitude of the satellite in :math:`km`"""
        return self.lla.altitude

    def update(self) -> None:
        """Updates the TLE in memory

        .. note::

            This method is called when properties with affect the propagation of the TLE have changed.
        """
        if self.loaded and self.key is not None:
            DLLs.tle.TleUpdateSatFrArray(self.key, self.c_double_array, self.c_char_array)

    def get_range_at_epoch(self, epoch: Epoch, other: "TLE") -> float:
        """Get the range between two satellites at a given epoch

        :param epoch: The epoch at which to calculate the range
        :param other: The other TLE to compare
        :return: The range between the two satellites in :math:`km`
        """
        pri_state = self.get_state_at_epoch(epoch)
        sec_state = other.get_state_at_epoch(epoch)
        return (pri_state.position - sec_state.position).magnitude

    def destroy(self) -> None:
        """Remove the TLE from memory"""
        if self.loaded and self.key is not None:
            DLLs.tle.TleRemoveSat(self.key)
            DLLs.sgp4_prop.Sgp4RemoveSat(self.key)
            self.key = None
            self.loaded = False

    def load(self) -> None:
        """Load the TLE into memory"""
        if not self.loaded:
            key = DLLs.tle.TleAddSatFrArray(self.c_double_array, self.c_char_array)
            if key == PySAALKeyErrorCode.BAD_KEY.value or key == PySAALKeyErrorCode.DUPLICATE_KEY.value:
                raise PySAALError
            status = DLLs.sgp4_prop.Sgp4InitSat(key)
            if status != SGP4ErrorCode.NONE.value:
                raise PySAALError
            self.key = key
            self.loaded = True

    def get_state_at_epoch(self, epoch: Epoch) -> PropagatedTLE:
        """Get the full orbit state at a given epoch

        :param epoch: The epoch at which to calculate the state
        :raises PySAALError: If there is an error during propagation or the subsequent call to calculate the orbit
            state
        """
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
        """Get the keys of all TLEs in memory"""
        keys = (c_longlong * TLE.get_number_in_memory())()
        DLLs.tle.TleGetLoaded(9, keys)
        return keys

    @property
    def classification(self) -> Classification:
        """Classification of the satellite"""
        return Classification(self.c_char_array.value.decode()[XS_TLE_SECCLASS_0_1])

    @classification.setter
    def classification(self, value: Classification):
        self.c_char_array[XS_TLE_SECCLASS_0_1] = value.value.encode()
        self.update()

    @property
    def designator(self) -> str:
        """8-character designator of the satellite"""
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
        """The two lines of the TLE"""
        line_1 = (c_char * XS_TLE_SIZE)()
        line_2 = (c_char * XS_TLE_SIZE)()
        DLLs.tle.TleGPArrayToLines(self.c_double_array, self.c_char_array, line_1, line_2)
        return line_1.value.decode().strip(), line_2.value.decode().strip()

    @property
    def line_1(self) -> str:
        """The first line of the TLE"""
        return self.lines[0]

    @property
    def line_2(self) -> str:
        """The second line of the TLE"""
        return self.lines[1]

    @property
    def satellite_id(self) -> int:
        """The alpha-5 compatible satellite ID"""
        return int(self.c_double_array[XA_TLE_SATNUM])

    @satellite_id.setter
    def satellite_id(self, value: int):
        if value > self.MAX_SATELLITE_ID:
            raise ValueError(f"Satellite ID exceeds maximum value of {self.MAX_SATELLITE_ID}")
        self.c_double_array[XA_TLE_SATNUM] = float(value)
        self.update()

    @property
    def epoch(self) -> Epoch:
        """Epoch of the TLE"""
        return Epoch(self.c_double_array[XA_TLE_EPOCH])

    @epoch.setter
    def epoch(self, value: Epoch):
        self.c_double_array[XA_TLE_EPOCH] = value.utc_ds50
        self.update()

    @property
    def n_dot(self) -> float:
        r"""Mean motion derivative in :math:`\frac{rev}{2*day}`"""
        return self.c_double_array[XA_TLE_NDOT]

    @n_dot.setter
    def n_dot(self, value: float):
        self.c_double_array[XA_TLE_NDOT] = value
        self.update()

    @property
    def n_dot_dot(self) -> float:
        r"""Mean motion second derivative in :math:`\frac{rev}{6*day^2}`"""
        return self.c_double_array[XA_TLE_NDOTDOT]

    @n_dot_dot.setter
    def n_dot_dot(self, value: float):
        self.c_double_array[XA_TLE_NDOTDOT] = value
        self.update()

    @property
    def b_star(self) -> float:
        r"""B* drag term in :math:`\frac{1}{er}`"""
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
        """Ephemeris type of the TLE"""
        return TLEType(self.c_double_array[XA_TLE_EPHTYPE])

    @ephemeris_type.setter
    def ephemeris_type(self, value: TLEType):
        self.c_double_array[XA_TLE_EPHTYPE] = value.value
        self.update()

    @property
    def inclination(self) -> float:
        """Inclination in :math:`degrees`"""
        return self.c_double_array[XA_TLE_INCLI]

    @inclination.setter
    def inclination(self, value: float):
        self.c_double_array[XA_TLE_INCLI] = value
        self.update()

    @property
    def raan(self) -> float:
        """Right ascension of the ascending node in :math:`degrees`"""
        return self.c_double_array[XA_TLE_NODE]

    @raan.setter
    def raan(self, value: float):
        self.c_double_array[XA_TLE_NODE] = value
        self.update()

    @property
    def eccentricity(self) -> float:
        """Eccentricity (unitless)"""
        return self.c_double_array[XA_TLE_ECCEN]

    @eccentricity.setter
    def eccentricity(self, value: float):
        self.c_double_array[XA_TLE_ECCEN] = value
        self.update()

    @property
    def argument_of_perigee(self) -> float:
        """Argument of perigee in :math:`degrees`"""
        return self.c_double_array[XA_TLE_OMEGA]

    @argument_of_perigee.setter
    def argument_of_perigee(self, value: float):
        self.c_double_array[XA_TLE_OMEGA] = value
        self.update()

    @property
    def mean_anomaly(self) -> float:
        """Mean anomaly in :math:`degrees`"""
        return self.c_double_array[XA_TLE_MNANOM]

    @mean_anomaly.setter
    def mean_anomaly(self, value: float):
        self.c_double_array[XA_TLE_MNANOM] = value
        self.update()

    @property
    def mean_motion(self) -> float:
        r"""Mean motion in :math:`\frac{rev}{day}`"""
        return self.c_double_array[XA_TLE_MNMOTN]

    @mean_motion.setter
    def mean_motion(self, value: float):
        self.c_double_array[XA_TLE_MNMOTN] = value
        self.update()

    @property
    def revolution_number(self) -> int:
        """Revolution number"""
        return int(self.c_double_array[XA_TLE_REVNUM])

    @revolution_number.setter
    def revolution_number(self, value: int):
        self.c_double_array[XA_TLE_REVNUM] = value
        self.update()

    @property
    def element_set_number(self) -> int:
        """Element set number"""
        return int(self.c_double_array[XA_TLE_ELSETNUM])

    @element_set_number.setter
    def element_set_number(self, value: int):
        self.c_double_array[XA_TLE_ELSETNUM] = value
        self.update()

    @property
    def ballistic_coefficient(self) -> float:
        r"""Ballistic coefficient in :math:`\frac{m^2}{kg}`"""
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
        r"""Solar radiation pressure coefficient in :math:`\frac{m^2}{kg}`"""
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
        r"""Outgassing parameter in :math:`\frac{km}{s^2}`"""
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
