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
    assert Phrase("Madam, I'm Adam.").ispalindrome()


def test_letters_and_digits():
    assert Phrase("Madam, 42 I'm Adam.").letters_and_digits() == "Madam42ImAdam"


def test_integer_non_palindrome():
    assert not Phrase("12345").ispalindrome()


def test_integer_palindrome():
    assert Phrase("12321").ispalindrome()
