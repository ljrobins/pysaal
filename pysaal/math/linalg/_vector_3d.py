from ctypes import Array, c_double
from math import acos, sqrt


class Vector3D:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_c_array(cls, c_array: Array[c_double]) -> "Vector3D":
        return cls(c_array[0], c_array[1], c_array[2])

    @staticmethod
    def get_null_pointer() -> Array[c_double]:
        return (c_double * 3)()

    @property
    def c_array(self) -> Array[c_double]:
        c_array = (c_double * 3)()
        c_array[0] = self.x
        c_array[1] = self.y
        c_array[2] = self.z
        return c_array

    @property
    def magnitude(self) -> float:
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    @property
    def unit(self) -> "Vector3D":
        return self / self.magnitude

    def __add__(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> "Vector3D":
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar: float) -> "Vector3D":
        return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)

    def __str__(self) -> str:
        return f"[{self.x}, {self.y}, {self.z}]"

    def dot(self, other: "Vector3D") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def angle(self, other: "Vector3D") -> float:
        return acos(self.dot(other) / (self.magnitude * other.magnitude))
