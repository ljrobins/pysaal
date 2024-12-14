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
        DLLs.env_const.EnvSetGeoStr(model.value.encode())

    @staticmethod
    def get_model() -> EarthModel:
        mod = DLLs.get_null_string()
        DLLs.env_const.EnvGetGeoStr(mod)
        return EarthModel(mod.value.decode())

    @staticmethod
    def get_constant(geocon: int) -> float:
        return DLLs.env_const.EnvGetGeoConst(geocon)

    @staticmethod
    def get_flattening() -> float:
        return Earth.get_constant(XF_GEOCON_FF)

    @staticmethod
    def get_j2() -> float:
        return Earth.get_constant(XF_GEOCON_J2)

    @staticmethod
    def get_j3() -> float:
        return Earth.get_constant(XF_GEOCON_J3)

    @staticmethod
    def get_j4() -> float:
        return Earth.get_constant(XF_GEOCON_J4)

    @staticmethod
    def get_j5() -> float:
        return Earth.get_constant(XF_GEOCON_J5)

    @staticmethod
    def get_radius() -> float:
        return Earth.get_constant(XF_GEOCON_KMPER)

    @staticmethod
    def get_rotation_rate() -> float:
        return Earth.get_constant(XF_GEOCON_RPTIM)

    @staticmethod
    def get_mu() -> float:
        return Earth.get_constant(XF_GEOCON_MU)
