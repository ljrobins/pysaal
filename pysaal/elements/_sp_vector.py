from pysaal.configs import MAX_DESIGNATOR_LENGTH, MAX_SATELLITE_ID
from pysaal.defaults import (
    DEFAULT_AGOM,
    DEFAULT_B_TERM,
    DEFAULT_CLASSIFICATION,
    DEFAULT_SATELLITE_DESIGNATOR,
    DEFAULT_SATELLITE_NAME,
)
from pysaal.elements import CartesianElements
from pysaal.time import Epoch


class SPVector:
    def __init__(self, epoch: Epoch, els: CartesianElements, sat_id: int) -> None:

        #: The epoch for which the state is calculated
        self.epoch = epoch

        #: The cartesian elements of the satellite in :math:`km` and :math:`\frac{km}{s}`
        self.cartesian_elements = els

        #: The solar radiation pressure coefficient in :math:`\frac{km^2}{kg}`
        self.agom = DEFAULT_AGOM

        #: The ballistic coefficient in :math:`\frac{kg}{m^2}`
        self.b_term = DEFAULT_B_TERM

        self._designator = DEFAULT_SATELLITE_DESIGNATOR

        #: The name of the satellite
        self.name = DEFAULT_SATELLITE_NAME
        self._satellite_id = sat_id

        #: The classification of the satellite
        self.classification = DEFAULT_CLASSIFICATION

    @property
    def designator(self):
        """The 8-character designator of the satellite"""
        return self._designator

    @designator.setter
    def designator(self, value: str):
        if len(value) > MAX_DESIGNATOR_LENGTH:
            raise ValueError(f"Designator cannot exceed {MAX_DESIGNATOR_LENGTH} characters.")
        self._designator = value

    @property
    def satellite_id(self):
        """The unique satellite ID"""
        return self._satellite_id

    @satellite_id.setter
    def satellite_id(self, value: int):
        if value > MAX_SATELLITE_ID:
            raise ValueError(f"Satellite ID cannot exceed {MAX_SATELLITE_ID}.")
        self._satellite_id = value

    @property
    def position(self):
        """The position of the satellite in :math:`km`"""
        return self.cartesian_elements.position

    @property
    def velocity(self):
        r"""The velocity of the satellite in :math:`\frac{km}{s}`"""
        return self.cartesian_elements.velocity
