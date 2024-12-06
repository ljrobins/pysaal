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
    expected_tle.update()


def test_propagate_to_epoch(expected_tle):

    teme, lla = expected_tle.get_state_at_epoch(expected_tle.epoch + 1)
    expected_tle.destroy()

    assert teme.position.x == -6000.683061334345
    assert teme.position.y == 2024.4258851255618
    assert teme.position.z == -2456.1499345834163
    assert teme.velocity.x == -3.588289406024903
    assert teme.velocity.y == -4.171760521251378
    assert teme.velocity.z == 5.333708710662431
    assert lla.longitude == 87.54134638131
    assert lla.latitude == -21.32009251115934
    assert lla.altitude == 417.25424345521776


def test_get_ephemeris(expected_tle):
    ephem = expected_tle.get_ephemeris(expected_tle.epoch, expected_tle.epoch + 1, 1)
    assert len(ephem) == 1441
    assert ephem[-1].position.x == -6000.683061334345
    assert ephem[-1].position.y == 2024.4258851255618
    assert ephem[-1].position.z == -2456.1499345834163
    assert ephem[-1].velocity.x == -3.588289406024903
    assert ephem[-1].velocity.y == -4.171760521251378
    assert ephem[-1].velocity.z == 5.333708710662431


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
