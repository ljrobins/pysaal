from ctypes import Array, c_double

from pysaal.lib._astro_func import XA_EQNX_AF, XA_EQNX_AG, XA_EQNX_CHI, XA_EQNX_L, XA_EQNX_N, XA_EQNX_PSI, XA_EQNX_SIZE


class EquinoctialElements:
    def __init__(self, af: float, ag: float, chi: float, psi: float, l: float, n: float):

        self.af = af
        self.ag = ag
        self.chi = chi
        self.psi = psi
        self.l = l
        self.n = n

    @property
    def c_array(self) -> Array[c_double]:
        c_array = (c_double * XA_EQNX_SIZE)()
        c_array[XA_EQNX_AF] = self.af
        c_array[XA_EQNX_AG] = self.ag
        c_array[XA_EQNX_CHI] = self.chi
        c_array[XA_EQNX_PSI] = self.psi
        c_array[XA_EQNX_L] = self.l
        c_array[XA_EQNX_N] = self.n
        return c_array

    @staticmethod
    def get_null_pointer() -> Array[c_double]:
        return (c_double * XA_EQNX_SIZE)()

    @classmethod
    def from_c_array(cls, c_array: Array[c_double]):
        return cls(
            c_array[XA_EQNX_AF],
            c_array[XA_EQNX_AG],
            c_array[XA_EQNX_CHI],
            c_array[XA_EQNX_PSI],
            c_array[XA_EQNX_L],
            c_array[XA_EQNX_N],
        )
