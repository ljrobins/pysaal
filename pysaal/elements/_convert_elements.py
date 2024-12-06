from ctypes import c_double

from pysaal.elements._cartesian_elements import CartesianElements
from pysaal.elements._classical_elements import ClassicalElements
from pysaal.elements._equinoctial_elements import EquinoctialElements
from pysaal.elements._keplerian_elements import KeplerianElements
from pysaal.elements._mean_elements import MeanElements
from pysaal.lib import DLLs


class _GetEquinoctial:
    @staticmethod
    def from_equinoctial(kep: KeplerianElements) -> EquinoctialElements:
        c_eqnx = EquinoctialElements.get_null_pointer()
        DLLs.astro_func.KepToEqnx(kep.c_array, c_eqnx)
        return EquinoctialElements.from_c_array(c_eqnx)

    @staticmethod
    def from_classical(cl: ClassicalElements) -> EquinoctialElements:
        c_eqnx = EquinoctialElements.get_null_pointer()
        DLLs.astro_func.ClassToEqnx(cl.c_array, c_eqnx)
        return EquinoctialElements.from_c_array(c_eqnx)

    @staticmethod
    def from_cartesian(cart: CartesianElements, mu: float) -> EquinoctialElements:
        c_eqnx = EquinoctialElements.get_null_pointer()
        DLLs.astro_func.PosVelMuToEqnx(cart.position.c_array, cart.velocity.c_array, c_double(mu), c_eqnx)
        return EquinoctialElements.from_c_array(c_eqnx)


class _GetKeplerian:
    @staticmethod
    def from_equinoctial(eqnx: EquinoctialElements) -> KeplerianElements:
        c_kep = KeplerianElements.get_null_pointer()
        DLLs.astro_func.EqnxToKep(eqnx.c_array, c_kep)
        return KeplerianElements.from_c_array(c_kep)

    @staticmethod
    def from_cartesian(cart: CartesianElements, mu: float) -> KeplerianElements:
        c_kep = KeplerianElements.get_null_pointer()
        DLLs.astro_func.PosVelMuToKep(cart.position.c_array, cart.velocity.c_array, c_double(mu), c_kep)
        return KeplerianElements.from_c_array(c_kep)


class _GetCartesian:
    @staticmethod
    def from_keplerian(kep: KeplerianElements) -> CartesianElements:
        c_pos, c_vel = CartesianElements.get_null_pointers()
        DLLs.astro_func.KepToPosVel(kep.c_array, c_pos, c_vel)
        return CartesianElements.from_c_arrays(c_pos, c_vel)

    @staticmethod
    def from_equinoctial(eqnx: EquinoctialElements) -> CartesianElements:
        c_pos, c_vel = CartesianElements.get_null_pointers()
        DLLs.astro_func.EqnxToPosVel(eqnx.c_array, c_pos, c_vel)
        return CartesianElements.from_c_arrays(c_pos, c_vel)


class _GetClassical:
    @staticmethod
    def from_equinoctial(eqnx: EquinoctialElements) -> ClassicalElements:
        c_class = ClassicalElements.get_null_pointer()
        DLLs.astro_func.EqnxToClass(eqnx.c_array, c_class)
        return ClassicalElements.from_c_array(c_class)


class _GetMean:
    @staticmethod
    def from_keplerian(kep: KeplerianElements) -> MeanElements:
        c_mean = MeanElements.get_null_pointer()
        DLLs.astro_func.KepOscToMean(kep.c_array, c_mean)
        return MeanElements.from_c_array(c_mean)


class _GetBrouwer:
    @staticmethod
    def from_kozai(e: float, i: float, n: float) -> float:
        return DLLs.astro_func.KozaiToBrouwer(c_double(e), c_double(i), c_double(n))


class _GetKozai:
    @staticmethod
    def from_brouwer(e: float, i: float, n: float) -> float:
        return DLLs.astro_func.BrouwerToKozai(c_double(e), c_double(i), c_double(n))


class _GetMeanMotion:

    brouwer = _GetBrouwer
    kozai = _GetKozai

    @staticmethod
    def from_semi_major_axis(a: float) -> float:
        return DLLs.astro_func.AToN(c_double(a))


class ConvertElements:
    equinoctial = _GetEquinoctial
    keplerian = _GetKeplerian
    cartesian = _GetCartesian
    classical = _GetClassical
    mean = _GetMean
    mean_motion = _GetMeanMotion
