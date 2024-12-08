from enum import Enum

from pysaal.lib._sgp4_prop import SGP4_EPHEM_ECI, SGP4_EPHEM_J2K


class SGP4EphemerisType(Enum):
    TEME = SGP4_EPHEM_ECI
    J2000 = SGP4_EPHEM_J2K
