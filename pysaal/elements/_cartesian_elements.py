from ctypes import Array, c_double

from pysaal.math.linalg import Vector3D


class CartesianElements:
    def __init__(self, x: float, y: float, z: float, vx: float, vy: float, vz: float):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    @staticmethod
    def get_null_pointers() -> tuple[Array[c_double], Array[c_double]]:
        return (Vector3D.get_null_pointer(), Vector3D.get_null_pointer())

    @classmethod
    def from_c_arrays(cls, position: Array[c_double], velocity: Array[c_double]):
        return cls(
            position[0],
            position[1],
            position[2],
            velocity[0],
            velocity[1],
            velocity[2],
        )

    @property
    def c_arrays(self) -> tuple[Array[c_double], Array[c_double]]:
        c_pos = (c_double * 3)()
        c_pos[0] = self.x
        c_pos[1] = self.y
        c_pos[2] = self.z
        c_vel = (c_double * 3)()
        c_vel[0] = self.vx
        c_vel[1] = self.vy
        c_vel[2] = self.vz
        return c_pos, c_vel

    @property
    def position(self) -> Vector3D:
        return Vector3D(self.x, self.y, self.z)

    @property
    def velocity(self) -> Vector3D:
        return Vector3D(self.vx, self.vy, self.vz)
