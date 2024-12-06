from ctypes import c_double

from pysaal.math.linalg import Vector3D


def test_get_null_pointer():
    vec = Vector3D.get_null_pointer()
    assert vec[0] == 0.0
    assert vec[1] == 0.0
    assert vec[2] == 0.0


def test_from_c_array():
    c_array = (c_double * 3)(1.0, 2.0, 3.0)
    vec = Vector3D.from_c_array(c_array)
    assert vec.x == 1.0
    assert vec.y == 2.0
    assert vec.z == 3.0


def test_add():
    vec1 = Vector3D(1.0, 2.0, 3.0)
    vec2 = Vector3D(4.0, 5.0, 6.0)
    vec3 = vec1 + vec2
    assert vec3.x == 5.0
    assert vec3.y == 7.0
    assert vec3.z == 9.0


def test_subtract():
    vec1 = Vector3D(1.0, 2.0, 3.0)
    vec2 = Vector3D(4.0, 5.0, 6.0)
    vec3 = vec1 - vec2
    assert vec3.x == -3.0
    assert vec3.y == -3.0
    assert vec3.z == -3.0


def test_multiply():
    vec = Vector3D(1.0, 2.0, 3.0)
    vec2 = vec * 2
    assert vec2.x == 2.0
    assert vec2.y == 4.0
    assert vec2.z == 6.0


def test_divide():
    vec = Vector3D(1.0, 2.0, 3.0)
    vec2 = vec / 2
    assert vec2.x == 0.5
    assert vec2.y == 1.0
    assert vec2.z == 1.5


def test_dot():
    vec1 = Vector3D(1.0, 2.0, 3.0)
    vec2 = Vector3D(4.0, 5.0, 6.0)
    dot = vec1.dot(vec2)
    assert dot == 32.0


def test_cross():
    vec1 = Vector3D(1.0, 2.0, 3.0)
    vec2 = Vector3D(4.0, 5.0, 6.0)
    vec3 = vec1.cross(vec2)
    assert vec3.x == -3.0
    assert vec3.y == 6.0
    assert vec3.z == -3.0


def test_magnitude():
    vec = Vector3D(1.0, 2.0, 3.0)
    mag = vec.magnitude
    assert mag == 3.7416573867739413


def test_unit():
    vec = Vector3D(1.0, 2.0, 3.0)
    unit = vec.unit
    assert unit.x == 0.2672612419124244
    assert unit.y == 0.5345224838248488
    assert unit.z == 0.8017837257372732


def test_angle():
    vec1 = Vector3D(1.0, 2.0, 3.0)
    vec2 = Vector3D(4.0, 5.0, 6.0)
    angle = vec1.angle(vec2)
    assert angle == 0.2257261285527342


def test_str():
    vec = Vector3D(1.0, 2.0, 3.0)
    assert str(vec) == "[1.0, 2.0, 3.0]"


def test_c_array():
    vec = Vector3D(1.0, 2.0, 3.0)
    c_array = vec.c_array
    assert c_array[0] == 1.0
    assert c_array[1] == 2.0
    assert c_array[2] == 3.0
