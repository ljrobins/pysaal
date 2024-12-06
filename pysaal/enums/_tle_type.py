from enum import Enum

from pysaal.lib._tle import TLETYPE_SGP, TLETYPE_SGP4, TLETYPE_SP, TLETYPE_XP


class TLEType(Enum):

    #: TLE SGP elset (Kozai mean motion)
    SGP = TLETYPE_SGP

    #: TLE SGP4 elset (Brouwer mean motion)
    SGP4 = TLETYPE_SGP4

    #: TLE SGP4-XP elset (Brouwer mean motion)
    XP = TLETYPE_XP

    #: TLE SP elset (osculating elements)
    SP = TLETYPE_SP
