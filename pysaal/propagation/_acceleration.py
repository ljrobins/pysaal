from pysaal.bodies import Earth, Moon, Sun
from pysaal.math.linalg import Vector3D
from pysaal.time import Epoch


class Acceleration:
    @staticmethod
    def from_central_body(mu: float, position: Vector3D) -> Vector3D:
        r = position.magnitude
        return position * (-mu / (r * r * r))

    @staticmethod
    def from_third_body(mu: float, sat_position: Vector3D, body_position: Vector3D) -> Vector3D:
        r_vec = body_position - sat_position
        r_mag = r_vec.magnitude
        s_mag = body_position.magnitude
        vec_1 = r_vec * (1 / (r_mag * r_mag * r_mag))
        vec_2 = body_position * (1 / (s_mag * s_mag * s_mag))
        return (vec_1 - vec_2) * mu

    @staticmethod
    def from_j2(position: Vector3D) -> Vector3D:
        j2 = Earth.get_j2()
        mu = Earth.get_mu()
        r = position.magnitude
        r_earth = Earth.get_radius()
        z = position.z
        c = (-3 * j2 * mu * r_earth * r_earth) / (2 * r * r * r * r * r)
        d = 5 * z * z / (r * r)
        return Vector3D(
            c * position.x * (d - 1),
            c * position.y * (d - 1),
            c * position.z * (d - 3),
        )

    @staticmethod
    def from_earth(position: Vector3D) -> Vector3D:
        return Acceleration.from_central_body(Earth.get_mu(), position)

    @staticmethod
    def from_moon(epoch: Epoch, position: Vector3D) -> Vector3D:
        return Acceleration.from_third_body(Moon.MU, position, Moon.get_jpl_position(epoch))

    @staticmethod
    def from_sun(epoch: Epoch, position: Vector3D) -> Vector3D:
        return Acceleration.from_third_body(Sun.MU, position, Sun.get_jpl_position(epoch))

    @staticmethod
    def from_bodies(epoch: Epoch, position: Vector3D) -> Vector3D:
        return (
            Acceleration.from_earth(position)
            + Acceleration.from_moon(epoch, position)
            + Acceleration.from_sun(epoch, position)
            + Acceleration.from_j2(position)
        )
