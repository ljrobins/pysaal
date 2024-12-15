# This wrapper file was generated automatically by the GenDllWrappers program.
import platform
from ctypes import CDLL, c_char_p, c_double, c_int, c_longlong
from pathlib import Path

LIB_PATH = Path(__file__).parent

# get the right filename of the dll/so
if platform.uname()[0] == "Windows":
    DLL_NAME = LIB_PATH / "EnvConst.dll"

if platform.uname()[0] == "Linux":
    DLL_NAME = LIB_PATH / "libenvconst.so"

if platform.uname()[0] == "Darwin":
    DLL_NAME = LIB_PATH / "libenvconst.dylib"


def get_env_const_dll():
    """LoadEnvConstDll() -- Loads EnvConst.dll from the PATH or LD_LIBRARY_PATH
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
    # Initializes the EnvInit DLL for use in the program.
    # If this function returns an error, it is recommended that you stop the program immediately.
    #
    # An error will occur if you forget to load and initialize all the prerequisite DLLs, as listed in the DLL
    # Prerequisites section of the accompanying documentation, before using this DLL.
    #
    # When the function is called, the GEO model is set to WGS-72 and the FK model is set to FK5.  If the user plans to
    # use the SGP4 propagator, do NOT change this default setting. Otherwise, SGP4 won't work
    # apAddr: The handle that was returned from DllMainInit, see the documentation for DllMain.dll for
    # details. (in-Long)
    dllObj.EnvInit.restype = c_int
    dllObj.EnvInit.argtypes = [c_longlong]

    # Returns information about the EnvConst DLL.
    # The returned string provides information about the version number, build date, and the platform of the EnvConst
    # DLL.
    # infoStr: A string to hold the information about EnvConst.dll. (out-Character[128])
    dllObj.EnvGetInfo.restype = None
    dllObj.EnvGetInfo.argtypes = [c_char_p]

    # Reads Earth constants (GEO) model and fundamental catalogue (FK) model settings from a file.
    # The users can use NAME=VALUE pair to setup the GEO and FK models in the input file.
    #
    # For GEO model, the valid names are GEOCONST, BCONST and the valid values are WGS-72, WGS72,  72, WGS-84,
    # WGS84, 84, EGM-96, EGM96, 96, EGM-08, EGM08, 08, JGM-2, JGM2, 2, SEM68R, 68, GEM5, 5, GEM9, and 9.
    #
    # For FK model, the valid name is FKCONST and the valid values are: FK4, 4, FK5, 5.
    #
    # All the string literals are case-insensitive.
    # envFile: The name of the input file. (in-Character[512])
    dllObj.EnvLoadFile.restype = c_int
    dllObj.EnvLoadFile.argtypes = [c_char_p]

    # Saves the current Earth constants (GEO) model and fundamental catalogue (FK) model settings to a file.
    # Returns zero indicating the GEO and FK settings have been successfully saved to the file. Other values indicate
    # an error.
    # envConstFile: The name of the file in which to save the settings. (in-Character[512])
    # saveMode: Specifies whether to create a new file or append to an existing one. (0 = create,
    # 1= append) (in-Integer)
    # saveForm: Specifies the mode in which to save the file. (0 = text format, 1 = xml (not yet implemented, reserved
    # for future)) (in-Integer)
    dllObj.EnvSaveFile.restype = c_int
    dllObj.EnvSaveFile.argtypes = [c_char_p, c_int, c_int]

    # Returns the current fundamental catalogue (FK) setting.
    # The FK model is shared among all the Standardized Astrodynamic Algorithms DLLs in the program.
    dllObj.EnvGetFkIdx.restype = c_int
    dllObj.EnvGetFkIdx.argtypes = []

    # Changes the fundamental catalogue (FK) setting to the specified value.
    # If the users enter an invalid value for the fkIdx, the program will continue to use the current setting.
    #
    # The FK model is globally shared among the Standardized Astrodynamic Algorithms DLLs. If its setting is changed,
    # the new setting takes effect immediately.
    # The FK model must be set to FK5 to use the SGP4 propagator.
    # xf_FkMod: Specifies the FK model to use. The following values are accepted: xf_FkMod= 4: FK4, xf_FkMod= 5:
    # FK5 (in-Integer)
    dllObj.EnvSetFkIdx.restype = None
    dllObj.EnvSetFkIdx.argtypes = [c_int]

    # Returns the current Earth constants (GEO) setting.
    #
    # The GEO model is shared among all the Standardized Astrodynamic Algorithms DLLs in the program.
    #
    # The following table lists possible values of the return value GEO setting:
    #
    # table
    #
    # Value
    # Value interpretation
    #
    # 84WGS-84
    # 96EGM-96
    # 08EGM-08
    # 72WGS-72 (default)
    # 2JGM2
    # 68STEM68R, SEM68R
    # 5GEM5
    # 9GEM9
    #
    dllObj.EnvGetGeoIdx.restype = c_int
    dllObj.EnvGetGeoIdx.argtypes = []

    # Changes the Earth constants (GEO) setting to the specified value.
    #
    # If you specify an invalid value for xf_GeoMod, the program will continue to use the current setting.
    #
    # The GEO model is globally shared among the Standardized Astrodynamic Algorithms DLLs. If its setting is changed,
    # the new setting takes effect immediately
    #
    # The following table lists possible values of the parameter value GEO setting:
    #
    # table
    #
    # Value
    # Value interpretation
    #
    # 84WGS-84
    # 96EGM-96
    # 08EGM-08
    # 72WGS-72 (default)
    # 2JGM2
    # 68STEM68R, SEM68R
    # 5GEM5
    # 9GEM9
    #
    #
    # The GEO model must be set to WGS-72 to use the SGP4 propagator.
    # xf_GeoMod: Specifies the GEO model to use. (in-Integer)
    dllObj.EnvSetGeoIdx.restype = None
    dllObj.EnvSetGeoIdx.argtypes = [c_int]

    # Returns the name of the current Earth constants (GEO) model.
    #
    # The geoStr parameter may contain one of the following values:
    #
    # table
    # WGS-84
    # EGM-96
    # EGM-08
    # WGS-72
    # JGM2
    # SEM68R
    # GEM5
    # GEM9
    #
    # geoStr: A string to store the name of the current GEO model. (out-Character[6])
    dllObj.EnvGetGeoStr.restype = None
    dllObj.EnvGetGeoStr.argtypes = [c_char_p]

    # Changes the Earth constants (GEO) setting to the model specified by a string literal.
    #
    # If you specify an invalid value for geoStr, the program will continue to use the current setting.
    #
    # The GEO model is globally shared among the Standardized Astrodynamic Algorithms DLLs. If its setting is changed,
    # the new setting takes effect immediately.
    #
    # The following table lists possible values of the parameter value GEO setting:
    #
    # table
    #
    # geoStr (any string in the row)
    # Interpretation
    #
    # 'WGS-84', 'WGS84', '84'WGS-84
    # 'EGM-96', 'EGM96', '96'EGM-96
    # 'EGM-08', 'EGM08', '8'EGM-08
    # 'WGS-72', 'WGS72', '72'WGS-72 (default)
    # 'JGM-2, 'JGM2', '2'JGM-2
    # 'SEM68R', '68'STEM68R, SEM68R
    # 'GEM5', '5'GEM5
    # 'GEM9', '9'GEM9
    #
    #
    # The GEO model must be set to WGS-72 to use the SGP4 propagator.
    # geoStr: The GEO model to use, expressed as a string. (in-Character[6])
    dllObj.EnvSetGeoStr.restype = None
    dllObj.EnvSetGeoStr.argtypes = [c_char_p]

    # Retrieves the value of one of the constants from the current Earth constants (GEO) model.
    # xf_GeoCon: An index specifying the constant you wish to retrieve, see XF_GEOCON_? for field
    # specification (in-Integer)
    dllObj.EnvGetGeoConst.restype = c_double
    dllObj.EnvGetGeoConst.argtypes = [c_int]

    # Retrieves the value of one of the constants from the current fundamental catalogue (FK) model.
    # xf_FkCon: An index specifying the constant you wish to retrieve, , see XF_FKCON_? for field
    # specification (in-Integer)
    dllObj.EnvGetFkConst.restype = c_double
    dllObj.EnvGetFkConst.argtypes = [c_int]

    # Returns a handle that can be used to access the fundamental catalogue (FK) data structure.
    #
    # This function is needed when calling the ThetaGrnwch function from TimeFunc.dll.
    #
    # The handle returned by this function is sometimes called a pointer for historical reasons. The name EnvGetFkPtr
    # comes from the fact that the handle used to be called a pointer.
    dllObj.EnvGetFkPtr.restype = c_longlong
    dllObj.EnvGetFkPtr.argtypes = []

    # Specifies the shape of the earth that will be used by the Astro Standards software, either spherical earth or
    # oblate earth
    # earthShape: The value indicates the shape of the earth: 0=spherical earth, 1= oblate earth (default) (in-Integer)
    dllObj.EnvSetEarthShape.restype = None
    dllObj.EnvSetEarthShape.argtypes = [c_int]

    # Returns the value representing the shape of the earth being used by the Astro Standards software, either
    # spherical earth or oblate earth
    dllObj.EnvGetEarthShape.restype = c_int
    dllObj.EnvGetEarthShape.argtypes = []

    # Comment out the below line to disable load message
    return dllObj


# Indexes of Earth Constant fields
# Earth flattening (reciprocal; unitless)
XF_GEOCON_FF = 1
# J2 (unitless)
XF_GEOCON_J2 = 2
# J3 (unitless)
XF_GEOCON_J3 = 3
# J4 (unitless)
XF_GEOCON_J4 = 4
# Ke (er**1.5/min)
XF_GEOCON_KE = 5
# Earth radius (km/er)
XF_GEOCON_KMPER = 6
# Earth rotation rate w.r.t. fixed equinox (rad/min)
XF_GEOCON_RPTIM = 7

# J2/2 (unitless)
XF_GEOCON_CK2 = 8
# -3/8 J4 (unitless)
XF_GEOCON_CK4 = 9
# Converts km/sec to er/kem
XF_GEOCON_KS2EK = 10
# Earth rotation rate w.r.t. fixed equinox (rad/kemin)
XF_GEOCON_THDOT = 11
# J5 (unitless)
XF_GEOCON_J5 = 12
# Gravitational parameter km^3/(solar s)^2
XF_GEOCON_MU = 13


# Indexes of FK Constant fields
# Earth rotation rate w.r.t. moving equinox (rad/day)
XF_FKCON_C1 = 1
# Earth rotation acceleration(rad/day**2)
XF_FKCON_C1DOT = 2
# Greenwich angle (1970; rad)
XF_FKCON_THGR70 = 3

# Indexes represent geopotential models GEO
# Earth constants - JGM2
XF_GEOMOD_JGM2 = 2
# Earth constants - GEM5
XF_GEOMOD_GEM5 = 5
# Earth constants - EGM-08
XF_GEOMOD_EGM08 = 8
# Earth constants - GEM9
XF_GEOMOD_GEM9 = 9
# Earth constants - STEM68
XF_GEOMOD_STEM68 = 68
# Earth constants - WGS-72
XF_GEOMOD_WGS72 = 72
# Earth constants - WGS-84
XF_GEOMOD_WGS84 = 84
# Earth constants - EGM-96
XF_GEOMOD_EGM96 = 96
# Invalid earth model
XF_GEOMOD_UNKNOWN = 100

# *******************************************************************************

# Indexes represent fundamental catalogue FK
# Fundamental Catalog - FK5
XF_FKMOD_4 = 4
# Fundamental Catalog - FK4
XF_FKMOD_5 = 5


# ========================= End of auto generated code ==========================
