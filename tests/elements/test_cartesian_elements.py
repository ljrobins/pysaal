from ctypes import c_double

from pysaal.elements import CartesianElements


def test_from_c_arrays():
    c_pos = (c_double * 3)(1.0, 2.0, 3.0)
    c_vel = (c_double * 3)(4.0, 5.0, 6.0)
    cart = CartesianElements.from_c_arrays(c_pos, c_vel)
    assert cart.x == 1.0
    assert cart.y == 2.0
    assert cart.z == 3.0
    assert cart.vx == 4.0
    assert cart.vy == 5.0
    assert cart.vz == 6.0


def test_get_null_pointers():
    null_pos, null_vel = CartesianElements.get_null_pointers()
    assert null_pos[0] == 0.0
    assert null_pos[1] == 0.0
    assert null_pos[2] == 0.0
    assert null_vel[0] == 0.0
    assert null_vel[1] == 0.0
    assert null_vel[2] == 0.0


def test_c_arrays():
    cart = CartesianElements(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    c_pos, c_vel = cart.c_arrays
    assert c_pos[0] == 1.0
    assert c_pos[1] == 2.0
    assert c_pos[2] == 3.0
    assert c_vel[0] == 4.0
    assert c_vel[1] == 5.0
    assert c_vel[2] == 6.0


def test_position():
    cart = CartesianElements(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    pos = cart.position
    assert pos.x == 1.0
    assert pos.y == 2.0
    assert pos.z == 3.0


def test_velocity():
    cart = CartesianElements(1.0, 2.0, 3.0, 4.0, 5.0, 6.0)
    vel = cart.velocity
    assert vel.x == 4.0
    assert vel.y == 5.0
    assert vel.z == 6.0
