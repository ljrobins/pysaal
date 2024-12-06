from ctypes import c_double

import pytest

from pysaal.elements import KeplerianElements


def test_from_c_array():
    c_array = (c_double * 6)(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    kep = KeplerianElements.from_c_array(c_array)
    assert kep.semi_major_axis == 1.0
    assert kep.eccentricity == 2.0
    assert kep.inclination == 3.0
    assert kep.mean_anomaly == 4.0
    assert kep.raan == 5.0
    assert kep.argument_of_perigee == 6.0


def test_get_null_pointer():
    kep = KeplerianElements.get_null_pointer()
    assert kep[0] == 0.0
    assert kep[1] == 0.0
    assert kep[2] == 0.0
    assert kep[3] == 0.0
    assert kep[4] == 0.0
    assert kep[5] == 0.0


def test_c_array():
    kep = KeplerianElements(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    c_array = kep.c_array
    assert c_array[0] == 1.0
    assert c_array[1] == 2.0
    assert c_array[2] == 3.0
    assert c_array[3] == 4.0
    assert c_array[4] == 5.0
    assert c_array[5] == 6.0


def test_mean_motion(expected_classical, expected_keplerian):
    assert expected_classical.mean_motion == pytest.approx(expected_keplerian.mean_motion)


def test_eccentric_anomaly(expected_keplerian):
    assert expected_keplerian.eccentric_anomaly == 0.7331052038710836


def test_true_anomaly(expected_keplerian):
    assert expected_keplerian.true_anomaly == 42.00766838425196
