from ctypes import Array, c_double

from pysaal.lib import DLLs
from pysaal.lib._astro_func import XA_KEP_A, XA_KEP_E, XA_KEP_INCLI, XA_KEP_MA, XA_KEP_NODE, XA_KEP_OMEGA, XA_KEP_SIZE


class KeplerianElements:
    def __init__(self, sma: float, ecc: float, inc: float, ma: float, raan: float, aop: float):

        #: The semi-major axis of the orbit in :math:`km`
        self.semi_major_axis = sma

        #: The eccentricity of the orbit
        self.eccentricity = ecc

        #: The inclination of the orbit in :math:`deg`
        self.inclination = inc

        #: The mean anomaly of the orbit in :math:`deg`
        self.mean_anomaly = ma

        #: The right ascension of the ascending node in :math:`deg`
        self.raan = raan

        #: The argument of perigee in :math:`deg`
        self.argument_of_perigee = aop

    @property
    def c_array(self) -> Array[c_double]:
        """The Keplerian elements as a C array to be used by the SAAL library"""
        c_array = (c_double * XA_KEP_SIZE)()
        c_array[XA_KEP_A] = self.semi_major_axis
        c_array[XA_KEP_E] = self.eccentricity
        c_array[XA_KEP_INCLI] = self.inclination
        c_array[XA_KEP_MA] = self.mean_anomaly
        c_array[XA_KEP_NODE] = self.raan
        c_array[XA_KEP_OMEGA] = self.argument_of_perigee
        return c_array

    @property
    def eccentric_anomaly(self) -> float:
        """The eccentric anomaly of the orbit in :math:`deg`"""
        return DLLs.astro_func.SolveKepEqtn(self.c_array)

    @property
    def true_anomaly(self) -> float:
        """The true anomaly of the orbit in :math:`deg`"""
        return DLLs.astro_func.CompTrueAnomaly(self.c_array)

    @property
    def mean_motion(self) -> float:
        """The mean motion of the orbit in :math:`\frac{rev}{day}`"""
        return DLLs.astro_func.AToN(self.semi_major_axis)

    @staticmethod
    def get_null_pointer() -> Array[c_double]:
        """Generate a null pointer to a C array of length :attr:`XA_KEP_SIZE` to be used by the SAAL library"""
        return (c_double * XA_KEP_SIZE)()

    @classmethod
    def from_c_array(cls, c_array: Array[c_double]):
        """Constructor used when interfacing directly with the SAAL library"""
        return cls(
            c_array[XA_KEP_A],
            c_array[XA_KEP_E],
            c_array[XA_KEP_INCLI],
            c_array[XA_KEP_MA],
            c_array[XA_KEP_NODE],
            c_array[XA_KEP_OMEGA],
        )
