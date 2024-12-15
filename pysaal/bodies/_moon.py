from ctypes import c_double

from pysaal.lib import DLLs
from pysaal.math.linalg import Vector3D
from pysaal.time import Epoch


class Moon:

    #: The gravitational parameter of the Moon in :math:`\frac{km^3}{s^2}`.
    MU = 4902.800305555

    @staticmethod
    def get_analytic_position(epoch: Epoch) -> Vector3D:
        """Get the position of the Moon using an analytic model. :math:`(km)`

        :param epoch: The epoch at which to calculate the position.
        """
        u_vec = Vector3D.get_null_pointer()
        vec_mag = c_double()
        DLLs.astro_func.CompMoonPos(epoch.tt_ds50, u_vec, vec_mag)
        return Vector3D.from_c_array(u_vec) * vec_mag.value

    @staticmethod
    def get_jpl_position(epoch: Epoch) -> Vector3D:
        """Get the position of the Moon using the JPL ephemeris. :math:`(km)`

        :param epoch: The epoch at which to calculate the position.
        """
        _ = Vector3D.get_null_pointer()
        moon_vec = Vector3D.get_null_pointer()
        DLLs.astro_func.JplCompSunMoonPos(epoch.tt_ds50, _, moon_vec)
        return Vector3D.from_c_array(moon_vec)
