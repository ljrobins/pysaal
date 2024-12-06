# This wrapper file was generated automatically by the GenDllWrappers program.
import platform
from ctypes import CDLL, POINTER, c_char_p, c_double, c_int, c_longlong, c_void_p
from pathlib import Path

c_int_p = POINTER(c_int)
c_double_p = POINTER(c_double)

LIB_PATH = Path(__file__).parent

# get the right filename of the dll/so
if platform.uname()[0] == "Windows":
    DLL_NAME = LIB_PATH / "ExtEphem.dll"

if platform.uname()[0] == "Linux":
    DLL_NAME = LIB_PATH / "libextephem.so"

if platform.uname()[0] == "Darwin":
    DLL_NAME = LIB_PATH / "libextephem.dylib"


def get_ext_ephem_dll():
    """LoadExtEphemDll() -- Loads ExtEphem.dll from the PATH or LD_LIBRARY_PATH
    depending on Operating System and returns the object type.
    for each of its functions.

    Return Value
    an object which can be used to access the dll."""

    # load the dll
    if DLL_NAME.exists():
        dllObj = CDLL(DLL_NAME.as_posix())
    else:
        raise FileNotFoundError(f"{DLL_NAME} not found.")
    # set parameter list and return type for each function

    # Notes: This function has been deprecated since v9.0.
    # Initializes ExtEphem DLL for use in the program
    # If this function returns an error, it is recommended that the users stop the program immediately.
    # The error occurs if the users forget to load and initialize all the prerequisite DLLs, as listed
    # in the DLL Prerequisite section, before using this DLL.
    # apAddr: The handle that was returned from DllMainInit() (in-Long)
    dllObj.ExtEphInit.restype = c_int
    dllObj.ExtEphInit.argtypes = [c_longlong]

    # Returns information about the current version of ExtEphem DLL.
    # The information is placed in the string parameter passed in.
    # The returned string provides information about the version number, build date, and the platform of the ExtEphem
    # DLL.
    # infoStr: A string to hold the information about ExtEphem.dll (out-Character[128])
    dllObj.ExtEphGetInfo.restype = None
    dllObj.ExtEphGetInfo.argtypes = [c_char_p]

    # Loads a file containing EXTEPHEM's
    # The users can use this function repeatedly to load EXTEPHEMs from different input files.
    # However, only unique satKeys are stored in the binary tree. Duplicated EXTEPHEMs
    # (determined by same file name, satellite number + epoch) won't be stored.
    #
    # EXTEPHEMs can be included directly in the main input file or they can be read from a
    # separate file identified with "EPHFIL =[pathname\filename]".
    #
    # This function only reads EXTEPHEMs from the main input file or EXTEPHEMs from the file
    # identified with EPHFIL in the input file. It won't read anything else.
    # extEphFile: The name of the file containing external ephemeris data to be loaded (in-Character[512])
    dllObj.ExtEphLoadFile.restype = c_int
    dllObj.ExtEphLoadFile.argtypes = [c_char_p]

    # Saves the currently loaded EXTEPHEM's to a file (EPHFIL=input file name)
    # extEphFile: The name of the file in which to save the settings (in-Character[512])
    # saveMode: Specifies whether to create a new file or append to an existing one (0 = create, 1= append) (in-Integer)
    # saveForm: Specifies the mode in which to save the file (0 = text format, 1 = not yet implemented, reserved for
    # future) (in-Integer)
    dllObj.ExtEphSaveFile.restype = c_int
    dllObj.ExtEphSaveFile.argtypes = [c_char_p, c_int, c_int]

    # Removes an EXTEPHEM represented by the satKey from memory
    # If the users enter an invalid satKey (the satKey does not exist in memory), the function will return a non-zero
    # value indicating an error.
    # satKey: The unique key of the satellite to be removed (in-Long)
    dllObj.ExtEphRemoveSat.restype = c_int
    dllObj.ExtEphRemoveSat.argtypes = [c_longlong]

    # Removes all EXTEPHEMS from memory
    dllObj.ExtEphRemoveAllSats.restype = c_int
    dllObj.ExtEphRemoveAllSats.argtypes = []

    # Returns the number of EXTEPHEM's currently loaded
    # See ExtEphGetLoaded for example.
    # This function is useful for dynamically allocating memory for the array that is passed to the function
    # ExtEphGetLoaded().
    dllObj.ExtEphGetCount.restype = c_int
    dllObj.ExtEphGetCount.argtypes = []

    # Retrieves all of the currently loaded satKeys. These satKeys can be used to access the external ephemeris data
    # for the EXTEPHEM's
    # It is recommended that ExtEphGetCount() is used to count how many satellites are currently loaded in the ExtEphem
    # DLL's binary tree.
    # The users then use this number to dynamically allocate the satKeys array and pass it to this function.
    #
    # If the users prefer to pass a static array to the function, ensure that it is big enough to store all the satKeys
    # in memory.
    # order: Specifies the order in which the satKeys should be returned: 0=ascending, 1=descending, 2=order as loaded
    # (in-Integer)
    # satKeys: The array in which to store the satKeys (out-Long[*])
    dllObj.ExtEphGetLoaded.restype = None
    dllObj.ExtEphGetLoaded.argtypes = [c_int, c_void_p]

    # Allows for an EXTEPHEM to be added to memory without using an input file. The function creates a place holder for
    # an EXTEPHEM
    # If the same satellite (same satNum and epochDs50UTC) was previously added to the ExtEphem DLL's binary tree,
    # the function will generate a new unique satKey. This is very useful when the users want to compare ephemerides
    # of the same satellite number and same epoch time from different sources.
    # satNum: Satellite number (in-Integer)
    # epochDs50UTC: Epoch time in ds50UTC (in-Double)
    # ae: Mean Earth radius (km) (in-Double)
    # ke: Earth gravitational constant (in-Double)
    # coordSys: Ephemeris coordinate system, see COORD_? for avaialble coordinate sytems (in-Integer)
    dllObj.ExtEphAddSat.restype = c_longlong
    dllObj.ExtEphAddSat.argtypes = [c_int, c_double, c_double, c_double, c_int]

    # Adds an ephemeris point to the end of an EXTEPHEM's set of ephemeris points
    # The new ephemeris point will only be added to the array if its time is greater than the times of all points
    # already in the array.
    # Therefore, the array is always in sorted order (t1 < t2 <... < tn).
    # satKey: The satellite's unique key (in-Long)
    # ds50UTC: Epoch time in ds50UTC (in-Double)
    # pos: Position at cuurent time (km) (in-Double[3])
    # vel: Velocity at current time (km/sec) (in-Double[3])
    # revNum: The ephemeris point revolution number (in-Integer)
    dllObj.ExtEphAddSatEphem.restype = c_int
    dllObj.ExtEphAddSatEphem.argtypes = [c_longlong, c_double, c_double * 3, c_double * 3, c_int]

    # Adds an ephemeris point (including covariance matrix) to the end of an EXTEPHEM's set of ephemeris points
    # satKey: The satellite's unique key (in-Long)
    # ds50UTC: Epoch time in ds50UTC (in-Double)
    # pos: Position at cuurent time (km) (in-Double[3])
    # vel: Velocity at current time (km/sec) (in-Double[3])
    # revNum: The ephemeris point revolution number (in-Integer)
    # covUVW: The covariance matrix in vector format (21 terms in one-dimensional array) (in-Double[21])
    dllObj.ExtEphAddSatEphemCovMtx.restype = c_int
    dllObj.ExtEphAddSatEphemCovMtx.argtypes = [c_longlong, c_double, c_double * 3, c_double * 3, c_int, c_double * 21]

    # Adds an ephemeris point (including covariance matrix) to the end of an EXTEPHEM's set of ephemeris points
    # satKey: The satellite's unique key (in-Long)
    # ds50UTC: Epoch time in ds50UTC (in-Double)
    # pos: Position at cuurent time (km) (in-Double[3])
    # vel: Velocity at current time (km/sec) (in-Double[3])
    # revNum: The ephemeris point revolution number (in-Integer)
    # extArr: The extra array: 1-21=lower triangle matrix, 22-128=future use (in-Double[128])
    dllObj.ExtEphAddSatEphemExt.restype = c_int
    dllObj.ExtEphAddSatEphemExt.argtypes = [c_longlong, c_double, c_double * 3, c_double * 3, c_int, c_double * 128]

    # Loads satellite data from an external ephemeris file (any valid external ephemeris file formats) and returns a
    # satKey on success
    # extEphFile: The name of the file containing external ephemeris data to be loaded (in-Character[512])
    dllObj.ExtEphAddSatFrFile.restype = c_longlong
    dllObj.ExtEphAddSatFrFile.argtypes = [c_char_p]

    # Retrieves all data for an EXTEPHEM with a single function call
    # satKey: The satellite's unique key (in-Long)
    # satNum: Satellite number (out-Integer)
    # satName: Satellite international designator (out-Character[8])
    # recName: Record name (default to source file path, fileLoc) (out-Character[128])
    # epochDs50UTC: Satellite epoch time in ds50UTC (out-Double)
    # ae: Mean Earth radius (km) (out-Double)
    # ke: Earth gravitational constant (er**3/2 per minute) (out-Double)
    # pos: Position at epoch (km) (out-Double[3])
    # vel: Velocity at epoch (km/s) (out-Double[3])
    # coordSys: Ephemeris coordinate, see COORD_? for avaialble coordinate sytems (out-Integer)
    # numOfPts: Number of ephemeris points (out-Integer)
    # fileLoc: File location (out-Character[512])
    dllObj.ExtEphGetAllFields.restype = c_int
    dllObj.ExtEphGetAllFields.argtypes = [
        c_longlong,
        c_int_p,
        c_char_p,
        c_char_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double * 3,
        c_double * 3,
        c_int_p,
        c_int_p,
        c_char_p,
    ]

    # Retrieves the value of a specific field of an EXTEPHEM
    #
    # When using xf_ExtEph = 11, the input coordinate system is returned as an integer value.  The table below shows
    # the coordinate system values:
    #
    # table
    #
    # Value
    # Coordinate System
    #
    # 1  ECI TEME of DATE
    # 2  MEME of J2K
    # 3  Earth Fixed Greenwich (EFG)
    # 4  Earch Centered Rotation (ECR)
    # 100Invalid
    #
    # satKey: The satellite's unique key (in-Long)
    # xf_ExtEph: Predefined number specifying which field to retrieve, see XF_EXTEPH_? for field specification
    # (in-Integer)
    # valueStr: A string to contain the value of the requested field (out-Character[512])
    dllObj.ExtEphGetField.restype = c_int
    dllObj.ExtEphGetField.argtypes = [c_longlong, c_int, c_char_p]

    # Updates the value of a specific field of an EXTEPHEM
    # satKey: The satellite's unique key (in-Long)
    # xf_ExtEph: Predefined number specifying which field to set, see XF_EXTEPH_? for field specification (in-Integer)
    # valueStr: The new value of the specified field, expressed as a string (in-Character[512])
    dllObj.ExtEphSetField.restype = c_int
    dllObj.ExtEphSetField.argtypes = [c_longlong, c_int, c_char_p]

    # Retrieves the times (in days since 1950 UTC) of the start and end ephemeris points of the EXTEPHEM
    # satKey: The satellite's unique key (in-Long)
    # startDs50UTC: The ephemeris start time (first ephemeris point) in days since 1950, UTC (out-Double)
    # endDs50UTC: The ephemeris end time (last ephemeris point) in days since 1950, UTC (out-Double)
    dllObj.ExtEphStartEndTime.restype = c_int
    dllObj.ExtEphStartEndTime.argtypes = [c_longlong, c_double_p, c_double_p]

    # Retrieves the data for a specific point within an EXTEPHEM
    # It is important to know that the array subscript starts at one (not zero).
    # satKey: The satellite's unique key (in-Long)
    # index: The position number of the ephemeris point to be retrieved (1=first point) (in-Integer)
    # ds50UTC: The resulting time in ds50UTC (out-Double)
    # pos: The resulting position (km) (out-Double[3])
    # vel: The resulting velocity (km/s) (out-Double[3])
    # revNum: The resulting revolution number (out-Integer)
    dllObj.ExtEphGetEphemeris.restype = c_int
    dllObj.ExtEphGetEphemeris.argtypes = [c_longlong, c_int, c_double_p, c_double * 3, c_double * 3, c_int_p]

    # Retrieves the data (including the covariance matrix) for a specific point within an EXTEPHEM
    # satKey: The satellite's unique key (in-Long)
    # index: The position number of the ephemeris point to be retrieved (1=first point) (in-Integer)
    # ds50UTC: The resulting time in ds50UTC (out-Double)
    # pos: The resulting position (km) (out-Double[3])
    # vel: The resulting velocity (km/s) (out-Double[3])
    # revNum: The resulting revolution number (out-Integer)
    # covMtx: The 6x6 covariance matrix (out-Double[6, 6])
    dllObj.ExtEphGetCovMtx.restype = c_int
    dllObj.ExtEphGetCovMtx.argtypes = [c_longlong, c_int, c_double_p, c_double * 3, c_double * 3, c_int_p, c_void_p]

    # Interpolates the external ephemeris data to the requested time in minutes since the satellite's epoch time
    # The coordinate system of the output position and velocity is the same as the input ephemerides.
    # satKey: The satellite's unique key (in-Long)
    # mse: The requested time in minutes since the satellite's epoch time (in-Double)
    # ds50UTC: The resulting time in ds50UTC (out-Double)
    # pos: The resulting position (km) (out-Double[3])
    # vel: The resulting velocity (km/s) (out-Double[3])
    # revNum: The resulting revolution number (out-Integer)
    dllObj.ExtEphMse.restype = c_int
    dllObj.ExtEphMse.argtypes = [c_longlong, c_double, c_double_p, c_double * 3, c_double * 3, c_int_p]

    # Interpolates the external ephemeris data to the requested time in minutes since the satellite's epoch time
    # satKey: The satellite's unique key (in-Long)
    # mse: The requested time in minutes since the satellite's epoch time (in-Double)
    # ds50UTC: The resulting time in ds50UTC (out-Double)
    # pos: The resulting position (km) (out-Double[3])
    # vel: The resulting velocity (km/s) (out-Double[3])
    # revNum: The resulting revolution number (out-Integer)
    # covMtx: The 6x6 covariance matrix (out-Double[6, 6])
    dllObj.ExtEphMseCovMtx.restype = c_int
    dllObj.ExtEphMseCovMtx.argtypes = [c_longlong, c_double, c_double_p, c_double * 3, c_double * 3, c_int_p, c_void_p]

    # Interpolates the external ephemeris data to the requested time in days since 1950, UTC
    # The coordinate system of the output position and velocity is the same as the input ephemerides.
    # satKey: The satellite's unique key (in-Long)
    # ds50UTC: The requested time in ds50UTC (in-Double)
    # mse: The resulting time in minutes since the satellite's epoch time (out-Double)
    # pos: The resulting position (km) (out-Double[3])
    # vel: The resulting velocity (km/s) (out-Double[3])
    # revNum: The resulting revolution number (out-Integer)
    dllObj.ExtEphDs50UTC.restype = c_int
    dllObj.ExtEphDs50UTC.argtypes = [c_longlong, c_double, c_double_p, c_double * 3, c_double * 3, c_int_p]

    # Interpolates the external ephemeris data to the requested time in days since 1950, UTC
    # satKey: The satellite's unique key (in-Long)
    # ds50UTC: The requested time in ds50UTC (in-Double)
    # mse: The resulting time in minutes since the satellite's epoch time (out-Double)
    # pos: The resulting position (km) (out-Double[3])
    # vel: The resulting velocity (km/s) (out-Double[3])
    # revNum: The resulting revolution number (out-Integer)
    # covMtx: The 6x6 covariance matrix (out-Double[6, 6])
    dllObj.ExtEphDs50UTCCovMtx.restype = c_int
    dllObj.ExtEphDs50UTCCovMtx.argtypes = [
        c_longlong,
        c_double,
        c_double_p,
        c_double * 3,
        c_double * 3,
        c_int_p,
        c_void_p,
    ]

    # Extensible routine which retrieves/interpolates external ephemeris data based on user's request
    # satKey: The satellite's unique key (in-Long)
    # xf_getEph: Input type: 1=using MSE, 2=using Ds50UTC, 3=using index (one-based) (in-Integer)
    # inVal: Input value as indicated in the input type (in-Double)
    # extArr: The resulting array: 1st=mse, 2=ds50UTC, 3-5=pos, 5-8=vel, 9=revNum, 10-30=6x6 covMtx lower triangle
    # (out-Double[128])
    dllObj.ExtEphXten.restype = c_int
    dllObj.ExtEphXten.argtypes = [c_longlong, c_int, c_double, c_double * 128]

    # This function returns a string that represents the EXTFIL= directive used to read a particular EXTEPHEM
    # satKey: The satellite's unique key (in-Long)
    # line: A string representing the directive used to read a particular EXTEPHEM (out-Character[512])
    dllObj.ExtEphGetLine.restype = c_int
    dllObj.ExtEphGetLine.argtypes = [c_longlong, c_char_p]

    # Returns the first satKey that matches the satNum in the EXTEPHEM binary tree
    # This function is useful when ExtEphem DLL is used in applications that requires only one record (one EXTEPHEM
    # entry)
    # for one satellite and the applications refer to that EXTEPHEM by its satellite number.
    # However, the Astrodynamic Standard Shared library only uses satKeys; this function helps to return the associated
    # satKey of that satellite.
    # satNum: input satellite number (in-Integer)
    dllObj.ExtEphGetSatKey.restype = c_longlong
    dllObj.ExtEphGetSatKey.argtypes = [c_int]

    # Creates satKey from EXTEPHEM's satelite number and date time group string
    # This is the proper way to reconstruct a satKey from its fields. If the users use their own routine to do this,
    # the computed satKey might be different.
    # satNum: input satellite number (in-Integer)
    # epochDtg: input date time group string: [yy]yydddhhmmss.sss or [yy]yyddd.ddddddd or DTG15, DTG17,
    # DTG20 (in-Character[20])
    dllObj.ExtEphFieldsToSatKey.restype = c_longlong
    dllObj.ExtEphFieldsToSatKey.argtypes = [c_int, c_char_p]

    return dllObj


