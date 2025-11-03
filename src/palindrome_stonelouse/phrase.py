import re


class Phrase:
    """A class to represent phrases."""

    def __init__(self, content):
        self.content = content

    def ispalindrome(self):
        """Return True for a palindrome, False otherwise."""
        return self._processed_content() == reverse(self._processed_content())

    def _processed_content(self):
        """Process content for palindrome testing."""
        """Process content for palindrome testing."""
        return self.letters().lower()

    def letters(self):
        """Return only the letters in the content."""
        return "".join(re.findall(r"[A-Za-z]", self.content))

    def __iter__(self):
        self.phrase_iterator = iter(self.content)
        return self

    def __next__(self):
        return next(self.phrase_iterator)


def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string))
