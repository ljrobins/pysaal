# This wrapper file was generated automatically by the GenDllWrappers program.
import platform
from ctypes import CDLL, POINTER, c_char, c_char_p, c_double, c_int, c_longlong, c_void_p
from pathlib import Path

c_longlong_p = POINTER(c_longlong)
c_int_p = POINTER(c_int)
c_double_p = POINTER(c_double)

# get the right filename of the dll/so
LIB_PATH = Path(__file__).parent
if platform.uname()[0] == "Windows":
    DLL_NAME = LIB_PATH / "Tle.dll"

if platform.uname()[0] == "Linux":
    DLL_NAME = LIB_PATH / "libtle.so"

if platform.uname()[0] == "Darwin":
    DLL_NAME = LIB_PATH / "libtle.dylib"


def get_tle_dll():
    """LoadTleDll() -- Loads Tle.dll from the PATH or LD_LIBRARY_PATH
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
    # Initializes Tle DLL for use in the program.
    # If this function returns an error, it is recommended that you stop the program immediately.
    #
    # An error will occur if you forget to load and initialize all the prerequisite DLLs, as listed in the DLL
    # Prerequisites section of the accompanying documentation, before using this DLL.
    # apAddr: The handle that was returned from DllMainInit. See the documentation for DllMain.dll for
    # details. (in-Long)
    dllObj.TleInit.restype = c_int
    dllObj.TleInit.argtypes = [c_longlong]

    # Returns the information about the Tle DLL.
    # The returned string provides information about the version number, build date, and the platform of the Tle DLL.
    # infoStr: A string to hold the information about the Tle DLL. (out-Character[128])
    dllObj.TleGetInfo.restype = None
    dllObj.TleGetInfo.argtypes = [c_char_p]

    # Loads TLEs (satellites) contained in a text file into the TLE DLL's binary tree.
    # You may use this function repeatedly to load TLEs from different input files. However, only unique satKeys are
    # loaded. Duplicated TLEs won't be stored.
    #
    # TLEs can be included directly in the specified file, or they can be read from a separate file identified with
    # "ELTFIL=[path\filename]" or "VECFIL=[path\filename]".
    #
    # The input file is read in two passes. The function first looks for "ELTFIL=" and "VECFIL=" lines, then it looks
    # for TLEs which were included directly. The result of this is that data entered using both methods will be
    # processed, but the "ELTFIL=" and "VECFIL=" data will be processed first.
    # tleFile: The name of the file containing two line element sets to be loaded. (in-Character[512])
    dllObj.TleLoadFile.restype = c_int
    dllObj.TleLoadFile.argtypes = [c_char_p]

    # Saves currently loaded TLEs to a file.
    # In append mode, if the specified file does not exist it will be created.
    # If you call this routine immediately after TleLoadFile(), the TLE contents in the two files should be the
    # same (minus duplicated TLE's or bad TLE's).
    #
    # The purpose of this function is to save the current state of the loaded TLE's, usually used in GUI applications,
    # for future use.
    # tleFile: The name of the file in which to save the TLE's. (in-Character[512])
    # saveMode: Specifies whether to create a new file or append to an existing file. (0 = create new file, 1= append
    # to existing file) (in-Integer)
    # xf_tleForm: Specifies the format in which to save the file. (0 = two-line element set format, 1 =  CSV,
    # others = future implementation) (in-Integer)
    dllObj.TleSaveFile.restype = c_int
    dllObj.TleSaveFile.argtypes = [c_char_p, c_int, c_int]

    # Removes a TLE represented by the satKey from memory.
    # If the users enter an invalid satKey (a non-existing satKey), the function will return a non-zero value
    # indicating an error.
    # satKey: The unique key of the satellite to be removed. (in-Long)
    dllObj.TleRemoveSat.restype = c_int
    dllObj.TleRemoveSat.argtypes = [c_longlong]

    # Removes all the TLEs from memory.
    dllObj.TleRemoveAllSats.restype = c_int
    dllObj.TleRemoveAllSats.argtypes = []

    # Returns the number of TLEs currently loaded.
    # See TleGetLoaded for an example.
    # This function is useful for dynamically allocating memory for the array that is passed to the function
    # TleGetLoaded().
    dllObj.TleGetCount.restype = c_int
    dllObj.TleGetCount.argtypes = []

    # Retrieves all of the currently loaded satKeys. These satKeys can be used to access the internal data for
    # the TLE's.
    # It is recommended that TleGetCount() be  used to determine how many satellites are currently loaded. This value
    # can then be used to dynamically allocate an array to hold the satKeys.
    #
    # If you are going to pass a statically allocated array to this function, ensure it is large enough to hold all of
    # the returned satKeys.
    # order: Specifies the order in which the satKeys should be returned. 0 = sort in ascending order of satKeys,
    # 1 = sort in descending order of satKeys, 2 = sort in the order in which the satKeys were loaded in memory,
    # 9 = Quickest: sort in the order in which the satKeys were stored in the tree (in-Integer)
    # satKeys: The array in which to store the satKeys. (out-Long[*])
    dllObj.TleGetLoaded.restype = None
    dllObj.TleGetLoaded.argtypes = [c_int, c_void_p]

    # Adds a TLE (satellite), using its directly specified first and second lines.
    # The function will indicate an error if the specified two line element set corresponds to a satellite that is
    # already in memory.
    #
    # This function can be called repeatedly to add many TLEs, one at a time.
    # line1: The first line of a two line element set (or CSV Tle). (in-Character[512])
    # line2: The second line of a two line element set (in-Character[512])
    dllObj.TleAddSatFrLines.restype = c_longlong
    dllObj.TleAddSatFrLines.argtypes = [c_char_p, c_char_p]

    # This function is similar to TleAddSatFrLines but designed to be used in Matlab.
    # Matlab doesn't correctly return the 19-digit satellite key using TleAddSatFrLines. This method is an alternative
    # way to return the satKey output.
    # line1: The first line of a two line element set (or CSV Tle). (in-Character[512])
    # line2: The second line of a two line element set (in-Character[512])
    # satKey: The satKey of the newly added TLE on success, a negative value on error. (out-Long)
    dllObj.TleAddSatFrLinesML.restype = None
    dllObj.TleAddSatFrLinesML.argtypes = [c_char_p, c_char_p, c_longlong_p]

    # Adds a TLE (satellite), using its CSV string format.
    # csvLine: Input CSV TLE string (in-Character[512])
    dllObj.TleAddSatFrCsv.restype = c_longlong
    dllObj.TleAddSatFrCsv.argtypes = [c_char_p]

    # This function is similar to TleAddSatFrCsv but designed to be used in Matlab.
    # csvLine: Input CSV TLE string (in-Character[512])
    # satKey: The satKey of the newly added TLE on success, a negative value on error. (out-Long)
    dllObj.TleAddSatFrCsvML.restype = None
    dllObj.TleAddSatFrCsvML.argtypes = [c_char_p, c_longlong_p]

    # Adds a GP TLE using its individually provided field values.
    # The function will indicate an error if the specified two line element set corresponds to a satellite that is
    # already in memory.
    #
    # This function can be called repeatedly to add many satellites (one satellite at a time).
    #
    # SGP satellites (ephType = 0) use Kozai mean motion. SGP4 satellites (ephType = 2) use Brouwer mean motion.
    # satNum: Satellite number (in-Integer)
    # secClass: Security classification (in-Character)
    # satName: Satellite international designator (in-Character[8])
    # epochYr: Element epoch time - year, [YY]YY (in-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (in-Double)
    # bstar: B* drag term (1/er) (ephType = 0, 2) or BTerm - ballistic coefficient (m2/kg) (ephType = 4,
    # XP) (in-Double)
    # ephType: Satellite ephemeris type (0: SGP, 2: SGP4) (in-Integer)
    # elsetNum: Element set number (in-Integer)
    # incli: Orbit inclination (degrees) (in-Double)
    # node: Right ascension of ascending node (degrees) (in-Double)
    # eccen: Eccentricity (in-Double)
    # omega: Argument of perigee (degrees) (in-Double)
    # mnAnomaly: Mean anomaly (degrees) (in-Double)
    # mnMotion: Mean motion (rev/day) (ephType = 0: Kozai mean motion, ephType = 2 or 4:
    # Brouwer mean motion) (in-Double)
    # revNum: Revolution number at epoch (in-Integer)
    dllObj.TleAddSatFrFieldsGP.restype = c_longlong
    dllObj.TleAddSatFrFieldsGP.argtypes = [
        c_int,
        c_char,
        c_char_p,
        c_int,
        c_double,
        c_double,
        c_int,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
    ]

    # This function is similar to TleAddSatFrFieldsGP but includes nDotO2 and n2DotO6.
    # nDotO2 and n2DotO6 values are not used in the SGP4 propagator. However, some users still want to preserve the
    # integrity of all input data.
    # satNum: Satellite number (in-Integer)
    # secClass: Security classification (in-Character)
    # satName: Satellite international designator (in-Character[8])
    # epochYr: Element epoch time - year, [YY]YY (in-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (in-Double)
    # bstar: B* drag term (1/er) (ephType = 0, 2) or BTerm - ballistic coefficient (m2/kg) (ephType = 4,
    # XP) (in-Double)
    # ephType: Satellite ephemeris type (0: SGP, 2: SGP4) (in-Integer)
    # elsetNum: Element set number (in-Integer)
    # incli: Orbit inclination (degrees) (in-Double)
    # node: Right ascension of ascending node (degrees) (in-Double)
    # eccen: Eccentricity (in-Double)
    # omega: Argument of perigee (degrees) (in-Double)
    # mnAnomaly: Mean anomaly (degrees) (in-Double)
    # mnMotion: Mean motion (rev/day) (ephType = 0: Kozai mean motion, ephType = 2 or 4: Brouwer mean
    # motion) (in-Double)
    # revNum: Revolution number at epoch (in-Integer)
    # nDotO2: Mean motion derivative (rev/day /2) (in-Double)
    # n2DotO6: Mean motion second derivative (rev/day**2 /6) or agom (ephType = 4, XP) (m2/kg) (in-Double)
    dllObj.TleAddSatFrFieldsGP2.restype = c_longlong
    dllObj.TleAddSatFrFieldsGP2.argtypes = [
        c_int,
        c_char,
        c_char_p,
        c_int,
        c_double,
        c_double,
        c_int,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
        c_double,
        c_double,
    ]

    # This function is similar to TleAddSatFrFieldsGP2 but designed to be used in Matlab.
    # Matlab doesn't seem to correctly return the 19-digit satellite key using TleAddSatFrFieldsGP2. This method is an
    # alternative way to return the satKey output.
    # satNum: Satellite number (in-Integer)
    # secClass: Security classification (in-Character)
    # satName: Satellite international designator (in-Character[8])
    # epochYr: Element epoch time - year, [YY]YY (in-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (in-Double)
    # bstar: B* drag term (1/er) (ephType = 0, 2) or BTerm - ballistic coefficient (m2/kg) (ephType = 4, XP) (in-Double)
    # ephType: Satellite ephemeris type (0: SGP, 2: SGP4) (in-Integer)
    # elsetNum: Element set number (in-Integer)
    # incli: Orbit inclination (degrees) (in-Double)
    # node: Right ascension of ascending node (degrees) (in-Double)
    # eccen: Eccentricity (in-Double)
    # omega: Argument of perigee (degrees) (in-Double)
    # mnAnomaly: Mean anomaly (degrees) (in-Double)
    # mnMotion: Mean motion (rev/day) (ephType = 0: Kozai mean motion, ephType = 2 or 4: Brouwer mean
    # motion) (in-Double)
    # revNum: Revolution number at epoch (in-Integer)
    # nDotO2: Mean motion derivative (rev/day /2) (in-Double)
    # n2DotO6: Mean motion second derivative (rev/day**2 /6) or agom (ephType = 4, XP) (m2/kg) (in-Double)
    # satKey: The satKey of the newly added TLE on success, a negative value on error. (out-Long)
    dllObj.TleAddSatFrFieldsGP2ML.restype = None
    dllObj.TleAddSatFrFieldsGP2ML.argtypes = [
        c_int,
        c_char,
        c_char_p,
        c_int,
        c_double,
        c_double,
        c_int,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
        c_double,
        c_double,
        c_longlong_p,
    ]

    # Updates a GP satellite's data in memory by providing its individual field values. Note: satNum, year, day, and
    # ephtype can't be updated.
    # The satellite's unique key will not be changed by this function. If you specify a satKey that does not correspond
    # to a currently loaded satellite, the function will indicate an error.
    #
    # Remember to use the correct mean motion depending on the satellite's ephType.
    # satKey: The satellite's unique key (in-Long)
    # secClass: Security classification (in-Character)
    # satName: Satellite international designator (in-Character[8])
    # bstar: B* drag term (1/er) (ephType = 0, 2) or BTerm - ballistic coefficient (m2/kg) (ephType = 4, XP) (in-Double)
    # elsetNum: Element set number (in-Integer)
    # incli: Orbit inclination (degrees) (in-Double)
    # node: Right ascension of ascending node (degrees) (in-Double)
    # eccen: Eccentricity (in-Double)
    # omega: Argument of perigee (degrees) (in-Double)
    # mnAnomaly: Mean anomaly (degrees) (in-Double)
    # mnMotion: Mean motion  (rev/day) (ephType = 0: Kozai mean motion, ephType = 2: Brouwer mean motion) (in-Double)
    # revNum: Revolution number at epoch (in-Integer)
    dllObj.TleUpdateSatFrFieldsGP.restype = c_int
    dllObj.TleUpdateSatFrFieldsGP.argtypes = [
        c_longlong,
        c_char,
        c_char_p,
        c_double,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
    ]

    # This function is similar to TleUpdateSatFrFieldsGP but includes nDotO2 and n2DotO6. Note: satNum, year, day, and
    # ephtype can't be updated.
    # nDotO2 and n2DotO6 values are not used in the SGP4 propagator. However, some users still want to preserve the
    # integrity of all input data.
    # satKey: The satellite's unique key (in-Long)
    # secClass: Security classification (in-Character)
    # satName: Satellite international designator (in-Character[8])
    # bstar: B* drag term (1/er) (ephType = 0, 2) or BTerm - ballistic coefficient (m2/kg) (ephType = 4, XP) (in-Double)
    # elsetNum: Element set number (in-Integer)
    # incli: Orbit inclination (degrees) (in-Double)
    # node: Right ascension of ascending node (degrees) (in-Double)
    # eccen: Eccentricity (in-Double)
    # omega: Argument of perigee (degrees) (in-Double)
    # mnAnomaly: Mean anomaly (degrees) (in-Double)
    # mnMotion: Mean motion  (rev/day) (ephType = 0: Kozai mean motion, ephType = 2: Brouwer mean motion) (in-Double)
    # revNum: Revolution number at epoch (in-Integer)
    # nDotO2: Mean motion derivative (rev/day /2) (in-Double)
    # n2DotO6: Mean motion second derivative (rev/day**2 /6) or agom (ephType = 4, XP) (m2/kg) (in-Double)
    dllObj.TleUpdateSatFrFieldsGP2.restype = c_int
    dllObj.TleUpdateSatFrFieldsGP2.argtypes = [
        c_longlong,
        c_char,
        c_char_p,
        c_double,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
        c_double,
        c_double,
    ]

    # Adds an SP satellite using the individually provided field values.
    # Only applies to SP propagator.
    # satNum: Satellite number (in-Integer)
    # secClass: Security classification (in-Character)
    # satName: Satellite international designator (in-Character[8])
    # epochYr: Element epoch time - year, [YY]YY (in-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (in-Double)
    # bTerm: Ballistic coefficient (m^2/kg) (in-Double)
    # ogParm: Outgassing parameter/Thrust Acceleration (km/s^2) (in-Double)
    # agom: agom (m^2/kg) (in-Double)
    # elsetNum: Element set number (in-Integer)
    # incli: Orbit inclination (degrees) (in-Double)
    # node: Right ascension of ascending node (degrees) (in-Double)
    # eccen: Eccentricity (in-Double)
    # omega: Argument of perigee (degrees) (in-Double)
    # mnAnomaly: Mean anomaly (degrees) (in-Double)
    # mnMotion: Mean motion (rev/day) (in-Double)
    # revNum: Revolution number at epoch (in-Integer)
    dllObj.TleAddSatFrFieldsSP.restype = c_longlong
    dllObj.TleAddSatFrFieldsSP.argtypes = [
        c_int,
        c_char,
        c_char_p,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
    ]

    # This function is similar to TleAddSatFrFieldsSP but designed to be used in Matlab.
    # Only applies to SP propagator.
    # Matlab doesn't correctly return the 19-digit satellite key using TleAddSatFrFieldsSP. This method is an
    # alternative way to return the satKey output.
    # satNum: Satellite number (in-Integer)
    # secClass: Security classification (in-Character)
    # satName: Satellite international designator (in-Character[8])
    # epochYr: Element epoch time - year, [YY]YY (in-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (in-Double)
    # bTerm: Ballistic coefficient (m^2/kg) (in-Double)
    # ogParm: Outgassing parameter/Thrust Acceleration (km/s^2) (in-Double)
    # agom: agom (m^2/kg) (in-Double)
    # elsetNum: Element set number (in-Integer)
    # incli: Orbit inclination (degrees) (in-Double)
    # node: Right ascension of ascending node (degrees) (in-Double)
    # eccen: Eccentricity (in-Double)
    # omega: Argument of perigee (degrees) (in-Double)
    # mnAnomaly: Mean anomaly (degrees) (in-Double)
    # mnMotion: Mean motion (rev/day) (in-Double)
    # revNum: Revolution number at epoch (in-Integer)
    # satKey: The satKey of the newly added TLE on success, a negative value on error. (out-Long)
    dllObj.TleAddSatFrFieldsSPML.restype = None
    dllObj.TleAddSatFrFieldsSPML.argtypes = [
        c_int,
        c_char,
        c_char_p,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
        c_longlong_p,
    ]

    # Updates an SP satellite's data in memory using its individually provided field values. Note: satNum, year, day,
    # and ephtype can't be updated.
    # Only applies to SP propagator.
    # The satellite's unique key will not be changed by this function. If you specify a satKey that does not correspond
    # to a currently loaded TLE, the function will indicate an error.
    # satKey: The satellite's unique key (in-Long)
    # secClass: Security classification (in-Character)
    # satName: Satellite international designator (in-Character[8])
    # bterm: Ballistic coefficient (m^2/kg) (in-Double)
    # ogParm: Outgassing parameter/Thrust Acceleration (km/s^2) (in-Double)
    # agom: agom (m^2/kg) (in-Double)
    # elsetNum: Element set number (in-Integer)
    # incli: Orbit inclination (degrees) (in-Double)
    # node: Right ascension of ascending node (degrees) (in-Double)
    # eccen: Eccentricity (in-Double)
    # omega: Argument of perigee (degrees) (in-Double)
    # mnAnomaly: Mean anomaly (degrees) (in-Double)
    # mnMotion: Mean motion (rev/day) (in-Double)
    # revNum: Revolution number at epoch (in-Integer)
    dllObj.TleUpdateSatFrFieldsSP.restype = c_int
    dllObj.TleUpdateSatFrFieldsSP.argtypes = [
        c_longlong,
        c_char,
        c_char_p,
        c_double,
        c_double,
        c_double,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
    ]

    # Updates the value of a field of a TLE. This function can be used for both GP and SP satellites.
    #
    # The table below indicates which index values correspond to which fields. Make sure to use the appropriate field
    # index for GP TLEs and SP TLEs.  For indexes 5, 15 and 16, the interpretation depends on the ephemeris type of the
    # TLE.
    # satNum (1), Epoch (4), and Ephemeris Type (5) cannot be altered.
    #
    # table
    #
    # 	index
    # 	index Interpretation
    #
    # 1Satellite number
    # 2Security classification
    # 3Satellite international designator
    # 4Epoch
    # 5Ephemeris type = 0,2: B* drag term (1/er) Ephemeris type = 6   : SP radiation pressure
    # coefficient agom (m2/kg)
    # 6Ephemeris type
    # 7Element set number
    # 8Orbit inclination (degrees)
    # 9Right ascension of ascending node (degrees)
    # 10Eccentricity
    # 11Argument of perigee (degrees)
    # 12Mean anomaly (degrees)
    # 13Mean motion (rev/day)
    # 14Revolution number at epoch
    # 15Ephemeris type = 0: SGP mean motion derivative (rev/day /2) or Ephemeris type = 6: SP
    # ballistic coefficient (m2/kg)
    # 16Ephemeris type = 0: SGP mean motion second derivative (rev/day**2 /6) or Ephemeris type = 6:
    # SP Outgassing parameter/Thrust Acceleration (km/s2)
    #
    # satKey: The satellite's unique key. (in-Long)
    # xf_Tle: Predefined number specifying which field to set. See remarks. (in-Integer)
    # valueStr: The new value of the specified field, expressed as a string. (in-Character[512])
    dllObj.TleSetField.restype = c_int
    dllObj.TleSetField.argtypes = [c_longlong, c_int, c_char_p]

    # Retrieves the value of a specific field of a TLE.
    #
    # The table below indicates which index values correspond to which fields. Make sure to use the appropriate field
    # index for GP TLEs and SP TLEs.  For indexes 5, 15 and 16, the interpretation depends on the ephemeris type of the
    # TLE.
    #
    # table
    #
    # 	index
    # 	index Interpretation
    #
    # 1Satellite number
    # 2Security classification
    # 3Satellite international designator
    # 4Epoch
    # 5Ephemeris type = 0,2: B* drag term (1/er) Ephemeris type = 6   : SP radiation pressure
    # coefficient agom (m2/kg)
    # 6Ephemeris type
    # 7Element set number
    # 8Orbit inclination (degrees)
    # 9Right ascension of ascending node (degrees)
    # 10Eccentricity
    # 11Argument of perigee (degrees)
    # 12Mean anomaly (degrees)
    # 13Mean motion (rev/day)
    # 14Revolution number at epoch
    # 15Ephemeris type = 0: SGP mean motion derivative (rev/day /2) or Ephemeris type = 6: SP
    # ballistic coefficient (m2/kg)
    # 16Ephemeris type = 0: SGP mean motion second derivative (rev/day**2 /6) or Ephemeris type = 6:
    # SP Outgassing parameter/Thrust Acceleration (km/s2)
    #
    # satKey: The satellite's unique key. (in-Long)
    # xf_Tle: Predefined number specifying which field to retrieve. See remarks. (in-Integer)
    # valueStr: A string to contain the value of the requested field. (out-Character[512])
    dllObj.TleGetField.restype = c_int
    dllObj.TleGetField.argtypes = [c_longlong, c_int, c_char_p]

    # Retrieves all of the data for a GP satellite in a single function call.
    # This function only works for GP satellites. The field values are placed in the corresponding parameters of the
    # function.
    # satKey: The satellite's unique key (in-Long)
    # satNum: Satellite number (out-Integer)
    # secClass: Security classification (out-Character)
    # satName: Satellite international designator (out-Character[8])
    # epochYr: Element epoch time - year, [YY]YY (out-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (out-Double)
    # bstar: B* drag term (1/er) (ephType = 0, 2) or BTerm - ballistic coefficient (m2/kg) (ephType = 4,
    # XP) (out-Double)
    # ephType: Satellite ephemeris type (0: SGP, 2: SGP4, 6: SP) (out-Integer)
    # elsetNum: Element set number (out-Integer)
    # incli: Orbit inclination (degrees) (out-Double)
    # node: Right ascension of ascending node (degrees) (out-Double)
    # eccen: Eccentricity (out-Double)
    # omega: Argument of perigee (degrees) (out-Double)
    # mnAnomaly: Mean anomaly (deg) (out-Double)
    # mnMotion: Mean motion (rev/day) (ephType = 0: Kozai mean motion, ephType = 2 or 4: Brouwer mean
    # motion) (out-Double)
    # revNum: Revolution number at epoch (out-Integer)
    dllObj.TleGetAllFieldsGP.restype = c_int
    dllObj.TleGetAllFieldsGP.argtypes = [
        c_longlong,
        c_int_p,
        c_char_p,
        c_char_p,
        c_int_p,
        c_double_p,
        c_double_p,
        c_int_p,
        c_int_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_int_p,
    ]

    # Retrieves all of the data (including nDotO2 and n2DotO6) for a GP satellite in a single function call.
    # This function is similar to TleGetAllFieldsGP but also includes nDotO2 and n2DotO6.
    # This function only works for GP satellites. The field values are placed in the corresponding parameters of the
    # function.
    # satKey: The satellite's unique key (in-Long)
    # satNum: Satellite number (out-Integer)
    # secClass: Security classification (out-Character)
    # satName: Satellite international designator (out-Character[8])
    # epochYr: Element epoch time - year, [YY]YY (out-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (out-Double)
    # bstar: B* drag term (1/er) (ephType = 0, 2) or BTerm - ballistic coefficient (m2/kg) (ephType = 4,
    # XP) (out-Double)
    # ephType: Satellite ephemeris type (0: SGP, 2: SGP4, 6: SP) (out-Integer)
    # elsetNum: Element set number (out-Integer)
    # incli: Orbit inclination (degrees) (out-Double)
    # node: Right ascension of ascending node (degrees) (out-Double)
    # eccen: Eccentricity (out-Double)
    # omega: Argument of perigee (degrees) (out-Double)
    # mnAnomaly: Mean anomaly (degrees) (out-Double)
    # mnMotion: Mean motion (rev/day) (ephType = 0: Kozai mean motion, ephType = 2 or 4: Brouwer mean
    # motion) (out-Double)
    # revNum: Revolution number at epoch (out-Integer)
    # nDotO2: Mean motion derivative (rev/day /2) (out-Double)
    # n2DotO6: Mean motion second derivative (rev/day**2 /6) or agom (ephType = 4, XP) (m2/kg) (out-Double)
    dllObj.TleGetAllFieldsGP2.restype = c_int
    dllObj.TleGetAllFieldsGP2.argtypes = [
        c_longlong,
        c_int_p,
        c_char_p,
        c_char_p,
        c_int_p,
        c_double_p,
        c_double_p,
        c_int_p,
        c_int_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_int_p,
        c_double_p,
        c_double_p,
    ]

    # Retrieves all of the data for an SP satellite in a single function call.
    # Only applies to SP propagator.
    # This function only works for SP satellites. The field values are placed in the corresponding parameters of the
    # function.
    # satKey: The satellite's unique key (in-Long)
    # satNum: Satellite number (out-Integer)
    # secClass: Security classification (out-Character)
    # satName: Satellite international designator (out-Character[8])
    # epochYr: Element epoch time - year, [YY]YY (out-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (out-Double)
    # bTerm: Ballistic coefficient (m^2/kg) (out-Double)
    # ogParm: Outgassing parameter/Thrust Acceleration (km/s^2) (out-Double)
    # agom: Agom (m^2/kg) (out-Double)
    # elsetNum: Element set number (out-Integer)
    # incli: Orbit inclination (degrees) (out-Double)
    # node: Right ascension of ascending node (degrees) (out-Double)
    # eccen: Eccentricity (out-Double)
    # omega: Argument of perigee (degrees) (out-Double)
    # mnAnomaly: Mean anomaly (degrees) (out-Double)
    # mnMotion: Mean motion (rev/day) (out-Double)
    # revNum: Revolution number at epoch (out-Integer)
    dllObj.TleGetAllFieldsSP.restype = c_int
    dllObj.TleGetAllFieldsSP.argtypes = [
        c_longlong,
        c_int_p,
        c_char_p,
        c_char_p,
        c_int_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_int_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_int_p,
    ]

    # Parses GP data from the input first and second lines of a two line element set or a CSV Tle.
    # This function only parses data from the input TLE but DOES NOT load/add the input TLE to memory.
    # line1: The first line of the two line element set or a CSV tle (in-Character[512])
    # line2: The second line of the two line element set or an empty string for a CVS tle (in-Character[512])
    # satNum: Satellite number (out-Integer)
    # secClass: Security classification (out-Character)
    # satName: Satellite international designator (out-Character[8])
    # epochYr: Element epoch time - year, [YY]YY (out-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (out-Double)
    # nDotO2: n-dot/2 (for SGP, ephType = 0) (out-Double)
    # n2DotO6: n-double-dot/6 (for SGP, ephType = 0) or agom (ephType = 4, XP) (m2/kg) (out-Double)
    # bstar: B* drag term (1/er) (ephType = 0, 2) or BTerm - ballistic coefficient (m2/kg) (ephType = 4,
    # XP) (out-Double)
    # ephType: Satellite ephemeris type (0: SGP, 2: SGP4, 6: SP) (out-Integer)
    # elsetNum: Element set number (out-Integer)
    # incli: Orbit inclination (degrees) (out-Double)
    # node: Right ascension of ascending node (degrees) (out-Double)
    # eccen: Eccentricity (out-Double)
    # omega: Argument of perigee (degrees) (out-Double)
    # mnAnomaly: Mean anomaly (degrees) (out-Double)
    # mnMotion: Mean motion (rev/day) (ephType = 0: Kozai mean motion, ephType = 2 or 4: Brouwer mean
    # motion) (out-Double)
    # revNum: Revolution number at epoch (out-Integer)
    dllObj.TleParseGP.restype = c_int
    dllObj.TleParseGP.argtypes = [
        c_char_p,
        c_char_p,
        c_int_p,
        c_char_p,
        c_char_p,
        c_int_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_int_p,
        c_int_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_int_p,
    ]

    # Parses GP data from the input first and second lines of a two line element set or a CSV tle and store that data
    # back into the output parameters.
    # This function only parses data from the input TLE but DOES NOT load/add the input TLE to memory.
    # line1: The first line of the two line element set or a CSV tle (in-Character[512])
    # line2: The second line of the two line element set or an empty string for a CVS tle (in-Character[512])
    # xa_tle: Array containing TLE's numerical fields, see XA_TLE_? for array arrangement (out-Double[64])
    # xs_tle: Output string that contains all TLE's text fields, see XS_TLE_? for column
    # arrangement (out-Character[512])
    dllObj.TleLinesToArray.restype = c_int
    dllObj.TleLinesToArray.argtypes = [c_char_p, c_char_p, c_double * 64, c_char_p]

    # Parses SP data from the input first and second lines of a two line element set.
    # Only applies to SP propagator.
    # This function only parses data from the input TLE but DOES NOT load/add the input TLE to memory.
    # line1: The first line of the two line element set (in-Character[512])
    # line2: The second line of the two line element set (in-Character[512])
    # satNum: Satellite number (out-Integer)
    # secClass: Security classification (out-Character)
    # satName: Satellite international designator (out-Character[8])
    # epochYr: Element epoch time - year, [YY]YY (out-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (out-Double)
    # bTerm: Ballistic coefficient (m^2/kg) (out-Double)
    # ogParm: Outgassing parameter/Thrust Acceleration (km/s^2) (out-Double)
    # agom: Agom (m^2/kg) (out-Double)
    # elsetNum: Element set number (out-Integer)
    # incli: Orbit inclination (degrees) (out-Double)
    # node: Right ascension of ascending node (degrees) (out-Double)
    # eccen: Eccentricity (out-Double)
    # omega: Argument of perigee (degrees) (out-Double)
    # mnAnomaly: Mean anomaly (degrees) (out-Double)
    # mnMotion: Mean motion (rev/day) (out-Double)
    # revNum: Revolution number at epoch (out-Integer)
    dllObj.TleParseSP.restype = c_int
    dllObj.TleParseSP.argtypes = [
        c_char_p,
        c_char_p,
        c_int_p,
        c_char_p,
        c_char_p,
        c_int_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_int_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_double_p,
        c_int_p,
    ]

    # Returns the first and second lines representation of a TLE of a satellite.
    # satKey: The satellite's unique key. (in-Long)
    # line1: A string to hold the first line of the TLE (out-Character[512])
    # line2: A string to hold the second line of the TLE (out-Character[512])
    dllObj.TleGetLines.restype = c_int
    dllObj.TleGetLines.argtypes = [c_longlong, c_char_p, c_char_p]

    # Returns the CSV string representation of a TLE of a satellite.
    # satKey: The satellite's unique key. (in-Long)
    # csvLine: A string to hold the TLE in csv format. (out-Character[512])
    dllObj.TleGetCsv.restype = c_int
    dllObj.TleGetCsv.argtypes = [c_longlong, c_char_p]

    # Constructs a TLE from individually provided GP data fields.
    # This function only parses data from the input fields but DOES NOT load/add the TLE to memory.
    # Returned line1 and line2 will be empty if the function fails to construct the lines as requested.
    # satNum: Satellite number (in-Integer)
    # secClass: Security classification (in-Character)
    # satName: Satellite international designator (in-Character[8])
    # epochYr: Element epoch time - year, [YY]YY (in-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (in-Double)
    # nDotO2: N Dot/2 (rev/day /2) (in-Double)
    # n2DotO6: N Double Dot/6 (rev/day**2 /6) or agom (ephType = 4, XP) (m2/kg) (in-Double)
    # bstar: B* drag term (1/er) (ephType = 0, 2) or BTerm - ballistic coefficient (m2/kg) (ephType = 4, XP) (in-Double)
    # ephType: Satellite ephemeris type (0: SGP, 2: SGP4) (in-Integer)
    # elsetNum: Element set number (in-Integer)
    # incli: Orbit inclination (degrees) (in-Double)
    # node: Right ascension of ascending node (degrees) (in-Double)
    # eccen: Eccentricity (in-Double)
    # omega: Argument of perigee (degrees) (in-Double)
    # mnAnomaly: Mean anomaly (degrees) (in-Double)
    # mnMotion: Mean motion (rev/day) (ephType = 0: Kozai mean motion, ephType = 2 or 4: Brouwer mean
    # motion) (in-Double)
    # revNum: Revolution number at epoch (in-Integer)
    # line1: Returned first line of a TLE. (out-Character[512])
    # line2: Returned second line of a TLE. (out-Character[512])
    dllObj.TleGPFieldsToLines.restype = None
    dllObj.TleGPFieldsToLines.argtypes = [
        c_int,
        c_char,
        c_char_p,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
        c_char_p,
        c_char_p,
    ]

    # Constructs a TLE from individually provided GP data fields.
    # This function only parses data from the input fields but DOES NOT load/add the TLE to memory.
    # Returned line1 and line2 will be empty if the function fails to construct the lines as requested.
    # satNum: Satellite number (in-Integer)
    # secClass: Security classification (in-Character)
    # satName: Satellite international designator (in-Character[8])
    # epochYr: Element epoch time - year, [YY]YY (in-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (in-Double)
    # nDotO2: N Dot/2 (rev/day /2) (in-Double)
    # n2DotO6: N Double Dot/6 (rev/day**2 /6) or agom (ephType = 4, XP) (m2/kg) (in-Double)
    # bstar: B* drag term (1/er) (ephType = 0, 2) or BTerm - ballistic coefficient (m2/kg) (ephType = 4, XP) (in-Double)
    # ephType: Satellite ephemeris type (0: SGP, 2: SGP4) (in-Integer)
    # elsetNum: Element set number (in-Integer)
    # incli: Orbit inclination (degrees) (in-Double)
    # node: Right ascension of ascending node (degrees) (in-Double)
    # eccen: Eccentricity (in-Double)
    # omega: Argument of perigee (degrees) (in-Double)
    # mnAnomaly: Mean anomaly (degrees) (in-Double)
    # mnMotion: Mean motion (rev/day) (ephType = 0: Kozai mean motion, ephType = 2 or 4: Brouwer mean
    # motion) (in-Double)
    # revNum: Revolution number at epoch (in-Integer)
    # csvLine: A string to hold the TLE in csv format. (out-Character[512])
    dllObj.TleGPFieldsToCsv.restype = None
    dllObj.TleGPFieldsToCsv.argtypes = [
        c_int,
        c_char,
        c_char_p,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
        c_char_p,
    ]

    # Constructs a TLE from GP data stored in the input parameters.
    # This function only parses data from the input data but DOES NOT load/add the TLE to memory.
    #
    # Returned line1 and line2 will be empty if the function fails to construct the lines as requested.
    # xa_tle: Array containing TLE's numerical fields, see XA_TLE_? for array arrangement (in-Double[64])
    # xs_tle: Input string that contains all TLE's text fields, see XS_TLE_? for column arrangement (in-Character[512])
    # line1: Returned first line of a TLE (out-Character[512])
    # line2: Returned second line of a TLE (out-Character[512])
    dllObj.TleGPArrayToLines.restype = None
    dllObj.TleGPArrayToLines.argtypes = [c_double * 64, c_char_p, c_char_p, c_char_p]

    # Constructs a TLE from GP data stored in the input parameters.
    # This function only parses data from the input data but DOES NOT load/add the TLE to memory.
    # Returned line1 and line2 will be empty if the function fails to construct the lines as requested.
    # xa_tle: Array containing TLE's numerical fields, see XA_TLE_? for array arrangement (in-Double[64])
    # xs_tle: Input string that contains all TLE's text fields, see XS_TLE_? for column arrangement (in-Character[512])
    # csvline: Returned csv format elements. (out-Character[512])
    dllObj.TleGPArrayToCsv.restype = None
    dllObj.TleGPArrayToCsv.argtypes = [c_double * 64, c_char_p, c_char_p]

    # Constructs a TLE from individually provided SP data fields.
    # Only applies to SP propagator.
    # This function only parses data from the input fields but DOES NOT load/add the TLE to memory.
    # Returned line1 and line2 will be empty if the function fails to construct the lines as requested.
    # satNum: Satellite number (in-Integer)
    # secClass: Security classification (in-Character)
    # satName: Satellite international designator (in-Character[8])
    # epochYr: Element epoch time - year, [YY]YY (in-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (in-Double)
    # bTerm: Ballistic coefficient (m^2/kg) (in-Double)
    # ogParm: Outgassing parameter/Thrust Acceleration (km/s^2) (in-Double)
    # agom: Agom (m^2/kg) (in-Double)
    # elsetNum: Element set number (in-Integer)
    # incli: Orbit inclination (degrees) (in-Double)
    # node: Right ascension of ascending node (degrees) (in-Double)
    # eccen: Eccentricity (in-Double)
    # omega: Argument of perigee (degrees) (in-Double)
    # mnAnomaly: Mean anomaly (degrees) (in-Double)
    # mnMotion: Mean motion (rev/day) (in-Double)
    # revNum: Revolution number at epoch (in-Integer)
    # line1: Returned first line of a TLE. (out-Character[512])
    # line2: Returned second line of a TLE. (out-Character[512])
    dllObj.TleSPFieldsToLines.restype = None
    dllObj.TleSPFieldsToLines.argtypes = [
        c_int,
        c_char,
        c_char_p,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_double,
        c_int,
        c_char_p,
        c_char_p,
    ]

    # Returns the first satKey from the currently loaded set of TLEs that contains the specified satellite number.
    # This function is useful when Tle.dll is used in applications that require only one record (one TLE entry) for one
    # satellite, and which refer to that TLE by its satellite number. This function can be used to retrieve a satKey in
    # that situation, which is useful since the Standardized Astrodynamic Algorithms library works only with satKeys.
    # A negative value will be returned if there is an error.
    # satNum: Satellite number (in-Integer)
    dllObj.TleGetSatKey.restype = c_longlong
    dllObj.TleGetSatKey.argtypes = [c_int]

    # This function is similar to TleGetSatKey but designed to be used in Matlab.
    # Matlab doesn't correctly return the 19-digit satellite key using TleGetSatKey. This method is an alternative way
    # to return the satKey output.
    # This function is useful when Tle.dll is used in applications that require only one record (one TLE entry) for one
    # satellite, and which refer to that TLE by its satellite number. This function can be used to retrieve a satKey in
    # that situation, which is useful since the Standardized Astrodynamic Algorithms library works only with satKeys.
    # A negative value will be returned in satKey if there is an error.
    # satNum: Satellite number (in-Integer)
    # satKey: The satKey of the satellite if a satellite with the requested number is found in the set of loaded
    # satellites, a negative value if there is an error. (out-Long)
    dllObj.TleGetSatKeyML.restype = None
    dllObj.TleGetSatKeyML.argtypes = [c_int, c_longlong_p]

    # Computes a satKey from the input data.
    # There is no need for a matching satellite to be loaded prior to using this function. The function simply computes
    # the satKey from the provided fields.
    #
    # This is the proper way to reconstruct a satKey from its fields. If you use your own routine to do this, the
    # computed satKey might be different.
    # A negative value will be returned if there is an error.
    # satNum: Satellite number (in-Integer)
    # epochYr: Element epoch time - year, [YY]YY (in-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (in-Double)
    # ephType: Ephemeris type (in-Integer)
    dllObj.TleFieldsToSatKey.restype = c_longlong
    dllObj.TleFieldsToSatKey.argtypes = [c_int, c_int, c_double, c_int]

    # This function is similar to TleFieldsToSatKey but designed to be used in Matlab.
    # Matlab doesn't correctly return the 19-digit satellite key using TleFieldsToSatKey. This method is an alternative
    # way to return the satKey output.
    # There is no need for a matching satellite to be loaded prior to using this function. The function simply computes
    # the satKey from the provided fields.
    #
    # This is the proper way to reconstruct a satKey from its fields. If you use your own routine to do this, the
    # computed satKey might be different.
    # A negative value will be returned in satKey if there is an error.
    # satNum: Satellite number (in-Integer)
    # epochYr: Element epoch time - year, [YY]YY (in-Integer)
    # epochDays: Element epoch time - day of year, DDD.DDDDDDDD (in-Double)
    # ephType: Ephemeris type (in-Integer)
    # satKey: The satKey if the computation is successful, a negative value if there is an error. (out-Long)
    dllObj.TleFieldsToSatKeyML.restype = None
    dllObj.TleFieldsToSatKeyML.argtypes = [c_int, c_int, c_double, c_int, c_longlong_p]

    # Adds a TLE (satellite), using its data stored in the input parameters.
    # xa_tle: Array containing TLE's numerical fields, see XA_TLE_? for array arrangement (in-Double[64])
    # xs_tle: Input string that contains all TLE's text fields, see XS_TLE_? for column arrangement (in-Character[512])
    dllObj.TleAddSatFrArray.restype = c_longlong
    dllObj.TleAddSatFrArray.argtypes = [c_double * 64, c_char_p]

    # This function is similar to TleAddSatFrArray but designed to be used in Matlab.
    # xa_tle: Array containing TLE's numerical fields, see XA_TLE_? for array arrangement (in-Double[64])
    # xs_tle: Input string that contains all TLE's text fields, see XS_TLE_? for column arrangement (in-Character[512])
    # satKey: The satKey of the newly added TLE on success, a negative value on error. (out-Long)
    dllObj.TleAddSatFrArrayML.restype = None
    dllObj.TleAddSatFrArrayML.argtypes = [c_double * 64, c_char_p, c_longlong_p]

    # Updates existing TLE data with the provided new data stored in the input parameters. Note: satNum, year, day, and
    # ephtype can't be updated.
    # nDotO2 and n2DotO6 values are not used in the SGP4 propagator. However, some users still want to preserve the
    # integrity of all input data.
    # satKey: The satellite's unique key (in-Long)
    # xa_tle: Array containing TLE's numerical fields, see XA_TLE_? for array arrangement (in-Double[64])
    # xs_tle: Input string that contains all TLE's text fields, see XS_TLE_? for column arrangement (in-Character[512])
    dllObj.TleUpdateSatFrArray.restype = c_int
    dllObj.TleUpdateSatFrArray.argtypes = [c_longlong, c_double * 64, c_char_p]

    # Retrieves TLE data and stored it in the passing parameters
    # satKey: The satellite's unique key (in-Long)
    # xa_tle: Array containing TLE's numerical fields, see XA_TLE_? for array arrangement (out-Double[64])
    # xs_tle: Output string that contains all TLE's text fields, see XS_TLE_? for column
    # arrangement (out-Character[512])
    dllObj.TleDataToArray.restype = c_int
    dllObj.TleDataToArray.argtypes = [c_longlong, c_double * 64, c_char_p]

    # Converts TLE two line format to CSV format
    # line1: The first line of a two line element set (in-Character[512])
    # line2: The second line of a two line element set (in-Character[512])
    # csvline: A string to hold the TLE in csv format. (out-Character[512])
    dllObj.TleLinesToCsv.restype = c_int
    dllObj.TleLinesToCsv.argtypes = [c_char_p, c_char_p, c_char_p]

    # Converts TLE CSV format to two line format
    # csvLine: The input TLE in CSV format (in-Character[512])
    # newSatno: New satellite number to replace what's in CSV obs if desired (won't use/renumber if it's
    # zero) (in-Integer)
    # line1: The output first line of the two line element set (out-Character[512])
    # line2: The output second line of the two line element set (out-Character[512])
    dllObj.TleCsvToLines.restype = c_int
    dllObj.TleCsvToLines.argtypes = [c_char_p, c_int, c_char_p, c_char_p]

    # Sets TLE key mode - This function was deprecated, please use DllMain/SetElsetKeyMode() instead
    # tle_keyMode: Desired Tle key mode (in-Integer)
    dllObj.SetTleKeyMode.restype = c_int
    dllObj.SetTleKeyMode.argtypes = [c_int]

    # Gets current TLE key mode - This function was deprecated, please use DllMain/GetElsetKeyMode() instead
    dllObj.GetTleKeyMode.restype = c_int
    dllObj.GetTleKeyMode.argtypes = []

    # Finds the check sums of TLE lines
    # line1: The input TLE line 1 in TLE format (in-Character[512])
    # line2: The input TLE line 2 in TLE format (in-Character[512])
    # chkSum1: Check Sum of Line 1 (out-Integer)
    # chkSum2: Check Sum of Line 2 (out-Integer)
    # errCode: Error code - 0 if successful, non-0 if there is an error (out-Integer)
    dllObj.GetCheckSums.restype = None
    dllObj.GetCheckSums.argtypes = [c_char_p, c_char_p, c_int_p, c_int_p, c_int_p]

    return dllObj


# TLE types (TLE ephemeris types) - They are different than ELTTYPE
# TLE SGP elset (Kozai mean motion)
TLETYPE_SGP = 0
# TLE SGP4 elset (Brouwer mean motion)
TLETYPE_SGP4 = 2
# TLE SGP4-XP elset (Brouwer mean motion)
TLETYPE_XP = 4
# TLE SP elset (osculating elements)
TLETYPE_SP = 6

# Indexes of TLE data fields
# Satellite number
XF_TLE_SATNUM = 1
# Security classification U: unclass, C: confidential, S: Secret
XF_TLE_CLASS = 2
# Satellite name A8
XF_TLE_SATNAME = 3
# Satellite's epoch time "YYYYJJJ.jjjjjjjj"
XF_TLE_EPOCH = 4
# GP B* drag term (1/er)  (not the same as XF_TLE_BTERM)
XF_TLE_BSTAR = 5
# Satellite ephemeris type: 0=SGP, 2=SGP4, 4=SGP4-XP, 6=SP
XF_TLE_EPHTYPE = 6
# Element set number
XF_TLE_ELSETNUM = 7
# Orbit inclination (deg)
XF_TLE_INCLI = 8
# Right ascension of asending node (deg)
XF_TLE_NODE = 9
# Eccentricity
XF_TLE_ECCEN = 10
# Argument of perigee (deg)
XF_TLE_OMEGA = 11
# Mean anomaly (deg)
XF_TLE_MNANOM = 12
# Mean motion (rev/day) (ephType=0: Kozai, ephType=2: Brouwer)
XF_TLE_MNMOTN = 13
# Revolution number at epoch
XF_TLE_REVNUM = 14

# GP Mean motion derivative (rev/day /2)
XF_TLE_NDOT = 15
# GP Mean motion second derivative (rev/day**2 /6)
XF_TLE_NDOTDOT = 16
# Solar radiation pressure GP (m2/kg)
XF_TLE_AGOMGP = 16

# SP Radiation Pressure Coefficient
XF_TLE_SP_AGOM = 5
# SP ballistic coefficient (m2/kg)
XF_TLE_SP_BTERM = 15
# SP outgassing parameter (km/s2)
XF_TLE_SP_OGPARM = 16

# Original satellite number
XF_TLE_ORGSATNUM = 17
# GP ballistic coefficient (m2/kg) (not the same as XF_TLE_BSTAR)
XF_TLE_BTERM = 18
# Time of last observation relative to epoch +/- fractional days
XF_TLE_OBSTIME = 19
# Last calculated error growth rate (km/day)
XF_TLE_EGR = 20
# Last calculated energy dissipation rate (w/kg)
XF_TLE_EDR = 21
# Median Vismag
XF_TLE_VISMAG = 22
# Median RCS - diameter in centimeters (cm)
XF_TLE_RCS = 23
# Object Type (Payload, Rocket Body, Platform, Debris, Unknown)
XF_TLE_OBJTYPE = 24
# Satellite name A12 (upto 12 character long)
XF_TLE_SATNAME_12 = 25


# Indexes of TLE numerical data in an array
# Line 1
# Satellite number
XA_TLE_SATNUM = 0
# Satellite's epoch time in DS50UTC
XA_TLE_EPOCH = 1
# GP Mean motion derivative (rev/day /2)
XA_TLE_NDOT = 2
# GP Mean motion second derivative (rev/day**2 /6)
XA_TLE_NDOTDOT = 3
# GP B* drag term (1/er)
XA_TLE_BSTAR = 4
# Satellite ephemeris type: 0=SGP, 2=SGP4, 4=SGP4-XP, 6=SP
XA_TLE_EPHTYPE = 5

# Line 2
# Orbit inclination (deg)
XA_TLE_INCLI = 20
# Right ascension of asending node (deg)
XA_TLE_NODE = 21
# Eccentricity
XA_TLE_ECCEN = 22
# Argument of perigee (deg)
XA_TLE_OMEGA = 23
# Mean anomaly (deg)
XA_TLE_MNANOM = 24
# Mean motion (rev/day) (ephType=0, 4: Kozai, ephType=2: Brouwer)
XA_TLE_MNMOTN = 25
# Revolution number at epoch
XA_TLE_REVNUM = 26
# Element set number
XA_TLE_ELSETNUM = 30

# CSV (or TLE-XP, ephemType=4) specific fields
# Original satellite number
XA_TLE_ORGSATNUM = 31
# SP/SGP4-XP ballistic coefficient (m2/kg)
XA_TLE_BTERM = 32
# Time of last observation relative to epoch +/- fractional days
XA_TLE_OBSTIME = 33
# Last calculated error growth rate (km/day)
XA_TLE_EGR = 34
# Last calculated energy dissipation rate (w/kg)
XA_TLE_EDR = 35
# Median Vismag
XA_TLE_VISMAG = 36
# Median RCS - diameter in centimeters (cm)
XA_TLE_RCS = 37

# CSV (or TLE-XP, ephemType=4)
# Solar Radiation Pressure Coefficient GP (m2/kg)
XA_TLE_AGOMGP = 38


# SP specific fields
# SP ballistic coefficient (m2/kg)
XA_TLE_SP_BTERM = 2
# SP outgassing parameter (km/s2)
XA_TLE_SP_OGPARM = 3
# SP Radiation Pressure Coefficient
XA_TLE_SP_AGOM = 4

XA_TLE_SIZE = 64

# Indexes of TLE text data in an array of chars
# Security classification of line 1 and line 2
XS_TLE_SECCLASS_1 = 0
# Satellite name
XS_TLE_SATNAME_12 = 1
# Object Type (Payload, Rocket Body, Platform, Debris, Unknown) - csv only
XS_TLE_OBJTYPE_11 = 13

XS_TLE_SIZE = 512

# TLE's text data fields - new convention (start index, string length)
# Security classification of line 1 and line 2
XS_TLE_SECCLASS_0_1 = 0
# Satellite name
XS_TLE_SATNAME_1_12 = 1
# Object Type (Payload, Rocket Body, Platform, Debris, Unknown) - csv only
XS_TLE_OBJTYPE_13_1 = 13

XS_TLE_LENGTH = 512

# Indexes of different TLE file's formats
# Original TLE format
XF_TLEFORM_ORG = 0
# CSV format
XF_TLEFORM_CSV = 1


# ========================= End of auto generated code ==========================
