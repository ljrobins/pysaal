from datetime import datetime, timezone

import pytest

from pysaal.time import Epoch


def test_time_constants_loaded():
    assert Epoch.time_constants_loaded()


def test_from_components():
    epoch = Epoch.from_components(2021, 1, 1, 0, 0, 0.0)
    assert epoch.utc_ds50 == 25934.0


def test_from_dtg():
    assert Epoch.from_dtg("2021/001 0000 00.000").utc_ds50 == 25934.0
    assert Epoch.from_dtg("2021Jan01000000.000").utc_ds50 == 25934.0
    assert Epoch.from_dtg("2021/001.00000000").utc_ds50 == 25934.0
    assert Epoch.from_dtg("21001000000.000").utc_ds50 == 25934.0


def test_tai_ds50():
    epoch = Epoch(25934.0)
    assert epoch.tai_ds50 == 25934.00042824074


def test_ut1_ds50():
    epoch = Epoch(25934.0)
    assert epoch.ut1_ds50 == 25933.99999797014


def test_tt_ds50():
    epoch = Epoch(25934.0)
    assert epoch.tt_ds50 == 25934.000800740738


def test_dtg_20():
    epoch = Epoch(25934.0)
    assert epoch.dtg_20 == "2021/001 0000 00.000"


def test_dtg_19():
    epoch = Epoch(25934.0)
    assert epoch.dtg_19 == "2021Jan01000000.000"


def test_dtg_17():
    epoch = Epoch(25934.0)
    assert epoch.dtg_17 == "2021/001.00000000"


def test_dtg_15():
    epoch = Epoch(25934.0)
    assert epoch.dtg_15 == "21001000000.000"


def test_year():
    epoch = Epoch(25934.0)
    assert epoch.year == 2021


def test_month():
    epoch = Epoch.from_components(2021, 2, 1, 0, 0, 0.0)
    assert epoch.month == 2


def test_day():
    epoch = Epoch.from_components(2021, 1, 2, 0, 0, 0.0)
    assert epoch.day == 2


def test_hour():
    epoch = Epoch.from_components(2021, 1, 1, 1, 0, 0.0)
    assert epoch.hour == 1


def test_minute():
    epoch = Epoch.from_components(2021, 1, 1, 0, 1, 0.0)
    assert epoch.minute == 1


def test_second():
    epoch = Epoch.from_components(2021, 1, 1, 0, 0, 1.2)
    assert epoch.second == pytest.approx(1.2)


def test_subtract():
    epoch = Epoch(25934.0)
    new_epoch = epoch - 1
    assert new_epoch.utc_ds50 == 25933.0


def test_greater_than():
    epoch = Epoch(25934.0)
    new_epoch = epoch + 1
    assert new_epoch > epoch


def test_less_than():
    epoch = Epoch(25934.0)
    new_epoch = epoch - 1
    assert new_epoch < epoch


def test_greater_than_or_equal():
    epoch = Epoch(25934.0)
    new_epoch = epoch + 1
    assert new_epoch >= epoch
    assert epoch >= epoch


def test_less_than_or_equal():
    epoch = Epoch(25934.0)
    new_epoch = epoch - 1
    assert new_epoch <= epoch
    assert epoch <= epoch


def test_equal():
    epoch = Epoch(25934.0)
    new_epoch = Epoch(25934.0)
    assert new_epoch == epoch


def test_not_equal():
    epoch = Epoch(25934.0)
    new_epoch = epoch + 1
    assert new_epoch != epoch


def test_day_of_year():
    epoch = Epoch.from_components(2021, 2, 1, 0, 0, 0.0)
    assert epoch.day_of_year == 32


def test_datetime():
    epoch = Epoch(25934.0)
    assert epoch.datetime == datetime(2021, 1, 1, 0, 0, 0, tzinfo=timezone.utc)


def test_fk4_greenwich_angle():
    epoch = Epoch(25934.0)
    assert epoch.fk4_greenwich_angle == 1.7604850134918522


def test_fk5_greenwich_angle():
    epoch = Epoch(25934.0)
    assert epoch.fk5_greenwich_angle == 1.7604919497334706


def test_add():
    epoch = Epoch(25934.0)
    new_epoch = epoch + 1
    assert new_epoch.utc_ds50 == 25935.0


def test_greenwich_angle():
    epoch = Epoch(25934.0)
    assert epoch.greenwich_angle == 1.7604919497334706


def test_from_year_and_days():
    epoch = Epoch.from_year_and_days(2021, 1)
    assert epoch.utc_ds50 == 25934.0
