from ctypes import Array, c_double

from pysaal.elements._cartesian_elements import CartesianElements
from pysaal.time import Epoch


class OrbitState:
    def __init__(self, epoch: Epoch, elements: CartesianElements):
        self.epoch = epoch
        self.cartesian = elements

    @staticmethod
    def get_null_pointer() -> Array[c_double]:
        return (c_double * 7)()

    @classmethod
    def from_c_array(cls, c_array):
        epoch = Epoch(c_array[0])
        elements = CartesianElements(c_array[1], c_array[2], c_array[3], c_array[4], c_array[5], c_array[6])
        return cls(epoch, elements)

    @property
    def position(self):
        return self.cartesian.position

    @property
    def velocity(self):
        return self.cartesian.velocity
