import pytest

from pysaal.elements import TLE
from pysaal.lib._tle import XA_TLE_SIZE, XS_TLE_SIZE
from pysaal.time import Epoch


def test_line_1(expected_tle, expected_line_1):
    assert expected_tle.line_1 == expected_line_1


def test_line_2(expected_tle, expected_line_2):
    assert expected_tle.line_2 == expected_line_2


def test_get_null_pointers():
    xa_tle, xs_tle = TLE.get_null_pointers()
    assert len(xa_tle) == XA_TLE_SIZE
    assert len(xs_tle) == XS_TLE_SIZE


def test_update(expected_tle):
    expected_tle.load()
    expected_tle.inclination = 42
    state = expected_tle.get_state_at_epoch(expected_tle.epoch)
    expected_tle.destroy()
    assert expected_tle.inclination == 42
    assert state.position.x == pytest.approx(5907.241830363182)
    assert state.position.y == pytest.approx(-1812.0856674529778)
    assert state.position.z == pytest.approx(2828.6276707425336)
    assert state.velocity.x == pytest.approx(3.765882542507204)
    assert state.velocity.y == pytest.approx(4.312300334009153)
    assert state.velocity.z == pytest.approx(-5.088378313453208)
    assert state.longitude == pytest.approx(270.1158920066335)
    assert state.latitude == pytest.approx(24.734533628750928)
    assert state.altitude == pytest.approx(421.19273186284363)


def test_propagate_to_epoch(expected_tle):

    state = expected_tle.get_state_at_epoch(expected_tle.epoch + 1)
    expected_tle.destroy()

    assert state.position.x == pytest.approx(-6000.683061334345)
    assert state.position.y == pytest.approx(2024.4258851255618)
    assert state.position.z == pytest.approx(-2456.1499345834163)
    assert state.velocity.x == pytest.approx(-3.588289406024903)
    assert state.velocity.y == pytest.approx(-4.171760521251378)
    assert state.velocity.z == pytest.approx(5.333708710662431)
    assert state.longitude == pytest.approx(87.54134638131)
    assert state.latitude == pytest.approx(-21.32009251115934)
    assert state.altitude == pytest.approx(417.25424345521776)


def test_get_loaded_keys(expected_tle):
    expected_tle.load()
    keys = expected_tle.get_loaded_keys()
    assert keys[0] == expected_tle.key
    expected_tle.destroy()


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


def test_from_c_arrays(expected_tle):
    tle_2 = TLE.from_c_arrays(expected_tle.c_double_array, expected_tle.c_char_array)
    assert tle_2.line_1 == expected_tle.line_1
    assert tle_2.line_2 == expected_tle.line_2


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


def test_epoch(expected_tle):
    assert expected_tle.epoch.utc_ds50 == 27368.99323416
    expected_tle.epoch = Epoch(27368.0)
    assert expected_tle.line_1 == "1 25544U 98067A   24340.00000000 +.00018216  00000 0  32316-3 0 0999"


def test_n_dot(expected_tle):
    assert expected_tle.n_dot == 0.00018216
    expected_tle.n_dot = 0.00018217
    assert expected_tle.n_dot == 0.00018217
    assert expected_tle.line_1 == "1 25544U 98067A   24340.99323416 +.00018217  00000 0  32316-3 0 0999"


def test_n_dot_dot(expected_tle):
    assert expected_tle.n_dot_dot == 0.0
    expected_tle.n_dot_dot = 0.00000001
    assert expected_tle.n_dot_dot == 0.00000001
    assert expected_tle.line_1 == "1 25544U 98067A   24340.99323416 +.00018216  10000-7  32316-3 0 0999"


def test_b_star(expected_tle):
    assert expected_tle.b_star == 0.00032316
    expected_tle.b_star = 0.00032317
    assert expected_tle.b_star == 0.00032317
    assert expected_tle.line_1 == "1 25544U 98067A   24340.99323416 +.00018216  00000 0  32317-3 0 0999"


def test_ballistic_coefficient(expected_tle):
    assert expected_tle.ballistic_coefficient == 0.00411758224236
    expected_tle.ballistic_coefficient = 0.00411770965857
    assert expected_tle.b_star == 0.00032317
    assert expected_tle.line_1 == "1 25544U 98067A   24340.99323416 +.00018216  00000 0  32317-3 0 0999"


def test_agom(expected_tle):
    assert expected_tle.agom == 0


def test_write_loaded_tles_to_file(expected_tle, tmp_path):
    expected_tle.load()
    TLE.write_loaded_tles_to_file(tmp_path / "tle.txt")
    expected_tle.destroy()
    with open(tmp_path / "tle.txt", "r") as f:
        lines = f.readlines()
        assert lines[0] == "1 25544U 98067A   24340.99323416 +.00018216  00000 0  32316-3 0 0999\n"
        assert lines[1] == "2 25544  51.6388 184.2057 0007028 306.7642 201.1123 15.5026597648519\n"
