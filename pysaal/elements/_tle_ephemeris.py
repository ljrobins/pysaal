import numpy as np
import pandas as pd
from scipy.signal import find_peaks  # type: ignore

from pysaal.elements._propagated_tle import PropagatedTLE
from pysaal.elements._tle import TLE
from pysaal.math.constants import SECONDS_TO_DAYS
from pysaal.time import ConvertTime, Epoch


def _propagated_tle_to_numpy_array(propagated_tle: PropagatedTLE) -> np.ndarray:
    return propagated_tle.numpy_array


class TLEEphemeris(list[PropagatedTLE]):
    def __init__(self, *args):
        super().__init__(args)
        self._numpy_array = None
        self._dataframe = None

    @classmethod
    def from_tle(cls, tle: TLE, start: Epoch, end: Epoch, step: int) -> "TLEEphemeris":
        destroy = not tle.loaded
        vectorized_state_at_epoch = np.vectorize(TLE.get_state_at_epoch, otypes=[PropagatedTLE], excluded=["self"])
        ds50_array = np.arange(start.utc_ds50, end.utc_ds50, step * SECONDS_TO_DAYS)
        epoch_array = ConvertTime.epoch_array.from_ds50_array(ds50_array)
        states = vectorized_state_at_epoch(tle, epoch_array)
        if destroy:
            tle.destroy()
        return cls(*states)

    @property
    def numpy_array(self) -> np.ndarray:
        if self._numpy_array is None:
            vectorized_propagated_tle_to_numpy_array = np.vectorize(
                _propagated_tle_to_numpy_array, signature="()->(27)"
            )
            self._numpy_array = vectorized_propagated_tle_to_numpy_array(self)
        return self._numpy_array

    @property
    def epochs(self) -> pd.Series:
        return self.dataframe["epoch"]

    @property
    def semi_major_axes(self) -> pd.Series:
        return self.dataframe["mean_a"]

    @property
    def inclinations(self) -> pd.Series:
        return self.dataframe["mean_i"]

    @property
    def raans(self) -> pd.Series:
        return self.dataframe["mean_raan"]

    @property
    def eccentricities(self) -> pd.Series:
        return self.dataframe["mean_e"]

    @property
    def semi_major_axis_signals(self) -> pd.Series:
        return self.dataframe["abs_grad_a"]

    @property
    def inclination_signals(self) -> pd.Series:
        return self.dataframe["abs_grad_i"]

    @property
    def raan_signals(self) -> pd.Series:
        return self.dataframe["abs_grad_raan"]

    @property
    def eccentricity_signals(self) -> pd.Series:
        return self.dataframe["abs_grad_e"]

    def get_sma_peaks(self, threshold: float, separation: int) -> tuple[pd.Series, pd.Series]:
        peaks, _ = find_peaks(self.dataframe["abs_grad_a"], height=threshold, distance=separation)
        return self.dataframe["epoch"].iloc[peaks], self.dataframe["mean_a"].iloc[peaks]

    def get_raan_peaks(self, threshold: float, separation: int) -> tuple[pd.Series, pd.Series]:
        peaks, _ = find_peaks(self.dataframe["abs_grad_raan"], height=threshold, distance=separation)
        return self.dataframe["epoch"].iloc[peaks], self.dataframe["mean_raan"].iloc[peaks]

    def get_inclination_peaks(self, threshold: float, separation: int) -> tuple[pd.Series, pd.Series]:
        peaks, _ = find_peaks(self.dataframe["abs_grad_i"], height=threshold, distance=separation)
        return self.dataframe["epoch"].iloc[peaks], self.dataframe["mean_i"].iloc[peaks]

    def get_eccentricity_peaks(self, threshold: float, separation: int) -> tuple[pd.Series, pd.Series]:
        peaks, _ = find_peaks(self.dataframe["abs_grad_e"], height=threshold, distance=separation)
        return self.dataframe["epoch"].iloc[peaks], self.dataframe["mean_e"].iloc[peaks]

    @property
    def dataframe(self) -> pd.DataFrame:
        if self._dataframe is None:
            self._dataframe = pd.DataFrame(self.numpy_array)
            self._dataframe.columns = self[0].dataframe.columns
            min_a = self._dataframe["mean_a"].min()
            max_a = self._dataframe["mean_a"].max()
            self._dataframe["norm_a"] = (self._dataframe["mean_a"] - min_a) / (max_a - min_a)
            self._dataframe["grad_a"] = np.gradient(self._dataframe["norm_a"])
            self._dataframe["abs_grad_a"] = np.abs(self._dataframe["grad_a"])
            min_i = self._dataframe["mean_i"].min()
            max_i = self._dataframe["mean_i"].max()
            self._dataframe["norm_i"] = (self._dataframe["mean_i"] - min_i) / (max_i - min_i)
            self._dataframe["grad_i"] = np.gradient(self._dataframe["norm_i"])
            self._dataframe["abs_grad_i"] = np.abs(self._dataframe["grad_i"])
            min_e = self._dataframe["mean_e"].min()
            max_e = self._dataframe["mean_e"].max()
            self._dataframe["norm_e"] = (self._dataframe["mean_e"] - min_e) / (max_e - min_e)
            self._dataframe["grad_e"] = np.gradient(self._dataframe["norm_e"])
            self._dataframe["abs_grad_e"] = np.abs(self._dataframe["grad_e"])
            min_raan = self._dataframe["mean_raan"].min()
            max_raan = self._dataframe["mean_raan"].max()
            self._dataframe["norm_raan"] = (self._dataframe["mean_raan"] - min_raan) / (max_raan - min_raan)
            self._dataframe["grad_raan"] = np.gradient(self._dataframe["norm_raan"])
            self._dataframe["abs_grad_raan"] = np.abs(self._dataframe["grad_raan"])
        return self._dataframe

    def append(self, object: PropagatedTLE) -> None:
        if not isinstance(object, PropagatedTLE):
            raise TypeError(f"Expected PropagatedTLE, got {type(object)}")
        elif len(self) != 0 and object.epoch < self[-1].epoch:
            raise ValueError("PropagatedTLE must be appended in chronological order")
        self._numpy_array = None
        self._dataframe = None
        return super().append(object)

    def filter_before(self, epoch: Epoch) -> "TLEEphemeris":
        return TLEEphemeris(*[prop_tle for prop_tle in self if prop_tle.epoch >= epoch])

    def filter_after(self, epoch: Epoch) -> "TLEEphemeris":
        return TLEEphemeris(*[prop_tle for prop_tle in self if prop_tle.epoch <= epoch])

    def filter_between(self, start: Epoch, stop: Epoch) -> "TLEEphemeris":
        return TLEEphemeris(*[prop_tle for prop_tle in self if start <= prop_tle.epoch <= stop])
