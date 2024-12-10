from ctypes import c_double

from pysaal.lib import DLLs
from pysaal.math.linalg import Vector3D
from pysaal.time import Epoch


class Moon:

    MU = 4902.800066

    @staticmethod
    def get_analytic_position(epoch: Epoch) -> Vector3D:
        u_vec = Vector3D.get_null_pointer()
        vec_mag = c_double()
        DLLs.astro_func.CompMoonPos(epoch.tt_ds50, u_vec, vec_mag)
        return Vector3D.from_c_array(u_vec) * vec_mag.value

    @staticmethod
    def get_jpl_position(epoch: Epoch) -> Vector3D:
        _ = Vector3D.get_null_pointer()
        moon_vec = Vector3D.get_null_pointer()
        DLLs.astro_func.JplCompSunMoonPos(epoch.tt_ds50, _, moon_vec)
        return Vector3D.from_c_array(moon_vec)
