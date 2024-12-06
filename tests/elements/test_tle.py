import pytest

from pysaal.elements import TLE
from pysaal.lib._tle import XA_TLE_SIZE, XS_TLE_SIZE


def test_line_1(expected_tle, expected_line_1):
    assert expected_tle.line_1 == expected_line_1


def test_line_2(expected_tle, expected_line_2):
    assert expected_tle.line_2 == expected_line_2


def test_get_null_pointers():
    xa_tle, xs_tle = TLE.get_null_pointers()
    assert len(xa_tle) == XA_TLE_SIZE
    assert len(xs_tle) == XS_TLE_SIZE


def test_update(expected_tle):
    expected_tle.update()


def test_classification(expected_tle, expected_classification, new_classification):
    assert expected_tle.classification == expected_classification
    expected_tle.classification = new_classification
    assert expected_tle.classification == new_classification


def test_name(expected_tle, expected_name):
    assert expected_tle.name == expected_name


def test_satellite_id(expected_tle):
    assert expected_tle.satellite_id == 25544
    expected_tle.satellite_id = 25545
    assert expected_tle.satellite_id == 25545
    with pytest.raises(ValueError, match="Satellite ID exceeds maximum value"):
        expected_tle.satellite_id = TLE.MAX_SATELLITE_ID + 1


def test_designator(expected_tle, expected_name):
    assert expected_tle.designator == expected_name
    with pytest.raises(ValueError, match="Name exceeds maximum length"):
        expected_tle.designator = "".join(["A" for _ in range(TLE.MAX_DESIGNATOR_LENGTH + 1)])


def test_get_number_in_memory():
    assert TLE.get_number_in_memory() == 0


def test_destroy(expected_tle):
    expected_tle.load()
    expected_tle.destroy()
    assert expected_tle.key is None
    assert not expected_tle.loaded
    assert TLE.get_number_in_memory() == 0


def test_load(expected_tle):
    expected_tle.load()
    assert expected_tle.key is not None
    assert expected_tle.loaded
    assert TLE.get_number_in_memory() == 1
    expected_tle.destroy()
