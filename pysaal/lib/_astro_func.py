# This wrapper file was generated automatically by the GenDllWrappers program.
import platform
from ctypes import CDLL, POINTER, c_char_p, c_double, c_int, c_longlong, c_void_p
from pathlib import Path

c_double_p = POINTER(c_double)


LIB_PATH = Path(__file__).parent

# get the right filename of the dll/so
if platform.uname()[0] == "Windows":
    DLL_NAME = LIB_PATH / "AstroFunc.dll"

if platform.uname()[0] == "Linux":
    DLL_NAME = LIB_PATH / "libastrofunc.so"

if platform.uname()[0] == "Darwin":
    DLL_NAME = LIB_PATH / "libastrofunc.dylib"


def get_astro_func_dll():
    """LoadAstroFuncDll() -- Loads AstroFunc.dll from the PATH or LD_LIBRARY_PATH
    depending on Operating System and returns the object type.
    for each of its functions.

    Return Value
    an object which can be used to access the dll."""

    # load the dll
    if DLL_NAME.exists():
        dllObj = CDLL(DLL_NAME.as_posix())
    else:
        raise FileNotFoundError(f"{DLL_NAME} not found")

    # set parameter list and return type for each function

    # Notes: This function has been deprecated since v9.0.
    # Initializes AstroFunc DLL for use in the program.
    # If this function returns an error, it is recommended that you stop the program immediately.
    #
    # An error will occur if you forget to load and initialize all the prerequisite DLLs, as listed in the DLL
    # Prerequisites section of the accompanying documentation, before using this DLL.
    # apAddr: The handle that was returned from DllMainInit(). See the documentation for DllMain.dll for
    # details. (in-Long)
    dllObj.AstroFuncInit.restype = c_int
    dllObj.AstroFuncInit.argtypes = [c_longlong]

    # Retrieves information about the current version of AstroFunc.dll. The information is placed in the string
    # parameter you pass in.
    # The returned string provides information about the version number, build date, and platform.
    # infoStr: A string to hold the information about AstroFunc.dll. (out-Character[128])
    dllObj.AstroFuncGetInfo.restype = None
    dllObj.AstroFuncGetInfo.argtypes = [c_char_p]

    # Converts a set of Keplerian elements to a set of equinoctial elements.
    # xa_kep: The set of Keplerian elements to be converted. see XA_KEP_? (in-Double[6])
    # xa_eqnx: The resulting set of equinoctial elements. see XA_EQNX_? (out-Double[6])
    dllObj.KepToEqnx.restype = None
    dllObj.KepToEqnx.argtypes = [c_double * 6, c_double * 6]

    # Converts a set of osculating Keplerian elements to osculating position and velocity vectors.
    # xa_kep: The set of Keplerian elements to be converted. see XA_KEP_? (in-Double[6])
    # pos: The resulting position vector. (out-Double[3])
    # vel: The resulting velocity vector. (out-Double[3])
    dllObj.KepToPosVel.restype = None
    dllObj.KepToPosVel.argtypes = [c_double * 6, c_double * 3, c_double * 3]

    # Converts a set of Keplerian elements to Ubar, Vbar, and Wbar vectors.
    # xa_kep: The set of Keplerian elements to be converted. see XA_KEP_? (in-Double[6])
    # uBar: The resulting ubar vector. (out-Double[3])
    # vBar: The resulting vbar vector. (out-Double[3])
    # wBar: The resulting wbar vector. (out-Double[3])
    dllObj.KepToUVW.restype = None
    dllObj.KepToUVW.argtypes = [c_double * 6, c_double * 3, c_double * 3, c_double * 3]

    # Converts a set of classical elements to a set of equinoctial elements.
    # xa_cls: The set of classical elements to be converted. see XA_CLS_? (in-Double[6])
    # xa_eqnx: The resulting set of equinoctial elements. see XA_EQNX_? (out-Double[6])
    dllObj.ClassToEqnx.restype = None
    dllObj.ClassToEqnx.argtypes = [c_double * 6, c_double * 6]

    # Converts a set of equinoctial elements to a set of classical elements.
    # xa_eqnx: The set of equinoctial elements to be converted. see XA_EQNX_? (in-Double[6])
    # xa_cls: The resulting set of classical elements. see XA_CLS_? (out-Double[6])
    dllObj.EqnxToClass.restype = None
    dllObj.EqnxToClass.argtypes = [c_double * 6, c_double * 6]

    # Converts a set of equinoctial elements to a set of Keplerian elements.
    # xa_eqnx: The set of equinoctial elements to be converted. see XA_EQNX_? (in-Double[6])
    # xa_kep: The resulting set of Keplerian elements. see XA_KEP_? (out-Double[6])
    dllObj.EqnxToKep.restype = None
    dllObj.EqnxToKep.argtypes = [c_double * 6, c_double * 6]

    # Converts a set of equinoctial elements to position and velocity vectors.
    # xa_eqnx: The set of equinoctial elements to be converted. see XA_EQNX_? (in-Double[6])
    # pos: The resulting position vector. (out-Double[3])
    # vel: The resulting velocity vector. (out-Double[3])
    dllObj.EqnxToPosVel.restype = None
    dllObj.EqnxToPosVel.argtypes = [c_double * 6, c_double * 3, c_double * 3]

    # Converts position and velocity vectors to a set of equinoctial elements.
    # pos: The position vector to be converted. (in-Double[3])
    # vel: The velocity vector to be converted. (in-Double[3])
    # xa_eqnx: The resulting set of equinoctial elements. see XA_EQNX_? (out-Double[6])
    dllObj.PosVelToEqnx.restype = None
    dllObj.PosVelToEqnx.argtypes = [c_double * 3, c_double * 3, c_double * 6]

    # Converts position and velocity vectors to a set of equinoctial elements with the given mu value.
    # This function is used when working with the SP propagator to get a more accurate set of equinoctial elements.
    # pos: The position vector to be converted. (in-Double[3])
    # vel: The velocity vector to be converted. (in-Double[3])
    # mu: The value of mu. (in-Double)
    # xa_eqnx: The resulting set of equinoctial elements. see XA_EQNX_? (out-Double[6])
    dllObj.PosVelMuToEqnx.restype = None
    dllObj.PosVelMuToEqnx.argtypes = [c_double * 3, c_double * 3, c_double, c_double * 6]

    # Converts osculating position and velocity vectors to a set of osculating Keplerian elements.
    # pos: The position vector to be converted. (in-Double[3])
    # vel: The velocity vector to be converted. (in-Double[3])
    # xa_kep: The resulting set of Keplerian elements. see XA_KEP_? (out-Double[6])
    dllObj.PosVelToKep.restype = None
    dllObj.PosVelToKep.argtypes = [c_double * 3, c_double * 3, c_double * 6]

    # Converts osculating position and velocity vectors to a set of osculating Keplerian elements with the given value
    # of mu.
    # This function is used when working with the SP propagator to get a more accurate set of Keplerian elements.
    # pos: The position vector to be converted. (in-Double[3])
    # vel: The velocity vector to be converted. (in-Double[3])
    # mu: The value of mu. (in-Double)
    # xa_kep: The resulting set of Keplerian elements. see XA_KEP_? (out-Double[6])
    dllObj.PosVelMuToKep.restype = None
    dllObj.PosVelMuToKep.argtypes = [c_double * 3, c_double * 3, c_double, c_double * 6]

    # Converts position and velocity vectors to U, V, W vectors. See the remarks section for details.
    # The resulting vectors have the following meanings.
    # U vector: along radial direction
    # V vector: W x U
    # W vector: pos x vel
    # pos: The position vector to be converted. (in-Double[3])
    # vel: The velocity vector to be converted. (in-Double[3])
    # uvec: The resulting U vector. (out-Double[3])
    # vVec: The resulting V vector. (out-Double[3])
    # wVec: The resulting W vector. (out-Double[3])
    dllObj.PosVelToUUVW.restype = None
    dllObj.PosVelToUUVW.argtypes = [c_double * 3, c_double * 3, c_double * 3, c_double * 3, c_double * 3]

    # Converts position and velocity vectors to U, V, W vectors. See the remarks section for details.
    # The resulting vectors have the following meanings.
    # U vector: V x W
    # V vector: along velocity direction
    # W vector: pos x vel
    # pos: The position vector. (in-Double[3])
    # vel: The velocity vector. (in-Double[3])
    # uvec: The resulting U vector. (out-Double[3])
    # vVec: The resulting V vector. (out-Double[3])
    # wVec: The resulting W vector. (out-Double[3])
    dllObj.PosVelToPTW.restype = None
    dllObj.PosVelToPTW.argtypes = [c_double * 3, c_double * 3, c_double * 3, c_double * 3, c_double * 3]

    # Solves Kepler's equation (M = E - e sin(E)) for the eccentric anomaly, E, by iteration.
    # xa_kep: The set of Keplerian elements for which to solve the equation. see XA_KEP_? (in-Double[6])
    dllObj.SolveKepEqtn.restype = c_double
    dllObj.SolveKepEqtn.argtypes = [c_double * 6]

    # Computes true anomaly from a set of Keplerian elements.
    # xa_kep: The set of Keplerian elements for which to compute true anomaly. see XA_KEP_? (in-Double[6])
    dllObj.CompTrueAnomaly.restype = c_double
    dllObj.CompTrueAnomaly.argtypes = [c_double * 6]

    # Converts mean motion N to semi-major axis A.
    # n: Mean motion N (revs/day). (in-Double)
    dllObj.NToA.restype = c_double
    dllObj.NToA.argtypes = [c_double]

    # Converts semi-major axis A to mean motion N.
    # a: Semi-major axis A (km). (in-Double)
    dllObj.AToN.restype = c_double
    dllObj.AToN.argtypes = [c_double]

    # Converts Kozai mean motion to Brouwer mean motion.
    # SGP TLE's use Kozai mean motion while SGP4/SGP4-XP TLE's use Brouwer mean motion.
    # eccen: eccentricity (in-Double)
    # incli: inclination (degrees) (in-Double)
    # nKozai: Kozai mean motion (revs/day). (in-Double)
    dllObj.KozaiToBrouwer.restype = c_double
    dllObj.KozaiToBrouwer.argtypes = [c_double, c_double, c_double]

    # Converts Brouwer mean motion to Kozai mean motion.
    # SGP TLE's use Kozai mean motion while SGP4/SGP4-XP TLE's use Brouwer mean motion.
    # eccen: eccentricity (in-Double)
    # incli: inclination (degrees) (in-Double)
    # nBrouwer: Brouwer mean motion (revs/day). (in-Double)
    dllObj.BrouwerToKozai.restype = c_double
    dllObj.BrouwerToKozai.argtypes = [c_double, c_double, c_double]

    # Converts a set of osculating Keplerian elements to a set of mean Keplerian elements using method 9 algorithm.
    # xa_OscKep: The set of osculating Keplerian elements to be converted. see XA_KEP_? (in-Double[6])
    # xa_MeanKep: The resulting set of mean Keplerian elements. see XA_KEP_? (out-Double[6])
    dllObj.KepOscToMean.restype = None
    dllObj.KepOscToMean.argtypes = [c_double * 6, c_double * 6]

    # Converts an ECI position vector XYZ to geodetic latitude, longitude, and height.
    # thetaG: ThetaG - Greenwich mean sidereal time (rad). (in-Double)
    # metricPos: The ECI (TEME of Date) position vector (km) to be converted. (in-Double[3])
    # metricLLH: The resulting geodetic north latitude (degree), east longitude(degree), and
    # height (km). (out-Double[3])
    dllObj.XYZToLLH.restype = None
    dllObj.XYZToLLH.argtypes = [c_double, c_double * 3, c_double * 3]

    # Converts an ECI position vector XYZ to geodetic latitude, longitude, and height at the specified time.
    # ds50UTC: Input time in days since 1950 UTC (in-Double)
    # metricPos: The ECI (TEME of Date) position vector (km) to be converted. (in-Double[3])
    # metricLLH: The resulting geodetic north latitude (degree), east longitude(degree), and
    # height (km). (out-Double[3])
    dllObj.XYZToLLHTime.restype = None
    dllObj.XYZToLLHTime.argtypes = [c_double, c_double * 3, c_double * 3]

    # Converts geodetic latitude, longitude, and height to an ECI position vector XYZ.
    # thetaG: Theta - Greenwich mean sidereal time (rad). (in-Double)
    # metricLLH: An array containing geodetic north latitude (degree), east longitude (degree), and height (km) to
    # be converted. (in-Double[3])
    # metricXYZ: The resulting ECI (TEME of Date) position vector (km). (out-Double[3])
    dllObj.LLHToXYZ.restype = None
    dllObj.LLHToXYZ.argtypes = [c_double, c_double * 3, c_double * 3]

    # Converts geodetic latitude, longitude, and height to an ECI position vector XYZ at the specified time.
    # ds50UTC: Input time in days since 1950 UTC (in-Double)
    # metricLLH: An array containing geodetic north latitude (degree), east longitude (degree), and height (km) to be
    # converted. (in-Double[3])
    # metricXYZ: The resulting ECI (TEME of Date) position vector (km). (out-Double[3])
    dllObj.LLHToXYZTime.restype = None
    dllObj.LLHToXYZTime.argtypes = [c_double, c_double * 3, c_double * 3]

    # Converts EFG position and velocity vectors to ECI position and velocity vectors.
    # thetaG: Theta - Greenwich mean sidereal time (rad). (in-Double)
    # posEFG: The EFG position vector (km) to be converted. (in-Double[3])
    # velEFG: The EFG velocity vector (km/s) to be converted. (in-Double[3])
    # posECI: The resulting ECI (TEME of Date) position vector (km). (out-Double[3])
    # velECI: The resulting ECI (TEME of Date) velocity vector (km/s). (out-Double[3])
    dllObj.EFGToECI.restype = None
    dllObj.EFGToECI.argtypes = [c_double, c_double * 3, c_double * 3, c_double * 3, c_double * 3]

    # Converts EFG position and velocity vectors to ECI position and velocity vectors at the specified time.
    # ds50UTC: Input time in days since 1950 UTC (in-Double)
    # posEFG: The EFG position vector (km) to be converted. (in-Double[3])
    # velEFG: The EFG velocity vector (km/s) to be converted. (in-Double[3])
    # posECI: The resulting ECI (TEME of Date) position vector (km). (out-Double[3])
    # velECI: The resulting ECI (TEME of Date) velocity vector (km/s). (out-Double[3])
    dllObj.EFGToECITime.restype = None
    dllObj.EFGToECITime.argtypes = [c_double, c_double * 3, c_double * 3, c_double * 3, c_double * 3]

    # Converts ECI position and velocity vectors to EFG position and velocity vectors.
    # thetaG: Theta - Greenwich mean sidereal time (rad). (in-Double)
    # posECI: The ECI (TEME of Date) position vector (km) to be converted. (in-Double[3])
    # velECI: The ECI (TEME of Date) velocity vector (km/s) to be converted. (in-Double[3])
    # posEFG: The resulting EFG position vector (km). (out-Double[3])
    # velEFG: The resulting EFG velocity vector (km/s). (out-Double[3])
    dllObj.ECIToEFG.restype = None
    dllObj.ECIToEFG.argtypes = [c_double, c_double * 3, c_double * 3, c_double * 3, c_double * 3]

    # Converts ECI position and velocity vectors to EFG position and velocity vectors at the specified time.
    # ds50UTC: Input time in days since 1950 UTC (in-Double)
    # posECI: The ECI (TEME of Date) position vector (km) to be converted. (in-Double[3])
    # velECI: The ECI (TEME of Date) velocity vector (km/s) to be converted. (in-Double[3])
    # posEFG: The resulting EFG position vector (km). (out-Double[3])
    # velEFG: The resulting EFG velocity vector (km/s). (out-Double[3])
    dllObj.ECIToEFGTime.restype = None
    dllObj.ECIToEFGTime.argtypes = [c_double, c_double * 3, c_double * 3, c_double * 3, c_double * 3]

    # Converts ECR position and velocity vectors to EFG position and velocity vectors.
    # polarX: Polar motion X (arc-sec). (in-Double)
    # polarY: Polar motion Y (arc-sec). (in-Double)
    # posECR: The ECR position vector (km) to be converted. (in-Double[3])
    # velECR: The ECR velocity vector (km/s) to be converted. (in-Double[3])
    # posEFG: The resulting EFG position vector (km). (out-Double[3])
    # velEFG: The resulting EFG velocity vector (km/s). (out-Double[3])
    dllObj.ECRToEFG.restype = None
    dllObj.ECRToEFG.argtypes = [c_double, c_double, c_double * 3, c_double * 3, c_double * 3, c_double * 3]

    # Converts ECR position and velocity vectors to EFG position and velocity vectors at the specified time.
    # ds50UTC: Input time in days since 1950 UTC. (in-Double)
    # posECR: The ECR position vector (km) to be converted. (in-Double[3])
    # velECR: The ECR velocity vector (km/s) to be converted. (in-Double[3])
    # posEFG: The resulting EFG position vector (km) (set to zeros if timing constants not loaded). (out-Double[3])
    # velEFG: The resulting EFG velocity vector (km/s) (set to zeros if timing constants not loaded). (out-Double[3])
    dllObj.ECRToEFGTime.restype = None
    dllObj.ECRToEFGTime.argtypes = [c_double, c_double * 3, c_double * 3, c_double * 3, c_double * 3]

    # Converts EFG position and velocity vectors to ECR position and velocity vectors.
    # polarX: Polar motion X (arc-sec). (in-Double)
    # polarY: Polar motion Y (arc-sec). (in-Double)
    # posEFG: The EFG position vector (km) to be converted. (in-Double[3])
    # velEFG: The EFG velocity vector (km/s) to be converted. (in-Double[3])
    # posECR: The resulting ECR position vector (km). (out-Double[3])
    # velECR: The resulting ECR velocity vector (km/s). (out-Double[3])
    dllObj.EFGToECR.restype = None
    dllObj.EFGToECR.argtypes = [c_double, c_double, c_double * 3, c_double * 3, c_double * 3, c_double * 3]

    # Converts EFG position and velocity vectors to ECR position and velocity vectors at the specified time.
    # ds50UTC: Input time in days since 1950 UTC (in-Double)
    # posEFG: The EFG position vector (km) to be converted. (in-Double[3])
    # velEFG: The EFG velocity vector (km/s) to be converted. (in-Double[3])
    # posECR: The resulting ECR position vector (km) (set to zeros if timing constants not loaded). (out-Double[3])
    # velECR: The resulting ECR velocity vector (km/s) (set to zeros if timing constants not loaded). (out-Double[3])
    dllObj.EFGToECRTime.restype = None
    dllObj.EFGToECRTime.argtypes = [c_double, c_double * 3, c_double * 3, c_double * 3, c_double * 3]

    # Converts an EFG position vector to geodetic latitude, longitude, and height.
    # posEFG: The EFG position vector (km) to be converted. (in-Double[3])
    # metricLLH: The resulting geodetic north latitude (degree), east longitude (degree), and
    # height (km). (out-Double[3])
    dllObj.EFGPosToLLH.restype = None
    dllObj.EFGPosToLLH.argtypes = [c_double * 3, c_double * 3]

    # Converts geodetic latitude, longitude, and height to an EFG position vector.
    # metricLLH: An Array containing the geodetic north latitude (degree), east longitude (degree), and
    # height (km) to be converted. (in-Double[3])
    # posEFG: The resulting EFG position vector (km). (out-Double[3])
    dllObj.LLHToEFGPos.restype = None
    dllObj.LLHToEFGPos.argtypes = [c_double * 3, c_double * 3]

    # Rotates position and velocity vectors from J2000 to coordinates of the specified date, expressed in ds50TAI.
    # spectr: Specifies whether to run in SPECTR compatibility mode. A value of 1 means Yes. (in-Integer)
    # nutationTerms: Nutation terms (4-106, 4:least accurate, 106:most acurate). (in-Integer)
    # ds50TAI: The date to rotate to coordinates of, expressed in days since 1950, TAI. (in-Double)
    # posJ2K: The position vector from J2000. (in-Double[3])
    # velJ2K: The velocity vector from J2000. (in-Double[3])
    # posDate: The resulting position vector in coordinates of date, ds50TAI. (out-Double[3])
    # velDate: The resulting velocity vector in coordinates of date, ds50TAI. (out-Double[3])
    dllObj.RotJ2KToDate.restype = None
    dllObj.RotJ2KToDate.argtypes = [c_int, c_int, c_double, c_double * 3, c_double * 3, c_double * 3, c_double * 3]

    # Rotates position and velocity vectors from coordinates of date to J2000.
    # spectr: Specifies whether to run in SPECTR compatibility mode. A value of 1 means Yes. (in-Integer)
    # nutationTerms: Nutation terms (4-106, 4:least accurate, 106:most acurate). (in-Integer)
    # ds50TAI: Time in days since 1950, TAI for which the coordinates of position and velocity vectors are currently
    # expressed. (in-Double)
    # posDate: The position vector from coordinates of Date. (in-Double[3])
    # velDate: The velocity vector from coordinates of Date. (in-Double[3])
    # posJ2K: The resulting position vector in coordinates of J2000. (out-Double[3])
    # velJ2K: The resulting velocity vector in coordinates of J2000. (out-Double[3])
    dllObj.RotDateToJ2K.restype = None
    dllObj.RotDateToJ2K.argtypes = [c_int, c_int, c_double, c_double * 3, c_double * 3, c_double * 3, c_double * 3]

    # Computes the Sun and Moon position at the specified time.
    # ds50ET: The number of days since 1950, ET (Ephemeris Time/Terrestrial Time) for which to compute the sun and moon
    # position. (in-Double)
    # uvecSun: The resulting sun position unit vector. (out-Double[3])
    # sunVecMag: The resulting magnitude of the sun position vector (km). (out-Double)
    # uvecMoon: The resulting moon position unit vector. (out-Double[3])
    # moonVecMag: The resulting magnitude of the moon position vector (km). (out-Double)
    dllObj.CompSunMoonPos.restype = None
    dllObj.CompSunMoonPos.argtypes = [c_double, c_double * 3, c_double_p, c_double * 3, c_double_p]

    # Computes the Sun position at the specified time.
    # ds50ET: The number of days since 1950, ET (Ephemeris Time/Terrestrial Time) for which to compute the sun
    # position. (in-Double)
    # uvecSun: The resulting sun position unit vector. (out-Double[3])
    # sunVecMag: The resulting magnitude of the sun position vector (km). (out-Double)
    dllObj.CompSunPos.restype = None
    dllObj.CompSunPos.argtypes = [c_double, c_double * 3, c_double_p]

    # Computes the Moon position at the specified time.
    # ds50ET: The number of days since 1950, ET (Ephemeris Time/Terrestrial Time) for which to compute the moon
    # position. (in-Double)
    # uvecMoon: The resulting moon position unit vector. (out-Double[3])
    # moonVecMag: The resulting magnitude of the moon position vector (km). (out-Double)
    dllObj.CompMoonPos.restype = None
    dllObj.CompMoonPos.argtypes = [c_double, c_double * 3, c_double_p]

    # This function is intended for future use.  No information is currently available.
    # This function is intended for future use.  No information is currently available.
    # xf_Conv: Index of the conversion function (in-Integer)
    # frArr: The input array (in-Double[128])
    # toArr: The resulting array (out-Double[128])
    dllObj.AstroConvFrTo.restype = None
    dllObj.AstroConvFrTo.argtypes = [c_int, c_double * 128, c_double * 128]

    # Converts right ascension and declination to vector triad LAD in topocentric equatorial coordinate system.
    # ra: Right ascension (deg). (in-Double)
    # dec: Declination (deg). (in-Double)
    # l: The resulting unit vector from the station to the satellite (referred to the equatorial coordinate system
    # axis). (out-Double[3])
    # a_tilde: The resulting unit vector perpendicular to the hour circle passing through the satellite, in the
    # direction of increasing RA. (out-Double[3])
    # d_tilde: The resulting unit vector perpendicular to L and is directed toward the north, in the plane of the hour
    # circle. (out-Double[3])
    dllObj.RADecToLAD.restype = None
    dllObj.RADecToLAD.argtypes = [c_double, c_double, c_double * 3, c_double * 3, c_double * 3]

    # Converts azimuth and elevation to vector triad LAD in topocentric horizontal coordinate system.
    # az: Input azimuth (deg). (in-Double)
    # el: Input elevation angle (deg). (in-Double)
    # lh: The resulting unit vector from the station to the satellite (referred to the horizon coordinate system
    # axis). (out-Double[3])
    # ah: The resulting unit vector perpendicular to the hour circle passing through the satellite, in the direction of
    # increasing Az. (out-Double[3])
    # dh: The resulting unit vector perpendicular to L and is directed toward the zenith, in the plane of the hour
    # circle. (out-Double[3])
    dllObj.AzElToLAD.restype = None
    dllObj.AzElToLAD.argtypes = [c_double, c_double, c_double * 3, c_double * 3, c_double * 3]

    # Converts satellite ECI position/velocity vectors and sensor location to topocentric components.
    # The xa_topo array has the following structure:
    # [0]: Resulting right ascension (RA) (deg)
    # [1]: Declination (deg)
    # [2]: Azimuth (deg)
    # [3]: Elevation (deg)
    # [4]: Range (km)
    # [5]: RAdot (first derivative of right ascension) (deg/s)
    # [6]: DecDot (first derivative of declination) (deg/s)
    # [7]: AzDot (first derivative of azimuth) (deg/s)
    # [8]: ElDot (first derivative of elevation) (deg/s)
    # [9]: RangeDot (first derivative of range) (km/s)
    # theta: Theta - local sidereal time(rad). (in-Double)
    # lat: Station's astronomical latitude (deg). (+N) (-S) (in-Double)
    # senPos: Sensor position in ECI (km). (in-Double[3])
    # satPos: Satellite position in ECI (km). (in-Double[3])
    # satVel: Satellite velocity in ECI (km/s). (in-Double[3])
    # xa_topo: An array that stores the resulting topocentric components.  see XA_TOPO_? (out-Double[10])
    dllObj.ECIToTopoComps.restype = None
    dllObj.ECIToTopoComps.argtypes = [c_double, c_double, c_double * 3, c_double * 3, c_double * 3, c_double * 10]

    # Converts right ascension and declination in the topocentric reference frame to Azimuth/Elevation in the local
    # horizon reference frame.
    # thetaG: Theta - Greenwich mean sidereal time (rad). (in-Double)
    # lat: Station's astronomical latitude (deg). (+N) (-S) (in-Double)
    # lon: Station's astronomical longitude (deg). (+E) (-W) (in-Double)
    # ra: Right ascension (deg) (in-Double)
    # dec: Declination (deg) (in-Double)
    # az: Azimuth (deg) (out-Double)
    # el: Elevation (deg) (out-Double)
    dllObj.RaDecToAzEl.restype = None
    dllObj.RaDecToAzEl.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double_p, c_double_p]

    # Converts right ascension and declination in the topocentric reference frame to Azimuth/Elevation in the local
    # horizon reference frame.
    # ds50UTC: Input time in days since 1950 UTC (in-Double)
    # lat: Station's astronomical latitude (deg). (+N) (-S) (in-Double)
    # lon: Station's astronomical longitude (deg). (+E) (-W) (in-Double)
    # ra: Right ascension (deg) (in-Double)
    # dec: Declination (deg) (in-Double)
    # az: Azimuth (deg) (out-Double)
    # el: Elevation (deg) (out-Double)
    dllObj.RaDecToAzElTime.restype = None
    dllObj.RaDecToAzElTime.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double_p, c_double_p]

    # Converts Azimuth/Elevation in the local horizon reference frame to Right ascension/Declination in the topocentric
    # reference frame
    # thetaG: Theta - Greenwich mean sidereal time (rad). (in-Double)
    # lat: Station's astronomical latitude (deg). (+N) (-S) (in-Double)
    # lon: Station's astronomical longitude (deg). (+E) (-W) (in-Double)
    # az: Azimuth (deg) (in-Double)
    # el: Elevation (deg) (in-Double)
    # ra: Right ascension (deg) (out-Double)
    # dec: Declination (deg) (out-Double)
    dllObj.AzElToRaDec.restype = None
    dllObj.AzElToRaDec.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double_p, c_double_p]

    # Converts Azimuth/Elevation in the local horizon reference frame to Right ascension/Declination in the topocentric
    # reference frame
    # ds50UTC: Input time in days since 1950 UTC (in-Double)
    # lat: Station's astronomical latitude (deg). (+N) (-S) (in-Double)
    # lon: Station's astronomical longitude (deg). (+E) (-W) (in-Double)
    # az: Azimuth (deg) (in-Double)
    # el: Elevation (deg) (in-Double)
    # ra: Right ascension (deg) (out-Double)
    # dec: Declination (deg) (out-Double)
    dllObj.AzElToRaDecTime.restype = None
    dllObj.AzElToRaDecTime.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double_p, c_double_p]

    # Converts full state RAE (range, az, el, and their rates) to full state ECI (position and velocity)
    # The xa_rae array has the following structure:
    # [0]: Range (km)
    # [1]: Azimuth (deg)
    # [2]: Elevation (deg)
    # [3]: Range Dot (km/s)
    # [4]: Azimuth Dot (deg/s)
    # [5]: Elevation Dot (deg/s)
    # theta: Theta - local sidereal time(rad). (in-Double)
    # astroLat: Astronomical latitude (ded). (in-Double)
    # xa_rae: An array contains input data.  see XA_RAE_? (in-Double[6])
    # senPos: Sensor position in ECI (km). (in-Double[3])
    # satPos: Satellite position in ECI (km). (out-Double[3])
    # satVel: Satellite velocity in ECI (km/s). (out-Double[3])
    dllObj.RAEToECI.restype = None
    dllObj.RAEToECI.argtypes = [c_double, c_double, c_double * 6, c_double * 3, c_double * 3, c_double * 3]

    # Computes initial values for the SGP drag term nDot and the SGP4 drag term BSTAR based upon eccentricity and
    # semi-major axis.
    # semiMajorAxis: Semi-major axis (km). (in-Double)
    # eccen: Eccentricity (unitless). (in-Double)
    # nDot: nDot (revs/day^2). (out-Double)
    # bstar: Bstar (1/earth radii). (out-Double)
    dllObj.GetInitialDrag.restype = None
    dllObj.GetInitialDrag.argtypes = [c_double, c_double, c_double_p, c_double_p]

    # Converts covariance matrix PTW to UVW.
    # PTW = P: TxW, T: along velocity direction, W: pos x vel.
    # UVW = U: radial direction, V: in plane, perpendicular to U, W: pos x vel.
    # pos: The input position vector (km). (in-Double[3])
    # vel: The input velocity vector (km/s). (in-Double[3])
    # ptwCovMtx: The PTW covariance matrix to be converted. (in-Double[6, 6])
    # uvwCovMtx: The resulting UVW covariance matrix. (out-Double[6, 6])
    dllObj.CovMtxPTWToUVW.restype = None
    dllObj.CovMtxPTWToUVW.argtypes = [c_double * 3, c_double * 3, c_void_p, c_void_p]

    # Converts covariance matrix UVW to PTW.
    # PTW = P: TxW, T: along velocity direction, W: pos x vel.
    # UVW = U: radial direction, V: in plane, perpendicular to U, W: pos x vel.
    # pos: The input position vector (km). (in-Double[3])
    # vel: The input velocity vector (km/s). (in-Double[3])
    # uvwCovMtx: The UVW covariance matrix to be converted. (in-Double[6, 6])
    # ptwCovMtx: The resulting PTW covariance matrix. (out-Double[6, 6])
    dllObj.CovMtxUVWToPTW.restype = None
    dllObj.CovMtxUVWToPTW.argtypes = [c_double * 3, c_double * 3, c_void_p, c_void_p]

    # Computes Earth/Sensor/Earth Limb and Earth/Sensor/Satellite angles.
    # earthLimb: Earth limb distance (km). (in-Double)
    # satECI: Satellite position in ECI (km). (in-Double[3])
    # senECI: Sensor position in ECI (km). (in-Double[3])
    # earthSenLimb: The resulting earth/sensor/limb angle (deg). (out-Double)
    # earthSenSat: The resulting earth/sensor/sat angle (deg). (out-Double)
    # satEarthSen: The resulting sat/earth/sensor angle (deg). (out-Double)
    dllObj.EarthObstructionAngles.restype = None
    dllObj.EarthObstructionAngles.argtypes = [c_double, c_double * 3, c_double * 3, c_double_p, c_double_p, c_double_p]

    # Determines if a point in space is sunlit at the input time ds50ET
    # ds50ET: The number of days since 1950, ET (Ephemeris Time/Terrestrial Time) for which to determine if the point
    # is sunlit. (in-Double)
    # ptEci: a position in ECI (km). (in-Double[3])
    dllObj.IsPointSunlit.restype = c_int
    dllObj.IsPointSunlit.argtypes = [c_double, c_double * 3]

    # Rotates Right Ascension and Declination to specified epoch
    # nutationTerms: Nutation terms (4-106, 4:least accurate, 106:most acurate). (in-Integer)
    # dir: 1: TEME of Date To MEME year of equinox, 2: MEME year of equinox to TEME of Date (in-Integer)
    # ds50UTCIn: Origin time in days since 1950 UTC (in-Double)
    # raIn: Input right ascension (deg) (in-Double)
    # declIn: Input declination (deg) (in-Double)
    # ds50UTCOut: Destination time in days since 1950 UTC (in-Double)
    # raOut: Output right ascension (deg) (out-Double)
    # declOut: Output declination (deg) (out-Double)
    dllObj.RotRADecl.restype = None
    dllObj.RotRADecl.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double, c_double_p, c_double_p]

    # Rotates Right Ascension and Declination from TEME of Date to MEME of the specified year of equinox
    # nutationTerms: Nutation terms (4-106, 4:least accurate, 106:most acurate). (in-Integer)
    # yrOfEqnx: Year of equinox (=1: 0 Jan of input year, =2: J2000, =3: B1950) (in-Integer)
    # ds50UTCIn: Input time in days since 1950 UTC (in-Double)
    # raIn: Input right ascension (deg) (in-Double)
    # declIn: Input declination (deg) (in-Double)
    # raOut: Output right ascension (deg) (out-Double)
    # declOut: Output declination (deg) (out-Double)
    dllObj.RotRADec_DateToEqnx.restype = c_int
    dllObj.RotRADec_DateToEqnx.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double_p, c_double_p]

    # Rotates Right Ascension and Declination from MEME of the specified year of equinox to TEME of Date
    # nutationTerms: Nutation terms (4-106, 4:least accurate, 106:most acurate) (in-Integer)
    # yrOfEqnx: Year of equinox (=1: 0 Jan of input year, =2: J2000, =3: B1950) (in-Integer)
    # ds50UTCIn: Input time in days since 1950 UTC (in-Double)
    # raIn: Input right ascension (deg) (in-Double)
    # declIn: Input declination (deg) (in-Double)
    # raOut: Output right ascension (deg) (out-Double)
    # declOut: Output declination (deg) (out-Double)
    dllObj.RotRADec_EqnxToDate.restype = c_int
    dllObj.RotRADec_EqnxToDate.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double_p, c_double_p]

    # Rotates the Equinoctial covariance to UVW
    # Note: This method uses the global Earth constants so make sure that you select the right Earth model by calling
    # the EnvConst/EnvSetGeoIdx method
    # The n terms must be normalized by n
    # The input position, velocity and covariance must all have the same reference equator and equinox.
    # pos: The input position vector in ECI (in-Double[3])
    # vel: The input velocity vector in ECI (in-Double[3])
    # covMtxEqnx: The input covariance matrix in equinoctial elements (af, ag, Lbar, n/n, chi, psi) (in-Double[6, 6])
    # covMtxUVW: The output covariance in UVW (out-Double[6, 6])
    dllObj.CovMtxEqnxToUVW.restype = None
    dllObj.CovMtxEqnxToUVW.argtypes = [c_double * 3, c_double * 3, c_void_p, c_void_p]

    # Rotates the UVW covariance to Equinoctial
    # Note: This method uses the global Earth constants so make sure that you select the right Earth model by calling
    # the EnvConst/EnvSetGeoIdx method
    # The n terms are normalized by n
    # The input position, velocity reference equator and equinox determine the output covariance reference frame.
    # pos: The input position vector in ECI TEME Of Date (in-Double[3])
    # vel: The input velocity vector in ECI TEME Of Date (in-Double[3])
    # covMtxUVW: The input covariance matrix UVW (in-Double[6, 6])
    # covMtxEqnx: The output covariance in in equinoctial elements (af, ag, Lbar, n/n, chi, psi) (out-Double[6, 6])
    dllObj.CovMtxUVWToEqnx.restype = None
    dllObj.CovMtxUVWToEqnx.argtypes = [c_double * 3, c_double * 3, c_void_p, c_void_p]

    # Rotates the ECI covariance to UVW
    # Note: This method uses the global Earth constants so make sure that you select the proper Earth model by calling
    # the EnvConst/EnvSetGeoIdx method
    # pos: The input position vector in either TEME or J2K ECI (in-Double[3])
    # vel: The input velocity vector in either TEME or J2K ECI (in-Double[3])
    # covMtxECI: The input covariance matrix in ECI (in-Double[6, 6])
    # covMtxUVW: The output covariance in UVW (out-Double[6, 6])
    dllObj.CovMtxECIToUVW.restype = None
    dllObj.CovMtxECIToUVW.argtypes = [c_double * 3, c_double * 3, c_void_p, c_void_p]

    # Rotates the UVW covariance to ECI
    # Note: This method uses the global Earth constants so make sure that you select the proper Earth model by calling
    # the EnvConst/EnvSetGeoIdx method
    # pos: The input position vector in either TEME or J2K ECI (in-Double[3])
    # vel: The input velocity vector in either TEME or J2K ECI (in-Double[3])
    # covMtxUVW: The input covariance matrix in UVW (in-Double[6, 6])
    # covMtxECI: The output covariance in ECI (out-Double[6, 6])
    dllObj.CovMtxUVWToECI.restype = None
    dllObj.CovMtxUVWToECI.argtypes = [c_double * 3, c_double * 3, c_void_p, c_void_p]

    # Converts covariance matrix ECI to EFG.
    # EFG = Earth Fixed Greenwich
    # ECI = Earth Centered Inertial - need to determine TEME or J2K
    # thetaG: theta - local sidereal time (rad) (in-Double)
    # covECI: 6x6 ECI Covariance (in-Double[6, 6])
    # covEFG: 6x6 EFG Covariance (out-Double[6, 6])
    dllObj.CovMtxECIToEFG.restype = None
    dllObj.CovMtxECIToEFG.argtypes = [c_double, c_void_p, c_void_p]

    # Converts covariance matrix EFG to ECI.
    # EFG = Earth Fixed Greenwich
    # ECI = Earth Centered Inertial - need to determine TEME or J2K
    # thetaG: theta - local sidereal time (rad) (in-Double)
    # covEFG: 6x6 EFG Covariance (in-Double[6, 6])
    # covECI: 6x6 ECI Covariance (out-Double[6, 6])
    dllObj.CovMtxEFGToECI.restype = None
    dllObj.CovMtxEFGToECI.argtypes = [c_double, c_void_p, c_void_p]

    # Converts 6x6 symmetric Matrix/2D array to 1D array of 21 elements (lower triangular of a 6x6 symmetric matrix)
    # symMtx6x6: Input 6x6 symmetric matrix (in-Double[6, 6])
    # lta21: Output 1D array of 21 elements (lower triangular of a 6x6 matrix) (out-Double[21])
    dllObj.Mtx6x6ToLTA21.restype = None
    dllObj.Mtx6x6ToLTA21.argtypes = [c_void_p, c_double * 21]

    # Converts 1D array of 21 elements (lower triangular of a 6x6 symmetric matrix) to a 6x6 symmetric matrix
    # lta21: Input 1D array of 21 elements (lower triangular of a 6x6 matrix) (in-Double[21])
    # symMtx6x6: Output 6x6 symmetric matrix (out-Double[6, 6])
    dllObj.LTA21ToMtx6x6.restype = None
    dllObj.LTA21ToMtx6x6.argtypes = [c_double * 21, c_void_p]

    # Converts 9x9 symmetric Matrix/2D array to 1D array of 45 elements (lower triangular of a 9x9 symmetric matrix)
    # symMtx9x9: Input 9x9 symmetric matrix (in-Double[9, 9])
    # lta45: Output 1D array of 45 elements (lower triangular of a 9x9 matrix) (out-Double[45])
    dllObj.Mtx9x9ToLTA45.restype = None
    dllObj.Mtx9x9ToLTA45.argtypes = [c_void_p, c_double * 45]

    # Converts 1D array of 45 elements (lower triangular of a 9x9 symmetric matrix) to a 9x9 symmetric matrix
    # lta45: Input 1D array of 45 elements (lower triangular of a 9x9 matrix) (in-Double[45])
    # symMtx9x9: Output 9x9 symmetric matrix (out-Double[9, 9])
    dllObj.LTA45ToMtx9x9.restype = None
    dllObj.LTA45ToMtx9x9.argtypes = [c_double * 45, c_void_p]

    # Propagate xyzDate covariance forward to the propagation time
    # rms: Root mean square of observation residulas (in-Double)
    # consider: Density consider parameter, 12 is recommended (this is a percentile) (in-Double)
    # stateArray: State transition matrix (in-Double[54])
    # cov: Covariance matrix at start time (in-Double[9, 9])
    # propCov: Covariance at end time for state matrix (out-Double[6, 6])
    dllObj.PropCovFrState.restype = None
    dllObj.PropCovFrState.argtypes = [c_double, c_double, c_double * 54, c_void_p, c_void_p]

    # Rotates the ECI covariance to UVW
    # Note: This method uses the global Earth constants so make sure that you select the proper Earth model by calling
    # the EnvConst/EnvSetGeoIdx method
    # pos: The input position vector in either TEME or J2K ECI (in-Double[3])
    # vel: The input velocity vector in either TEME or J2K ECI (in-Double[3])
    # covMtxECI: The input covariance matrix in ECI (in-Double[9, 9])
    # covMtxEqnx: The output covariance in UVW (out-Double[9, 9])
    dllObj.CovMtxECIToEqnx.restype = None
    dllObj.CovMtxECIToEqnx.argtypes = [c_double * 3, c_double * 3, c_void_p, c_void_p]

    # Rotates the UVW covariance to ECI
    # Note: This method uses the global Earth constants so make sure that you select the proper Earth model by calling
    # the EnvConst/EnvSetGeoIdx method
    # pos: The input position vector in either TEME or J2K ECI (in-Double[3])
    # vel: The input velocity vector in either TEME or J2K ECI (in-Double[3])
    # covEqnx: 45 or 55 (in-Double[9, 9])
    # covMtxECI: The output covariance in ECI (out-Double[9, 9])
    dllObj.CovMtxEqnxToECI9x9.restype = None
    dllObj.CovMtxEqnxToECI9x9.argtypes = [c_double * 3, c_double * 3, c_void_p, c_void_p]

    # Rotates the UVW covariance to ECI
    # Note: This method uses the global Earth constants so make sure that you select the proper Earth model by calling
    # the EnvConst/EnvSetGeoIdx method
    # pos: The input position vector in either TEME or J2K ECI (in-Double[3])
    # vel: The input velocity vector in either TEME or J2K ECI (in-Double[3])
    # covEqnx: 45 or 55 (in-Double[9, 9])
    # covMtxUVW: The output covariance in ECI (out-Double[9, 9])
    dllObj.CovMtxEqnxToUVW9x9.restype = None
    dllObj.CovMtxEqnxToUVW9x9.argtypes = [c_double * 3, c_double * 3, c_void_p, c_void_p]

    # Update (propagate) covariance to a future time with a supplied covariance, state transition matrix
    # consider parameter and RMS. Consider parameter is applied to the drag term only.
    # Full covariance matrix is multiplied by RMS squared.  State transition matrix can be obtained from
    # SpProp.SpGetStateMtx or supplying your own. State matrix, input and output covariance must be in
    # matching coordinate systems.
    # rmsIn: Root mean square of sensor errors (in-Double)
    # consider: Consider parameter (percentage) (in-Double)
    # cov: Covariance at epoch (in-Double[9, 9])
    # stateArray: Consider parameter and root mean square (in-Double[54])
    # propCov: Updated covariance (out-Double[6, 6])
    dllObj.CovMtxUpdate.restype = None
    dllObj.CovMtxUpdate.argtypes = [c_double, c_double, c_void_p, c_double * 54, c_void_p]

    # Annual Aberration calculated using equations from Astronomical Algorithms, Jean Meeus, 2nd Edition with
    # Corrections as of June 15, 2005
    # ra: Input right ascension (deg) (in-Double)
    # decl: Input declination (deg) (in-Double)
    # dS50UTC: Time in days since 1950 UTC (in-Double)
    # raDelta: Right Ascension delta due to Annual Aberration (deg) (out-Double)
    # decDelta: Declination delta due to Annual Aberration (deg) (out-Double)
    dllObj.AberrationAnnual.restype = None
    dllObj.AberrationAnnual.argtypes = [c_double, c_double, c_double, c_double_p, c_double_p]

    # Diurnal Aberration is due to the rotation of the Earth about it's axis. This is only valid for ground based
    # sensors.
    # Diurnal Aberration calculated using equations from Explanatory Supplement to the Astronomical Almanac 3rd
    # Edition, 2013
    # ra: Input right ascension (deg) (in-Double)
    # decl: Input declination (deg) (in-Double)
    # dS50UTC: Time in days since 1950 UTC (in-Double)
    # senPos: Sensor EFG geocentric position (meters) (in-Double[3])
    # raDelta: Right Ascension delta due to Diurnal Aberration (deg) (out-Double)
    # decDelta: Declination delta due to Diurnal Aberration (deg) (out-Double)
    dllObj.AberrationDiurnal.restype = None
    dllObj.AberrationDiurnal.argtypes = [c_double, c_double, c_double, c_double * 3, c_double_p, c_double_p]

    # Sets JPL parameters
    # Notes: Set JPL parameters will be used by SP, SPG4-XP, and anything that requires access to JPL data
    # jplFile: The name of the JPL file. (in-Character[512])
    # ds50Start: Start Time of JPL ephmeris to load (in-Double)
    # ds50Stop: End Time of JPL ephemeris to load (in-Double)
    dllObj.JplSetParameters.restype = None
    dllObj.JplSetParameters.argtypes = [c_char_p, c_double, c_double]

    # Gets JPL parameters
    # jplFile: The name of the JPL file. (out-Character[512])
    # ds50Start: Start Time of Ephmeris to load (out-Double)
    # ds50Stop: End Time of Ephemeris to load (out-Double)
    dllObj.JplGetParameters.restype = None
    dllObj.JplGetParameters.argtypes = [c_char_p, c_double_p, c_double_p]

    # Resets JPL parameters & removes JPL ephemeris data
    dllObj.JplReset.restype = None
    dllObj.JplReset.argtypes = []

    # Computes various Sun and Moon vectors base on loaded JPL data at the specified time.
    # Note: if JPL data isn't loaded or available, all output parameters are set to zero
    # ds50UTC: Input time in day since 1950 UTC (in-Double)
    # uvecSun: The resulting sun position unit vector. (out-Double[3])
    # sunVecMag: The resulting magnitude of the sun position vector (km). (out-Double)
    # uvecMoon: The resulting moon position unit vector. (out-Double[3])
    # moonVecMag: The resulting magnitude of the moon position vector (km). (out-Double)
    dllObj.JplCompSunMoonVec.restype = None
    dllObj.JplCompSunMoonVec.argtypes = [c_double, c_double * 3, c_double_p, c_double * 3, c_double_p]

    # Computes Sun and Moon position vectors base on loaded JPL data at the specified time.
    # Note: if JPL data isn't loaded or available, all output parameters are set to zero
    # ds50UTC: Input time in day since 1950 UTC (in-Double)
    # sunVec: The resulting sun position vector (km). (out-Double[3])
    # moonVec: The resulting sun position vector (km). (out-Double[3])
    dllObj.JplCompSunMoonPos.restype = None
    dllObj.JplCompSunMoonPos.argtypes = [c_double, c_double * 3, c_double * 3]

    # Removes the JPL ephemeris from memory
    dllObj.RemoveJpl.restype = None
    dllObj.RemoveJpl.argtypes = []

    # Rotates position and velocity vectors from TEME of Epoch to TEME of Date
    # nutationTerms: Nutation terms (4-106, 4:least accurate, 106:most acurate). (in-Integer)
    # epochDs50TAI: The date of which posEpoch/velEpoch are based on, expressed in days since 1950, TAI. (in-Double)
    # dateDs50TAI: The date of which posEpoch/velEpoch will rotate to, expressed in days since 1950, TAI. (in-Double)
    # posEpoch: The position vector in TEME of Epoch. (in-Double[3])
    # velEpoch: The velocity vector in TEME of Epoch. (in-Double[3])
    # posDate: The resulting position vector in TEME of Date. (out-Double[3])
    # velDate: The resulting velocity vector in TEME of Date. (out-Double[3])
    dllObj.TemeEpochToDate.restype = None
    dllObj.TemeEpochToDate.argtypes = [
        c_int,
        c_double,
        c_double,
        c_double * 3,
        c_double * 3,
        c_double * 3,
        c_double * 3,
    ]

    return dllObj


