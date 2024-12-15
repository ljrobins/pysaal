from pysaal.enums import EarthModel
from pysaal.lib import DLLs
from pysaal.lib._env_const import (
    XF_GEOCON_FF,
    XF_GEOCON_J2,
    XF_GEOCON_J3,
    XF_GEOCON_J4,
    XF_GEOCON_J5,
    XF_GEOCON_KMPER,
    XF_GEOCON_MU,
    XF_GEOCON_RPTIM,
)


class Earth:
    @staticmethod
    def set_model(model: EarthModel) -> None:
        """Update the global geodetic model used in the environment constants.

        :param model: The new geodetic model to use.  See :ref:`earth_model` for options.
        """
        DLLs.env_const.EnvSetGeoStr(model.value.encode())

    @staticmethod
    def get_model() -> EarthModel:
        """Get the global geodetic model used in the environment constants."""
        mod = DLLs.get_null_string()
        DLLs.env_const.EnvGetGeoStr(mod)
        return EarthModel(mod.value.decode())

    @staticmethod
    def _get_constant(geocon: int) -> float:
        """Get an environment constant by index.

        .. note::

            This method is not intended to be used directly.  Instead, most constants have been exposed as methods.
        """

        return DLLs.env_const.EnvGetGeoConst(geocon)

    @staticmethod
    def get_flattening() -> float:
        """Get the flattening factor of the Earth."""
        return Earth._get_constant(XF_GEOCON_FF)

    @staticmethod
    def get_j2() -> float:
        """Get the J2 coefficient of the Earth. (unitless)"""
        return Earth._get_constant(XF_GEOCON_J2)

    @staticmethod
    def get_j3() -> float:
        """Get the J3 coefficient of the Earth. (unitless)"""
        return Earth._get_constant(XF_GEOCON_J3)

    @staticmethod
    def get_j4() -> float:
        """Get the J4 coefficient of the Earth. (unitless)"""
        return Earth._get_constant(XF_GEOCON_J4)

    @staticmethod
    def get_j5() -> float:
        """Get the J5 coefficient of the Earth. (unitless)"""
        return Earth._get_constant(XF_GEOCON_J5)

    @staticmethod
    def get_radius() -> float:
        """Get the equatorial radius of the Earth. :math:`(km)`"""
        return Earth._get_constant(XF_GEOCON_KMPER)

    @staticmethod
    def get_rotation_rate() -> float:
        r"""Get the rotation rate of the Earth. :math:`\frac{rad}{min}`"""
        return Earth._get_constant(XF_GEOCON_RPTIM)

    @staticmethod
    def get_mu() -> float:
        r"""Get the gravitational parameter of the Earth. :math:`\frac{km^3}{s^2}`"""
        return Earth._get_constant(XF_GEOCON_MU)
