from ctypes import c_double

from pysaal.elements import EquinoctialElements


def test_from_c_array():
    c_array = (c_double * 6)(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    eqnx = EquinoctialElements.from_c_array(c_array)
    assert eqnx.af == 1.0
    assert eqnx.ag == 2.0
    assert eqnx.chi == 3.0
    assert eqnx.psi == 4.0
    assert eqnx.l == 5.0
    assert eqnx.n == 6.0


def test_get_null_pointer():
    eqnx = EquinoctialElements.get_null_pointer()
    assert eqnx[0] == 0.0
    assert eqnx[1] == 0.0
    assert eqnx[2] == 0.0
    assert eqnx[3] == 0.0
    assert eqnx[4] == 0.0
    assert eqnx[5] == 0.0


def test_c_array():
    eqnx = EquinoctialElements(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    c_array = eqnx.c_array
    assert c_array[0] == 1.0
    assert c_array[1] == 2.0
    assert c_array[2] == 3.0
    assert c_array[3] == 4.0
    assert c_array[4] == 5.0
    assert c_array[5] == 6.0
