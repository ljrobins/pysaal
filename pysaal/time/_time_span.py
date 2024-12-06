from pysaal.math.constants import DAYS_TO_MINUTES
from pysaal.time._epoch import Epoch


class TimeSpan:
    def __init__(self, start: Epoch, end: Epoch):
        self.start = start
        self.end = end

    @property
    def days(self) -> float:
        """Return the time span in days."""
        return self.end.utc_ds50 - self.start.utc_ds50

    @property
    def minutes(self) -> float:
        """Return the time span in minutes."""
        return self.days * DAYS_TO_MINUTES
