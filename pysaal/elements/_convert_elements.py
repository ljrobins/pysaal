from ctypes import c_double

from pysaal.elements._cartesian_elements import CartesianElements
from pysaal.elements._classical_elements import ClassicalElements
from pysaal.elements._equinoctial_elements import EquinoctialElements
from pysaal.elements._keplerian_elements import KeplerianElements
from pysaal.elements._mean_elements import MeanElements
from pysaal.elements._sp_vector import SPVector
from pysaal.elements._tle import TLE
from pysaal.enums import TLEType
from pysaal.lib import DLLs
from pysaal.math.constants import B_STAR_TO_B_TERM_COEFFICIENT


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


class _GetTLE:
    @staticmethod
    def from_sp_vector(sp: SPVector, tle_type: TLEType) -> TLE:
        xa_tle, xs_tle = TLE.get_null_pointers()
        tle = TLE.from_c_arrays(xa_tle, xs_tle)
        tle.satellite_id = sp.satellite_id
        tle.epoch = sp.epoch
        tle.ephemeris_type = tle_type
        tle.ballistic_coefficient = sp.b_term
        tle.b_star = sp.b_term / B_STAR_TO_B_TERM_COEFFICIENT
        tle.agom = sp.agom
        tle.designator = sp.designator
        tle.classification = sp.classification
        DLLs.sgp4_prop.Sgp4PosVelToTleArr(sp.position.c_array, sp.velocity.c_array, tle.c_double_array)
        return tle


class ConvertElements:
    equinoctial = _GetEquinoctial
    keplerian = _GetKeplerian
    cartesian = _GetCartesian
    classical = _GetClassical
    mean = _GetMean
    mean_motion = _GetMeanMotion
    tle = _GetTLE
