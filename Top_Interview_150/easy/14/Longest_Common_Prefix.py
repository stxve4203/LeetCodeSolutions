import unittest
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    # No string
    if not strs:
        return ""

    shortest_str = min(strs, key=len)
    for i, char in enumerate(shortest_str):
        for other in strs:
            if other[i] != char:
                return shortest_str[:i]
    return shortest_str

class longestCommonPrefixTest(unittest.TestCase):

    def test_longestCommonPrefixTest(self):
        input_1 = ["flower", "flow", "flight"]
        output_2 = "fl"
        self.assertEqual(longestCommonPrefix(input_1), output_2)


if __name__ == '__main__':
    unittest.main()
