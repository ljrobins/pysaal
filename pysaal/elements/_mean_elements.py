from pysaal.elements._keplerian_elements import KeplerianElements


class MeanElements(KeplerianElements):
    def __init__(self, sma: float, ecc: float, inc: float, ma: float, raan: float, aop: float):
        super().__init__(sma, ecc, inc, ma, raan, aop)
