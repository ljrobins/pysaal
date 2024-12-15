from ctypes import Array, c_double

from pysaal.math.linalg import Vector3D


class CartesianElements:
    """Class used to store the cartesian elements of a satellite"""

    def __init__(self, x: float, y: float, z: float, vx: float, vy: float, vz: float):

        #: The x-coordinate of the satellite in :math:`km`
        self.x = x

        #: The y-coordinate of the satellite in :math:`km`
        self.y = y

        #: The z-coordinate of the satellite in :math:`km`
        self.z = z

        #: The x-component of the velocity of the satellite in :math:`\frac{km}{s}`
        self.vx = vx

        #: The y-component of the velocity of the satellite in :math:`\frac{km}{s}`
        self.vy = vy

        #: The z-component of the velocity of the satellite in :math:`\frac{km}{s}`
        self.vz = vz

    @staticmethod
    def get_null_pointers() -> tuple[Array[c_double], Array[c_double]]:
        """Generate a null pointer to a C array of length 3 to be used by the SAAL library"""
        return (Vector3D.get_null_pointer(), Vector3D.get_null_pointer())

    @classmethod
    def from_c_arrays(cls, position: Array[c_double], velocity: Array[c_double]):
        """Constructor used when interfacing directly with the SAAL library"""
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
        """The position and velocity as C arrays to be used by the SAAL library"""
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
        """The first three elements as a single vector in :math:`km`"""
        return Vector3D(self.x, self.y, self.z)

    @property
    def velocity(self) -> Vector3D:
        r"""The last three elements as a single vector in :math:`\frac{km}{s}`"""
        return Vector3D(self.vx, self.vy, self.vz)
