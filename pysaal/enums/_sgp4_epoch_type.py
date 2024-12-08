from enum import Enum

from pysaal.lib._sgp4_prop import SGP4_TIMETYPE_DS50UTC, SGP4_TIMETYPE_MSE


class SGP4EpochType(Enum):
    MINUTES_SINCE_EPOCH = SGP4_TIMETYPE_MSE
    UTC = SGP4_TIMETYPE_DS50UTC
