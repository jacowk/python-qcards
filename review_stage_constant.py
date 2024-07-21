from enum import Enum

"""
An enum representing the data in t_lookup_review_stage

Jaco Koekemoer
2023-04-08
"""
class ReviewStage(Enum):

    DAILY = 1
    EVERY_2ND_DAY = 2
    WEEKLY = 3
    MONTHLY = 4

"""
An enum representing the data in t_lookup_odd_even

Jaco Koekemoer
2023-04-08
"""
class OddEven(Enum):

    ODD = 1
    EVEN = 2

"""
An enum representing the data in t_lookup_weekday

Jaco Koekemoer
2023-04-08
"""
class Weekday(Enum):

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

"""
An enum representing the first selection for review stage comboboxes

Jaco Koekemoer
2023-05-04
"""
class ReviewStageSelectValues(Enum):

    SELECT_REVIEW_STAGE = "Select Review Stage"
    SELECT_ODD_OR_EVEN = "Select Odd or Even"
    SELECT_WEEKDAY = "Select Weekday"
