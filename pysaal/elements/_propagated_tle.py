from ctypes import Array, c_double

import numpy as np
import pandas as pd

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

    @property
    def numpy_array(self) -> np.ndarray:
        return np.array(
            [
                self.epoch.datetime,
                self.minutes_since_epoch,
                self.cartesian_elements.position.magnitude,
                self.cartesian_elements.position.x,
                self.cartesian_elements.position.y,
                self.cartesian_elements.position.z,
                self.cartesian_elements.velocity.magnitude,
                self.cartesian_elements.velocity.x,
                self.cartesian_elements.velocity.y,
                self.cartesian_elements.velocity.z,
                self.lla.latitude,
                self.lla.longitude,
                self.lla.altitude,
                self.revolution_number,
                self.nodal_period,
                self.mean_elements.semi_major_axis,
                self.mean_elements.eccentricity,
                self.mean_elements.inclination,
                self.mean_elements.mean_anomaly,
                self.mean_elements.raan,
                self.mean_elements.argument_of_perigee,
                self.osculating_elements.semi_major_axis,
                self.osculating_elements.eccentricity,
                self.osculating_elements.inclination,
                self.osculating_elements.mean_anomaly,
                self.osculating_elements.raan,
                self.osculating_elements.argument_of_perigee,
            ]
        )

    @property
    def dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(
            [self.numpy_array],
            columns=[
                "epoch",
                "min_since_epoch",
                "radius",
                "teme_x_pos",
                "teme_y_pos",
                "teme_z_pos",
                "velocity",
                "teme_x_vel",
                "teme_y_vel",
                "teme_z_vel",
                "latitude",
                "longitude",
                "altitude",
                "rev_no",
                "nodal_period",
                "mean_a",
                "mean_e",
                "mean_i",
                "mean_ma",
                "mean_raan",
                "mean_arg_perigee",
                "osc_a",
                "osc_e",
                "osc_i",
                "osc_ma",
                "osc_raan",
                "osc_arg_perigee",
            ],
        )

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
