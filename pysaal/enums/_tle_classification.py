from enum import Enum


class TLEClassification(Enum):
    NONE = " "
    UNCLASSIFIED = "U"
    CONFIDENTIAL = "C"
    SECRET = "S"
