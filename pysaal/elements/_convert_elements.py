from ctypes import c_double

from pysaal.elements._cartesian_elements import CartesianElements
from pysaal.elements._classical_elements import ClassicalElements
from pysaal.elements._equinoctial_elements import EquinoctialElements
from pysaal.elements._keplerian_elements import KeplerianElements
from pysaal.elements._mean_elements import MeanElements
from pysaal.elements._sp_vector import SPVector
from pysaal.elements._tle import TLE
from pysaal.enums import TLEType
from pysaal.lib import DLLs
from pysaal.math.constants import B_STAR_TO_B_TERM_COEFFICIENT


class _GetEquinoctial:
    """Class used to calculate the equinoctial elements of a satellite orbit

    .. note::

        This class is not intended to be used directly. Use the :class:`ConvertElements` class instead.
    """

    @staticmethod
    def from_keplerian(kep: KeplerianElements) -> EquinoctialElements:
        """Converts from Keplerian elements to Equinoctial elements

        :param kep: The Keplerian elements to convert

        :example:

        .. code-block:: python

            from pysaal.elements import ConvertElements, KeplerianElements

            kep = KeplerianElements(42164, 0.0001, 0.42, 42, 200, 300)
            eqnx = ConvertElements.equinoctial.from_keplerian(kep)
        """
        c_eqnx = EquinoctialElements.get_null_pointer()
        DLLs.astro_func.KepToEqnx(kep.c_array, c_eqnx)
        return EquinoctialElements.from_c_array(c_eqnx)

    @staticmethod
    def from_classical(cl: ClassicalElements) -> EquinoctialElements:
        """Converts from Classical elements to Equinoctial elements

        :param cl: The Classical elements to convert

        :example:

        .. code-block:: python

            from pysaal.elements import ConvertElements, ClassicalElements

            cl = ClassicalElements(
                1.0027444112324284,
                0.0001,
                0.42,
                42,
                200,
                300,
            )
            eqnx = ConvertElements.equinoctial.from_classical(cl)
        """
        c_eqnx = EquinoctialElements.get_null_pointer()
        DLLs.astro_func.ClassToEqnx(cl.c_array, c_eqnx)
        return EquinoctialElements.from_c_array(c_eqnx)

    @staticmethod
    def from_cartesian(cart: CartesianElements, mu: float) -> EquinoctialElements:
        r"""Converts from Cartesian elements to Equinoctial elements

        :param cart: The TEME cartesian elements in :math:`km` and :math:`\frac{km}{s}`
        :param mu: The gravitational parameter of the central body in :math:`\frac{km^3}{s^2}`

        :example:

        .. code-block:: python

            from pysaal.elements import ConvertElements, CartesianElements
            from pysaal.bodies import Earth

            cart = CartesianElements(
                -42134.866555365596,
                -1477.3611216130757,
                -95.4631435846219,
                0.10749110300482166,
                -3.072941987275631,
                0.021437245884576635,
            )
            eqnx = ConvertElements.equinoctial.from_cartesian(cart, Earth.get_mu())
        """
        c_eqnx = EquinoctialElements.get_null_pointer()
        DLLs.astro_func.PosVelMuToEqnx(cart.position.c_array, cart.velocity.c_array, c_double(mu), c_eqnx)
        return EquinoctialElements.from_c_array(c_eqnx)


class _GetKeplerian:
    """Class used to calculate the keplerian elements of a satellite orbit

    .. note::

        This class is not intended to be used directly. Use the :class:`ConvertElements` class instead.
    """

    @staticmethod
    def from_equinoctial(eqnx: EquinoctialElements) -> KeplerianElements:
        """Converts from Equinoctial elements to Keplerian elements

        :param eqnx: The Equinoctial elements to convert

        :example:

        .. code-block:: python

            from pysaal.elements import ConvertElements, EquinoctialElements

            eqnx = EquinoctialElements(
                -7.660444431189783e-05,
                6.42787609686539e-05, -0.001253574911285049,
                -0.0034441687623505044,
                542.0000000000001,
                1.0027444112324284
            )
            kep = ConvertElements.keplerian.from_equinoctial(eqnx)
        """
        c_kep = KeplerianElements.get_null_pointer()
        DLLs.astro_func.EqnxToKep(eqnx.c_array, c_kep)
        return KeplerianElements.from_c_array(c_kep)

    @staticmethod
    def from_cartesian(cart: CartesianElements, mu: float) -> KeplerianElements:
        r"""Converts from Cartesian elements to Keplerian elements

        :param cart: The cartesian elements in :math:`km` and :math:`\frac{km}{s}`

        :param mu: The gravitational parameter of the central body in :math:`\frac{km^3}{s^2}`

        :example:

        .. code-block:: python

            from pysaal.elements import ConvertElements, CartesianElements
            from pysaal.bodies import Earth

            cart = CartesianElements(
                -42134.866555365596,
                -1477.3611216130757,
                -95.4631435846219,
                0.10749110300482166,
                -3.072941987275631,
                0.021437245884576635,
            )
            kep = ConvertElements.keplerian.from_cartesian(cart, Earth.get_mu())
        """
        c_kep = KeplerianElements.get_null_pointer()
        DLLs.astro_func.PosVelMuToKep(cart.position.c_array, cart.velocity.c_array, c_double(mu), c_kep)
        return KeplerianElements.from_c_array(c_kep)