# Index of Keplerian elements
# semi-major axis (km)
XA_KEP_A = 0
# eccentricity (unitless)
XA_KEP_E = 1
# inclination (deg)
XA_KEP_INCLI = 2
# mean anomaly (deg)
XA_KEP_MA = 3
# right ascension of the asending node (deg)
XA_KEP_NODE = 4
# argument of perigee (deg)
XA_KEP_OMEGA = 5
XA_KEP_SIZE = 6

# Index of classical elements
# N mean motion (revs/day)
XA_CLS_N = 0
# eccentricity (unitless)
XA_CLS_E = 1
# inclination (deg)
XA_CLS_INCLI = 2
# mean anomaly (deg)
XA_CLS_MA = 3
# right ascension of the asending node (deg)
XA_CLS_NODE = 4
# argument of perigee (deg)
XA_CLS_OMEGA = 5
XA_CLS_SIZE = 6

# Index of equinoctial elements
# Af (unitless)
XA_EQNX_AF = 0
# Ag (unitless)
XA_EQNX_AG = 1
# chi (unitless)
XA_EQNX_CHI = 2
# psi (unitless)
XA_EQNX_PSI = 3
# L mean longitude (deg)
XA_EQNX_L = 4
# N mean motion (revs/day)
XA_EQNX_N = 5
XA_EQNX_SIZE = 6

