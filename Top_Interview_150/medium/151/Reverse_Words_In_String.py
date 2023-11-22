import unittest

def reverseWords(s: str) -> str:
    w = s.split()
    w2 = []
    x = len(w) - 1
    while x >= 0:
        w2.append(w[x])
        x -= 1
    return ' '.join(w2)


class ReverseWordsTest(unittest.TestCase):

    def test_reverseWords(self):
        input_1 = " hello world "
        output_2 = "world hello"
        self.assertEqual(reverseWords(input_1), output_2)


if __name__ == '__main__':
    unittest.main()