class _GetCartesian:
    """Class used to calculate the cartesian elements of a satellite orbit

    .. note::

        This class is not intended to be used directly. Use the :class:`ConvertElements` class instead.
    """

    @staticmethod
    def from_keplerian(kep: KeplerianElements) -> CartesianElements:
        """Converts from Keplerian elements to Cartesian elements

        :param kep: The Keplerian elements to convert

        :example:

        .. code-block:: python

            from pysaal.elements import ConvertElements, KeplerianElements

            kep = KeplerianElements(42164, 0.0001, 0.42, 42, 200, 300)
            cart = ConvertElements.cartesian.from_keplerian(kep)
        """
        c_pos, c_vel = CartesianElements.get_null_pointers()
        DLLs.astro_func.KepToPosVel(kep.c_array, c_pos, c_vel)
        return CartesianElements.from_c_arrays(c_pos, c_vel)

    @staticmethod
    def from_equinoctial(eqnx: EquinoctialElements) -> CartesianElements:
        """Converts from Equinoctial elements to Cartesian elements

        :param eqnx: The Equinoctial elements to convert

        :example:

        .. code-block:: python

            from pysaal.elements import ConvertElements, EquinoctialElements

            eqnx = EquinoctialElements(
                -7.660444431189783e-05,
                6.42787609686539e-05,
                -0.001253574911285049,
                -0.0034441687623505044,
                542.0000000000001,
                1.0027444112324284
            )
            cart = ConvertElements.cartesian.from_equinoctial(eqnx)
        """
        c_pos, c_vel = CartesianElements.get_null_pointers()
        DLLs.astro_func.EqnxToPosVel(eqnx.c_array, c_pos, c_vel)
        return CartesianElements.from_c_arrays(c_pos, c_vel)


class _GetClassical:
    """Class used to calculate the classical elements of a satellite orbit

    .. note::

        This class is not intended to be used directly. Use the :class:`ConvertElements` class instead.
    """

    @staticmethod
    def from_equinoctial(eqnx: EquinoctialElements) -> ClassicalElements:
        """Converts from Equinoctial elements to Classical elements

        :param eqnx: The Equinoctial elements to convert

        :example:

        .. code-block:: python

            from pysaal.elements import ConvertElements, EquinoctialElements

            eqnx = EquinoctialElements(
                -7.660444431189783e-05,
                6.42787609686539e-05,
                -0.001253574911285049,
                -0.0034441687623505044,
                542.0000000000001,
                1.0027444112324284
            )
            cl = ConvertElements.classical.from_equinoctial(eqnx)
        """
        c_class = ClassicalElements.get_null_pointer()
        DLLs.astro_func.EqnxToClass(eqnx.c_array, c_class)
        return ClassicalElements.from_c_array(c_class)


class _GetMean:
    """Class used to calculate the mean elements of a satellite orbit

    .. note::

        This class is not intended to be used directly. Use the :class:`ConvertElements` class instead.
    """

    @staticmethod
    def from_keplerian(kep: KeplerianElements) -> MeanElements:
        """Converts from Keplerian elements to Mean elements

        :param kep: The Keplerian elements to convert

        :example:

        .. code-block:: python

            from pysaal.elements import ConvertElements, KeplerianElements

            kep = KeplerianElements(42164, 0.0001, 0.42, 42, 200, 300)
            mean = ConvertElements.mean.from_keplerian(kep)
        """
        c_mean = MeanElements.get_null_pointer()
        DLLs.astro_func.KepOscToMean(kep.c_array, c_mean)
        return MeanElements.from_c_array(c_mean)


