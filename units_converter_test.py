"""
Unit tests for the units converter functions.
"""

# import the code to be tested
from units_converter import mpg2kpl


def describe_a_set_of_units_converters():
    def that_can_convert_mpg_to_kpl():
        """
        Test that the mpg2kpl function works as expected
        """
        assert mpg2kpl(25) == 10.6285926874
