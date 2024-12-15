from pysaal.elements._keplerian_elements import KeplerianElements


class MeanElements(KeplerianElements):
    """Class used to interface with the mean elements of a satellite orbit.

    .. note::

        This class inherits all properties and methods from :ref:`keplerian_elements`.
    """

    def __init__(self, sma: float, ecc: float, inc: float, ma: float, raan: float, aop: float):
        super().__init__(sma, ecc, inc, ma, raan, aop)