# Indexes of AstroConvFrTo
# SGP4 (A, E, Incli, BStar) to SGP (nDot, n2Dot)
XF_CONV_SGP42SGP = 101


# Indexes for topocentric components
# Right ascension (deg)
XA_TOPO_RA = 0
# Declination (deg)
XA_TOPO_DEC = 1
# Azimuth (deg)
XA_TOPO_AZ = 2
# Elevation (deg)
XA_TOPO_EL = 3
# Range (km)
XA_TOPO_RANGE = 4
# Right ascension dot (deg/s)
XA_TOPO_RADOT = 5
# Declincation dot (deg/s)
XA_TOPO_DECDOT = 6
# Azimuth dot (deg/s)
XA_TOPO_AZDOT = 7
# Elevation dot (deg/s)
XA_TOPO_ELDOT = 8
# Range dot (km/s)
XA_TOPO_RANGEDOT = 9
XA_TOPO_SIZE = 10


# Indexes for RAE components
# Range (km)
XA_RAE_RANGE = 0
# Azimuth (deg)
XA_RAE_AZ = 1
# Elevation (deg)
XA_RAE_EL = 2
# Range dot (km/s)
XA_RAE_RANGEDOT = 3
# Azimuth dot (deg/s)
XA_RAE_AZDOT = 4
# Elevation dot (deg/s)
XA_RAE_ELDOT = 5
XA_RAE_SIZE = 6


# Year of Equinox indicator
# Date of observation
YROFEQNX_OBTIME = 0
# 0 Jan of Date
YROFEQNX_CURR = 1
# J2000
YROFEQNX_2000 = 2
# B1950
YROFEQNX_1950 = 3

# ========================= End of auto generated code ==========================
