from pysaal.bodies import Earth
from pysaal.enums import EarthModel


def test_j2():
    assert Earth.get_j2() == 0.001082616


def test_j3():
    assert Earth.get_j3() == -2.53881e-06


def test_j4():
    assert Earth.get_j4() == -1.65597e-06


def test_j5():
    assert Earth.get_j5() == -2.184827e-07


def test_mu():

    default_model = Earth.get_model()

    Earth.set_model(EarthModel.WGS_72)
    wgs_72_mu = Earth.get_mu()
    Earth.set_model(EarthModel.WGS_84)
    wgs_84_mu = Earth.get_mu()
    Earth.set_model(EarthModel.EGM_96)
    egm_96_mu = Earth.get_mu()
    Earth.set_model(EarthModel.EGM_08)
    egm_08_mu = Earth.get_mu()
    Earth.set_model(EarthModel.JGM_2)
    jgm_2_mu = Earth.get_mu()
    Earth.set_model(EarthModel.SEM68R)
    sem68r_mu = Earth.get_mu()
    Earth.set_model(EarthModel.GEM5)
    gem5_mu = Earth.get_mu()
    Earth.set_model(EarthModel.GEM9)
    gem9_mu = Earth.get_mu()

    assert wgs_72_mu == 398600.8
    assert wgs_84_mu == 398600.5
    assert egm_96_mu == 398600.4415
    assert egm_08_mu == 398600.4415
    assert jgm_2_mu == 398600.4415
    assert sem68r_mu == 398601.199437963
    assert gem5_mu == 398601.299998451
    assert gem9_mu == 398600.639998969

    Earth.set_model(default_model)


def test_radius():

    default_model = Earth.get_model()

    Earth.set_model(EarthModel.WGS_72)
    wgs_72_radius = Earth.get_radius()
    Earth.set_model(EarthModel.WGS_84)
    wgs_84_radius = Earth.get_radius()
    Earth.set_model(EarthModel.EGM_96)
    egm_96_radius = Earth.get_radius()
    Earth.set_model(EarthModel.EGM_08)
    egm_08_radius = Earth.get_radius()
    Earth.set_model(EarthModel.JGM_2)
    jgm_2_radius = Earth.get_radius()
    Earth.set_model(EarthModel.SEM68R)
    sem68r_radius = Earth.get_radius()
    Earth.set_model(EarthModel.GEM5)
    gem5_radius = Earth.get_radius()
    Earth.set_model(EarthModel.GEM9)
    gem9_radius = Earth.get_radius()

    assert wgs_72_radius == 6378.135
    assert wgs_84_radius == 6378.137
    assert egm_96_radius == 6378.1363
    assert egm_08_radius == 6378.1363
    assert jgm_2_radius == 6378.1363
    assert sem68r_radius == 6378.145
    assert gem5_radius == 6378.155
    assert gem9_radius == 6378.14

    Earth.set_model(default_model)


def test_flattening():
    assert Earth.get_flattening() == 0.003352779454167505


def test_rotation_rate():
    assert Earth.get_rotation_rate() == 0.0043752690880113
