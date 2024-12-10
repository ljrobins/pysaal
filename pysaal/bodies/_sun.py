from ctypes import c_double

from pysaal.lib import DLLs
from pysaal.math.linalg import Vector3D
from pysaal.time import Epoch


class Sun:

    MU = 132712440018.0

    @staticmethod
    def get_analytic_position(epoch: Epoch) -> Vector3D:
        u_vec = Vector3D.get_null_pointer()
        vec_mag = c_double()
        DLLs.astro_func.CompSunPos(epoch.tt_ds50, u_vec, vec_mag)
        return Vector3D.from_c_array(u_vec) * vec_mag.value

    @staticmethod
    def get_jpl_position(epoch: Epoch) -> Vector3D:
        sun_vec = Vector3D.get_null_pointer()
        _ = Vector3D.get_null_pointer()
        DLLs.astro_func.JplCompSunMoonPos(epoch.tt_ds50, sun_vec, _)
        return Vector3D.from_c_array(sun_vec)
