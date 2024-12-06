from ctypes import Array, c_double

from pysaal.elements._orbit_state import OrbitState


class Ephemeris:
    def __init__(self, c_array: Array[Array[c_double]]):
        self.c_array = c_array

    def __getitem__(self, item: int) -> OrbitState:
        if abs(item) > len(self.c_array):
            raise IndexError("Index out of range")
        return OrbitState.from_c_array(self.c_array[item])

    def __len__(self) -> int:
        return len(self.c_array)

    @staticmethod
    def null_pointer(num_pts: int) -> Array[Array[c_double]]:
        return ((c_double * 7) * num_pts)()
