import pytest

from pysaal.bodies import Earth
from pysaal.elements import ConvertElements
from pysaal.enums import TLEType
from pysaal.math.constants import MINUTES_IN_DAY, MINUTUES_TO_DAYS


def test_equinoctial_from_keplerian(expected_keplerian, expected_equinoctial):
    eqnx = ConvertElements.equinoctial.from_keplerian(expected_keplerian)
    assert eqnx.af == pytest.approx(expected_equinoctial.af)
    assert eqnx.ag == pytest.approx(expected_equinoctial.ag)
    assert eqnx.chi == pytest.approx(expected_equinoctial.chi)
    assert eqnx.psi == pytest.approx(expected_equinoctial.psi)
    assert eqnx.l == pytest.approx(expected_equinoctial.l)
    assert eqnx.n == pytest.approx(expected_equinoctial.n)


def test_equinoctial_from_classical(expected_equinoctial, expected_classical):
    eqnx = ConvertElements.equinoctial.from_classical(expected_classical)
    assert eqnx.af == pytest.approx(expected_equinoctial.af)
    assert eqnx.ag == pytest.approx(expected_equinoctial.ag)
    assert eqnx.chi == pytest.approx(expected_equinoctial.chi)
    assert eqnx.psi == pytest.approx(expected_equinoctial.psi)
    assert eqnx.l == pytest.approx(expected_equinoctial.l)
    assert eqnx.n == pytest.approx(expected_equinoctial.n)


def test_equinoctial_from_cartesian(expected_equinoctial, expected_cartesian):
    eqnx = ConvertElements.equinoctial.from_cartesian(expected_cartesian, Earth.get_mu())
    assert eqnx.af == pytest.approx(expected_equinoctial.af)
    assert eqnx.ag == pytest.approx(expected_equinoctial.ag)
    assert eqnx.chi == pytest.approx(expected_equinoctial.chi)
    assert eqnx.psi == pytest.approx(expected_equinoctial.psi)
    assert eqnx.n == pytest.approx(expected_equinoctial.n)


def test_classical_from_equinoctial(expected_equinoctial, expected_classical):
    cl = ConvertElements.classical.from_equinoctial(expected_equinoctial)
    assert cl.mean_motion == pytest.approx(expected_classical.mean_motion)
    assert cl.eccentricity == pytest.approx(expected_classical.eccentricity)
    assert cl.inclination == pytest.approx(expected_classical.inclination)
    assert cl.raan == pytest.approx(expected_classical.raan)
    assert cl.argument_of_perigee == pytest.approx(expected_classical.argument_of_perigee)
    assert cl.mean_anomaly == pytest.approx(expected_classical.mean_anomaly)


def test_keplerian_from_equinoctial(expected_equinoctial, expected_keplerian):
    kep = ConvertElements.keplerian.from_equinoctial(expected_equinoctial)
    assert kep.semi_major_axis == pytest.approx(expected_keplerian.semi_major_axis)
    assert kep.eccentricity == pytest.approx(expected_keplerian.eccentricity)
    assert kep.inclination == pytest.approx(expected_keplerian.inclination)
    assert kep.mean_anomaly == pytest.approx(expected_keplerian.mean_anomaly)
    assert kep.raan == pytest.approx(expected_keplerian.raan)
    assert kep.argument_of_perigee == pytest.approx(expected_keplerian.argument_of_perigee)


def test_keplerian_from_cartesian(expected_keplerian, expected_cartesian):
    kep = ConvertElements.keplerian.from_cartesian(expected_cartesian, Earth.get_mu())
    assert kep.semi_major_axis == pytest.approx(expected_keplerian.semi_major_axis)
    assert kep.eccentricity == pytest.approx(expected_keplerian.eccentricity)
    assert kep.inclination == pytest.approx(expected_keplerian.inclination)
    assert kep.mean_anomaly == pytest.approx(expected_keplerian.mean_anomaly)
    assert kep.raan == pytest.approx(expected_keplerian.raan)
    assert kep.argument_of_perigee == pytest.approx(expected_keplerian.argument_of_perigee)


def test_cartesian_from_keplerian(expected_cartesian, expected_keplerian):
    cart = ConvertElements.cartesian.from_keplerian(expected_keplerian)
    assert cart.x == pytest.approx(expected_cartesian.x)
    assert cart.y == pytest.approx(expected_cartesian.y)
    assert cart.z == pytest.approx(expected_cartesian.z)
    assert cart.vx == pytest.approx(expected_cartesian.vx)
    assert cart.vy == pytest.approx(expected_cartesian.vy)
    assert cart.vz == pytest.approx(expected_cartesian.vz)


def test_cartesian_from_equinoctial(expected_cartesian, expected_equinoctial):
    cart = ConvertElements.cartesian.from_equinoctial(expected_equinoctial)
    assert cart.x == pytest.approx(expected_cartesian.x)
    assert cart.y == pytest.approx(expected_cartesian.y)
    assert cart.z == pytest.approx(expected_cartesian.z)
    assert cart.vx == pytest.approx(expected_cartesian.vx)
    assert cart.vy == pytest.approx(expected_cartesian.vy)
    assert cart.vz == pytest.approx(expected_cartesian.vz)


def test_mean_from_keplerian(expected_keplerian, expected_mean):
    mean = ConvertElements.mean.from_keplerian(expected_keplerian)
    assert mean.semi_major_axis == pytest.approx(expected_mean.semi_major_axis)
    assert mean.eccentricity == pytest.approx(expected_mean.eccentricity)
    assert mean.inclination == pytest.approx(expected_mean.inclination)
    assert mean.raan == pytest.approx(expected_mean.raan)
    assert mean.argument_of_perigee == pytest.approx(expected_mean.argument_of_perigee)
    assert mean.mean_anomaly == pytest.approx(expected_mean.mean_anomaly)


def test_brouwer_from_kozai():
    assert ConvertElements.mean_motion.brouwer.from_kozai(0.1, 0.2, 0.3) == 0.29999773551067593


def test_kozai_from_brouwer():
    assert ConvertElements.mean_motion.kozai.from_brouwer(0.1, 0.2, 0.3) == 0.3000022645292086


def test_mean_motion_from_semi_major_axis(expected_classical, expected_keplerian):
    mm = ConvertElements.mean_motion.from_semi_major_axis(expected_classical.semi_major_axis)
    assert mm == pytest.approx(expected_keplerian.mean_motion)


def test_tle_from_sp_vector(expected_sp_vector, expected_tle):
    tle = ConvertElements.tle.from_sp_vector(expected_sp_vector, TLEType.SGP4)
    dists = []
    for t in range(MINUTES_IN_DAY * 10):
        dists.append(expected_tle.get_range_at_epoch(expected_tle.epoch + t * MINUTUES_TO_DAYS, tle))

    tle.destroy()
    expected_tle.destroy()
    assert max(dists) < 5
    assert max(dists) > 0
