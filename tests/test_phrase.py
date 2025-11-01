## Our test suite for the Phrase class

# Importing 'Phrase' in the test file
from palindrome_stonelouse.phrase import Phrase

def test_non_palindrome():
    assert not Phrase("apple").ispalindrome()

def test_literal_palindrome():
    assert Phrase("racecar").ispalindrome()
