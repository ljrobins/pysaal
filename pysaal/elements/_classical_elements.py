from ctypes import Array, c_double

from pysaal.lib import DLLs
from pysaal.lib._astro_func import XA_CLS_E, XA_CLS_INCLI, XA_CLS_MA, XA_CLS_N, XA_CLS_NODE, XA_CLS_OMEGA, XA_CLS_SIZE


class ClassicalElements:
    def __init__(self, n: float, e: float, incli: float, ma: float, node: float, omega: float):
        self.mean_motion = n
        self.eccentricity = e
        self.inclination = incli
        self.mean_anomaly = ma
        self.raan = node
        self.argument_of_perigee = omega

    @property
    def semi_major_axis(self) -> float:
        return DLLs.astro_func.NToA(self.mean_motion)

    @property
    def c_array(self) -> Array[c_double]:
        c_array = (c_double * XA_CLS_SIZE)()
        c_array[XA_CLS_N] = self.mean_motion
        c_array[XA_CLS_E] = self.eccentricity
        c_array[XA_CLS_INCLI] = self.inclination
        c_array[XA_CLS_MA] = self.mean_anomaly
        c_array[XA_CLS_NODE] = self.raan
        c_array[XA_CLS_OMEGA] = self.argument_of_perigee
        return c_array

    @staticmethod
    def get_null_pointer() -> Array[c_double]:
        return (c_double * XA_CLS_SIZE)()

    @classmethod
    def from_c_array(cls, c_array: Array[c_double]):
        return cls(
            c_array[XA_CLS_N],
            c_array[XA_CLS_E],
            c_array[XA_CLS_INCLI],
            c_array[XA_CLS_MA],
            c_array[XA_CLS_NODE],
            c_array[XA_CLS_OMEGA],
        )
