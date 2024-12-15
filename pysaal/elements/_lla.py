from ctypes import c_double


class LLA:
    """Class used to store the latitude, longitude, and altitude of a point on the Earth's surface."""

    def __init__(self, lat: float, long: float, alt: float):

        #: The latitude of the point in :math:`deg`
        self.latitude = lat

        #: The longitude of the point in :math:`deg`
        self.longitude = long

        #: The altitude of the point in :math:`km`
        self.altitude = alt

    @staticmethod
    def get_null_pointer():
        """Generate a null pointer to a C array of length 3 to be used by the SAAL library."""
        return (c_double * 3)(0.0, 0.0, 0.0)

    @classmethod
    def from_c_array(cls, c_array):
        """Constructor used when interfacing directly with the SAAL library."""
        return cls(c_array[0], c_array[1], c_array[2])
