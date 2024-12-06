# This wrapper file was generated automatically by the GenDllWrappers program.
import platform
from ctypes import CDLL, POINTER, c_char, c_char_p, c_double, c_int, c_longlong, c_void_p
from pathlib import Path

c_double_p = POINTER(c_double)
c_int_p = POINTER(c_int)
c_longlong_p = POINTER(c_longlong)

LIB_PATH = Path(__file__).parent

# get the right filename of the dll/so
if platform.uname()[0] == "Windows":
    DLL_NAME = LIB_PATH / "Obs.dll"

if platform.uname()[0] == "Linux":
    DLL_NAME = LIB_PATH / "libobs.so"

if platform.uname()[0] == "Darwin":
    DLL_NAME = LIB_PATH / "libobs.dylib"


def get_obs_dll():
    """LoadObsDll() -- Loads Obs.dll from the PATH or LD_LIBRARY_PATH
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
    # Initializes Obs DLL for use in the program
    # apAddr: The handle that was returned from DllMainInit() (in-Long)
    dllObj.ObsInit.restype = c_int
    dllObj.ObsInit.argtypes = [c_longlong]

    # Returns information about the current version of Obs DLL.
    # The information is placed in the string parameter passed in.
    # infoStr: A string to hold the information about Obs.dll (out-Character[128])
    dllObj.ObsGetInfo.restype = None
    dllObj.ObsGetInfo.argtypes = [c_char_p]

    # Sets the year for transmission observation format (TTY) input files
    # ttyYear: 2 or 4 digits year (in-Integer)
    dllObj.ObsSetTTYYear.restype = None
    dllObj.ObsSetTTYYear.argtypes = [c_int]

    # Loads observation data from an input text file
    # obsFile: The name of the file containing obs-related data (in-Character[512])
    dllObj.ObsLoadFile.restype = c_int
    dllObj.ObsLoadFile.argtypes = [c_char_p]

    # Saves the currently loaded obs data to a file
    # obsFile: The name of the file in which to save the loaded obs (in-Character[512])
    # saveMode: Specifies whether to create a new file or append to an existing one (0 = create, 1= append) (in-Integer)
    # obsForm: Specifies the mode in which to save the file (0 = B3 format, 1 = TTY, 2 = CSV) (in-Integer)
    dllObj.ObsSaveFile.restype = c_int
    dllObj.ObsSaveFile.argtypes = [c_char_p, c_int, c_int]

    # Removes an obs, represented by the obsKey, from the set of currently loaded observations
    # obsKey: The observation's unique key (in-Long)
    dllObj.ObsRemove.restype = c_int
    dllObj.ObsRemove.argtypes = [c_longlong]

    # Removes all currently loaded observations from memory
    dllObj.ObsRemoveAll.restype = c_int
    dllObj.ObsRemoveAll.argtypes = []

    # Returns the number of observations currently loaded
    dllObj.ObsGetCount.restype = c_int
    dllObj.ObsGetCount.argtypes = []

    # Retrieves all of the currently loaded obsKeys. These obsKeys can be used to access the internal data for the
    # observations
    # Sort options (order):
    # (+/-)1 = (descending/ascending) time, sensor, obsType, elev
    # (+/-)2 = (descending/ascending) time, elevation
    # (+/-)3 = (descending/ascending) time, sensor, otype, el, satno
    # (+/-)4 = (descending/ascending) sensor, satno, time, elev
    # (+/-)5 = (descending/ascending) sensor, time, elevation
    # (+/-)6 = (descending/ascending) sensor, satno, obsType, time, elev
    # (+/-)7 = (descending/ascending) satno, time, sensor, otype, el
    # (+/-)8 = (reversed/same)        order as obs were read
    # 9 : as is in the tree
    # order: Specifies the order in which the obsKeys should be returned (in-Integer)
    # obsKeys: The array in which to store the obsKeys (out-Long[*])
    dllObj.ObsGetLoaded.restype = None
    dllObj.ObsGetLoaded.argtypes = [c_int, c_void_p]

    # Loads a single observation-typed card
    # card: Any single observation-typed card (B3, B3E, TTY, ...) but not OBSFIL= (in-Character[512])
    dllObj.ObsLoadCard.restype = c_int
    dllObj.ObsLoadCard.argtypes = [c_char_p]

    # Loads a one-line or two-line observation
    # card1: Any single observation-typed card (B3, B3E, TTY, ...) or Card #1 of TTY obs type 4, 7, 8,
    # 9 (in-Character[512])
    # card2: Card #2 of TTY obs type 4, 7, 8, 9 (in-Character[512])
    dllObj.ObsLoadTwoCards.restype = c_int
    dllObj.ObsLoadTwoCards.argtypes = [c_char_p, c_char_p]

    # Adds an observation from a string in B3 observation format
    # card: The input string in B3 observation format (in-Character[512])
    dllObj.ObsAddFrB3Card.restype = c_longlong
    dllObj.ObsAddFrB3Card.argtypes = [c_char_p]

    # Works like ObsAddFrB3Card but designed for Matlab
    # card: The input string in B3 observation format (in-Character[512])
    # obsKey: The obsKey of the newly added observation on success, a negative value on error (out-Long)
    dllObj.ObsAddFrB3CardML.restype = None
    dllObj.ObsAddFrB3CardML.argtypes = [c_char_p, c_longlong_p]

    # Converts B3 format to csv format without loading B3 obs into memory
    # card: The input string in B3 observation format (in-Character[512])
    # csvLine: The output string in csv observation format (out-Character[512])
    dllObj.ObsB3ToCsv.restype = c_int
    dllObj.ObsB3ToCsv.argtypes = [c_char_p, c_char_p]

    # Converts CSV format to B3 format without loading CSV obs into memory
    # csvLine: The input string in csv observation format (in-Character[512])
    # newSatno: New satellite number to replace what's in CSV obs if desired (value of zero does not
    # renumber) (in-Integer)
    # card: The output string in B3 observation format (out-Character[512])
    dllObj.ObsCsvToB3.restype = c_int
    dllObj.ObsCsvToB3.argtypes = [c_char_p, c_int, c_char_p]

    # Adds an observation from a TTY (1 line or 2 lines) observation format
    # card1: Card #1 of a TTY obs (in-Character[512])
    # card2: Card #2 of TTY obs type 4, 7, 8, 9 or an empty string for other TTY obs types (in-Character[512])
    dllObj.ObsAddFrTTYCards.restype = c_longlong
    dllObj.ObsAddFrTTYCards.argtypes = [c_char_p, c_char_p]

    # Works like ObsAddFrTTYCards but designed for Matlab
    # card1: Card #1 of a TTY obs (in-Character[512])
    # card2: Card #2 of TTY obs type 4, 7, 8, 9 or an empty string for other TTY obs types (in-Character[512])
    # obsKey: The obsKey of the newly added observation on success, a negative value on error (out-Long)
    dllObj.ObsAddFrTTYCardsML.restype = None
    dllObj.ObsAddFrTTYCardsML.argtypes = [c_char_p, c_char_p, c_longlong_p]

    # Converts TTY format to CSV format without loading TTY obs into memory
    # card1: Card #1 of a TTY obs (in-Character[512])
    # card2: Card #2 of TTY obs type 4, 7, 8, 9 or an empty string for other TTY obs types (in-Character[512])
    # csvLine: The obs in csv format (out-Character[512])
    dllObj.ObsTTYToCsv.restype = c_int
    dllObj.ObsTTYToCsv.argtypes = [c_char_p, c_char_p, c_char_p]

    # Converts CSV format to TTY format without loading CSV obs into memory
    # csvLine: The obs in csv format (in-Character[512])
    # newSatno: New satellite number to replace what's in CSV obs if desired (value of zero does not
    # renumber) (in-Integer)
    # card1: Card #1 of a TTY obs (out-Character[512])
    # card2: Card #2 of TTY obs type 4, 7, 8, 9 or an empty string for other TTY obs types (out-Character[512])
    dllObj.ObsCsvToTTY.restype = c_int
    dllObj.ObsCsvToTTY.argtypes = [c_char_p, c_int, c_char_p, c_char_p]

    # Adds one observation using csv obs string
    # csvLine: Input csv obs string (in-Character[512])
    dllObj.ObsAddFrCsv.restype = c_longlong
    dllObj.ObsAddFrCsv.argtypes = [c_char_p]

    # Adds one observation using csv obs string - for MatLab
    # csvLine: Input csv obs string (in-Character[512])
    # obsKey: The obsKey of the newly added observation on success, a negative value on error (out-Long)
    dllObj.ObsAddFrCsvML.restype = None
    dllObj.ObsAddFrCsvML.argtypes = [c_char_p, c_longlong_p]

    # Adds one observation using its input data. Depending on the observation type, some input data might be
    # unavailable and left blank
    # secClass: security classification (in-Character)
    # satNum: satellite number (in-Integer)
    # senNum: sensor number (in-Integer)
    # obsTimeDs50utc: observation time in days since 1950 UTC (in-Double)
    # elOrDec: elevation or declination (deg) (in-Double)
    # azOrRA: azimuth or right-ascension (deg) (in-Double)
    # range: range (km) (in-Double)
    # rangeRate: range rate (km/s), or equinox indicator (0-3) for obs type 5/9 (in-Double)
    # elRate: elevation rate (deg/s) (in-Double)
    # azRate: azimuth rate (deg/s) (in-Double)
    # rangeAccel: range acceleration (km/s^2) (in-Double)
    # obsType: observation type (in-Character)
    # trackInd: track position indicator (3=start track ob, 4=in track ob, 5=end track ob) (in-Integer)
    # astat: association status assigned by SPADOC (in-Integer)
    # siteTag: original satellite number (in-Integer)
    # spadocTag: SPADOC-asssigned tag number (in-Integer)
    # pos: position XYZ (km) (ECI or EFG) (in-Double[3])
    # vel: velocity XYZ (km/s) (ECI or EFG) (in-Double[3])
    # extArr: extra array - future use (in-Double[128])
    dllObj.ObsAddFrFields.restype = c_longlong
    dllObj.ObsAddFrFields.argtypes = [
        c_char,
        c_int,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_char,
        c_int,
        c_int,
        c_int,
        c_int,
        c_double * 3,
        c_double * 3,
        c_double * 128,
    ]

    # Works like ObsAddFrFields but designed for Matlab
    # secClass: security classification (in-Character)
    # satNum: satellite number (in-Integer)
    # senNum: sensor number (in-Integer)
    # obsTimeDs50utc: observation time in days since 1950 UTC (in-Double)
    # elOrDec: elevation or declination (deg) (in-Double)
    # azOrRA: azimuth or right-ascension (deg) (in-Double)
    # range: range (km) (in-Double)
    # rangeRate: range rate (km/s), or equinox indicator (0-3) for obs type 5/9 (in-Double)
    # elRate: elevation rate (deg/s) (in-Double)
    # azRate: azimuth rate (deg/s) (in-Double)
    # rangeAccel: range acceleration (km/s^2) (in-Double)
    # obsType: observation type (in-Character)
    # trackInd: track position indicator (3=start track ob, 4=in track ob, 5=end track ob) (in-Integer)
    # astat: association status assigned by SPADOC (in-Integer)
    # siteTag: original satellite number (in-Integer)
    # spadocTag: SPADOC-asssigned tag number (in-Integer)
    # pos: position XYZ (km) (ECI or EFG) (in-Double[3])
    # vel: velocity XYZ (km/s) (ECI or EFG) (in-Double[3])
    # extArr: extra array - future use (in-Double[128])
    # obsKey: The obsKey of the newly added observation on success, a negative value on error (out-Long)
    dllObj.ObsAddFrFieldsML.restype = None
    dllObj.ObsAddFrFieldsML.argtypes = [
        c_char,
        c_int,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_char,
        c_int,
        c_int,
        c_int,
        c_int,
        c_double * 3,
        c_double * 3,
        c_double * 128,
        c_longlong_p,
    ]

    # Adds one observation using its input data stored in an array. Depending on the observation type, some input data
    # might be unavailable and left blank
    # xa_obs: Array containing observation data, see XA_OBS_? for array arrangement (in-Double[64])
    dllObj.ObsAddFrArray.restype = c_longlong
    dllObj.ObsAddFrArray.argtypes = [c_double * 64]

    # Works like ObsAddFrArray but designed for Matlab
    # xa_obs: Array containing observation data, see XA_OBS_? for array arrangement (in-Double[64])
    # obsKey: The obsKey of the newly added observation on success, a negative value on error (out-Long)
    dllObj.ObsAddFrArrayML.restype = None
    dllObj.ObsAddFrArrayML.argtypes = [c_double * 64, c_longlong_p]

    # Retrieves all observation data in a single function call. Depending on the observation type, some input data
    # might be unavailable
    # obsKey: The unique key of the requested observation (in-Long)
    # secClass: security classification (out-Character)
    # satNum: satellite number (out-Integer)
    # senNum: sensor number (out-Integer)
    # obsTimeDs50utc: observation time in days since 1950 UTC (out-Double)
    # elOrDec: elevation or declination (deg) (out-Double)
    # azOrRA: azimuth or right-ascension (deg) (out-Double)
    # range: range (km) (out-Double)
    # rangeRate: range rate (km/s) (out-Double)
    # elRate: elevation rate (deg/s) (out-Double)
    # azRate: azimuth rate (deg/s) (out-Double)
    # rangeAccel: range acceleration (km/s^2) (out-Double)
    # obsType: observation type (out-Character)
    # trackInd: track position indicator (3=start track ob, 4=in track ob, 5=end track ob) (out-Integer)
    # astat: association status assigned by SPADOC (out-Integer)
    # siteTag: original satellite number (out-Integer)
    # spadocTag: SPADOC-asssigned tag number (out-Integer)
    # pos: position XYZ (km) (ECI or EFG) (out-Double[3])
    # vel: velocity XYZ (km/s) (ECI or EFG) (out-Double[3])
    # extArr: extra array - future use (out-Double[128])
    dllObj.ObsGetAllFields.restype = c_int
    dllObj.ObsGetAllFields.argtypes = [
        c_longlong,
        c_char_p,
        c_int_p,
        c_int_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_char_p,
        c_int_p,
        c_int_p,
        c_int_p,
        c_int_p,
        c_double * 3,
        c_double * 3,
        c_double * 128,
    ]

    # Retrieves observation data and stored it in the passing array. Depending on the observation type, some data
    # fields might be unavailable
    # See ObsGetField for description of xa_obs elements
    # obsKey: The unique key of the requested observation (in-Long)
    # xa_obs: The array containing observation data, see XA_OBS_? for array arrangement (out-Double[64])
    dllObj.ObsDataToArray.restype = c_int
    dllObj.ObsDataToArray.argtypes = [c_longlong, c_double * 64]

    # Updates existing observation data with the provided new data
    # obsKey: The unique key of the requested observation (in-Long)
    # secClass: security classification (in-Character)
    # elOrDec: elevation or declination (deg) (in-Double)
    # azOrRA: azimuth or right-ascension (deg) (in-Double)
    # range: range (km) (in-Double)
    # rangeRate: range rate (km/s), or equinox indicator (0-3) for obs type 5/9 (in-Double)
    # elRate: elevation rate (deg/s) (in-Double)
    # azRate: azimuth rate (deg/s) (in-Double)
    # rangeAccel: range acceleration (km/s^2) (in-Double)
    # obsType: observation type (in-Character)
    # trackInd: track position indicator (3=start track ob, 4=in track ob, 5=end track obs) (in-Integer)
    # astat: association status assigned by SPADOC (in-Integer)
    # siteTag: original satellite number (in-Integer)
    # spadocTag: SPADOC-asssigned tag number (in-Integer)
    # pos: position XYZ (km) (ECI or EFG) (in-Double[3])
    # vel: velocity XYZ (km/s) (ECI or EFG) (in-Double[3])
    # extArr: extra array - future use (in-Double[128])
    dllObj.ObsUpdateFrFields.restype = c_int
    dllObj.ObsUpdateFrFields.argtypes = [
        c_longlong,
        c_char,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_char,
        c_int,
        c_int,
        c_int,
        c_int,
        c_double * 3,
        c_double * 3,
        c_double * 128,
    ]

    # Retrieves the value of a specific field of an observation
    # obsKey: The observation's unique key (in-Long)
    # xf_Obs: The predefined number specifying which field to retrieve, see XF_OBS_? for field
    # specification (in-Integer)
    # strValue: A string to contain the value of the requested field (out-Character[512])
    dllObj.ObsGetField.restype = c_int
    dllObj.ObsGetField.argtypes = [c_longlong, c_int, c_char_p]

    # Updates the value of a field of an observation
    # See ObsGetField for a description of the xf_Obs parameter.
    # Satellite number, sensor number, and observation time are not allowed to be updated.
    # obsKey: The observation's unique key (in-Long)
    # xf_Obs: The predefined number specifying which field to update, see XF_OBS_? for field specification (in-Integer)
    # strValue: The new value of the specified field, expressed as a string (in-Character[512])
    dllObj.ObsSetField.restype = c_int
    dllObj.ObsSetField.argtypes = [c_longlong, c_int, c_char_p]

    # Returns observation in B3-card string
    # obsKey: The observation's unique key (in-Long)
    # b3Card: A string to hold the B3 observation format (out-Character[512])
    dllObj.ObsGetB3Card.restype = c_int
    dllObj.ObsGetB3Card.argtypes = [c_longlong, c_char_p]

    # Returns observation in TTY-card string
    # obsKey: The observation's unique key (in-Long)
    # ttyCard1: first line of a TTY card (out-Character[512])
    # ttyCard2: second line of a TTY card (might be unavailable for certain obs type) (out-Character[512])
    dllObj.ObsGetTTYCard.restype = c_int
    dllObj.ObsGetTTYCard.argtypes = [c_longlong, c_char_p, c_char_p]

    # Returns observation in CSV-format string
    # obsKey: The observation's unique key (in-Long)
    # csvline: A string to hold the CSV observation format (out-Character[512])
    dllObj.ObsGetCsv.restype = c_int
    dllObj.ObsGetCsv.argtypes = [c_longlong, c_char_p]

    # Constructs a B3-card string from the input observation data fields
    # secClass: security classification (in-Character)
    # satNum: satellite number (in-Integer)
    # senNum: sensor number (in-Integer)
    # obsTimeDs50utc: observation time in days since 1950 UTC (in-Double)
    # elOrDec: elevation or declination (deg) (in-Double)
    # azOrRA: azimuth or right-ascension (deg) (in-Double)
    # range: range (km) (in-Double)
    # rangeRate: range rate (km/s), or equinox indicator (0-3) for obs type 5/9 (in-Double)
    # elRate: elevation rate (deg/s) (in-Double)
    # azRate: azimuth rate (deg/s) (in-Double)
    # rangeAccel: range acceleration (km/s^2) (in-Double)
    # obsType: observation type (in-Character)
    # trackInd: track position indicator (3=start track ob, 4=in track ob, 5=end track ob) (in-Integer)
    # astat: association status assigned by SPADOC (in-Integer)
    # siteTag: original satellite number (in-Integer)
    # spadocTag: SPADOC-asssigned tag number (in-Integer)
    # pos: position XYZ (km) (ECI or EFG) (in-Double[3])
    # b3Card: A string to hold the B3 observation format (out-Character[512])
    dllObj.ObsFieldsToB3Card.restype = None
    dllObj.ObsFieldsToB3Card.argtypes = [
        c_char,
        c_int,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_char,
        c_int,
        c_int,
        c_int,
        c_int,
        c_double * 3,
        c_char_p,
    ]

    # Constructs a csv string from the input observation data fields
    # secClass: security classification (in-Character)
    # satNum: satellite number (in-Integer)
    # senNum: sensor number (in-Integer)
    # obsTimeDs50utc: observation time in days since 1950 UTC (in-Double)
    # elOrDec: elevation or declination (deg) (in-Double)
    # azOrRA: azimuth or right-ascension (deg) (in-Double)
    # range: range (km) (in-Double)
    # rangeRate: range rate (km/s), or equinox indicator (0-3) for obs type 5/9 (in-Double)
    # elRate: elevation rate (deg/s) (in-Double)
    # azRate: azimuth rate (deg/s) (in-Double)
    # rangeAccel: range acceleration (km/s^2) (in-Double)
    # obsType: observation type (in-Character)
    # trackInd: track position indicator (3=start track ob, 4=in track ob, 5=end track ob) (in-Integer)
    # astat: association status assigned by SPADOC (in-Integer)
    # siteTag: original satellite number (in-Integer)
    # spadocTag: SPADOC-asssigned tag number (in-Integer)
    # pos: position XYZ (km) (ECI or EFG) (in-Double[3])
    # csvLine: A string to hold the csv observation format (out-Character[512])
    dllObj.ObsFieldsToCsv.restype = None
    dllObj.ObsFieldsToCsv.argtypes = [
        c_char,
        c_int,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_char,
        c_int,
        c_int,
        c_int,
        c_int,
        c_double * 3,
        c_char_p,
    ]

    # Constructs a TTY-card string from the input observation data fields
    # secClass: security classification (in-Character)
    # satNum: satellite number (in-Integer)
    # senNum: sensor number (in-Integer)
    # obsTimeDs50utc: observation time in days since 1950 UTC (in-Double)
    # elOrDec: elevation or declination (deg) (in-Double)
    # azOrRA: azimuth or right-ascension (deg) (in-Double)
    # range: range (km) (in-Double)
    # rangeRate: range rate (km/s), or equinox indicator (0-3) for obs type 5/9 (in-Double)
    # elRate: elevation rate (deg/s) (in-Double)
    # azRate: azimuth rate (deg/s) (in-Double)
    # rangeAccel: range acceleration (km/s^2) (in-Double)
    # obsType: observation type (in-Character)
    # pos: position XYZ (km) (ECI or EFG) (in-Double[3])
    # ttyCard1: first line of a TTY card (out-Character[512])
    # ttyCard2: second line of a TTY card (might be unavailable for certain obs type) (out-Character[512])
    dllObj.ObsFieldsToTTYCard.restype = None
    dllObj.ObsFieldsToTTYCard.argtypes = [
        c_char,
        c_int,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_char,
        c_double * 3,
        c_char_p,
        c_char_p,
    ]

    # Computes an obsKey from individually provided fields
    # satNum: input satellite's number (in-Integer)
    # senNum: input sensor's number (in-Integer)
    # obsTimeDs50utc: input observation time in days since 1950, UTC (in-Double)
    dllObj.ObsFieldsToObsKey.restype = c_longlong
    dllObj.ObsFieldsToObsKey.argtypes = [c_int, c_int, c_double]

    # Works like ObsFieldsToObsKey but designed for Matlab
    # satNum: input satellite's number (in-Integer)
    # senNum: input sensor's number (in-Integer)
    # obsTimeDs50utc: input observation time in days since 1950, UTC (in-Double)
    # obsKey: The newly created observation Key (out-Long)
    dllObj.ObsFieldsToObsKeyML.restype = None
    dllObj.ObsFieldsToObsKeyML.argtypes = [c_int, c_int, c_double, c_longlong_p]

    # Parses observation data from a B3-card (or B3E) string / one-line TTY / or CSV - Converts obs data to TEME of
    # Date if neccessary
    # b3ObsCard: input B3 observation string (in-Character[512])
    # secClass: security classification (out-Character)
    # satNum: satellite number (out-Integer)
    # senNum: sensor number (out-Integer)
    # obsTimeDs50utc: observation time in days since 1950 UTC (out-Double)
    # elOrDec: elevation or declination (deg) (out-Double)
    # azOrRA: azimuth or right-ascension (deg) (out-Double)
    # range: range (km) (out-Double)
    # rangeRate: range rate (km/s) (out-Double)
    # elRate: elevation rate (deg/s) (out-Double)
    # azRate: azimuth rate (deg/s) (out-Double)
    # rangeAccel: range acceleration (km/s^2) (out-Double)
    # obsType: observation type (out-Character)
    # trackInd: track position indicator (3=start track ob, 4=in track ob, 5=end track ob) (out-Integer)
    # astat: association status assigned by SPADOC (out-Integer)
    # siteTag: original satellite number (out-Integer)
    # spadocTag: SPADOC-asssigned tag number (out-Integer)
    # pos: position XYZ (km) (ECI or EFG) (out-Double[3])
    dllObj.ObsB3Parse.restype = c_int
    dllObj.ObsB3Parse.argtypes = [
        c_char_p,
        c_char_p,
        c_int_p,
        c_int_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_char_p,
        c_int_p,
        c_int_p,
        c_int_p,
        c_int_p,
        c_double * 3,
    ]

    # Parses any observation data format (B3-card (or B3E) string / one or two line TTY / CSV - No conversion takes
    # place
    # line1: input observation string 1 (B3/B3E/line 1 TTY/CSV) (in-Character[512])
    # line2: input observation string 2 (line 2 of two-line TTY) (in-Character[512])
    # xa_obs: The array containing observation data, see XA_OBS_? for array arrangement (out-Double[64])
    dllObj.ObsParse.restype = c_int
    dllObj.ObsParse.argtypes = [c_char_p, c_char_p, c_double * 64]

    # Loads observation data from an input text file and group them together in the specified groupd id (gid).
    # This allows the users to easily manage (load/retrieve/remove/save) a group of observations using the group
    # id (gid)
    # obsFile: The name of the file containing obs-related data (in-Character[512])
    # gid: user specified group id (in-Integer)
    dllObj.ObsLoadFileGID.restype = c_int
    dllObj.ObsLoadFileGID.argtypes = [c_char_p, c_int]

    # Saves the currently loaded obs data belong to the specified group id (gid) to a file
    # obsFile: The name of the file in which to save the settings (in-Character[512])
    # gid: Group ID number (in-Integer)
    # saveMode: Specifies whether to create a new file or append to an existing one (0 = create, 1= append) (in-Integer)
    # obsForm: Specifies the obs format in which to save the file (0 = B3 format, 1 = TTY, 2 = CSV) (in-Integer)
    dllObj.ObsSaveFileGID.restype = c_int
    dllObj.ObsSaveFileGID.argtypes = [c_char_p, c_int, c_int, c_int]

    # Removes all observations belong to the specified group id (gid) from the set of currently loaded observations
    # gid: Group ID number (in-Integer)
    dllObj.ObsRemoveGID.restype = c_int
    dllObj.ObsRemoveGID.argtypes = [c_int]

    # Returns the number of observations currently loaded that have the same gid
    # gid: Group ID number (in-Integer)
    dllObj.ObsGetCountGID.restype = c_int
    dllObj.ObsGetCountGID.argtypes = [c_int]

    # Retrieves all of the currently loaded obsKeys that have the same gid. These obsKeys can be used to access the
    # internal data for the observations
    # Sort options (order):
    # (+/-)1 = (descending/ascending) time, sensor, obsType, elev
    # (+/-)2 = (descending/ascending) time, elevation
    # (+/-)3 = (descending/ascending) time, sensor, otype, el, satno
    # (+/-)4 = (descending/ascending) sensor, satno, time, elev
    # (+/-)5 = (descending/ascending) sensor, time, elevation
    # (+/-)6 = (descending/ascending) sensor, satno, obsType, time, elev
    # (+/-)7 = (descending/ascending) satno, time, sensor, otype, el
    # (+/-)8 = (reversed/same)        order as obs were read
    # 9 : as is in the tree
    # gid: Group ID number (in-Integer)
    # order: Specifies the order in which the obsKeys should be returned (in-Integer)
    # obsKeys: The array in which to store the obsKeys (out-Long[*])
    dllObj.ObsGetLoadedGID.restype = None
    dllObj.ObsGetLoadedGID.argtypes = [c_int, c_int, c_void_p]

    # Converts obs type from character to integer
    # obsTypeChar: The input obs type character (in-Character)
    dllObj.ObsTypeCToI.restype = c_int
    dllObj.ObsTypeCToI.argtypes = [c_char]

    # Converts obs type from integer to character
    # obsTypeInt: The input obs type integer (in-Integer)
    dllObj.ObsTypeIToC.restype = c_char
    dllObj.ObsTypeIToC.argtypes = [c_int]

    # Resets obs selection settings
    dllObj.ObsResetSelObs.restype = None
    dllObj.ObsResetSelObs.argtypes = []

    # Computes other states of the input observation
    #
    # The table below indicates which index values correspond to which fields in the xa_obState array.
    #
    # table
    #
    # Index
    # Index Interpretation
    #
    # 0Satellite number
    # 1Sensor number
    # 2Observation time in DS50UTC
    # 10Position X/ECI (km)
    # 11Position Y/ECI (km)
    # 12Position Z/ECI (km)
    # 13Velocity X/ECI (km/s)
    # 14Velocity Y/ECI (km/s)
    # 15Velocity Z/ECI (km/s)
    # 16Geodetic latitude (deg)
    # 17Geodetic longitude (deg)
    # 18Geodetic height (km)
    # 19Position X/EFG (km)
    # 20Position Y/EFG (km)
    # 21Position Z/EFG (km)
    #
    # obsKey: The observation's unique key (in-Long)
    # range_km: Use this default range (km) for angle only obs (in-Double)
    # xa_obState: Data derived from the obs data.  see XA_OBSTATE_? (out-Double[64])
    dllObj.ObsGetStates.restype = c_int
    dllObj.ObsGetStates.argtypes = [c_longlong, c_double, c_double * 64]

    # Computes observation states from the observation data
    # See ObsGetStates for a list of the values for the xa_obState parameter.
    # xa_obs: Array containing observation data, see XA_OBS_? for array arrangement (in-Double[64])
    # xa_obState: Data derived from the obs data.  see XA_OBSTATE_? (out-Double[64])
    dllObj.ObsDataToStates.restype = c_int
    dllObj.ObsDataToStates.argtypes = [c_double * 64, c_double * 64]

    # Reconstructs obs string (B3-card/one or two line TTY/CSV) from obs data in the input array xa_obs
    # xa_obs: The array containing observation data, see XA_OBS_? for array arrangement (in-Double[64])
    # obsForm: Desired obs string format (B3 = 0, TTY=1, CSV=2) (in-Integer)
    # line1: output observation string 1 (B3/B3E/line 1 TTY/CSV) (out-Character[512])
    # line2: output observation string 2 (line 2 of two-line TTY if obsForm = 1) (out-Character[512])
    dllObj.ObsArrToLines.restype = c_int
    dllObj.ObsArrToLines.argtypes = [c_double * 64, c_int, c_char_p, c_char_p]

    # Sets OBS key mode
    # This mode can also be turned on if the user loads an input text file that includes this line - "AS_DMA_OBS_ON" -
    # and is currently calling any of these methods: DllMainLoadFile(), or ObsLoadFile()
    # obs_keyMode: Desired obs key mode (see OBS_KEYMODE_? for available modes) (in-Integer)
    dllObj.SetObsKeyMode.restype = c_int
    dllObj.SetObsKeyMode.argtypes = [c_int]

    # Gets current OBS key mode
    dllObj.GetObsKeyMode.restype = c_int
    dllObj.GetObsKeyMode.argtypes = []

    # Returs the satellite number associated with the input obsKey
    # obsKey: The observation's unique key (in-Long)
    dllObj.SatNumFrObsKey.restype = c_int
    dllObj.SatNumFrObsKey.argtypes = [c_longlong]

    # Returs the sensor number associated with the input obsKey
    # obsKey: The observation's unique key (in-Long)
    dllObj.SenNumFrObsKey.restype = c_int
    dllObj.SenNumFrObsKey.argtypes = [c_longlong]

    # Retrieves only obs that match the selection criteria
    # xa_selob: Obs secletion criteria, see XA_SELOB_? for array arrangement (in-Double[128])
    # order: Specifies the order in which the obsKeys should be returned (in-Integer)
    # numMatchedObss: Number of obs that match the obs selection criteria (out-Integer)
    # obsKeys: The array in which to store the matching obs' obsKey - make sure the array is big enough to store all
    # the returning obsKeys (<= ObsGetCount()) (out-Long[*])
    dllObj.ObsGetSelected.restype = None
    dllObj.ObsGetSelected.argtypes = [c_double * 128, c_int, c_int_p, c_void_p]

    return dllObj


# Equinox indicator
# time of observation
EQUINOX_OBSTIME = 0
# time @ 0 Jan Year of Date
EQUINOX_OBSYEAR = 1
# J2000
EQUINOX_J2K = 2
# B1950
EQUINOX_B1950 = 3

# Indexes for sorting ob
# Sort options:
# (+/-) 1 = (descending/ascending) time, sensor, obsType, elev
# (+/-) 2 = (descending/ascending) time, elevation
# (+/-) 3 = (descending/ascending) time, sensor, otype, el, satno
# (+/-) 4 = (descending/ascending) sensor, satno, time, elev
# (+/-) 5 = (descending/ascending) sensor, time, elevation
# (+/-) 6 = (descending/ascending) sensor, satno, obsType, time, elev
# (+/-) 7 = (descending/ascending) satno, time, sensor, otype, el
# (+/-)10 = (descending/ascending) satno, sensor, time

# sort order is time, sensor, obsType, elev (negative value for reverse order)
SORT_TIMESENTYPEEL = 1
# sort order is time, elevation (negative value for reverse order)
SORT_TIMEEL = 2
# sort order is time, sensor, otype, el, satno (negative value for reverse order)
SORT_TIMESENTYPEELSAT = 3
# sort order is sensor, satno, time, elev (negative value for reverse order)
SORT_SENSATTIMEEL = 4
# sort order is sensor, time, elevation (negative value for reverse order)
SORT_SENTIMEEL = 5
# sort order is sensor, satno, obsType, time, elev (negative value for reverse order)
SORT_SENSATTYPETIMEEL = 6
# sort order is satno, time, sensor, otype, el (negative value for reverse order)
SORT_SATTIMESENTYPEEL = 7
# sort order is the order of obs when they were loaded
SORT_ORDERASREAD = 8
# sort order is satno, sensor, time (negative value for reverse order)
SORT_SATSENTIME = 10


# Indexes of different obs file format
# B3 obs format
OBSFORM_B3 = 0
# Transmission obs format
OBSFORM_TTY = 1
# CSV obs format
OBSFORM_CSV = 2
# Radio Frequency (TDOA/FDOA) observations
OBSFORM_RF = 3

BADOBSKEY = -1
DUPOBSKEY = 0


# Different key mode options for obsKey
# Default - duplicate obs can not be loaded in binary tree
OBS_KEYMODE_NODUP = 0
# Allow duplicate obs to be loaded and have direct memory access (DMA - no duplication check and no binary tree)
OBS_KEYMODE_DMA = 1

# CSV sigma type indicator
CSVSIGMATYPE = 7

# Indexes of Observation data fields
# security classification
XF_OBS_SECCLASS = 1
# satellite number
XF_OBS_SATNUM = 2
# sensor number
XF_OBS_SENNUM = 3
# observation time in days since 1950 UTC
XF_OBS_DS50UTC = 4
# elevation (deg)
XF_OBS_ELEVATION = 5
# declination (deg)
XF_OBS_DECLINATION = 6
# azimuth (deg)
XF_OBS_AZIMUTH = 7
# right-ascension (deg)
XF_OBS_RA = 8
# range (km)
XF_OBS_RANGE = 9
# range rate (km/s)
XF_OBS_RANGERATE = 10
# elevation rate (deg/s)
XF_OBS_ELRATE = 11
# azimuth rate (deg/s)
XF_OBS_AZRATE = 12
# range acceleration (km/s^2)
XF_OBS_RANGEACCEL = 13
# observation type
XF_OBS_OBSTYPE = 14
# track position indicator (3=start track ob, 4=in track ob, 5=end track ob)
XF_OBS_TRACKIND = 15
# association status assigned by SPADOC
XF_OBS_ASTAT = 16
# original satellite number
XF_OBS_SITETAG = 17
# SPADOC-asssigned tag number
XF_OBS_SPADOCTAG = 18
# position X/EFG (km)
XF_OBS_POSE = 19
# position Y/EFG (km)
XF_OBS_POSF = 20
# position Z/EFG (km)
XF_OBS_POSG = 21
# position X/ECI (km)
XF_OBS_POSX = 22
# position Y/ECI (km)
XF_OBS_POSY = 23
# position Z/ECI (km)
XF_OBS_POSZ = 24

# Principal Polarization RCS
XF_OBS_RCS_PP = 25
# Orthogonal Polarization RCS
XF_OBS_RCS_OP = 26
# Principal Polarization RCS sigma
XF_OBS_RCS_PPS = 27
# Orthogonal Polarization RCS sigma
XF_OBS_RCS_OPS = 28
# Radar Signal to Noise Ratio
XF_OBS_SNR = 29
# Azimuth of Boresite
XF_OBS_BORE_AZ = 30
# Elevation of Boresite
XF_OBS_BORE_EL = 31
# Apparent Visual magnitude
XF_OBS_VISMAG = 32
# GEO Normalized Visual magnitude
XF_OBS_VISMAG_NORM = 33
# Solar Phase Angle
XF_OBS_SOL_PHASE = 34
# Frame Number
XF_OBS_FRAME = 35
# Aberration correction indicator (0=YES, 1=NO)
XF_OBS_ABERRATION = 36
# Either R" or T; ROTAS=General Perturbations, TRACK=Special Perturbations
XF_OBS_ASTAT_METHOD = 37

# Indexes of observation data in an array
# security classification, 1 = Unclassified, 2 = Confidential, 3 = Secret
XA_OBS_SECCLASS = 0
# satellite number
XA_OBS_SATNUM = 1
# sensor number
XA_OBS_SENNUM = 2
# observation time in days since 1950 UTC
XA_OBS_DS50UTC = 3
# observation type
XA_OBS_OBSTYPE = 11


# elevation (for ob type 1, 2, 3, 4, 8) or declination (for ob type 5, 9) (deg)
XA_OBS_ELORDEC = 4
# azimuth (for ob type 1, 2, 3, 4, 8) or right ascesion (for ob type 5, 9) (deg)
XA_OBS_AZORRA = 5
# range (km)
XA_OBS_RANGE = 6
# range rate (km/s) for non-optical obs type
XA_OBS_RANGERATE = 7
# elevation rate (deg/s)
XA_OBS_ELRATE = 8
# azimuth rate (deg/s)
XA_OBS_AZRATE = 9
# range acceleration (km/s^2)
XA_OBS_RANGEACCEL = 10
# track position indicator (3=start track ob, 4=in track ob, 5=end track ob)
XA_OBS_TRACKIND = 12
# association status assigned by SPADOC
XA_OBS_ASTAT = 13
# original satellite number
XA_OBS_SITETAG = 14
# SPADOC-asssigned tag number
XA_OBS_SPADOCTAG = 15
# position X/ECI or X/EFG (km)
XA_OBS_POSX = 16
# position Y/ECI or Y/EFG (km)
XA_OBS_POSY = 17
# position Z/ECI or Z/EFG (km)
XA_OBS_POSZ = 18
# velocity X/ECI (km/s)  (or Edot/EFG (km) for ob type 7 TTY)
XA_OBS_VELX = 19
# velocity Y/ECI (km/s)  (or Fdot/EFG (km) for ob type 7 TTY)
XA_OBS_VELY = 20
# velocity Z/ECI (km/s)  (or Gdot/EFG (km) for ob type 7 TTY)
XA_OBS_VELZ = 21
# year of equinox indicator for obs type 5/9 (0= Time of obs, 1= 0 Jan of date, 2= J2000, 3= B1950)
XA_OBS_YROFEQNX = 22
# aberration indicator, 0-not corrected, 1-corrceted
XA_OBS_ABERRATION = 23

# AZ/RA bias (deg)
XA_OBS_AZORRABIAS = 33
# EL/DEC bias (deg)
XA_OBS_ELORDECBIAS = 34
# Range bias (km)
XA_OBS_RGBIAS = 35
# Range-rate bias (km/sec)
XA_OBS_RRBIAS = 36
# Time bias (sec)
XA_OBS_TIMEBIAS = 37
# AZ/RA rate bias (deg/sec)
XA_OBS_RAZORRABIAS = 38
# EL/DEC rate bias (deg/sec)
XA_OBS_RELORDECBIAS = 39

# individual obs's sigmas type (0: N/A, 6: 6 elements, 21: 21 elements, 7: this is CSV obs)
XA_OBS_SIGMATYPE = 40
# sigma - covariance element 1 - 6 elemens - Az sigma
XA_OBS_SIGMAEL1 = 41
# sigma - covariance element 2 - 6 elemens - El sigma
XA_OBS_SIGMAEL2 = 42
# sigma - covariance element 3 - 6 elemens - Range sigma
XA_OBS_SIGMAEL3 = 43
# sigma - covariance element 4 - 6 elemens - Range rate sigma
XA_OBS_SIGMAEL4 = 44
# sigma - covariance element 5 - 6 elemens - Az rate sigma
XA_OBS_SIGMAEL5 = 45
# sigma - covariance element 6 - 6 elemens - El rate sigma
XA_OBS_SIGMAEL6 = 46
# sigma - covariance element 7
XA_OBS_SIGMAEL7 = 47
# sigma - covariance element 8
XA_OBS_SIGMAEL8 = 48
# sigma - covariance element 9
XA_OBS_SIGMAEL9 = 49
# sigma - covariance element 10
XA_OBS_SIGMAEL10 = 50
# sigma - covariance element 11
XA_OBS_SIGMAEL11 = 51
# sigma - covariance element 12
XA_OBS_SIGMAEL12 = 52
# sigma - covariance element 13
XA_OBS_SIGMAEL13 = 53
# sigma - covariance element 14
XA_OBS_SIGMAEL14 = 54
# sigma - covariance element 15
XA_OBS_SIGMAEL15 = 55
# sigma - covariance element 16
XA_OBS_SIGMAEL16 = 56
# sigma - covariance element 17
XA_OBS_SIGMAEL17 = 57
# sigma - covariance element 18
XA_OBS_SIGMAEL18 = 58
# sigma - covariance element 19
XA_OBS_SIGMAEL19 = 59
# sigma - covariance element 20
XA_OBS_SIGMAEL20 = 60
# sigma - covariance element 21
XA_OBS_SIGMAEL21 = 61

XA_OBS_SIZE = 64

# Indexes of observation data in an array (Obs Type CSV specific)
# security classification, 1 = Unclassified, 2 = Confidential, 3 = Secret
XA_OTCSV_SECCLASS = 0
# satellite number
XA_OTCSV_SATNUM = 1
# sensor number
XA_OTCSV_SENNUM = 2
# observation time in days since 1950 UTC
XA_OTCSV_DS50UTC = 3
# elevation (for ob type 1, 2, 3, 4, 8) or declination (for ob type 5, 9) (deg)
XA_OTCSV_ELORDEC = 4
# azimuth (for ob type 1, 2, 3, 4, 8) or right ascesion (for ob type 5, 9) (deg)
XA_OTCSV_AZORRA = 5
# range (km)
XA_OTCSV_RANGE = 6
# range rate (km/s) for non-optical obs type
XA_OTCSV_RANGERATE = 7
# elevation rate (deg/s)
XA_OTCSV_ELRATE = 8
# azimuth rate (deg/s)
XA_OTCSV_AZRATE = 9
# range acceleration (km/s^2)
XA_OTCSV_RANGEACCEL = 10
# observation type
XA_OTCSV_OBSTYPE = 11
# track position indicator (3=start track ob, 4=in track ob, 5=end track ob)
XA_OTCSV_TRACKIND = 12
# association status assigned by SPADOC
XA_OTCSV_ASTAT = 13
# original satellite number
XA_OTCSV_SITETAG = 14
# SPADOC-asssigned tag number
XA_OTCSV_SPADOCTAG = 15
# position X/ECI or X/EFG (km)
XA_OTCSV_POSX = 16
# position Y/ECI or Y/EFG (km)
XA_OTCSV_POSY = 17
# position Z/ECI or Z/EFG (km)
XA_OTCSV_POSZ = 18
# velocity X/ECI (km/s)  (or Edot/EFG (km) for ob type 7 TTY)
XA_OTCSV_VELX = 19
# velocity Y/ECI (km/s)  (or Fdot/EFG (km) for ob type 7 TTY)
XA_OTCSV_VELY = 20
# velocity Z/ECI (km/s)  (or Gdot/EFG (km) for ob type 7 TTY)
XA_OTCSV_VELZ = 21
# year of equinox indicator for obs type 5/9 (0= Time of obs, 1= 0 Jan of date, 2= J2000, 3= B1950)
XA_OTCSV_YROFEQNX = 22

# Principal Polarization RCS
XA_OTCSV_RCS_PP = 23
# Orthogonal Polarization RCS
XA_OTCSV_RCS_OP = 24
# Principal Polarization RCS sigma
XA_OTCSV_RCS_PPS = 25
# Orthogonal Polarization RCS sigma
XA_OTCSV_RCS_OPS = 26
# Radar Signal to Noise Ratio
XA_OTCSV_SNR = 27
# Azimuth of Boresite
XA_OTCSV_BORE_AZ = 28
# Elevation of Boresite
XA_OTCSV_BORE_EL = 29
# Apparent Visual magnitude
XA_OTCSV_VISMAG = 30
# GEO Normalized Visual magnitude
XA_OTCSV_VISMAG_NORM = 31
# Solar Phase Angle
XA_OTCSV_SOL_PHASE = 32
# Frame Number
XA_OTCSV_FRAME = 33
# Aberration correction indicator (0=YES, 1=NO)
XA_OTCSV_ABERRATION = 34
# 0 = ROTAS, 1 = TRACK
XA_OTCSV_ASTAT_METHOD = 35

# must equal to 7 to signify this is CSV format
XA_OTCSV_SIGMATYPE = 40
# sigma - covariance element 1 - Az sigma
XA_OTCSV_SIGMAEL1 = 41
# sigma - covariance element 2 - El sigma
XA_OTCSV_SIGMAEL2 = 42
# sigma - covariance element 3 - Range sigma
XA_OTCSV_SIGMAEL3 = 43
# sigma - covariance element 4 - Range rate sigma
XA_OTCSV_SIGMAEL4 = 44
# sigma - covariance element 5 - Az rate sigma
XA_OTCSV_SIGMAEL5 = 45
# sigma - covariance element 6 - El rate sigma
XA_OTCSV_SIGMAEL6 = 46
# sigma - covariance element 7 - Time sigma
XA_OTCSV_SIGMAEL7 = 47
# AZ/RA bias
XA_OTCSV_BIAS1 = 48
# EL/DEC bias
XA_OTCSV_BIAS2 = 49
# Range bias
XA_OTCSV_BIAS3 = 50
# Range-rate bias
XA_OTCSV_BIAS4 = 51
# Time bias
XA_OTCSV_BIAS5 = 52


XA_OTCSV_SIZE = 64

# Indexes of observation data in an array
# satellite number
XA_OBSTATE_SATNUM = 0
# sensor number
XA_OBSTATE_SENNUM = 1
# observation time in days since 1950 UTC
XA_OBSTATE_DS50UTC = 2

# position X/ECI (km)
XA_OBSTATE_POSX = 10
# position Y/ECI (km)
XA_OBSTATE_POSY = 11
# position Z/ECI (km)
XA_OBSTATE_POSZ = 12
# velocity X/ECI (km/s)
XA_OBSTATE_VELX = 13
# velocity Y/ECI (km/s)
XA_OBSTATE_VELY = 14
# velocity Z/ECI (km/s)
XA_OBSTATE_VELZ = 15
# geodetic latitude (deg)
XA_OBSTATE_LAT = 16
# geodetic longitude (deg)
XA_OBSTATE_LON = 17
# geodetic height (km)
XA_OBSTATE_HGHT = 18
# position X/EFG (km)
XA_OBSTATE_POSE = 19
# position Y/EFG (km)
XA_OBSTATE_POSF = 20
# position Z/EFG (km)
XA_OBSTATE_POSG = 21


XA_OBSTATE_SIZE = 64

# Indexes of observation data available for each obs type (OT0: obs type 0, OT1: obs type 1, ...)
# All obs types have these common data fields  XA_OBS_SECCLASS = 0, XA_OBS_SATNUM = 1, XA_OBS_SENNUM = 2,
# XA_OBS_DS50UTC = 3, and XA_OBS_OBSTYPE = 11
# range rate (km/s)
XA_OT0_RANGERATE = 7

# elevation (deg)
XA_OT1_ELEVATION = 4
# azimuth (deg)
XA_OT1_AZIMUTH = 5

# elevation (deg)
XA_OT2_ELEVATION = 4
# azimuth (deg)
XA_OT2_AZIMUTH = 5
# range (km)
XA_OT2_RANGE = 6

# elevation (deg)
XA_OT3_ELEVATION = 4
# azimuth (deg)
XA_OT3_AZIMUTH = 5
# range (km)
XA_OT3_RANGE = 6
# range rate (km/s)
XA_OT3_RANGERATE = 7

# elevation (deg)
XA_OT4_ELEVATION = 4
# azimuth (deg)
XA_OT4_AZIMUTH = 5
# range (km)
XA_OT4_RANGE = 6
# range rate (km/s)
XA_OT4_RANGERATE = 7
# elevation rate (deg/s)
XA_OT4_ELRATE = 8
# azimuth rate (deg/s)
XA_OT4_AZRATE = 9
# range acceleration (km/s^2)
XA_OT4_RANGEACCEL = 10

# declination (deg)
XA_OT5_DECL = 4
# right ascesion (deg)
XA_OT5_RIGHTASC = 5
# year of equinox indicator (0= Time of obs, 1= 0 Jan of date, 2= J2000, 3= B1950)
XA_OT5_YROFEQNX = 22
# ABERRATION INDICATOR, 0-NOT CORRECTED, 1-CORRCETED
XA_OT5_ABERRATION = 23

# range (km)
XA_OT6_RANGE = 6

# elevation (deg)
XA_OT8_ELEVATION = 4
# azimuth (deg)
XA_OT8_AZIMUTH = 5
# optional - range (km)
XA_OT8_RANGE = 6
# orbiting sensor position X/EFG (km)
XA_OT8_POSE = 16
# orbiting sensor position Y/EFG (km)
XA_OT8_POSF = 17
# orbiting sensor position Z/EFG (km)
XA_OT8_POSG = 18

# declination (deg)
XA_OT9_DECL = 4
# right ascesion (deg)
XA_OT9_RIGHTASC = 5
# optional - range (km)
XA_OT9_RANGE = 6
# orbiting sensor position X/EFG (km)
XA_OT9_POSE = 16
# orbiting sensor position Y/EFG (km)
XA_OT9_POSF = 17
# orbiting sensor position Z/EFG (km)
XA_OT9_POSG = 18
# year of equinox indicator (0= Time of obs, 1= 0 Jan of date, 2= J2000, 3= B1950)
XA_OT9_YROFEQNX = 22
# ABERRATION INDICATOR, 0-NOT CORRECTED, 1-CORRCETED
XA_OT9_ABERRATION = 23

# position X/ECI or X/EFG (km)
XA_OTP_POSX = 16
# position Y/ECI or Y/EFG (km)
XA_OTP_POSY = 17
# position Z/ECI or Z/EFG (km)
XA_OTP_POSZ = 18

# position X/ECI or X/EFG (km)
XA_OTV_POSX = 16
# position Y/ECI or Y/EFG (km)
XA_OTV_POSY = 17
# position Z/ECI or Z/EFG (km)
XA_OTV_POSZ = 18
# velocity X/ECI (km/s)  (or Edot/EFG (km) for ob type 7 TTY)
XA_OTV_VELX = 19
# velocity Y/ECI (km/s)  (or Fdot/EFG (km) for ob type 7 TTY)
XA_OTV_VELY = 20
# velocity Z/ECI (km/s)  (or Gdot/EFG (km) for ob type 7 TTY)
XA_OTV_VELZ = 21

XA_OT_SIZE = 64

# Obs selection criteria
# Seclection mode (unused for now)
XA_SELOB_MODE = 0

# From time
XA_SELOB_FRTIME = 1
# To time
XA_SELOB_TOTIME = 2

# From time
XA_SELOB_FRIDX = 3
# To time
XA_SELOB_TOIDX = 4

# Select any obs that match this satellite number #1
XA_SELOB_SAT1 = 11
# Select any obs that match this satellite number #2
XA_SELOB_SAT2 = 12
# Select any obs that match this satellite number #3
XA_SELOB_SAT3 = 13
# Select any obs that match this satellite number #4
XA_SELOB_SAT4 = 14
# Select any obs that match this satellite number #5
XA_SELOB_SAT5 = 15
# Select any obs that match this satellite number #6
XA_SELOB_SAT6 = 16
# Select any obs that match this satellite number #7
XA_SELOB_SAT7 = 17
# Select any obs that match this satellite number #8
XA_SELOB_SAT8 = 18
# Select any obs that match this satellite number #9
XA_SELOB_SAT9 = 19
# Select any obs that match this satellite number #10
XA_SELOB_SAT10 = 20

# Select any obs that are obtained by this sensor site #1
XA_SELOB_SEN1 = 21
# Select any obs that are obtained by this sensor site #2
XA_SELOB_SEN2 = 22
# Select any obs that are obtained by this sensor site #3
XA_SELOB_SEN3 = 23
# Select any obs that are obtained by this sensor site #4
XA_SELOB_SEN4 = 24
# Select any obs that are obtained by this sensor site #5
XA_SELOB_SEN5 = 25
# Select any obs that are obtained by this sensor site #6
XA_SELOB_SEN6 = 26
# Select any obs that are obtained by this sensor site #7
XA_SELOB_SEN7 = 27
# Select any obs that are obtained by this sensor site #8
XA_SELOB_SEN8 = 28
# Select any obs that are obtained by this sensor site #9
XA_SELOB_SEN9 = 29
# Select any obs that are obtained by this sensor site #10
XA_SELOB_SEN10 = 30

# Select any obs that match this obs type #1, use OT_RRATE_SELOB for type 0/range rate only
XA_SELOB_OT1 = 31
# Select any obs that match this obs type #2
XA_SELOB_OT2 = 32
# Select any obs that match this obs type #3
XA_SELOB_OT3 = 33
# Select any obs that match this obs type #4
XA_SELOB_OT4 = 34
# Select any obs that match this obs type #5
XA_SELOB_OT5 = 35
# Select any obs that match this obs type #6
XA_SELOB_OT6 = 36
# Select any obs that match this obs type #7
XA_SELOB_OT7 = 37
# Select any obs that match this obs type #8
XA_SELOB_OT8 = 38
# Select any obs that match this obs type #9
XA_SELOB_OT9 = 39
# Select any obs that match this obs type #10
XA_SELOB_OT10 = 40

# From azimuth
XA_SELOB_FRAZ = 41
# To azimuth
XA_SELOB_TOAZ = 42
# From elevation
XA_SELOB_FREL = 43
# To elevation
XA_SELOB_TOEL = 44
# From right ascension
XA_SELOB_FRRA = 45
# To right ascension
XA_SELOB_TORA = 46
# From declincation
XA_SELOB_FRDEC = 47
# To declination
XA_SELOB_TODEC = 48
# From range
XA_SELOB_FRRNG = 49
# To range
XA_SELOB_TORNG = 50
# From range rate
XA_SELOB_FRRNGRT = 51
# To range rate
XA_SELOB_TORNGRT = 52
# From azimuth rate
XA_SELOB_FRAZRT = 53
# To azimuth rate
XA_SELOB_TOAZRT = 54
# From elevation rate
XA_SELOB_FRELRT = 55
# To elevation rate
XA_SELOB_TOELRT = 56
# From ASTAT (0 to 4)
XA_SELOB_FRASTAT = 57
# To ASTAT (0 to 4) (0 < val < 1.0 if want to retrieve ASTAT 0)
XA_SELOB_TOASTAT = 58

XA_SELOB_SIZE = 128


# ========================= End of auto generated code ==========================
