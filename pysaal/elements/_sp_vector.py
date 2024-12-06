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
        self.epoch = epoch
        self.els = els
        self.agom = DEFAULT_AGOM
        self.b_term = DEFAULT_B_TERM
        self._designator = DEFAULT_SATELLITE_DESIGNATOR
        self.name = DEFAULT_SATELLITE_NAME
        self._satellite_id = sat_id
        self.classification = DEFAULT_CLASSIFICATION

    @property
    def designator(self):
        return self._designator

    @designator.setter
    def designator(self, value: str):
        if len(value) > MAX_DESIGNATOR_LENGTH:
            raise ValueError(f"Designator cannot exceed {MAX_DESIGNATOR_LENGTH} characters.")
        self._designator = value

    @property
    def satellite_id(self):
        return self._satellite_id

    @satellite_id.setter
    def satellite_id(self, value: int):
        if value > MAX_SATELLITE_ID:
            raise ValueError(f"Satellite ID cannot exceed {MAX_SATELLITE_ID}.")
        self._satellite_id = value

    @property
    def position(self):
        return self.els.position

    @property
    def velocity(self):
        return self.els.velocity