# Indexes of coordinate systems
# ECI TEME of DATE
COORD_ECI = 1
# MEME of J2K
COORD_J2K = 2
# Earth Fixed Greenwich (EFG)
COORD_EFG = 3
# Earch Centered Rotation (ECR)
COORD_ECR = 4
# Lat Lon Height and a vector offset (range, azimuth, elevation)
COORD_LLH = 5
# Sensor site (ECR) and a vector offset (range, azimuth, elevation)
COORD_SEN = 6

# ECI TEME of DATE, fixed point
COORD_ECIFP = 11
# MEME of J2K, fixed point
COORD_J2KFP = 12
# Earth Fixed Greenwich (EFG), fixed point
COORD_EFGFP = 13
# Earch Centered Rotation (ECR), fixed point
COORD_ECRFP = 14
# Lat Lon Height and an offset vector (range, azimuth, elevation)
COORD_LLHOV = 15
# Sensor site (ECR) and an offset vector (range, azimuth, elevation)
COORD_SENOV = 16
# Current position (LLH), heading (azimuth), and constant speed of an mobile object that travels in a rhumb line course
COORD_HCSRL = 17
# List of waypoints (LLH) that describes the movement of an object that travels in a rhumb line course
COORD_WPTRL = 18
# Current position (LLH), initial heading (azimuth), and constant speed of an mobile object that travels in a great
# circle course
COORD_HCSGC = 19
# List of waypoints (LLH) that describes the movement of an object that travels in a great circle course
COORD_WPTGC = 20


