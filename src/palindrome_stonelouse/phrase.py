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
        return self.letters().lower()

    def letters(self):
        """Return only the letters in the content."""
        the_letters = []
        for char in self.content:
            if re.search(r"[a-zA-Z]", char):
                the_letters.append(char)
        return "".join(the_letters)

    def __iter__(self):
        self.phrase_iterator = iter(self.content)
        return self

    def __next__(self):
        return next(self.phrase_iterator)


def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string))
