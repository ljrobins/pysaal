import numpy as np
import pandas as pd

from pysaal.elements._propagated_tle import PropagatedTLE
from pysaal.elements._tle import TLE
from pysaal.math.constants import SECONDS_TO_DAYS
from pysaal.time import ConvertTime, Epoch


def _propagated_tle_to_numpy_array(propagated_tle: PropagatedTLE) -> np.ndarray:
    return propagated_tle.numpy_array


class TLEEphemeris(list[PropagatedTLE]):
    def __init__(self, *args):
        super().__init__(args)

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
        vectorized_propagated_tle_to_numpy_array = np.vectorize(_propagated_tle_to_numpy_array, signature="()->(27)")
        return vectorized_propagated_tle_to_numpy_array(self)

    @property
    def dataframe(self) -> pd.DataFrame:
        df = pd.DataFrame(self.numpy_array)
        df.columns = self[0].dataframe.columns
        return df

    def append(self, object: PropagatedTLE) -> None:
        if not isinstance(object, PropagatedTLE):
            raise TypeError(f"Expected PropagatedTLE, got {type(object)}")
        elif object.epoch < self[-1].epoch:
            raise ValueError("PropagatedTLE must be appended in chronological order")
        return super().append(object)
