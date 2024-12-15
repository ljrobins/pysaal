from ctypes import Array, c_double

from pysaal.lib import DLLs
from pysaal.lib._astro_func import XA_CLS_E, XA_CLS_INCLI, XA_CLS_MA, XA_CLS_N, XA_CLS_NODE, XA_CLS_OMEGA, XA_CLS_SIZE


class ClassicalElements:
    """Class used to store the classical orbital elements of a satellite"""

    def __init__(self, n: float, e: float, incli: float, ma: float, node: float, omega: float):

        #: The mean motion of the orbit in :math:`\frac{rev}{day}`.
        self.mean_motion = n

        #: The eccentricity of the orbit.
        self.eccentricity = e

        #: The inclination of the orbit in :math:`deg`.
        self.inclination = incli

        #: The mean anomaly of the orbit in :math:`deg`.
        self.mean_anomaly = ma

        #: The right ascension of the ascending node in :math:`deg`.
        self.raan = node

        #: The argument of perigee in :math:`deg`.
        self.argument_of_perigee = omega

    @property
    def semi_major_axis(self) -> float:
        """The semi-major axis of the orbit in :math:`km`"""
        return DLLs.astro_func.NToA(self.mean_motion)

    @property
    def c_array(self) -> Array[c_double]:
        """The classical elements as a C array to be used by the SAAL library"""
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
        """Generate a null pointer to a C array of length :attr:`XA_CLS_SIZE` to be used by the SAAL library"""
        return (c_double * XA_CLS_SIZE)()

    @classmethod
    def from_c_array(cls, c_array: Array[c_double]):
        """Constructor used when interfacing directly with the SAAL library"""
        return cls(
            c_array[XA_CLS_N],
            c_array[XA_CLS_E],
            c_array[XA_CLS_INCLI],
            c_array[XA_CLS_MA],
            c_array[XA_CLS_NODE],
            c_array[XA_CLS_OMEGA],
        )
