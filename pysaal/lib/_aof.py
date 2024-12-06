# This wrapper file was generated automatically by the GenDllWrappers program.
import platform
from ctypes import CDLL, POINTER, c_char_p, c_double, c_int, c_longlong, c_void_p
from pathlib import Path

c_int_p = POINTER(c_int)

LIB_PATH = Path(__file__).parent

# get the right filename of the dll/so
if platform.uname()[0] == "Windows":
    DLL_NAME = LIB_PATH / "Aof.dll"

if platform.uname()[0] == "Linux":
    DLL_NAME = LIB_PATH / "libaof.so"

if platform.uname()[0] == "Darwin":
    DLL_NAME = LIB_PATH / "libaof.dylib"


def get_aof_dll():
    """LoadAofDll() -- Loads Aof.dll from the PATH or LD_LIBRARY_PATH
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
    # Initializes Aof dll for use in the program
    # apAddr: The handle that was returned from DllMainInit() (in-Long)
    dllObj.AofInit.restype = c_int
    dllObj.AofInit.argtypes = [c_longlong]

    # Returns information about the current version of Aof.dll. The information is placed in the string parameter you
    # pass in
    # infoStr: A string to hold the information about Aof.dll. (out-Character[128])
    dllObj.AofGetInfo.restype = None
    dllObj.AofGetInfo.argtypes = [c_char_p]

    # Loads Aof-related parameters (1P/2P/3P cards, and Aof parameter free format) from an input text file
    # aofInputFile: The name of the file containing Aof-related parameters (in-Character[512])
    dllObj.AofLoadFile.restype = c_int
    dllObj.AofLoadFile.argtypes = [c_char_p]

    # Loads Aof-related parameters from an input text file
    # aofInputFile: The name of the file containing Aof-related parameters (in-Character[512])
    dllObj.AofLoadFileAll.restype = c_int
    dllObj.AofLoadFileAll.argtypes = [c_char_p]

    # Loads a single Aof-typed card
    # card: Aof-type input card (in-Character[512])
    dllObj.AofLoadCard.restype = c_int
    dllObj.AofLoadCard.argtypes = [c_char_p]

    # This function retrieves various AOF input data being entered from input flat files (and/or various AOF input
    # cards)
    # xa_aofCtrl: AOF control parameters, see XA_AOFCTRL_? for array arrangement (out-Double[16])
    # numOfInpSats: Number of satellite numbers entered in AOF P-card and/or 8P-card (out-Integer)
    # aofInpSats: Array of satellite numbers entered via AOF P-card and/or 8P-card (out-Integer[100])
    # numOfMissions: Number of satellite/mission records entered via Satellite/Mission (Satellite/Sensor) Data
    # card (out-Integer)
    # xa_aofSen: Array of mission records entered via Satellite/Mission (Satellite/Sensor) Data card, see
    # XA_AOFSEN_? for array arrangement (out-Double[100, 16])
    # numOfAreas: Number of defended areas entered via Defended Area Data card (out-Integer)
    # xa_aofArea: Array of defended areas entered via Defended Area Data card, see XA_AOFAREA_? (out-Double[100, 16])
    dllObj.AofGetDataFrInputFiles.restype = None
    dllObj.AofGetDataFrInputFiles.argtypes = [c_double * 16, c_int_p, c_int * 100, c_int_p, c_void_p, c_int_p, c_void_p]

    # This function resets all Aof control parameters previously loaded from input text files
    dllObj.AofReset.restype = None
    dllObj.AofReset.argtypes = []

    # Computes entry/exit times of basic overflight satellite/sensor (cone) versus basic defended areas (box, circle,
    # point)
    #
    # Note:  for xa_aofArea type=4 (polygon), use the AofComplex method.
    # xa_aofRun: aof run parameters, see XA_AOFRUN_? for array arrangement (in-Double[8])
    # satKey: the overflight satellite's unique key (in-Long)
    # xa_aofSen: satellite/mission data, see XA_AOFSEN_? for array arrangement (in-Double[16])
    # xa_aofArea: defended area data, see XA_AOFAREA_? for array arrangement (in-Double[16])
    # numOfPasses: number of passes found (out-Integer)
    # xa_entExitTimes: array of entry/exit times (out-Double[*])
    dllObj.AofBasic.restype = c_int
    dllObj.AofBasic.argtypes = [c_double * 8, c_longlong, c_double * 16, c_double * 16, c_int_p, c_void_p]

    # Computes entry/exit times of overflight satellite/sensor having complex configurations (cone, donut, butterfly,
    # leftButterly, rightButterfly)
    # versus defended areas defined by multiple lat lon height points (polygon)
    # For a description of the input parameter arrays xa_aofRun and xa_aofSen, see AofBasic.
    # The input array llhArr is a zero-based array with latitude, longitude and altitude of each point in subsequent
    # entries, e.g.:
    # llhArr[0] = point 1 latitude,
    # llhArr[1] = point 1 longitude,
    # llhArr[2] = point 1 altitude,
    # llhArr[3] = point 2 latitude, etc.
    # xa_aofRun: aof run parameters, see XA_AOFRUN_? for array arrangement (in-Double[8])
    # satKey: the overflight satellite's unique key (in-Long)
    # xa_aofSen: satellite/mission data, see XA_AOFSEN_? for array arrangement (in-Double[16])
    # numOfLlhPts: number of actual input lat-lon-height points (maximum 120 points) - lat+N (deg)/lon+E (deg)/
    # height (m) (in-Integer)
    # llhArr: defended area defined by array of lat-lon-height points (maximum 120 points) (in-Double[360])
    # numOfPasses: number of passes found (out-Integer)
    # xa_entExitTimes: array of entry/exit times (out-Double[*])
    dllObj.AofComplex.restype = c_int
    dllObj.AofComplex.argtypes = [c_double * 8, c_longlong, c_double * 16, c_int, c_double * 360, c_int_p, c_void_p]

    # This function returns a look angle from the llh point to the overfly satellite at the specified time
    # ds50TAI: Time, in ds50TAI, for which to compute the look angle (in-Double)
    # llh: lat +N -S (deg) /lon (+E) (deg) / height (m) (in-Double[3])
    # satKey: the overflight satellite's unique key (in-Long)
    # xa_look: look angle data, see XA_LOOK_? for array arrangement (out-Double[8])
    dllObj.AofGetLook.restype = c_int
    dllObj.AofGetLook.argtypes = [c_double, c_double * 3, c_longlong, c_double * 8]

    # This function returns a view angle from the overfly satellite to a llh point at the specified time
    # ds50TAI: Time, in ds50TAI, for which to compute the view angle (in-Double)
    # llh: lat +N -S (deg) /lon (+E) (deg) / height (m) (in-Double[3])
    # satKey: the overflight satellite's unique key (in-Long)
    # xa_aofView: view angle data, see XA_AOFVIEW_? for array arrangement (out-Double[8])
    dllObj.AofGetView.restype = c_int
    dllObj.AofGetView.argtypes = [c_double, c_double * 3, c_longlong, c_double * 8]

    # Determines darkness level of the "defended" area at the specified time
    # For a description of the input parameter array xa_aofArea, see AofBasic.
    # ds50TAI: Time, in ds50TAI, for which to compute the darkness status of the defended area (in-Double)
    # xa_aofArea: defended area data, see XA_AOFAREA_? for array arrangement (in-Double[16])
    dllObj.AofGetDarknessLevel.restype = c_int
    dllObj.AofGetDarknessLevel.argtypes = [c_double, c_double * 16]

    return dllObj


# AOF parameters
# input start/stop time type: 1=minutes since epoch (MSE), 0=date time (DTG)
XA_AOFCTRL_TIMEFLG = 0
# start time of interest (either MSE or DTG)
XA_AOFCTRL_START = 1
# stop time of interest (either MSE or DTG)
XA_AOFCTRL_STOP = 2
# search interval (min)
XA_AOFCTRL_INTERVAL = 3
# print output control flag; 0=print penetrations only, 1=print penetrations and data description
XA_AOFCTRL_PRTOPT = 4
# search method: 0=use brute force method, 1=use analytical method
XA_AOFCTRL_SRCHMET = 5
# output sort type: S=sort each area by sat#, then time, T=sort each area by time, then sat#
XA_AOFCTRL_SRTTYPE = 6

XA_AOFCTRL_SIZE = 16


# Defended area types
# area box type
AREATYPE_I_BOX = 1
# area circle type
AREATYPE_I_CIRCLE = 2
# area point type
AREATYPE_I_POINT = 3
# area polygon type
AREATYPE_I_POLYGON = 4


# AOF satellite/mission (satellite/sensor) data
# satellite number of sensor-bearing satellite
XA_AOFSEN_SATNUM = 0
# reserved for future use
XA_AOFSEN_TYPE = 1
# off nadir minimum look angle (deg) (=0 for Cone)
XA_AOFSEN_MINEL = 2
# off nadir maximum look angle (deg)
XA_AOFSEN_MAXEL = 3
# minimum azimuth of first azimuth range (deg)
XA_AOFSEN_MINAZ1 = 4
# maximum azimuth of first azimuth range (deg)
XA_AOFSEN_MAXAZ1 = 5
# minimum azimuth of second azimuth range (deg)
XA_AOFSEN_MINAZ2 = 6
# maximum azimuth of second azimuth range (deg)
XA_AOFSEN_MAXAZ2 = 7
# reserved for future use
XA_AOFSEN_ELEM7 = 8
# reserved for future use
XA_AOFSEN_ELEM8 = 9
# reserved for future use
XA_AOFSEN_ELEM9 = 10
# reserved for future use
XA_AOFSEN_ELEM10 = 11

XA_AOFSEN_SIZE = 16


# AOF satellite/sensor types
# circle (specify only off-nadir maximum look angle)
AOFSENTYPE_CIRCLE = 0


# AOF run parameters
# Maximum number of passes that AOF returns in one start/stop time
XA_AOFRUN_MAXPASSES = 0
# AOF start time in days since 1950, UTC
XA_AOFRUN_START = 1
# AOF stop time in days since 1950, UTC
XA_AOFRUN_STOP = 2
# Search interval (min)
XA_AOFRUN_INTERVAL = 3

XA_AOFRUN_SIZE = 8


# AOF defended area types
# Defended area is a box
AOF_AREATYPE_BOX = 1
# Defended area is a circle
AOF_AREATYPE_CIRCLE = 2
# Defended area is a point
AOF_AREATYPE_POINT = 3
# Defended area is a polygon
AOF_AREATYPE_POLYGON = 4


# AOF defended area data
# Area number
XA_AOFAREA_NUM = 0
# | 1 = BOX                       | 2 = CIRCLE              | 3 = POINT
XA_AOFAREA_TYPE = 1
# | N lat (deg) upper left corner | N lat (deg) center point| N lat (deg) center point
XA_AOFAREA_ELEM1 = 2
# | E lon (deg) upper left corner | E lon (deg) center point| E lon (deg) center point
XA_AOFAREA_ELEM2 = 3
# | N lat (deg) lower right corner| circle radius (km)      | height (km, above reference geoid)
XA_AOFAREA_ELEM3 = 4
# | E lon (deg) lower right corner|                         |
XA_AOFAREA_ELEM4 = 5

XA_AOFAREA_SIZE = 16


# Penetration-level darkness status
# lit throughout penetration
DARKLEVEL_ALLLIT = 0
# dark throughout penetration
DARKLEVEL_ALLDARK = 1
# partly-lit during penetration
DARKLEVEL_PARTLIT = 2

# View angle from overfly satellite to a llh point
# Azimuth (deg)
XA_AOFVIEW_AZIM = 0
# Elevation (deg)
XA_AOFVIEW_ELEV = 1
# Has line of sight to the point (1=Yes, 0=No-earth obstructs the view)
XA_AOFVIEW_HASLOS = 2

XA_AOFVIEW_SIZE = 8

# maximum of number of lat-lon-height points that can be used to describe a defended area
MAX_LLHPOINTS = 120


# ========================= End of auto generated code ==========================
