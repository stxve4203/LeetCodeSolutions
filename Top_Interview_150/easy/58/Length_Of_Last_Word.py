import unittest
from typing import List

# Given a string s consisting of words and spaces, return the length of the last word in the string.
"""
stripped = s.strip(): This line removes leading and trailing whitespace from the input string s using the strip method. This is done to handle cases where there might be spaces at the beginning or end of the string.

strList = stripped.split(" "): This line splits the stripped string stripped into a list of words using a space as the delimiter. It uses the split method, which separates the string into a list of substrings wherever it encounters a space character.

lastWord = strList[-1]: This line extracts the last element (which is the last word) from the strList by using the index -1. This assumes that words in the string are separated by spaces.

return len(lastWord): Finally, the code returns the length of the lastWord using the len function. This length represents the number of characters in the last word of the input string.

"""
def lengthOfLastWord(s: str) -> int:
    stripped = s.strip()
    strList = stripped.split(" ")
    lastWord = strList[-1]
    return len(lastWord)


class LengthOfLastWordTest(unittest.TestCase):

    def test_lengthOfLastWord(self):
        input_1 = "Hello World"
        output_2 = 5
        self.assertEqual(lengthOfLastWord(input_1), output_2)

if __name__ == '__main__':
    unittest()
