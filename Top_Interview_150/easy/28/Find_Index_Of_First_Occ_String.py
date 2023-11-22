import unittest

# Given two strings needle and haystack,
# return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


def strStr(haystack: str, needle: str) -> int:
    lps = [0] * len(needle)

    pre = 0
    for i in range(1, len(needle)):
        while pre > 0 and needle[i] != needle[pre]:
            pre = lps[pre-1]
        if needle[pre] == needle[i]:
            pre+=1
            lps[i] = pre

    n = 0
    for h in range(len(haystack)):
        while n > 0 and needle[h] != haystack[n]:
            n = lps[n-1]
        if needle[n] == haystack[h]:
            n+=1
        if n == len(needle):
            return h - n + 1

    return -1

class FindIndexTest(unittest.TestCase):

    def test_strStr(self):
        haystack_1 = "sadbutsad"
        needle_1 = "sad"
        expected_1 = 0
        self.assertEqual(strStr(haystack_1, needle_1), expected_1)


if __name__ == '__main__':
    unittest.main()
