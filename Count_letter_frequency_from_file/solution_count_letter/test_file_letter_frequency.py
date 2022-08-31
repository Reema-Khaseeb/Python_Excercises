""" Test funcitonality of letter_frequency() function and time consumption"""
# Python program to show time by perf_counter()
from time import perf_counter

import pytest
from .file_letter_frequency import LetterFrequency


VALID_TIME_CONSUMPTION = 1


data = LetterFrequency('./data.txt')
data.read_file()

def letter_frequency_with_elapsed_time(letter):
    """ Count letter's frequency using letter_frequency() method, as well compute time elapsed for it
    Returns:
        letter_frequency_function: string
        (end-start): float
    """
    start = perf_counter()
    letter_frequency_result = data.letter_frequency(letter)
    end = perf_counter()

    return letter_frequency_result, (end-start)


@pytest.mark.parametrize("expected_letter_frequency, letter, valid_time_consumption", [
    (15145200, 'L', VALID_TIME_CONSUMPTION), (96929280, 'i', VALID_TIME_CONSUMPTION)])
def test_letter_frequency(expected_letter_frequency, letter, valid_time_consumption):
    ''' Ensure that letter_frequency method counts letter's frequency correctly
        within the expected range for the time elapsed
    Returns:
        bool
    '''
    letter_frequency_result, resulted_time_consumption = letter_frequency_with_elapsed_time(letter)

    assert letter_frequency_result == expected_letter_frequency
    assert resulted_time_consumption <= valid_time_consumption
