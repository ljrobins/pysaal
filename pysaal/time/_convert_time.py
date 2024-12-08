from datetime import datetime

import numpy as np

from pysaal.time._epoch import Epoch


class _GetDateTime:
    @staticmethod
    def from_ds50(ds50: float) -> datetime:
        return Epoch(ds50).datetime


class _GetDateTimeArray:

    from_ds50_array = np.vectorize(_GetDateTime.from_ds50)


class _GetEpochArray:

    from_ds50_array = np.vectorize(Epoch)


class ConvertTime:

    datetime = _GetDateTime
    datetime_array = _GetDateTimeArray
    epoch_array = _GetEpochArray
