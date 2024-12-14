from ctypes import Array, c_double

from pysaal.elements._cartesian_elements import CartesianElements
from pysaal.elements._keplerian_elements import KeplerianElements
from pysaal.elements._lla import LLA
from pysaal.elements._mean_elements import MeanElements
from pysaal.lib._sgp4_prop import (
    XA_SGP4OUT_DS50UTC,
    XA_SGP4OUT_HEIGHT,
    XA_SGP4OUT_LAT,
    XA_SGP4OUT_LON,
    XA_SGP4OUT_MN_A,
    XA_SGP4OUT_MN_E,
    XA_SGP4OUT_MN_INCLI,
    XA_SGP4OUT_MN_MA,
    XA_SGP4OUT_MN_NODE,
    XA_SGP4OUT_MN_OMEGA,
    XA_SGP4OUT_MSE,
    XA_SGP4OUT_NODALPER,
    XA_SGP4OUT_OSC_A,
    XA_SGP4OUT_OSC_E,
    XA_SGP4OUT_OSC_INCLI,
    XA_SGP4OUT_OSC_MA,
    XA_SGP4OUT_OSC_NODE,
    XA_SGP4OUT_OSC_OMEGA,
    XA_SGP4OUT_POSX,
    XA_SGP4OUT_POSY,
    XA_SGP4OUT_POSZ,
    XA_SGP4OUT_REVNUM,
    XA_SGP4OUT_SIZE,
    XA_SGP4OUT_VELX,
    XA_SGP4OUT_VELY,
    XA_SGP4OUT_VELZ,
)
from pysaal.math.linalg import Vector3D
from pysaal.time import Epoch


class PropagatedTLE:
    def __init__(
        self,
        epoch: Epoch,
        mse: float,
        cart: CartesianElements,
        mean: MeanElements,
        osc: KeplerianElements,
        lla: LLA,
        rev_no: int,
        nodal_period: float,
    ) -> None:
        self.epoch = epoch
        self.minutes_since_epoch = mse
        self.cartesian_elements = cart
        self.lla = lla
        self.revolution_number = rev_no
        self.nodal_period = nodal_period
        self.mean_elements = mean
        self.osculating_elements = osc

    @property
    def position(self) -> Vector3D:
        return self.cartesian_elements.position

    @property
    def velocity(self) -> Vector3D:
        return self.cartesian_elements.velocity

    @property
    def longitude(self) -> float:
        return self.lla.longitude

    @property
    def latitude(self) -> float:
        return self.lla.latitude

    @property
    def altitude(self) -> float:
        return self.lla.altitude

    @property
    def semi_major_axis(self) -> float:
        return self.osculating_elements.semi_major_axis

    @property
    def eccentricity(self) -> float:
        return self.osculating_elements.eccentricity

    @property
    def inclination(self) -> float:
        return self.osculating_elements.inclination

    @property
    def mean_anomaly(self) -> float:
        return self.osculating_elements.mean_anomaly

    @property
    def raan(self) -> float:
        return self.osculating_elements.raan

    @property
    def argument_of_perigee(self) -> float:
        return self.osculating_elements.argument_of_perigee

    @staticmethod
    def null_pointer() -> Array[c_double]:
        return (c_double * XA_SGP4OUT_SIZE)()

    @classmethod
    def from_c_array(cls, c_array: Array[c_double]) -> "PropagatedTLE":
        epoch = Epoch(c_array[XA_SGP4OUT_DS50UTC])
        mse = c_array[XA_SGP4OUT_MSE]
        cart = CartesianElements(
            c_array[XA_SGP4OUT_POSX],
            c_array[XA_SGP4OUT_POSY],
            c_array[XA_SGP4OUT_POSZ],
            c_array[XA_SGP4OUT_VELX],
            c_array[XA_SGP4OUT_VELY],
            c_array[XA_SGP4OUT_VELZ],
        )
        lla = LLA(c_array[XA_SGP4OUT_LAT], c_array[XA_SGP4OUT_LON], c_array[XA_SGP4OUT_HEIGHT])
        rev_no = int(c_array[XA_SGP4OUT_REVNUM])
        nodal_period = c_array[XA_SGP4OUT_NODALPER]
        mean = MeanElements(
            c_array[XA_SGP4OUT_MN_A],
            c_array[XA_SGP4OUT_MN_E],
            c_array[XA_SGP4OUT_MN_INCLI],
            c_array[XA_SGP4OUT_MN_MA],
            c_array[XA_SGP4OUT_MN_NODE],
            c_array[XA_SGP4OUT_MN_OMEGA],
        )
        osc = KeplerianElements(
            c_array[XA_SGP4OUT_OSC_A],
            c_array[XA_SGP4OUT_OSC_E],
            c_array[XA_SGP4OUT_OSC_INCLI],
            c_array[XA_SGP4OUT_OSC_MA],
            c_array[XA_SGP4OUT_OSC_NODE],
            c_array[XA_SGP4OUT_OSC_OMEGA],
        )
        return cls(epoch, mse, cart, mean, osc, lla, rev_no, nodal_period)
