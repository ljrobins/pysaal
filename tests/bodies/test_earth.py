from pysaal.bodies import Earth


def test_j2():
    assert Earth.get_j2() == 0.001082616


def test_j3():
    assert Earth.get_j3() == -2.53881e-06


def test_j4():
    assert Earth.get_j4() == -1.65597e-06


def test_j5():
    assert Earth.get_j5() == -2.184827e-07


def test_mu():
    assert Earth.get_mu() == 398600.8


def test_radius():
    assert Earth.get_radius() == 6378.135


def test_flattening():
    assert Earth.get_flattening() == 0.003352779454167505


def test_rotation_rate():
    assert Earth.get_rotation_rate() == 0.0043752690880113
