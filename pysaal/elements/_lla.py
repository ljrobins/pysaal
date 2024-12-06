from ctypes import c_double


class LLA:
    def __init__(self, lat: float, long: float, alt: float):
        self.latitude = lat
        self.longitude = long
        self.altitude = alt

    @staticmethod
    def get_null_pointer():
        return (c_double * 3)(0.0, 0.0, 0.0)

    @classmethod
    def from_c_array(cls, c_array):
        return cls(c_array[0], c_array[1], c_array[2])
