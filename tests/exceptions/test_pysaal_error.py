import pytest

from pysaal.enums import PySAALErrorCode
from pysaal.exceptions import PySAALError


def test_bad_key():
    with pytest.raises(PySAALError, match="Bad key"):
        raise PySAALError(PySAALErrorCode.BAD_KEY)


def test_duplicate_key():
    with pytest.raises(PySAALError, match="Duplicate key"):
        raise PySAALError(PySAALErrorCode.DUPLICATE_KEY)


def test_unknown():
    with pytest.raises(PySAALError, match=""):
        raise PySAALError(PySAALErrorCode.UNKNOWN)
