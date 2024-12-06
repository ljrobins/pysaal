from pysaal.lib import TIME_CONSTANTS_PATH
from pysaal.time import Epoch, TimeConstants


def test_from_epoch():
    epoch = Epoch(25934.0)
    tcons = TimeConstants.from_epoch(epoch)
    assert tcons.epoch.utc_ds50 == 25934.0
    assert tcons.tai_minus_utc == 37.0
    assert tcons.ut1_minus_utc == -0.17538
    assert tcons.ut1_rate == 0.057
    assert tcons.polar_x == 0.0687
    assert tcons.polar_y == 0.304


def test_get_loaded_time_span():
    tspan = TimeConstants.get_loaded_time_span()
    assert tspan.start.utc_ds50 == 8411.0
    assert tspan.end.utc_ds50 == 26408.0
    assert tspan.days == 17997.0


def test_is_file_loaded():
    assert TimeConstants.is_file_loaded()


def test_load_file():
    TimeConstants.load_file(TIME_CONSTANTS_PATH)
