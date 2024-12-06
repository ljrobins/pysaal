from pysaal.time._epoch import Epoch


class TimeSpan:
    def __init__(self, start: Epoch, end: Epoch):
        self.start = start
        self.end = end

    @property
    def days(self) -> float:
        """Return the time span in days.

        :return: Time span in days
        """
        return self.end.utc_ds50 - self.start.utc_ds50
