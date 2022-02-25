"""
A set of functions to convert numeric values from
one set of units to another.
"""


# useful constants
KPM = 1.609344  # kilometers per mile
GPL = 0.2641720524  # gallons per liter


def mpg2kpl(mpg, precision=4):
    """
    Converts MPG to KPL precisely to the specified
    number decimal places (defaults to 4)
    """
    return round(mpg * KPM * GPL, precision)
