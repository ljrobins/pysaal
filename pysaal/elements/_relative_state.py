from ctypes import Array, c_double

from pysaal.lib.SatStateWrapper import (
    XA_DELTA_ANGMOM,
    XA_DELTA_BETA,
    XA_DELTA_HEIGHT,
    XA_DELTA_MHLNBS_HTB,
    XA_DELTA_MHLNBS_UVW,
    XA_DELTA_PCRSSTRCK,
    XA_DELTA_PINTRCK,
    XA_DELTA_POS,
    XA_DELTA_PRADIAL,
    XA_DELTA_SIZE,
    XA_DELTA_TIME,
    XA_DELTA_VCRSSTRCK,
    XA_DELTA_VEL,
    XA_DELTA_VINTRCK,
    XA_DELTA_VRADIAL,
)


class RelativeState:
    def __init__(
        self,
        pos: float,
        t: float,
        prad: float,
        pintrck: float,
        pcrsstrck: float,
        vel: float,
        vrad: float,
        vintrck: float,
        vcrsstrck: float,
        beta: float,
        height: float,
        angmom: float,
        mhlbs_uvw: float,
        mhlbs_htb: float,
    ):
        self.range = pos
        self.time = t
        self.radial_position = prad
        self.in_track_position = pintrck
        self.cross_track_position = pcrsstrck
        self.velocity = vel
        self.radial_velocity = vrad
        self.in_track_velocity = vintrck
        self.cross_track_velocity = vcrsstrck
        self.plane = beta
        self.height = height
        self.angular_momentum = angmom
        self.mahalanobis_uvw = mhlbs_uvw
        self.mahalanobis_htb = mhlbs_htb

    @staticmethod
    def get_null_pointer() -> Array[c_double]:
        return (c_double * XA_DELTA_SIZE)()

    @classmethod
    def from_c_array(cls, c_array: Array[c_double]) -> "RelativeState":
        return cls(
            c_array[XA_DELTA_POS],
            c_array[XA_DELTA_TIME],
            c_array[XA_DELTA_PRADIAL],
            c_array[XA_DELTA_PINTRCK],
            c_array[XA_DELTA_PCRSSTRCK],
            c_array[XA_DELTA_VEL],
            c_array[XA_DELTA_VRADIAL],
            c_array[XA_DELTA_VINTRCK],
            c_array[XA_DELTA_VCRSSTRCK],
            c_array[XA_DELTA_BETA],
            c_array[XA_DELTA_HEIGHT],
            c_array[XA_DELTA_ANGMOM],
            c_array[XA_DELTA_MHLNBS_UVW],
            c_array[XA_DELTA_MHLNBS_HTB],
        )
