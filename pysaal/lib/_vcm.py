# This wrapper file was generated automatically by the GenDllWrappers program.
import platform
from ctypes import CDLL, POINTER, c_char_p, c_double, c_int, c_longlong, c_void_p
from pathlib import Path

c_double_p = POINTER(c_double)
c_int_p = POINTER(c_int)
c_longlong_p = POINTER(c_longlong)

LIB_PATH = Path(__file__).parent

# get the right filename of the dll/so
if platform.uname()[0] == "Windows":
    DLL_NAME = LIB_PATH / "Vcm.dll"

if platform.uname()[0] == "Linux":
    DLL_NAME = LIB_PATH / "libvcm.so"

if platform.uname()[0] == "Darwin":
    DLL_NAME = LIB_PATH / "libvcm.dylib"


def get_vcm_dll():
    """LoadVcmDll() -- Loads Vcm.dll from the PATH or LD_LIBRARY_PATH
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
    # Initializes Vcm DLL for use in the program
    # If this function returns an error, it is recommended that the users stop the program immediately. The error
    # occurs if the users forget to load and initialize all the prerequisite DLLs, as listed in the DLL Prerequisites
    # section, before using this DLL.
    # apAddr: The handle that was returned from DllMainInit() (in-Long)
    dllObj.VcmInit.restype = c_int
    dllObj.VcmInit.argtypes = [c_longlong]

    # Returns information about the current version of Vcm DLL. The information is placed in the string parameter you
    # pass in
    # The returned string provides information about the version number, build date, and the platform of the Vcm DLL.
    # infoStr: A string to hold the information about Vcm.dll (out-Character[128])
    dllObj.VcmGetInfo.restype = None
    dllObj.VcmGetInfo.argtypes = [c_char_p]

    # Loads a text file containing Vcm's
    # The users can use this function repeatedly to load Vcm records from different input files. However, only unique
    # satKeys are stored in the binary tree. Duplicated satKeys won't be stored.
    #
    # State vectors can be included directly in the main input file or they can be read from a separate file identified
    # with "ELTFIL=[pathname\filename]" or "VECFIL=[path/filename]" or "SPVMSG=[path/filename]".
    #
    # This function only reads Vcm records from the main input file or Vcm records from the file identified with ELTFIL
    # or VECFIL in the input file. It won't read anything else.
    # vcmFile: The name of the file containing VCMs to be loaded (in-Character[512])
    dllObj.VcmLoadFile.restype = c_int
    dllObj.VcmLoadFile.argtypes = [c_char_p]

    # Saves the currently loaded VCM's to a file
    # If the users call this routine immediately after VcmLoadFile. The VCMs contents in the two file should be the
    # same (minus duplicated VCMs or bad VCMs).
    #
    # The purpose of this function is to save the current state of the loaded VCMs, usually used in GUI applications,
    # for future use.
    # vcmFile: The name of the file in which to save the settings (in-Character[512])
    # saveMode: Specifies whether to create a new file or append to an existing one (0 = create, 1= append) (in-Integer)
    # saveForm: Specifies the mode in which to save the file (0 = text format, 1 = not yet implemented, reserved for
    # future) (in-Integer)
    dllObj.VcmSaveFile.restype = c_int
    dllObj.VcmSaveFile.argtypes = [c_char_p, c_int, c_int]

    # Removes a VCM represented by the satKey from memory
    # If the users enter an invalid satKey - a non-existing satKey in memory, the function will return a non-zero value
    # indicating an error.
    # satKey: The unique key of the satellite to be removed (in-Long)
    dllObj.VcmRemoveSat.restype = c_int
    dllObj.VcmRemoveSat.argtypes = [c_longlong]

    # Removes all VCM's from memory
    # The function returns zero if all the satellites are removed successfully from the Vcm DLL's binary tree.
    dllObj.VcmRemoveAllSats.restype = c_int
    dllObj.VcmRemoveAllSats.argtypes = []

    # Retrieves all of the currently loaded satKeys. These satKeys can be used to access the internal data for the VCM's
    # See VcmGetLoaded for an example.
    # This function is useful for dynamically allocating memory for the array that is passed to the function
    # VcmGetLoaded().
    dllObj.VcmGetCount.restype = c_int
    dllObj.VcmGetCount.argtypes = []

    # Retrieves all of the currently loaded satKeys. These satKeys can be used to access the internal data for the VCM's
    # It is recommended that VcmGetCount() is used to count how many satellites are currently loaded in the Vcm DLL's
    # binary tree. The users then use this number to dynamically allocate the satKeys array and pass it to this
    # function.
    #
    # If the users prefer to pass a static array to the function, make sure it is big enough to store all the satKeys
    # in memory.
    # order: Specifies the order in which the satKeys should be returned: 0=ascending, 1=descending, 2=order as loaded
    # (in-Integer)
    # satKeys: The array in which to store the satKeys (out-Long[*])
    dllObj.VcmGetLoaded.restype = None
    dllObj.VcmGetLoaded.argtypes = [c_int, c_void_p]

    # Adds a VCM using its 1-line or concatenated string formats
    # If the satellite was previously added to the Vcm DLL's binary tree, the function also returns a negative value
    # indicating an error.
    #
    # The users can use this function repeatedly to add many satellites (one satellite at a time) to the Vcm DLL's
    # binary tree.
    # vcmString: 1-line or concatenated string representation of the VCM (in-Character[4000])
    dllObj.VcmAddSatFrLines.restype = c_longlong
    dllObj.VcmAddSatFrLines.argtypes = [c_char_p]

    # Works like VcmAddSatFrLines but designed for Matlab
    # vcmString: 1-line or concatenated string representation of the VCM (in-Character[4000])
    # satKey: The satKey of the newly added VCM on success, a negative value on error (out-Long)
    dllObj.VcmAddSatFrLinesML.restype = None
    dllObj.VcmAddSatFrLinesML.argtypes = [c_char_p, c_longlong_p]

    # Adds a VCM using its individually provided field values
    #
    # The table below indicates starting character position for each field in the xs_vcm parameter:
    #
    # table
    #
    # Starting Character Position
    # Input Description
    #
    #  0satellite name, A8
    #  8common satellite name, A25
    # 33geopotential name, A6 (WGS-72, WGS-84, EGM-96, ...)
    # 39drag model, A12
    # 51lunar solar pertubations, A3 (ON, OFF)
    # 54radiation pressure pertubations, A3 (ON, OFF)
    # 57Earth + ocean tides pertubation, A3 (ON, OFF)
    # 60intrack thrust, A3 (ON, OFF)
    # 63integration mode, A6 (ASW, OSW, SPADOC, ...)
    # 69coordinate system, A5
    # 74type of partial derivatives, A8
    # 82step mode, A4 (AUTO, TIME, S)
    # 86fixed step size indicator, A3 (ON, OFF)
    # 89initial step size selection, A6 (AUTO, MANUAL)
    #
    #
    # The table below indicates the index for each field in the xa_vcm array:
    #
    # table
    #
    # Index (xa_vcm)
    # index Interpretation
    #
    #   0satellite number
    #   1satellite's epoch time
    #   2epoch revolution number
    #   3J2K position X (km)
    #   4J2K position Y (km)
    #   5J2K position Z (km)
    #   6J2K velocity X (km/s)
    #   7J2K velocity Y (km/s)
    #   8J2K velocity Z (km/s)
    #   9ECI position X (km)
    #  10ECI position Y (km)
    #  11ECI position Z (km)
    #  12ECI velocity X (km/s)
    #  13ECI velocity Y (km/s)
    #  14ECI velocity Z (km/s)
    #  15EFG position X (km)
    #  16EFG position Y (km)
    #  17EFG position Z (km)
    #  18EFG velocity X (km/s)
    #  19EFG velocity Y (km/s)
    #  20EFG velocity Z (km/s)
    #  21geopotential zonals
    #  22geopotential tesserals
    #  23ballistic coefficient (m^2/kg)
    #  24BDOT (m^2/kg-s)
    #  25solar radiation pressure coefficient (m^2/kg)
    #  26energy dissipation rate (w/kg)
    #  27outgassing parameter/thrust acceleration (km/s^2)
    #  28center of mass offset (m)
    #  29solar flux F10
    #  30average F10
    #  31average Ap
    #  32TAI - UTC (s)
    #  33UT1 - UTC (s)
    #  34UT1 rate (ms/day)
    #  35polar motion X (arcsec)
    #  36polar motion Y (arcsec)
    #  37nutation terms
    #  38leap second time in days since 1950 UTC
    #  39initial step size
    #  40integrator control error
    #  41position u sigma (km)
    #  42position v sigma (km)
    #  43position w sigma (km)
    #  44velocity u sigma (km/s)
    #  45velocity v sigma (km/s)
    #  46velocity w sigma (km/s)
    #  47covariance matrix size
    #  48weighted RM of last DC on the satellite
    # 100the lower triangle portion of the full cov matrix (100-120: 6x6 covmtx, ..., 100-144: 9x9
    # covmtx)
    #
    #
    # The order of the values in the lower half of the covariance matrix is described in the VCM Data Description
    # section.
    #
    # For a 6x6 covariance matrix, the 21 values should be entered in the xa_vcm array using index values 100-120.
    #
    # For a 9x9 covariance matrix, the 45 values should be entered using the index values 100-144.
    # xs_vcm: The input string that contains all VCM's text fields (in-Character[512])
    # xa_vcm: The input array that contains all VCM's numerical fields. see XA_VCM_? (in-Double[512])
    dllObj.VcmAddSatFrFields.restype = c_longlong
    dllObj.VcmAddSatFrFields.argtypes = [c_char_p, c_double * 512]

    # Works like VcmAddSatFrFields but designed for Matlab
    #
    # See VcmAddSatFrFields for definitions of the xs_vcm and xa_vcm parameters.
    # xs_vcm: The input string that contains all VCM's text fields (in-Character[512])
    # xa_vcm: The input array that contains all VCM's numerical fields.  see XA_VCM_? (in-Double[512])
    # satKey: The satKey of the newly added VCM on success, a negative value on error (out-Long)
    dllObj.VcmAddSatFrFieldsML.restype = None
    dllObj.VcmAddSatFrFieldsML.argtypes = [c_char_p, c_double * 512, c_longlong_p]

    # Retrieves VCM data associated with the input satKey
    # satKey: The satKey of the loaded VCM (in-Long)
    # xs_vcm: The output string that contains all VCM's text fields (out-Character[512])
    # xa_vcm: The output array that contains all VCM's numerical fields.  see XA_VCM_? (out-Double[512])
    dllObj.VcmRetrieveAllData.restype = c_int
    dllObj.VcmRetrieveAllData.argtypes = [c_longlong, c_char_p, c_double * 512]

    # Updates a VCM using its individual field values. Note: satellite's number and epoch won't be updated
    #
    # See VcmAddSatFrFields for definitions of the xs_vcm and xa_vcm parameters.
    # satKey: The unique key of the satellite to update (in-Long)
    # xs_vcm: The input string that contains all VCM's text fields (in-Character[512])
    # xa_vcm: The input array that contains all VCM's numerical fields.  see XA_VCM_? (in-Double[512])
    dllObj.VcmUpdateSatFrFields.restype = c_int
    dllObj.VcmUpdateSatFrFields.argtypes = [c_longlong, c_char_p, c_double * 512]

    # Retrieves the value of a specific field of a VCM
    #
    # The table below shows the values for the xf_Vcm parameter:
    #
    # table
    #
    # index
    # index Interpretation
    #
    #  1  Satellite number I5
    #  2  Satellite international designator A8
    #  3  Epoch YYYYDDDHHMMSS.SSS A17
    #  4  Revolution number I5
    #  5  position X (km) F16.8
    #  6  position Y (km) F16.8
    #  7  position Z (km) F16.8
    #  8  velocity X (km/s) F16.12
    #  9  velocity Y (km/s) F16.12
    # 10  velocity Z (km/s) F16.12
    # 11  Geo Name A6
    # 12  Geo zonals I2
    # 13  Geo tesserals I2
    # 14  Drag modelel A12 (NONE, JAC70/MSIS90)
    # 15  Lunar solar A3 (ON/OFF)
    # 16  Radiation pressure pertubations A3 (ON/OFF)
    # 17  Earth + ocean tides pertubations A3 (ON/OFF)
    # 18  Intrack thrust A3 (ON/OFF)
    # 19  Ballistic coefficient (m^2/kg)
    # 20  Radiation pressure coefficient  (m^2/kg)
    # 21  Outgassing parameter (km/s^2)
    # 22  Center of mass offset (m)
    # 23  Solar flux F10 I3
    # 24  Solar flux F10 average I3
    # 25  Ap average F5.1
    # 26  TAI minus UTC (s)I2
    # 27  UT1 minus UTC (s) F7.5
    # 28  UT1 rate (ms/day)  F5.3
    # 29  Polar motion X (arcsec) F6.4
    # 30  Polar motion Y (arcsec) F6.4
    # 31  Nutation terms I3
    # 32  Leap second time YYYYDDDHHMMSS.SSS A17
    # 33  Integration mode A6 (ASW, OSW, SPADOC)
    # 34  Type of partial derivatives A8 (ANALYTIC, FULL NUM, FAST NUM)
    # 35  Integration step mode A4 (AUTO/TIME, S)
    # 36  Fixed step size indicator A3 (ON/OFF)
    # 37  Initial step size selection A6 (AUTO/MANUAL)
    # 38  Initial integration step size F8.3
    # 39  Integrator error control E9.3
    # 40  Weighted RMS of last DC E10.5
    # 41  BDOT (M2/KG-S)
    # 42  EDR (W/KG)
    #
    # satKey: The satellite's unique key (in-Long)
    # xf_Vcm: Predefined number specifying which field to set (in-Integer)
    # valueStr: A string to contain the value of the requested field (out-Character[512])
    dllObj.VcmGetField.restype = c_int
    dllObj.VcmGetField.argtypes = [c_longlong, c_int, c_char_p]

    # Updates the value of a specific field of a VCM
    # See VcmGetField for a description of the xf_Vcm parameter.
    # satKey: The satellite's unique key (in-Long)
    # xf_Vcm: Predefined number specifying which field to set (in-Integer)
    # valueStr: The new value of the specified field, expressed as a string (in-Character[512])
    dllObj.VcmSetField.restype = c_int
    dllObj.VcmSetField.argtypes = [c_longlong, c_int, c_char_p]

    # Retrieves all of the data for a VCM in a single function call
    # satKey: The satellite's unique key (in-Long)
    # satNum: Satellite number (out-Integer)
    # satName: Satellite name A8 (out-Character[8])
    # epochDtg: Satellite epoch time A17 YYYYDDDHHMMSS.SSS (out-Character[17])
    # revNum: Revolution number (out-Integer)
    # posECI: ECI position (out-Double[3])
    # velECI: ECI velocity (out-Double[3])
    # geoName: Geopotential name A6 (WGS-72, WGS-84, EGM-96...) (out-Character[6])
    # geoZonals: Geopotential zonals (out-Integer)
    # geoTesserals: Geopotential tesserals (out-Integer)
    # dragModel: Drag model A12 (NONE, JAC70/MSIS90...) (out-Character[12])
    # lunarSolar: Lunar solar pertubations A3: ON, OFF (out-Character[3])
    # radPress: Radiation pressure pertubations A3: ON, OFF (out-Character[3])
    # earthTides: Earth + ocean tides pertubations A3: ON, OFF (out-Character[3])
    # intrackThrust: Intrack thrust A3: ON, OFF (out-Character[3])
    # bTerm: Ballistic coefficient (m2/kg) E13.10 (out-Double)
    # agom: Solar radiation pressure coefficient (m2/kg) E13.10 (out-Double)
    # ogParm: Outgassing parameter/Thrust acceleration (m/s2) E13.10 (out-Double)
    # cmOffset: Center of mass offset (m) (out-Double)
    # f10: Solar flux F10 I3 (out-Integer)
    # f10Avg: Soluar flux F10 average I3 (out-Integer)
    # apAvg: Ap average F5.1 (out-Double)
    # tconRec: 1: TaiMinusUTC, 2: UT1MinusUTC, 3: UT1Rate, 4: PolarX, 5: PolarY (out-Double[5])
    # nTerms: Number of nutation terms I3 (out-Integer)
    # leapYrDtg: Leap second time (out-Character[17])
    # integMode: Integration mode A6: ASW, OSW, SPADOC (SPECTR=1 if ASW, OSW) (out-Character[6])
    # partials: Type of partial derivatives A8 (Analytic, FULL NUM, FAST NUM) (out-Character[8])
    # stepMode: Integrator step mode A4: AUTO, TIME, S (out-Character[4])
    # fixStep: Fixed step size indicator A3: ON, OFF (out-Character[3])
    # stepSelection: Initial step size selection A6: AUTO, MANUAL (out-Character[6])
    # initStepSize: Initial integration step size  F8.3 (out-Double)
    # errCtrl: Integrator error control  E9.3 (out-Double)
    # rms: Weighted RMS of last DC on the satellite E10.5 (out-Double)
    dllObj.VcmGetAllFields.restype = c_int
    dllObj.VcmGetAllFields.argtypes = [
        c_longlong,
        c_int_p,
        c_char_p,
        c_char_p,
        c_int_p,
        c_double * 3,
        c_double * 3,
        c_char_p,
        c_int_p,
        c_int_p,
        c_char_p,
        c_char_p,
        c_char_p,
        c_char_p,
        c_char_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_int_p,
        c_int_p,
        c_double_p,
        c_double * 5,
        c_int_p,
        c_char_p,
        c_char_p,
        c_char_p,
        c_char_p,
        c_char_p,
        c_char_p,
        c_double_p,
        c_double_p,
        c_double_p,
    ]

    # Returns the concatenated string representation of a VCM by the satellite's satKey
    # satKey: The satellite's unique key (in-Long)
    # vcmLines: The resulting concatenated string representation of the VCM (out-Character[4000])
    dllObj.VcmGetLines.restype = c_int
    dllObj.VcmGetLines.argtypes = [c_longlong, c_char_p]

    # Converts VCM 1-line format to multi-line format (as a concatenated string)
    # vcm1Line: The input VCM 1-line format (in-Character[1500])
    # vcmLines: The resulting concatenated string (out-Character[4000])
    dllObj.Vcm1LineToMultiLine.restype = c_int
    dllObj.Vcm1LineToMultiLine.argtypes = [c_char_p, c_char_p]

    # Converts VCM multi-line format (as a concatenated string) to 1-line format
    # vcmLines: The input concatenated string (in-Character[4000])
    # vcm1Line: The resulting VCM 1-line format (out-Character[1500])
    dllObj.VcmMultiLineTo1Line.restype = c_int
    dllObj.VcmMultiLineTo1Line.argtypes = [c_char_p, c_char_p]

    # Returns the first satKey from the currently loaded set of VCM's that contains the specified satellite number
    # This function is useful when Vcm dll is used in applications that requires only one record (one Vcm entry) for
    # one satellite and the applications refer to that Vcm by its satellite number. However, the Standardized
    # Astrodynamic Algorithms library is only working with satKeys, this function helps to return the associated satKey
    # of that satellite.
    # satNum: The input satellite number (in-Integer)
    dllObj.VcmGetSatKey.restype = c_longlong
    dllObj.VcmGetSatKey.argtypes = [c_int]

    # Works like VcmGetSatKey but designed for Matlab
    # satNum: The input satellite number (in-Integer)
    # satKey: The satellite's unique key (out-Long)
    dllObj.VcmGetSatKeyML.restype = None
    dllObj.VcmGetSatKeyML.argtypes = [c_int, c_longlong_p]

    # Computes a satKey from the input data
    # This is the proper way to reconstruct a satKey from its fields. If the users use their own routine to do this,
    # the computed satKey might be different.
    # satNum: The input satellite number (in-Integer)
    # epochDtg: [yy]yydddhhmmss.sss or [yy]yyddd.ddddddd or DTG15, DTG17, DTG20 (in-Character[20])
    dllObj.VcmFieldsToSatKey.restype = c_longlong
    dllObj.VcmFieldsToSatKey.argtypes = [c_int, c_char_p]

    # Works like VcmFieldsToSatKey but designed for Matlab
    # satNum: The input satellite number (in-Integer)
    # epochDtg: [yy]yydddhhmmss.sss or [yy]yyddd.ddddddd or DTG15, DTG17, DTG20 (in-Character[20])
    # satKey: The satellite's unique key (out-Long)
    dllObj.VcmFieldsToSatKeyML.restype = None
    dllObj.VcmFieldsToSatKeyML.argtypes = [c_int, c_char_p, c_longlong_p]

    # Constructs a multi-line VCM (as a concatenated string) from the VCM data stored in the input arrays.
    # xa_vcm: Array containing VCM's numerical fields, see XA_VCM_? for array arrangement (in-Double[512])
    # xs_vcm: Input string that contains all VCM's text fields, see XS_VCM_? for column arrangement (in-Character[512])
    # vcmLines: The resulting concatenated string representation of a VCM (out-Character[4000])
    dllObj.VcmArrayToVcmLines.restype = None
    dllObj.VcmArrayToVcmLines.argtypes = [c_double * 512, c_char_p, c_char_p]

    # Constructs a 1-line VCM from the VCM data stored in the input arrays.
    # xa_vcm: Array containing VCM's numerical fields, see XA_VCM_? for array arrangement (in-Double[512])
    # xs_vcm: Input string that contains all VCM's text fields, see XS_VCM_? for column arrangement (in-Character[512])
    # vcm1Line: The resulting 1-line VCM (out-Character[1500])
    dllObj.VcmArrayToVcm1Line.restype = None
    dllObj.VcmArrayToVcm1Line.argtypes = [c_double * 512, c_char_p, c_char_p]

    # Parses data either in 1-line or multi-line (as a concatenated string) VCM and stores that data into the output
    # arrays
    # This function only parses data from the input VCM but DOES NOT load/add the input VCM to memory.
    # vcmString: An input 1-line or concatenated string representation of the VCM (in-Character[4000])
    # xa_vcm: Array containing VCM's numerical fields, see XA_VCM_? for array arrangement (out-Double[512])
    # xs_vcm: Output string that contains all VCM's text fields, see XS_VCM_? for column
    # arrangement (out-Character[512])
    dllObj.VcmStringToArray.restype = c_int
    dllObj.VcmStringToArray.argtypes = [c_char_p, c_double * 512, c_char_p]

    return dllObj


# Maximum string length of a multi-line VCM concatenated into one big string
VCMSTRLEN = 4000


# Maximum string length of a 1-line VCM string
VCM1LINELEN = 1500


# Starting location of the VCM's text data fields
# satellite name A8
XS_VCM_SATNAME = 0
# common satellite name A25
XS_VCM_COMMNAME = 8
# geopotential name A6 (WGS-72, WGS-84, EGM-96, ...)
XS_VCM_GEONAME = 33
# drag model A12
XS_VCM_DRAGMOD = 39
# lunar solar pertubations A3 (ON, OFF)
XS_VCM_LUNAR = 51
# radiation pressure pertubations A3 (ON, OFF)
XS_VCM_RADPRESS = 54
# Earth + ocean tides pertubation A3 (ON, OFF)
XS_VCM_EARTHTIDES = 57
# intrack thrust A3 (ON, OFF)
XS_VCM_INTRACK = 60
# integration mode A6 (ASW, OSW, SPADOC, ...)
XS_VCM_INTEGMODE = 63
# coordinate system A5
XS_VCM_COORDSYS = 69
# type of partial derivatives A8
XS_VCM_PARTIALS = 74
# step mode A4 (AUTO, TIME, S)
XS_VCM_STEPMODE = 82
# fixed step size indicator A3 (ON, OFF)
XS_VCM_FIXEDSTEP = 86
# initial step size selection A6 (AUTO, MANUAL)
XS_VCM_STEPSEL = 89

XS_VCM_SIZE = 512

# VCM's text data fields - new convention (start index, string length)
# satellite name A8
XS_VCM_SATNAME_0_8 = 0
# common satellite name A25
XS_VCM_COMMNAME_8_25 = 8
# geopotential name A6 (WGS-72, WGS-84, EGM-96, ...)
XS_VCM_GEONAME_33_6 = 33
# drag model A12
XS_VCM_DRAGMOD_39_12 = 39
# lunar solar pertubations A3 (ON, OFF)
XS_VCM_LUNAR_51_3 = 51
# radiation pressure pertubations A3 (ON, OFF)
XS_VCM_RADPRESS_54_3 = 54
# Earth + ocean tides pertubation A3 (ON, OFF)
XS_VCM_EARTHTIDES_57_3 = 57
# intrack thrust A3 (ON, OFF)
XS_VCM_INTRACK_60_3 = 60
# integration mode A6 (ASW, OSW, SPADOC, ...)
XS_VCM_INTEGMODE_63_6 = 63
# coordinate system A5
XS_VCM_COORDSYS_69_5 = 69
# type of partial derivatives A8
XS_VCM_PARTIALS_74_8 = 74
# step mode A4 (AUTO, TIME, S)
XS_VCM_STEPMODE_82_4 = 82
# fixed step size indicator A3 (ON, OFF)
XS_VCM_FIXEDSTEP_86_3 = 86
# initial step size selection A6 (AUTO, MANUAL)
XS_VCM_STEPSEL_89_6 = 89

XS_VCM_LENGTH = 512

# Indexes to access data from an array containing VCM numerical data fields
# satellite number
XA_VCM_SATNUM = 0
# satellite's epoch time
XA_VCM_EPOCHDS50UTC = 1
# epoch revolution number
XA_VCM_REVNUM = 2
# J2K position X (km)
XA_VCM_J2KPOSX = 3
# J2K position Y (km)
XA_VCM_J2KPOSY = 4
# J2K position Z (km)
XA_VCM_J2KPOSZ = 5
# J2K velocity X (km/s)
XA_VCM_J2KVELX = 6
# J2K velocity Y (km/s)
XA_VCM_J2KVELY = 7
# J2K velocity Z (km/s)
XA_VCM_J2KVELZ = 8
# ECI position X (km)
XA_VCM_ECIPOSX = 9
# ECI position Y (km)
XA_VCM_ECIPOSY = 10
# ECI position Z (km)
XA_VCM_ECIPOSZ = 11
# ECI velocity X (km/s)
XA_VCM_ECIVELX = 12
# ECI velocity Y (km/s)
XA_VCM_ECIVELY = 13
# ECI velocity Z (km/s)
XA_VCM_ECIVELZ = 14
# EFG position X (km)
XA_VCM_EFGPOSX = 15
# EFG position Y (km)
XA_VCM_EFGPOSY = 16
# EFG position Z (km)
XA_VCM_EFGPOSZ = 17
# EFG velocity X (km/s)
XA_VCM_EFGVELX = 18
# EFG velocity Y (km/s)
XA_VCM_EFGVELY = 19
# EFG velocity Z (km/s)
XA_VCM_EFGVELZ = 20
# geopotential zonals
XA_VCM_GEOZON = 21
# geopotential tesserals
XA_VCM_GEOTES = 22
# ballistic coefficient (m^2/kg)
XA_VCM_BTERM = 23
# BDOT (m^2/kg-s)
XA_VCM_BDOT = 24
# solar radiation pressure coefficient (m^2/kg)
XA_VCM_AGOM = 25
# energy dissipation rate (w/kg)
XA_VCM_EDR = 26
# outgassing parameter/thrust acceleration (m/s^2)
XA_VCM_OGPARM = 27
# center of mass offset (m)
XA_VCM_CMOFFSET = 28
# solar flux F10
XA_VCM_F10 = 29
# average F10
XA_VCM_F10AVG = 30
# average Ap
XA_VCM_APAVG = 31
# TAI - UTC (s)
XA_VCM_TAIMUTC = 32
# UT1 - UTC (s)
XA_VCM_UT1MUTC = 33
# UT1 rate (ms/day)
XA_VCM_UT1RATE = 34
# polar motion X (arcsec)
XA_VCM_POLMOTX = 35
# polar motion Y (arcsec)
XA_VCM_POLMOTY = 36
# nutation terms
XA_VCM_NUTTERMS = 37
# leap second time in days since 1950 UTC
XA_VCM_LEAPDS50UTC = 38
# initial step size
XA_VCM_INITSTEP = 39
# integrator control error
XA_VCM_ERRCTRL = 40
# position u sigma (km)
XA_VCM_POSUSIG = 41
# position v sigma (km)
XA_VCM_POSVSIG = 42
# position w sigma (km)
XA_VCM_POSWSIG = 43
# velocity u sigma (km/s)
XA_VCM_VELUSIG = 44
# velocity v sigma (km/s)
XA_VCM_VELVSIG = 45
# velocity w sigma (km/s)
XA_VCM_VELWSIG = 46
# covariance matrix size
XA_VCM_COVMTXSIZE = 47
# weighted RM of last DC on the satellite
XA_VCM_RMS = 48
# the lower triangle portion of the full cov matrix (100-120: 6x6 covmtx, ..., 100-144: 9x9 covmtx)
XA_VCM_COVELEMS = 100

XA_VCM_SIZE = 512

# Indexes of VCM data fields
# Satellite number I5
XF_VCM_SATNUM = 1
# Satellite international designator A8
XF_VCM_SATNAME = 2
# Epoch YYYYDDDHHMMSS.SSS A17
XF_VCM_EPOCH = 3
# Revolution number I5
XF_VCM_REVNUM = 4
# position X (km) F16.8
XF_VCM_POSX = 5
# position Y (km) F16.8
XF_VCM_POSY = 6
# position Z (km) F16.8
XF_VCM_POSZ = 7
# velocity X (km/s) F16.12
XF_VCM_VELX = 8
# velocity Y (km/s) F16.12
XF_VCM_VELY = 9
# velocity Z (km/s) F16.12
XF_VCM_VELZ = 10
# Geo Name A6
XF_VCM_GEONAME = 11
# Geo zonals I2
XF_VCM_GEOZONALS = 12
# Geo tesserals I2
XF_VCM_GEOTESSER = 13
# Drag modelel A12 (NONE, JAC70/MSIS90)
XF_VCM_DRAGMODE = 14
# Lunar solar A3 (ON/OFF)
XF_VCM_LUNSOL = 15
# Radiation pressure pertubations A3 (ON/OFF)
XF_VCM_RADPRESS = 16
# Earth + ocean tides pertubations A3 (ON/OFF)
XF_VCM_ERTHTIDES = 17
# Intrack thrust A3 (ON/OFF)
XF_VCM_INTRACK = 18
# Ballistic coefficient (m^2/kg)
XF_VCM_BTERM = 19
# Radiation pressure coefficient  (m^2/kg)
XF_VCM_AGOM = 20
# Outgassing parameter (m/s^2)
XF_VCM_OGPARM = 21
# Center of mass offset (m)
XF_VCM_CMOFFSET = 22
# Solar flux F10 I3
XF_VCM_F10 = 23
# Solar flux F10 average I3
XF_VCM_F10AVG = 24
# Ap average F5.1
XF_VCM_APAVG = 25
# TAI minus UTC (s)I2
XF_VCM_TAIMUTC = 26
# UT1 minus UTC (s) F7.5
XF_VCM_UT1MUTC = 27
# UT1 rate (ms/day)  F5.3
XF_VCM_UT1RATE = 28
# Polar motion X (arcsec) F6.4
XF_VCM_POLARX = 29
# Polar motion Y (arcsec) F6.4
XF_VCM_POLARY = 30
# Nutation terms I3
XF_VCM_NTERMS = 31
# Leap second time YYYYDDDHHMMSS.SSS A17
XF_VCM_LEAPYR = 32
# Integration mode A6 (ASW, OSW, SPADOC)
XF_VCM_INTEGMODE = 33
# Type of partial derivatives A8 (Analytic, FULL NUM, FAST NUM)
XF_VCM_PARTIALS = 34
# Integration step mode A4 (AUTO/TIME, S)
XF_VCM_STEPMODE = 35
# Fixed step size indicator A3 (ON/OFF)
XF_VCM_FIXEDSTEP = 36
# Initial step size selection A6 (AUTO/MANUAL)
XF_VCM_STEPSLCTN = 37
# Initial integration step size F8.3
XF_VCM_STEPSIZE = 38
# Integrator error control E9.3
XF_VCM_ERRCTRL = 39
# Weighted rms of last DC E10.5
XF_VCM_RMS = 40
# BDOT (M2/KG-S)
XF_VCM_BDOT = 41
# EDR (W/KG)
XF_VCM_EDR = 42


# *******************************************************************************
# Different ingetration control/step mode
STEPMODE_AUTO = (0,)
STEPMODE_TIME = (1,)
STEPMODE_S = 2


# ========================= End of auto generated code ==========================
