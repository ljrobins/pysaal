from ctypes import c_double

from pysaal.lib import DLLs
from pysaal.math.linalg import Vector3D
from pysaal.time import Epoch


class Sun:

    #: The gravitational parameter of the Sun in :math:`\frac{km^3}{s^2}`.
    MU = 1.327124400419e11

    @staticmethod
    def get_analytic_position(epoch: Epoch) -> Vector3D:
        """Get the position of the Sun using an analytic model. :math:`(km)`

        :param epoch: The epoch at which to calculate the position.
        """
        u_vec = Vector3D.get_null_pointer()
        vec_mag = c_double()
        DLLs.astro_func.CompSunPos(epoch.tt_ds50, u_vec, vec_mag)
        return Vector3D.from_c_array(u_vec) * vec_mag.value

    @staticmethod
    def get_jpl_position(epoch: Epoch) -> Vector3D:
        """Get the position of the Sun using the JPL ephemeris. :math:`(km)`

        :param epoch: The epoch at which to calculate the position.
        """
        sun_vec = Vector3D.get_null_pointer()
        _ = Vector3D.get_null_pointer()
        DLLs.astro_func.JplCompSunMoonPos(epoch.tt_ds50, sun_vec, _)
        return Vector3D.from_c_array(sun_vec)
