# This wrapper file was generated automatically by the GenDllWrappers program.
import platform
from ctypes import CDLL, POINTER, c_char_p, c_double, c_int, c_longlong, c_void_p
from pathlib import Path

c_int_p = POINTER(c_int)
c_longlong_p = POINTER(c_longlong)
c_double_p = POINTER(c_double)

LIB_PATH = Path(__file__).parent

# get the right filename of the dll/so
if platform.uname()[0] == "Windows":
    DLL_NAME = LIB_PATH / "TimeFunc.dll"

if platform.uname()[0] == "Linux":
    DLL_NAME = LIB_PATH / "libtimefunc.so"

if platform.uname()[0] == "Darwin":
    DLL_NAME = LIB_PATH / "libtimefunc.dylib"


def get_time_func_dll():
    """LoadTimeFuncDll() -- Loads TimeFunc.dll from the PATH or LD_LIBRARY_PATH
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
    # Initializes the TimeFunc DLL for use in the program.
    # If this function returns an error, it is recommended that you stop the program immediately.
    #
    # An error will occur if you forget to load and initialize all the prerequisite DLLs, as listed in the DLL
    # Prerequisites section of the accompanying documentation, before using this DLL.
    # apAddr: The pointer that was returned from DllMain.DllMainInit (in-Long)
    dllObj.TimeFuncInit.restype = c_int
    dllObj.TimeFuncInit.argtypes = [c_longlong]

    # Returns the information about the TimeFunc DLL.  The information is placed in the string parameter you pass in.
    # The returned string provides information about the version number, build date, and the platform of the TimeFunc
    # DLL.
    # infoStr: A string to hold the information about TimeFunc.dll. (out-Character[128])
    dllObj.TimeFuncGetInfo.restype = None
    dllObj.TimeFuncGetInfo.argtypes = [c_char_p]

    # Loads timing constants data from an input file.
    # Time constants can be included directly in the main input file or they can be read from a separate file
    # identified with "TIMFIL=[pathname\filename]".
    #
    # The input file is read in two passes. The function first looks for "TIMFIL=" lines, then it looks for timing
    # constant data which was included directly. The result of this is that data entered using both methods will be
    # processed, but the "TIMFIL=" data will be processed first.
    #
    # The time constants are also read in from each VCM. However, only the most recent time constants among VCMs are
    # stored in the memory, see VCM.dll documentation.
    # See the "Time Constants Data Description" section in the accompanying TimeFunc documentation file for supported
    # formats.
    # tconFile: The name of the file from which to read timing constants data. (in-Character[512])
    dllObj.TConLoadFile.restype = c_int
    dllObj.TConLoadFile.argtypes = [c_char_p]

    # Loads timing constants data and prediction control (6P-card) from an input file.
    # Time constants can be included directly in the main input file or they can be read from a separate file
    # identified with "TIMFIL=[pathname\filename]".
    #
    # The input file is read in two passes. The function first looks for "TIMFIL=" lines, then it looks for timing
    # constant data which was included directly. The result of this is that data entered using both methods will be
    # processed, but the "TIMFIL=" data will be processed first.
    #
    # The time constants are also read in from each VCM. However, only the most recent time constants among VCMs are
    # stored in the memory, see VCM.dll documentation.
    # tconFile: The name of the file from which to read timing constants data and/or prediction control
    # data. (in-Character[512])
    dllObj.TimeFuncLoadFile.restype = c_int
    dllObj.TimeFuncLoadFile.argtypes = [c_char_p]

    # Checks to see if timing constants have been loaded into memory.
    # The timing constants can be loaded from a timing constants file or from VCM(s).  See TConLoadFile, TConAddOne,
    # and TConAddARec functions.
    dllObj.IsTConFileLoaded.restype = c_int
    dllObj.IsTConFileLoaded.argtypes = []

    # Saves currently loaded timing constants data to a file.
    # The data will be saved in the format specified by the form parameter, regardless of the format or method
    # originally used to load it.
    # tconFile: The name of the file in which to save the timing constants data. (in-Character[512])
    # saveMode: Specifies whether to create a new file or append to an existing one. (0 = Create new file,
    # 1= Append to existing file) (in-Integer)
    # saveForm: Specifies the format in which to save the file. (0 = SPECTER Print Record format,
    # 1 = XML format (future implementation)) (in-Integer)
    dllObj.TConSaveFile.restype = c_int
    dllObj.TConSaveFile.argtypes = [c_char_p, c_int, c_int]

    # Adds a timing constant record to memory. Note that this function is solely for backward compatible with legacy
    # software.
    # Notes: only the latest timing record is stored in memory using this method. Input timing record will be
    # skipped/ignored if it's earlier than the existing one
    # The users should use TConLoadFile or TimeFuncLoadFile to load timing constants file instead.
    # refDs50UTC: Reference time (days since 1950, UTC) (in-Double)
    # leapDs50UTC: Leap Second time (days since 1950, UTC) (in-Double)
    # taiMinusUTC: TAI minus UTC offset at the reference time (seconds) (in-Double)
    # ut1MinusUTC: UT1 minus UTC offset at the reference time (seconds) (in-Double)
    # ut1Rate: UT1 rate of change versus UTC at the reference time (msec/day) (in-Double)
    # polarX: Polar wander (X direction) at the reference time (arc-seconds) (in-Double)
    # polarY: Polar wander (Y direction) at the reference time (arc-seconds) (in-Double)
    dllObj.TConAddARec.restype = c_int
    dllObj.TConAddARec.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double, c_double]

    # Adds one timing constant record to memory. This API can be used to avoid TConLoadFile's file I/O
    # refDs50UTC: Reference time (days since 1950, UTC) (in-Double)
    # taiMinusUTC: TAI minus UTC offset at the reference time (seconds) (in-Double)
    # ut1MinusUTC: UT1 minus UTC offset at the reference time (seconds) (in-Double)
    # ut1Rate: UT1 rate of change versus UTC at the reference time (msec/day) (in-Double)
    # polarX: Polar wander (X direction) at the reference time (arc-seconds) (in-Double)
    # polarY: Polar wander (Y direction) at the reference time (arc-seconds) (in-Double)
    dllObj.TConAddOne.restype = c_int
    dllObj.TConAddOne.argtypes = [c_double, c_double, c_double, c_double, c_double, c_double]

    # Retrieves the timing constants record, if exists, at the requested input time in ds50UTC.
    # If the requested record is not found, 0's will be returned for all of the constants. You can use this fact to
    # determine whether the record was found or not. Simply check the taiMinusUTC value after calling this function.
    # Since that value can never be 0 for a valid record, if it is 0 the record was not found.
    # ds50UTC: Input days since 1950, UTC (in-Double)
    # taiMinusUTC: Returned TAI minus UTC offset at requested time (seconds) (out-Double)
    # ut1MinusUTC: Returned UT1 minus UTC offset at requested time (seconds) (out-Double)
    # ut1Rate: Returned UT1 rate of change versus UTC at Reference time (msec/day) (out-Double)
    # polarX: Returned interpolated polar wander (X direction) at requested time (arc-seconds) (out-Double)
    # polarY: Returned interpolated polar wander (Y direction) at requested time (arc-seconds) (out-Double)
    dllObj.UTCToTConRec.restype = None
    dllObj.UTCToTConRec.argtypes = [c_double, c_double_p, c_double_p, c_double_p, c_double_p, c_double_p]

    # Removes all the timing constants records in memory.
    dllObj.TConRemoveAll.restype = c_int
    dllObj.TConRemoveAll.argtypes = []

    # Converts an internal time in ds50UTC to a string in DTG20 format. The resulting string takes the form
    # "YYYY/DDD HHMM SS.SSS".
    # The input ds50UTC must be greater than 2192.0, which corresponds to a time later than 1st Jan 1956. Any input
    # value less than or equal to 2192.0 will yield "1956/001 0000 00.000".
    # ds50UTC: Days since 1950, UTC to be converted. (in-Double)
    # dtg20: A string to hold the result of the conversion. (out-Character[20])
    dllObj.UTCToDTG20.restype = None
    dllObj.UTCToDTG20.argtypes = [c_double, c_char_p]

    # Converts a time in ds50UTC to a time in DTG19 format. The resulting string takes the form "YYYYMonDDHHMMSS.SSS".
    # See "UTCToDTG20" for an example.
    # The input ds50UTC must be greater than 2192.0, which corresponds to a time later than 1st Jan 1956. Any input
    # value less than or equal to 2192.0 will yield "1956Jan01000000.000".
    # Note, the return value is in the DTG19 format "YYYYMonDDHHMMSS.SSS", not the "YY DDD HH MM SS.SSS" format.
    # ds50UTC: Days since 1950, UTC to be converted. (in-Double)
    # dtg19: A string to hold the result of the conversion. (out-Character[19])
    dllObj.UTCToDTG19.restype = None
    dllObj.UTCToDTG19.argtypes = [c_double, c_char_p]

    # Converts a time in ds50UTC to a time in DTG17 format. The resulting string takes the form "YYYY/DDD.DDDDDDDD"
    # format.
    # See "UTCToDTG20" for an example.
    # The input ds50UTC must be greater than 2192.0, which corresponds to a time later than 1st Jan 1956. Any input
    # value less than or equal to 2192.0 will yield "1956/001.00000000".
    # ds50UTC: Days since 1950, UTC to be converted. (in-Double)
    # dtg17: A string to hold the result of the conversion. (out-Character[17])
    dllObj.UTCToDTG17.restype = None
    dllObj.UTCToDTG17.argtypes = [c_double, c_char_p]

    # Converts a time in ds50UTC to a time in DTG15 format. The resulting string takes the form "YYDDDHHMMSS.SSS".
    # See "UTCToDTG20" for an example.
    # The input ds50UTC must be greater than 2192.0, which corresponds to a time later than 1st Jan 1956. Any input
    # value less than or equal to 2192.0 will yield "56001000000.000".
    # ds50UTC: Days since 1950, UTC to be converted. (in-Double)
    # dtg15: A string to hold the result of the conversion. (out-Character[15])
    dllObj.UTCToDTG15.restype = None
    dllObj.UTCToDTG15.argtypes = [c_double, c_char_p]

    # Converts a time in one of the DTG formats to a time in ds50UTC. DTG15, DTG17, DTG19, and DTG20 formats are
    # accepted.
    # See "UTCToDTG20" for an example.
    # During the conversion, this function processes only numbers and the '.' character. This means that you can
    # format dtgStr in a format that makes sense. You can use spaces and the '/' character for example if you wish.
    #
    # The function can process dates from 1950 to 2049. Any input outside this range will yield "0.0".
    # This function supports DTG19 inputs in both "YY DDD HH MM SS.SSS" and "YYYYMonDDHHMMSS.SSS" formats.
    # dtg: The string to convert. Can be any of the DTG formats previously documented. (in-Character[20])
    dllObj.DTGToUTC.restype = c_double
    dllObj.DTGToUTC.argtypes = [c_char_p]

    # Converts a time in ds50UTC to a time in ds50TAI using timing constants records in memory.
    # If no timing constants records were loaded, ds50UTC and ds50TAI are the same.
    # Partial days may be returned.
    # ds50UTC: Days since 1950, UTC to be converted. (in-Double)
    dllObj.UTCToTAI.restype = c_double
    dllObj.UTCToTAI.argtypes = [c_double]

    # Converts a time in ds50UTC to a time in ds50UT1 using timing constants records in memory.
    # If no timing constants records were loaded, ds50UTC and ds50UT1 are the same.
    # Partial days may be returned.
    # ds50UTC: Days since 1950, UTC to be converted. (in-Double)
    dllObj.UTCToUT1.restype = c_double
    dllObj.UTCToUT1.argtypes = [c_double]

    # Converts a time in ds50UTC to a time in ds50ET (Ephemeris Time/Terrestrial Time) using timing constants records
    # in memory.
    # ds50UTC: Days since 1950, UTC to be converted. (in-Double)
    dllObj.UTCToET.restype = c_double
    dllObj.UTCToET.argtypes = [c_double]

    # Converts a time in ds50TAI to a time in ds50UTC using timing constants records in memory.
    # If no timing constants records were loaded, ds50TAI and ds50UTC are the same.
    # Partial days may be returned.
    # ds50TAI: Days since 1950, TAI to be converted. (in-Double)
    dllObj.TAIToUTC.restype = c_double
    dllObj.TAIToUTC.argtypes = [c_double]

    # Converts a time in ds50TAI to a time in ds50UT1 using timing constants records in memory.
    # If no timing constants records were loaded, ds50TAI and ds50UT1 are the same.
    # Partial days may be returned.
    # ds50TAI: Days since 1950, TAI to be converted. (in-Double)
    dllObj.TAIToUT1.restype = c_double
    dllObj.TAIToUT1.argtypes = [c_double]

    # Converts a year and a number of days to a time in ds50UTC.
    # Partial days may be returned.
    # year: Two or four digit years are accepted. (in-Integer)
    # dayOfYear: The day of year. Partial days can be specified. (in-Double)
    dllObj.YrDaysToUTC.restype = c_double
    dllObj.YrDaysToUTC.argtypes = [c_int, c_double]

    # Converts a time in ds50UTC to a year and day of year.
    # The input ds50UTC must be greater than 2192.0, which corresponds to a time later than 1st Jan 1956. Any input
    # value less than or equal to 2192.0 will yield Year=1956, Day=1.0.
    # ds50UTC: Days since 1950, UTC to be converted. (in-Double)
    # year: A reference to a variable in which to place the 4-digit year. (out-Integer)
    # dayOfYear: A reference to a variable in which to place the day of year. Partial days may be expressed in this
    # variable. (out-Double)
    dllObj.UTCToYrDays.restype = None
    dllObj.UTCToYrDays.argtypes = [c_double, c_int_p, c_double_p]

    # Converts a set of time components (year, day of year, hour, minute, second) to a time in ds50UTC.
    # Partial days may be returned.
    # See "TimeComps2ToUTC" for a function which takes a month and day instead of a day of year value.
    # year: Two or four digit years are accepted. (in-Integer)
    # dayOfYear: The day of year, expressed as a whole number. (in-Integer)
    # hh: The hour. (in-Integer)
    # mm: The minute. (in-Integer)
    # sss: The second, including partial seconds if desired. (in-Double)
    dllObj.TimeComps1ToUTC.restype = c_double
    dllObj.TimeComps1ToUTC.argtypes = [c_int, c_int, c_int, c_int, c_double]

    # Converts a time in ds50UTC to its individual components (year, day of year, hour, minute, second).
    # See "TimeComps1ToUTC" for an example.
    # The input ds50UTC must be greater than 2192.0, which corresponds to a time later than 1st Jan 1956. Any input
    # value less than or equal to 2192.0 will be reset to that value.
    # ds50UTC: Days since 1950, UTC to be converted. (in-Double)
    # year: A reference to a variable in which to store the 4-digit year. (out-Integer)
    # dayOfYear: A reference to a variable in which to store the day of year. (out-Integer)
    # hh: A reference to a variable in which to store the hour. (out-Integer)
    # mm: A reference to a variable in which to store the minute. (out-Integer)
    # sss: A reference to a variable in which to store the second. Partial seconds may be expressed if
    # necessary. (out-Double)
    dllObj.UTCToTimeComps1.restype = None
    dllObj.UTCToTimeComps1.argtypes = [c_double, c_int_p, c_int_p, c_int_p, c_int_p, c_double_p]

    # Converts a set of time components (year, month, day of month, hour, minute, second) to a time in ds50UTC.
    # Partial days may be returned.
    # See "TimeComps1ToUTC" for a function which takes a day of year value instead of a month and day.
    # year: Two or four digit years are accepted. (in-Integer)
    # mon: The month. (in-Integer)
    # dayOfMonth: The day of the month. (in-Integer)
    # hh: The hour. (in-Integer)
    # mm: The minute. (in-Integer)
    # sss: The second. (in-Double)
    dllObj.TimeComps2ToUTC.restype = c_double
    dllObj.TimeComps2ToUTC.argtypes = [c_int, c_int, c_int, c_int, c_int, c_double]

    # Converts a time in ds50UTC to its individual components (year, month, day of month, hour, minute, second).
    # See "TimeComps1ToUTC" for an example.
    # The input ds50UTC must be greater than 2192.0, which corresponds to a time later than 1st Jan 1956. Any input
    # value less than or equal to 2192.0 will be reset to that value.
    # ds50UTC: Days since 1950, UTC to be converted. (in-Double)
    # year: A reference to a variable in which to store the 4-digit year. (out-Integer)
    # month: A reference to a variable in which to store the month. (out-Integer)
    # dayOfMonth: A reference to a variable in which to store the day of the month. (out-Integer)
    # hh: A reference to a variable in which to store the hour. (out-Integer)
    # mm: A reference to a variable in which to store the minute. (out-Integer)
    # sss: A reference to a variable in which to store the second. Partial seconds may be expressed if
    # necessary. (out-Double)
    dllObj.UTCToTimeComps2.restype = None
    dllObj.UTCToTimeComps2.argtypes = [c_double, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_double_p]

    # Computes right ascension of Greenwich at the specified time in ds50UT1.
    # The Fk constants as you currently have them set up in EnvConst.dll are used.
    # EnvConst.dll is not marked as a direct dependency of TimeFunc.dll. However, it obviously must be loaded in order
    # to be able to use this function since you must first obtain a handle via the EnvGetFkPtr() function.
    # ds50UT1: Input days since 1950, UT1. (in-Double)
    # lenvFk: A handle to the FK data. Use the value returned from EnvGetFkPtr(), located in EnvConst.dll. (in-Long)
    dllObj.ThetaGrnwch.restype = c_double
    dllObj.ThetaGrnwch.argtypes = [c_double, c_longlong]

    # Computes right ascension of Greenwich at the specified time in ds50UT1 using the Fourth Fundamental
    # Catalogue (FK4).
    # There is no need to load or initialize EnvConst.dll when computing right ascension using this function.
    # ds50UT1: Days since 1950, UT1. (in-Double)
    dllObj.ThetaGrnwchFK4.restype = c_double
    dllObj.ThetaGrnwchFK4.argtypes = [c_double]

    # Computes right ascension of Greenwich at the specified time in ds50UT1 using the Fifth Fundamental
    # Catalogue (FK5).
    # There is no need to load or initialize EnvConst.dll when computing right ascension using this function.
    # ds50UT1: Input days since 1950, UT1. (in-Double)
    dllObj.ThetaGrnwchFK5.restype = c_double
    dllObj.ThetaGrnwchFK5.argtypes = [c_double]

    # This function is intended for future use.  No information is currently available.
    # This function is intended for future use.  No information is currently available.
    # funcIdx: Input function index (in-Integer)
    # frArr: Input (in-Double[*])
    # toArr: Output (out-Double[*])
    dllObj.TimeConvFrTo.restype = None
    dllObj.TimeConvFrTo.argtypes = [c_int, c_void_p, c_void_p]

    # Returns prediction control parameters. The parameters are placed in the reference variables passed to this
    # function.
    # startFrEpoch: Indicates whether startTime is expressed in minutes since epoch. (startFrEpoch = 1: startTime is
    # in minutes since epoch, startFrEpoch = 0: startTime is in days since 1950, UTC) (out-Integer)
    # stopFrEpoch: Indicates whether stopTime is expressed in minutes since epoch. (stopFrEpoch = 1: stopTime is in
    # minutes since epoch, stopFrEpoch = 0: stopTime is in days since 1950, UTC) (out-Integer)
    # startTime: The start time. Depending on the value of startFrEpoch, start time can be expressed in minutes since
    # epoch or days since 1950, UTC. (out-Double)
    # stopTime: The stop time. Depending on the value of stopFrEpoch, stop time can be expressed in minutes since epoch
    # or days since 1950, UTC. (out-Double)
    # interval: The Step size (min). (out-Double)
    dllObj.Get6P.restype = None
    dllObj.Get6P.argtypes = [c_int_p, c_int_p, c_double_p, c_double_p, c_double_p]

    # Sets prediction control parameters.
    # startFrEpoch: Indicates whether startTime is expressed in minutes since epoch. (startFrEpoch = 1: Value of
    # startTime is in minutes since epoch, startFrEpoch = 0: Value of startTime is in days since 1950, UTC) (in-Integer)
    # stopFrEpoch: Indicates whether stopTime is expressed in minutes since epoch. (stopFrEpoch = 1: Value of
    # stopTime is in minutes since epoch, stopFrEpoch = 0: Value of stopTime is in days since 1950, UTC) (in-Integer)
    # startTime: Start time. (in-Double)
    # stopTime: Stop time. (in-Double)
    # interval: Step size (min). (in-Double)
    dllObj.Set6P.restype = None
    dllObj.Set6P.argtypes = [c_int, c_int, c_double, c_double, c_double]

    # Returns current prediction control parameters in form of a 6P-Card string.
    # card6PLine: The resulting 6P-Card string. (out-Character[512])
    dllObj.Get6PCardLine.restype = None
    dllObj.Get6PCardLine.argtypes = [c_char_p]

    # Returns the time span of the loaded timing constants - the earliest and latest of loaded timing constant records
    # numOfRecs: Number of timing constants records loaded in memory (zero if timing constants aren't
    # loaded) (out-Integer)
    # frTimeDs50UTC: The time, in days since 1950 UTC,  of the earliest timing constant record loaded in memory
    # (zero if timing constants aren't loaded) (out-Double)
    # toTimeDs50UTC: The time, in days since 1950 UTC,  of the latest timing constant record loaded in memory
    # (zero if timing constants aren't loaded) (out-Double)
    dllObj.TConTimeSpan.restype = None
    dllObj.TConTimeSpan.argtypes = [c_int_p, c_double_p, c_double_p]

    return dllObj


# ========================= End of auto generated code ==========================
