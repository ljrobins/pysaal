from pysaal.elements import MeanElements


def test_mean_elements(expected_keplerian):
    mean = MeanElements(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    assert mean.semi_major_axis == 1.0
    assert mean.eccentricity == 2.0
    assert mean.inclination == 3.0
    assert mean.raan == 5.0
    assert mean.argument_of_perigee == 6.0
    assert mean.mean_anomaly == 4.0
