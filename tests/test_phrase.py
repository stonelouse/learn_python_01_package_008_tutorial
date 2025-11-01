## Our test suite for the Phrase class

# Importing 'Phrase' in the test file
from unittest import skip
from palindrome_stonelouse.phrase import Phrase


def test_non_palindrome():
    assert not Phrase("apple").ispalindrome()


def test_literal_palindrome():
    assert Phrase("racecar").ispalindrome()


def test_mixed_case_palindrome():
    assert Phrase("RaceCar").ispalindrome()


def test_palindrome_with_punctuation():
    skip("Not implemented yet")
