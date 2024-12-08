import pytest

from pysaal.elements import (
    TLE,
    CartesianElements,
    ClassicalElements,
    EquinoctialElements,
    KeplerianElements,
    MeanElements,
    SPVector,
)
from pysaal.enums import Classification, TLEType


@pytest.fixture
def expected_keplerian():
    return KeplerianElements(42164, 0.0001, 0.42, 42, 200, 300)


@pytest.fixture
def expected_line_1():
    return "1 25544U 98067A   24340.99323416 +.00018216  00000 0  32316-3 0 0999"


@pytest.fixture
def expected_line_2():
    return "2 25544  51.6388 184.2057 0007028 306.7642 201.1123 15.5026597648519"


@pytest.fixture
def expected_classification():
    return Classification("U")


@pytest.fixture
def new_classification():
    return Classification("C")


@pytest.fixture
def expected_name():
    return "98067A"


@pytest.fixture
def expected_type():
    return TLEType("0")


@pytest.fixture
def expected_tle(expected_line_1, expected_line_2):
    return TLE.from_lines(expected_line_1, expected_line_2)


@pytest.fixture
def expected_sp_vector(expected_tle):
    state = expected_tle.get_state_at_epoch(expected_tle.epoch)
    expected_tle.destroy()
    sp = SPVector(expected_tle.epoch, state.cartesian_elements, 1)
    sp.b_term = expected_tle.ballistic_coefficient
    return sp


@pytest.fixture
def expected_equinoctial():
    return EquinoctialElements(
        -7.660444431189783e-05,
        6.42787609686539e-05,
        -0.001253574911285049,
        -0.0034441687623505044,
        542.0000000000001,
        1.0027444112324284,
    )


@pytest.fixture
def expected_mean():
    return MeanElements(
        42164, 7.780854393098447e-05, 0.41999280970042774, 61.143041048518, 200.00055703590135, 280.85640147683625
    )


@pytest.fixture
def expected_classical():
    return ClassicalElements(1.0027444112324284, 0.0001, 0.42, 42, 200, 300)


@pytest.fixture
def expected_cartesian():
    return CartesianElements(
        -42134.866555365596,
        -1477.3611216130757,
        -95.4631435846219,
        0.10749110300482166,
        -3.072941987275631,
        0.021437245884576635,
    )