# Invalid coordinate system
COORD_INVALID = 100

# UVW convariance matrix - TEME of DATE
COVMTX_UVW_DATE = 0
# Cartesian covariance matrix - TEME of DATE
COVMTX_XYZ_DATE = 10
# Equinoctial covariance matrix - TEME of DATE
COVMTX_EQNX_DATE = 20
# UVW convariance matrix - MEME of J2K
COVMTX_UVW_J2K = 30
# Cartesian covariance matrix - MEME of J2K
COVMTX_XYZ_J2K = 40
# Equinoctial covariance matrix - MEME of J2K
COVMTX_EQNX_J2K = 50


# Get ephemeris data using time in minutes since epoch
XF_GETEPH_MSE = 1
# Get ephemeris data using time in days since 1950 UTC
XF_GETEPH_UTC = 2
# Get ephemeris data using index of the element in the array
XF_GETEPH_IDX = 3

# Indexes of EXTEPH data fields
# Satellite number I5
XF_EXTEPH_SATNUM = 1
# Epoch YYDDDHHMMSS.SSS
XF_EXTEPH_EPOCH = 2
# Earth radius (km)
XF_EXTEPH_AE = 3
# Ke
XF_EXTEPH_KE = 4
# position X (km) F16.8
XF_EXTEPH_POSX = 5
# position Y (km) F16.8
XF_EXTEPH_POSY = 6
# position Z (km) F16.8
XF_EXTEPH_POSZ = 7
# velocity X (km/s) F16.12
XF_EXTEPH_VELX = 8
# velocity Y (km/s) F16.12
XF_EXTEPH_VELY = 9
# velocity Z (km/s) F16.12
XF_EXTEPH_VELZ = 10
# Input coordinate systems
XF_EXTEPH_COORD = 11
# Num of ephemeris points
XF_EXTEPH_NUMOFPTS = 12
# Ephemeris file path
XF_EXTEPH_FILEPATH = 13
# International Designator
XF_EXTEPH_SATNAME = 14
# Record name
XF_EXTEPH_RECNAME = 15

# ========================= End of auto generated code ==========================