class _GetBrouwer:
    """Class used to calculate the Brouwer mean motion of a satellite orbit

    .. note::

        This class is not intended to be used directly. Use the :class:`ConvertElements` class instead.
    """

    @staticmethod
    def from_kozai(e: float, i: float, n: float) -> float:
        r"""Converts from Kozai mean motion to Brouwer mean motion

        :param e: The eccentricity of the orbit
        :param i: The inclination of the orbit in :math:`deg`
        :param n: The Kozai mean motion of the orbit in :math:`\frac{rev}{day}`

        :return: The Brouwer mean motion of the orbit in :math:`\frac{rev}{day}`

        :example:

        .. code-block:: python

            from pysaal.elements import ConvertElements

            brouwer_n = ConvertElements.mean_motion.brouwer.from_kozai(0.0001, 0.42, 42)
        """
        return DLLs.astro_func.KozaiToBrouwer(c_double(e), c_double(i), c_double(n))


class _GetKozai:
    """Class used to calculate the Kozai mean motion of a satellite orbit

    .. note::

        This class is not intended to be used directly. Use the :class:`ConvertElements` class instead.
    """

    @staticmethod
    def from_brouwer(e: float, i: float, n: float) -> float:
        r"""Converts from Brouwer mean motion to Kozai mean motion

        :param e: The eccentricity of the orbit
        :param i: The inclination of the orbit in :math:`deg`
        :param n: The Brouwer mean motion of the orbit in :math:`\frac{rev}{day}`

        :return: The Kozai mean motion of the orbit in :math:`\frac{rev}{day}`

        :example:

        .. code-block:: python

            from pysaal.elements import ConvertElements

            kozai_n = ConvertElements.mean_motion.kozai.from_brouwer(0.0001, 0.42, 42)
        """
        return DLLs.astro_func.BrouwerToKozai(c_double(e), c_double(i), c_double(n))


class _GetMeanMotion:
    """Class used to calculate the mean motion of a satellite orbit

    .. note::

        This class is not intended to be used directly. Use the :class:`ConvertElements` class instead.
    """

    #: Converts to Brouwer mean motion
    brouwer = _GetBrouwer

    #: Converts to Kozai mean motion
    kozai = _GetKozai

    @staticmethod
    def from_semi_major_axis(a: float) -> float:
        r"""Converts from semi-major axis to mean motion

        :param a: The semi-major axis of the orbit in :math:`km`

        :return: The mean motion of the orbit in :math:`\frac{rev}{day}`

        :example:

        .. code-block:: python

            from pysaal.elements import ConvertElements

            n = ConvertElements.mean_motion.from_semi_major_axis(42164)
        """
        return DLLs.astro_func.AToN(c_double(a))


class _GetTLE:
    """Class used to calculate the TLE of a satellite orbit

    .. note::

        This class is not intended to be used directly. Use the :class:`ConvertElements` class instead.
    """

    @staticmethod
    def from_sp_vector(sp: SPVector, tle_type: TLEType) -> TLE:
        r"""Converts from a SPVector to a TLE

        :param sp: The SPVector to convert
        :param tle_type: The type of TLE to generate

        :return: The TLE of the satellite

        :example:

        .. code-block:: python

            from pysaal.elements import ConvertElements, SPVector, CartesianElements
            from pysaal.time import Epoch
            from pysaal.enums import TLEType

            epoch = Epoch.now()
            teme_state = CartesianElements(
                -42134.866555365596,
                -1477.3611216130757,
                -95.4631435846219,
                0.10749110300482166,
                -3.072941987275631,
                0.021437245884576635,
            )
            sat_id = 1
            sp = SPVector(epoch, teme_state, sat_id)
            tle_type = TLEType.SGP4
            tle = ConvertElements.tle.from_sp_vector(sp, tle_type)
        """

        tle = TLE()
        tle.satellite_id = sp.satellite_id
        tle.epoch = sp.epoch
        tle.ephemeris_type = tle_type
        tle.ballistic_coefficient = sp.b_term
        tle.b_star = sp.b_term / B_STAR_TO_B_TERM_COEFFICIENT
        tle.agom = sp.agom
        tle.designator = sp.designator
        tle.classification = sp.classification
        DLLs.sgp4_prop.Sgp4PosVelToTleArr(sp.position.c_array, sp.velocity.c_array, tle.c_double_array)
        return tle


class ConvertElements:
    """Class used to convert between different types of orbital elements"""

    #: Converts to equinoctial elements
    equinoctial = _GetEquinoctial

    #: Converts to keplerian elements
    keplerian = _GetKeplerian

    #: Converts to cartesian elements
    cartesian = _GetCartesian

    #: Converts to classical elements
    classical = _GetClassical

    #: Converts to mean elements
    mean = _GetMean

    #: Converts to mean motion
    mean_motion = _GetMeanMotion

    #: Converts to TLE
    tle = _GetTLE
