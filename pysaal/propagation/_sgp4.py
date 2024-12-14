from ctypes import c_double

import numpy as np

from pysaal.elements import TLE
from pysaal.lib import DLLs
from pysaal.math.constants import SECONDS_TO_DAYS
from pysaal.time import Epoch


class SGP4:
    @staticmethod
    def get_loaded_states_at_epoch(epoch: Epoch) -> np.ndarray:
        num_loaded = TLE.get_number_in_memory()
        keys = TLE.get_loaded_keys()
        eph_arr = ((c_double * 6) * num_loaded)()
        DLLs.sgp4_prop.Sgp4PropAllSats(keys, num_loaded, epoch.utc_ds50, eph_arr)
        epochs = np.full((num_loaded, 1), epoch.utc_ds50)
        return np.column_stack((keys, epochs[:, 0], np.array(eph_arr)))

    @staticmethod
    def get_loaded_ephemeris(start: Epoch, stop: Epoch, step: float) -> np.ndarray:
        step_in_days = step * SECONDS_TO_DAYS
        epochs = np.arange(start.utc_ds50, stop.utc_ds50, step_in_days)
        vectorized = np.vectorize(SGP4.get_loaded_states_at_epoch, otypes=[np.ndarray])
        return vectorized(epochs)
