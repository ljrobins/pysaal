# This wrapper file was generated automatically by the GenDllWrappers program.
import platform
from ctypes import CDLL, POINTER, c_char_p, c_double, c_int, c_longlong, c_void_p
from pathlib import Path

c_double_p = POINTER(c_double)
c_int_p = POINTER(c_int)

# get the right filename of the dll/so
LIB_PATH = Path(__file__).parent
if platform.uname()[0] == "Windows":
    DLL_NAME = LIB_PATH / "Sgp4Prop.dll"

if platform.uname()[0] == "Linux":
    DLL_NAME = LIB_PATH / "libsgp4prop.so"

if platform.uname()[0] == "Darwin":
    DLL_NAME = LIB_PATH / "libsgp4prop.dylib"


def get_sgp4_prop_dll():
    """LoadSgp4PropDll() -- Loads Sgp4Prop.dll from the PATH or LD_LIBRARY_PATH
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
    # Initializes the Sgp4 DLL for use in the program.
    #
    # If this function returns an error, it is recommended that you stop the program immediately.
    #
    # An error will occur if you forget to load and initialize all the prerequisite DLLs, as listed in the DLL
    # Prerequisites section of the accompanying documentation, before using this DLL.
    # apAddr: The handle that was returned from DllMainInit(). See the documentation for DllMain.dll for
    # details. (in-Long)
    dllObj.Sgp4Init.restype = c_int
    dllObj.Sgp4Init.argtypes = [c_longlong]

    # Returns information about the current version of Sgp4Prop.dll. The information is placed in the string parameter
    # you pass in.
    # The returned string provides information about the version number, build date, and platform.
    # infoStr: A string to hold the information about Sgp4Prop.dll. (out-Character[128])
    dllObj.Sgp4GetInfo.restype = None
    dllObj.Sgp4GetInfo.argtypes = [c_char_p]

    # Loads SGP4-related parameters (prediction controls, JPL settings) and SGP4 elsets from a text file
    # sgp4InputFile: The name of the file containing SGP4-related parameters and SGP4 elsets (in-Character[512])
    dllObj.Sgp4LoadFileAll.restype = c_int
    dllObj.Sgp4LoadFileAll.argtypes = [c_char_p]

    # Saves currently loaded SGP4-related parameters (SGP4 application controls, prediction controls, integration
    # controls) to a file
    # The purpose of this function is to save the current SGP4-related settings, usually used in GUI applications, for
    # future use.
    # sgp4File: The name of the file in which to save the settings (in-Character[512])
    # saveMode: Sgp4ecifies whether to create a new file or append to an existing one (0 = create,
    # 1= append) (in-Integer)
    # saveForm: Sgp4ecifies the mode in which to save the file (0 = text format, 1 = not yet implemented, reserved for
    # future) (in-Integer)
    dllObj.Sgp4SaveFile.restype = c_int
    dllObj.Sgp4SaveFile.argtypes = [c_char_p, c_int, c_int]

    # Initializes an SGP4 satellite from an SGP or SGP4 TLE.
    # Internally, when this function is called, Tle.dll's set of TLEs is searched for the provided satKey. If found,
    # the associated TLE data will be used to create an SGP4 satellite which then will be added to Sgp4Prop.dll's set
    # of satellites. Subsequent calls to propagate this satellite will use the data in this set to compute the
    # satellite's new state.
    #
    # This routine should be called once for each satellite you wish to propagate before propagation begins, or any
    # time the associated data that is stored by Tle.dll is changed.
    #
    # The call to this routine needs to be placed before any calls to the SGP4 propagator routines (Sgp4PropMse(),
    # Sgp4PropDs50UTC(), etc.).
    # satKey: The satellite's unique key. This key will have been returned by one of the routines in Tle.dll. (in-Long)
    dllObj.Sgp4InitSat.restype = c_int
    dllObj.Sgp4InitSat.argtypes = [c_longlong]

    # Removing a satellite from the propagator's set of satellites does not affect the corresponding TLE data loaded by
    # calls to routines in Tle.dll.
    # satKey: The satellite's unique key. (in-Long)
    dllObj.Sgp4RemoveSat.restype = c_int
    dllObj.Sgp4RemoveSat.argtypes = [c_longlong]

    # Removes all currently loaded satellites from memory.
    # Calling this function removes all satellites from the set maintained by Sgp4Prop.dll. However, the TLE data
    # loaded by Tle.dll is unaffected by this function.
    dllObj.Sgp4RemoveAllSats.restype = c_int
    dllObj.Sgp4RemoveAllSats.argtypes = []

    # Returns the number of GP objects currently created.
    dllObj.Sgp4GetCount.restype = c_int
    dllObj.Sgp4GetCount.argtypes = []

    # Propagates a satellite, represented by the satKey, to the time expressed in minutes since the satellite's epoch
    # time.
    # The resulting data about the satellite is placed in the various reference parameters.
    # It is the users' responsibility to decide what to do with the returned value. For example, if the users want to
    # check for decay or low altitude, they can put that logic into their own code.
    #
    # This function can be called in random time requests.
    # The following cases will result in an error:
    #
    # Semi major axis A 1.0D6
    # Eccentricity E >= 1.0 or E
    # Mean anomaly MA>=1.0D10
    # Hyperbolic orbit E2>= 1.0
    # satKey doesn't exist in the set of loaded satellites
    # FK model not set to FK5
    #
    # satKey: The satellite's unique key. (in-Long)
    # mse: The time to propagate to, specified in minutes since the satellite's epoch time. (in-Double)
    # ds50UTC: Resulting time in days since 1950, UTC. (out-Double)
    # pos: Resulting ECI position vector (km) in True Equator and Mean Equinox of Epoch. (out-Double[3])
    # vel: Resulting ECI velocity vector (km/s) in True Equator and Mean Equinox of Epoch. (out-Double[3])
    # llh: Resulting geodetic latitude (deg), longitude(deg), and height (km). (out-Double[3])
    dllObj.Sgp4PropMse.restype = c_int
    dllObj.Sgp4PropMse.argtypes = [c_longlong, c_double, c_double_p, c_double * 3, c_double * 3, c_double * 3]

    # Propagates a satellite, represented by the satKey, to the time expressed in days since 1950, UTC.
    # The resulting data about the satellite is placed in the pos (position), vel (velocity), and llh (Lat/Lon/Height)
    # parameters.
    # It is the users' responsibility to decide what to do with the returned value. For example, if the users want to
    # check for decay or low altitude, they can put that logic into their own code.
    # The following cases will result in an error:
    #
    # Semi major axis A 1.0D6
    # Eccentricity E >= 1.0 or E
    # Mean anomaly MA>=1.0D10
    # Hyperbolic orbit E2>= 1.0
    # satKey doesn't exist in the set of loaded satellites
    # GEO model not set to WGS-72 and/or FK model not set to FK5
    #
    # satKey: The unique key of the satellite to propagate. (in-Long)
    # ds50UTC: The time to propagate to, expressed in days since 1950, UTC. (in-Double)
    # mse: Resulting time in minutes since the satellite's epoch time. (out-Double)
    # pos: Resulting ECI position vector (km) in True Equator and Mean Equinox of Epoch. (out-Double[3])
    # vel: Resulting ECI velocity vector (km/s) in True Equator and Mean Equinox of Epoch. (out-Double[3])
    # llh: Resulting geodetic latitude (deg), longitude(deg), and height (km). (out-Double[3])
    dllObj.Sgp4PropDs50UTC.restype = c_int
    dllObj.Sgp4PropDs50UTC.argtypes = [c_longlong, c_double, c_double_p, c_double * 3, c_double * 3, c_double * 3]

    # Propagates a satellite, represented by the satKey, to the time expressed in days since 1950, UTC.
    # The resulting data about the satellite is placed in the pos (position), vel (velocity) parameters.
    # satKey: The unique key of the satellite to propagate. (in-Long)
    # ds50UTC: The time to propagate to, expressed in days since 1950, UTC. (in-Double)
    # pos: Resulting ECI position vector (km) in True Equator and Mean Equinox of Epoch. (out-Double[3])
    # vel: Resulting ECI velocity vector (km/s) in True Equator and Mean Equinox of Epoch. (out-Double[3])
    dllObj.Sgp4PropDs50UtcPosVel.restype = c_int
    dllObj.Sgp4PropDs50UtcPosVel.argtypes = [c_longlong, c_double, c_double * 3, c_double * 3]

    # Propagates a satellite, represented by the satKey, to the time expressed in days since 1950, UTC.
    # Only the geodetic information is returned by this function.
    # It is the users' responsibility to decide what to do with the returned value. For example, if the users want to
    # check for decay or low altitude, they can put that logic into their own code.
    #
    # This function is similar to Sgp4PropDs50UTC but returns only LLH.  This function is designed especially for
    # applications which plot ground traces.
    # The following cases will result in an error:
    #
    # Semi major axis A 1.0D6
    # Eccentricity E >= 1.0 or E
    # Mean anomaly MA>=1.0D10
    # Hyperbolic orbit E2>= 1.0
    # satKey doesn't exist in the set of loaded satellites
    # GEO model not set to WGS-72 and/or FK model not set to FK5
    #
    # satKey: The unique key of the satellite to propagate. (in-Long)
    # ds50UTC: The time to propagate to, expressed in days since 1950, UTC. (in-Double)
    # llh: Resulting geodetic latitude (deg), longitude(deg), and height (km). (out-Double[3])
    dllObj.Sgp4PropDs50UtcLLH.restype = c_int
    dllObj.Sgp4PropDs50UtcLLH.argtypes = [c_longlong, c_double, c_double * 3]

    # Propagates a satellite, represented by the satKey, to the time expressed in days since 1950, UTC.
    # Only the ECI position vector is returned by this function.
    # It is the users' responsibility to decide what to do with the returned value. For example, if the users want to
    # check for decay or low altitude, they can put that logic into their own code.
    #
    # This function is similar to Sgp4PropDs50UTC but returns only ECI position vector.  This function is designed
    # especially for applications which plot satellite position in 3D.
    # The following cases will result in an error:
    #
    # Semi major axis A 1.0D6
    # Eccentricity E >= 1.0 or E
    # Mean anomaly MA>=1.0D10
    # Hyperbolic orbit E2>= 1.0
    # satKey doesn't exist in the set of loaded satellites
    # GEO model not set to WGS-72 and/or FK model not set to FK5
    #
    # satKey: The unique key of the satellite to propagate. (in-Long)
    # ds50UTC: The time to propagate to, expressed in days since 1950, UTC. (in-Double)
    # pos: Resulting ECI position vector (km) in True Equator and Mean Equinox of Epoch. (out-Double[3])
    dllObj.Sgp4PropDs50UtcPos.restype = c_int
    dllObj.Sgp4PropDs50UtcPos.argtypes = [c_longlong, c_double, c_double * 3]

    # Retrieves propagator's precomputed results. This function can be used to obtain results from
    # a propagation which are not made available through calls to the propagation functions themselves.
    #
    # See example in Sgp4PropMse or Sgp4PropDs50UTC.
    #
    # This function should be called immediately after a successful call to Sgp4PropMse() or Sgp4PropDs50UTC() to
    # retrieve the desired values.
    #
    # It is the caller's responsibility to ensure that the array passed in the destArray parameter is large enough to
    # hold the requested values. The required size can be found by looking at the destArray size column of the table
    # below describing valid index values.
    #
    # The destArray Arrangement column lists the order of the elements in the array. It is not necessarily the
    # subscript of the element in the array since this is language-dependent. For example, in C/C++ the first element
    # in every array is the zero-subscripted element. In other programming languages, the subscript of the first element
    # is 1.
    #
    # Note: This function is not thread safe, please use Sgp4PropAll() instead
    #
    # The table below shows the values for the xf_Sgp4Out parameter:
    #
    # table
    #
    # Index
    # Index Interpretation
    # DestArray size
    # DestArray Arrangement
    #
    # 1Revolution number1Revolution number (based on the Osculating Keplerian
    # Elements)
    # 2Nodal Apogee Perigee3nodal period (minutes)apogee
    # (km)perigee (km)
    # 3Mean Keplerian Elements6semi-major axis (km)eccentricity
    # (unitless)inclination (degree)mean anomaly (degree)right ascension of the ascending node
    # (degree)argument of perigee (degree)
    # 4Osculating Keplerian Elements6Same as Mean Keplerian Elements
    #
    # satKey: The unique key of the satellite for which to retrieve results. (in-Long)
    # xf_Sgp4Out: Specifies which propagator outputs to retrieve. (in-Integer)
    # destArr: Array to receive the resulting propagator outputs. (out-Double[*])
    dllObj.Sgp4GetPropOut.restype = c_int
    dllObj.Sgp4GetPropOut.argtypes = [c_longlong, c_int, c_void_p]

    # Propagates a satellite, represented by the satKey, to the time expressed in either minutes since epoch or days
    # since 1950, UTC.
    # All propagation data is returned by this function.
    # satKey: The unique key of the satellite to propagate. (in-Long)
    # timeType: The propagation time type: 0 = minutes since epoch, 1 = days since 1950, UTC (in-Integer)
    # timeIn: The time to propagate to, expressed in either minutes since epoch or days since 1950, UTC. (in-Double)
    # xa_Sgp4Out: The array that stores all Sgp4 propagation data, see XA_SGP4OUT_? for array
    # arrangement (out-Double[64])
    dllObj.Sgp4PropAll.restype = c_int
    dllObj.Sgp4PropAll.argtypes = [c_longlong, c_int, c_double, c_double * 64]

    # Converts osculating position and velocity vectors to a set of mean Keplerian SGP4 elements.
    # The new position and velocity vectors are the results of using SGP4 propagator to propagate the computed
    # sgp4MeanKep to the time specified in year and day of epoch time.
    # They should be closely matched with the input osculating position and velocity vectors.
    #
    # The mean Keplerian elements are SGP4's Brouwer mean motion not SGP's Kozai mean motion.
    # Notes: Even if the function fails, the less acurate results may still be availalbe
    # yr: 2 or 4 digit year of the epoch time. (in-Integer)
    # day: Day of year of the epoch time. (in-Double)
    # pos: Input osculating position vector (km). (in-Double[3])
    # vel: Input osculating velocity vector (km/s). (in-Double[3])
    # posNew: Resulting position vector (km) propagated from the input xa_kep. (out-Double[3])
    # velNew: Resulting velocity vector (km/s) propagated from the input xa_kep. (out-Double[3])
    # xa_kep: Resulting set of Sgp4 mean Keplerian elements, see XA_KEP_? for array arrangement. (out-Double[6])
    dllObj.Sgp4PosVelToKep.restype = c_int
    dllObj.Sgp4PosVelToKep.argtypes = [
        c_int,
        c_double,
        c_double * 3,
        c_double * 3,
        c_double * 3,
        c_double * 3,
        c_double * 6,
    ]

    # Converts osculating position and velocity vectors to TLE array - allows bstar/bterm, drag values to be used in
    # the conversion if desired
    # The function is similar to Sgp4PosVelToKep but allows the user to specify agom (XP mode) and bstar/bterm values,
    # if desired, to be used in solving for the new Keplerian elements.
    #
    # The updated elements returned in the xa_tle array is of type SGP and the mean motion is Kozai mean motion.
    # Notes: Even if the function fails, the less acurate results may still be availalbe
    # pos: Input osculating position vector (km). (in-Double[3])
    # vel: Input osculating velocity vector (km/s). (in-Double[3])
    # xa_tle: Input/Output array containing TLE's numerical fields, see XA_TLE_? for array arrangement; required data
    # include epoch, ephemType, drag, bstar/bterm (inout-Double[64])
    dllObj.Sgp4PosVelToTleArr.restype = c_int
    dllObj.Sgp4PosVelToTleArr.argtypes = [c_double * 3, c_double * 3, c_double * 64]

    # Reepochs a loaded TLE, represented by the satKey, to a new epoch.
    # satKey: The unique key of the satellite to reepoch. (in-Long)
    # reEpochDs50UTC: The new epoch, express in days since 1950, UTC. (in-Double)
    # line1Out: A string to hold the first line of the reepoched TLE. (out-Character[512])
    # line2Out: A string to hold the second line of the reepoched TLE. (out-Character[512])
    dllObj.Sgp4ReepochTLE.restype = c_int
    dllObj.Sgp4ReepochTLE.argtypes = [c_longlong, c_double, c_char_p, c_char_p]

    # Reepochs a loaded TLE, represented by the satKey, to a new epoch in Csv format.
    # satKey: The unique key of the satellite to reepoch. (in-Long)
    # reEpochDs50UTC: The new epoch, express in days since 1950, UTC. (in-Double)
    # csvLine: A string to hold the reepoched CSV. (out-Character[512])
    dllObj.Sgp4ReepochCsv.restype = c_int
    dllObj.Sgp4ReepochCsv.argtypes = [c_longlong, c_double, c_char_p]

    # This function has been deprecated since v8.2
    # Note: The only requirement now is that "SGP4_Open_License.txt" file needs to be in those folders specified in
    # PATH/LD_LIBRARY_PATH environment or AstroStds DLLs/SOs'
    # licFilePath: The file path to the Sgp4 Open License file (in-Character[512])
    dllObj.Sgp4SetLicFilePath.restype = None
    dllObj.Sgp4SetLicFilePath.argtypes = [c_char_p]

    # This function has been deprecated since v8.2
    # Note: The only requirement now is that "SGP4_Open_License.txt" file needs to be in those folders specified in
    # PATH/LD_LIBRARY_PATH environment or AstroStds DLLs/SOs'
    # licFilePath: The file path to the Sgp4 Open License file (out-Character[512])
    dllObj.Sgp4GetLicFilePath.restype = None
    dllObj.Sgp4GetLicFilePath.argtypes = [c_char_p]

    # Generates ephemerides for the input satellite, represented by its satKey, for the specified time span and step
    # size
    # Notes: if arrSize isn't big enough to store all the ephemeris points, the function will exit when the ephemArr
    # reaches
    # that many points (arrSize) and the errCode is set to IDX_ERR_WARN
    # satKey: The unique key of the satellite to generate ephemerides. (in-Long)
    # startTime: Start time expressed in days since 1950, UTC. (in-Double)
    # endTime: End time expressed in days since 1950, UTC. (in-Double)
    # stepSize: Step size in minutes (static); enter predefine negative values (DYN_SS_?) to request dynamic step
    # size (in-Double)
    # sgp4_ephem: Output ephemeris type 1=ECI, 2=J2K. (in-Integer)
    # arrSize: Size of input ephemArr (in-Integer)
    # ephemArr: Output ephemerides - 0: time in days since 1950 UTC, 1-3: pos (km), 4-6: vel (km/sec) (out-Double[*, 7])
    # genEphemPts: Actual number of ephemeris points generated (always &le; arrSize) (out-Integer)
    dllObj.Sgp4GenEphems.restype = c_int
    dllObj.Sgp4GenEphems.argtypes = [c_longlong, c_double, c_double, c_double, c_int, c_int, c_void_p, c_int_p]

    # Generates ephemerides for the input TLE - in an array format - for the specified time span and step
    # size (OS - in One Step)
    # Notes:
    # - This function takes in TLE data directly and doesn't need to go through loading/geting satKey/initializing steps
    # - if arrSize isn't big enough to store all the ephemeris points, the function will exit when the ephemArr reaches
    #   that many points (arrSize) and the errCode is set to IDX_ERR_WARN
    # xa_tle: Input array containing TLE's numerical fields, see XA_TLE_? for array arrangement (in-Double[64])
    # startTime: Start time expressed in days since 1950, UTC. (in-Double)
    # endTime: End time expressed in days since 1950, UTC. (in-Double)
    # stepSize: Step size in minutes (static); enter predefine negative values (DYN_SS_?) to request dynamic step
    # size (in-Double)
    # sgp4_ephem: Output ephemeris type 1=ECI, 2=J2K. (in-Integer)
    # arrSize: Size of input ephemArr (in-Integer)
    # ephemArr: Output ephemerides - 0: time in days since 1950 UTC, 1-3: pos (km), 4-6: vel (km/sec) (out-Double[*, 7])
    # genEphemPts: Actual number of ephemeris points generated (always &le; arrSize) (out-Integer)
    dllObj.Sgp4GenEphems_OS.restype = c_int
    dllObj.Sgp4GenEphems_OS.argtypes = [c_double * 64, c_double, c_double, c_double, c_int, c_int, c_void_p, c_int_p]

    # Propagates all input satellites, represented by their satKeys, to the time expressed in days since 1950, UTC.
    # satKeys: The satellite keys of all input satellites (in-Long[*])
    # numOfSats: The total number of satellites (in-Integer)
    # ds50UTC: The time to propagate all satelllites to, expressed in days since 1950, UTC. (in-Double)
    # ephemArr: 0-2: pos (km), 3-5: vel (km/sec) (out-Double[*, 6])
    dllObj.Sgp4PropAllSats.restype = c_int
    dllObj.Sgp4PropAllSats.argtypes = [c_void_p, c_int, c_double, c_void_p]

    # Provides the native XP equinoctial elements and rates at given time
    # satKey: The unique key of the satellite to reepoch. (in-Long)
    # ds50UTC: The new epoch, express in days since 1950, UTC. (in-Double)
    # xa_eqnx: Equinoctial Elements (subtract thetaG from Longitude) at reEpoch time (out-Double[6])
    # xa_eqnx_dot: Equinoctial Element rates (subtract earth rotation rate from Longitude Rate) at reEpoch
    # time (out-Double[6])
    dllObj.XpGetNativeElts.restype = c_int
    dllObj.XpGetNativeElts.argtypes = [c_longlong, c_double, c_double * 6, c_double * 6]

    # Reepochs to a csv and provides the native XP equinoctial elements and rates
    # satKey: Input satKey (in-Long)
    # reEpochDs50UTC: The new epoch, express in days since 1950, UTC. (in-Double)
    # csvLine: A string to hold the reepoched CSV. (out-Character[512])
    # xa_eqnx: Equinoctial Elements (subtract thetaG from Longitude) at reEpoch time (out-Double[6])
    # xa_eqnx_dot: Equinoctial Element rates (subtract earth rotation rate from Longitude Rate) at reEpoch
    # time (out-Double[6])
    dllObj.XpReepochGetNativeElts.restype = c_int
    dllObj.XpReepochGetNativeElts.argtypes = [c_longlong, c_double, c_char_p, c_double * 6, c_double * 6]

    return dllObj


# Different return values of errCode from Sgp4 propagation
# SGP4 propagates successfully
GP_ERR_NONE = 0
# Bad FK model (FK5 must be selected)
GP_ERR_BADFK = 1
# A is negative
GP_ERR_ANEGATIVE = 2
# A is to large
GP_ERR_ATOOLARGE = 3
# Eccentricity is hyperbolic
GP_ERR_EHYPERPOLIC = 4
# Eccentricity is negative
GP_ERR_ENEGATIVE = 5
# Mean anomaly is too large
GP_ERR_MATOOLARGE = 6
# e**2 is too large
GP_ERR_E2TOOLARGE = 7

# Different time types for passing to Sgp4PropAll
# propagation time is in minutes since epoch
SGP4_TIMETYPE_MSE = 0
# propagation time is in days since 1950, UTC
SGP4_TIMETYPE_DS50UTC = 1

# Sgp4 propagated output fields
# Revolution number
XF_SGP4OUT_REVNUM = 1
# Nodal period, apogee, perigee
XF_SGP4OUT_NODAL_AP_PER = 2
# Mean Keplerian
XF_SGP4OUT_MEAN_KEP = 3
# Osculating Keplerian
XF_SGP4OUT_OSC_KEP = 4

# Sgp4 propagated data
# Propagation time in days since 1950, UTC
XA_SGP4OUT_DS50UTC = 0
# Propagation time in minutes since the satellite's epoch time
XA_SGP4OUT_MSE = 1
# ECI X position (km) in True Equator and Mean Equinox of Epoch
XA_SGP4OUT_POSX = 2
# ECI Y position (km) in True Equator and Mean Equinox of Epoch
XA_SGP4OUT_POSY = 3
# ECI Z position (km) in True Equator and Mean Equinox of Epoch
XA_SGP4OUT_POSZ = 4
# ECI X velocity (km/s) in True Equator and Mean Equinox of Epoch
XA_SGP4OUT_VELX = 5
# ECI Y velocity (km/s) in True Equator and Mean Equinox of Epoch
XA_SGP4OUT_VELY = 6
# ECI Z velocity (km/s) in True Equator and Mean Equinox of Epoch
XA_SGP4OUT_VELZ = 7
# Geodetic latitude (deg)
XA_SGP4OUT_LAT = 8
# Geodetic longitude (deg)
XA_SGP4OUT_LON = 9
# Height above geoid (km)
XA_SGP4OUT_HEIGHT = 10
# Revolution number
XA_SGP4OUT_REVNUM = 11
# Nodal period (min)
XA_SGP4OUT_NODALPER = 12
# Apogee (km)
XA_SGP4OUT_APOGEE = 13
# Perigee (km)
XA_SGP4OUT_PERIGEE = 14
# Mean semi-major axis (km)
XA_SGP4OUT_MN_A = 15
# Mean eccentricity (unitless)
XA_SGP4OUT_MN_E = 16
# Mean inclination (deg)
XA_SGP4OUT_MN_INCLI = 17
# Mean mean anomaly (deg)
XA_SGP4OUT_MN_MA = 18
# Mean right ascension of the asending node (deg)
XA_SGP4OUT_MN_NODE = 19
# Mean argument of perigee (deg)
XA_SGP4OUT_MN_OMEGA = 20
# Osculating semi-major axis (km)
XA_SGP4OUT_OSC_A = 21
# Osculating eccentricity (unitless)
XA_SGP4OUT_OSC_E = 22
# Osculating inclination (deg)
XA_SGP4OUT_OSC_INCLI = 23
# Osculating mean anomaly (deg)
XA_SGP4OUT_OSC_MA = 24
# Osculating right ascension of the asending node (deg)
XA_SGP4OUT_OSC_NODE = 25
# Osculating argument of perigee (deg)
XA_SGP4OUT_OSC_OMEGA = 26

XA_SGP4OUT_SIZE = 64

# Different options for generating ephemerides from SGP4
# ECI TEME of DATE     - 0: time in days since 1950 UTC, 1-3: pos (km), 4-6: vel (km/sec)
SGP4_EPHEM_ECI = 1
# MEME of J2K (4 terms)- 0: time in days since 1950 UTC, 1-3: pos (km), 4-6: vel (km/sec)
SGP4_EPHEM_J2K = 2


# Different dynamic step size options
# Use a simple algorithm to determine step size based on satellite's current position
DYN_SS_BASIC = -1

# *******************************************************************************

# ========================= End of auto generated code ==========================
