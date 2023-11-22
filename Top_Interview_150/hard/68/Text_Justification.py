import unittest
from typing import List

def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    res, line, width = [], [], 0

    for w in words:
        if width + len(w) + len(line) > maxWidth:
            for i in range(maxWidth - width): line[i % (len(line) - 1 or 1)] += ' '
            res, line, width = res + [''.join(line)], [], 0
        line += [w]
        width += len(w)

    return res + [' '.join(line).ljust(maxWidth)]


class FullJustifyTest(unittest.TestCase):

    def test_fullJustify(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        max_width = 16
        output = ["This    is    an","example  of text","justification.  "]

        self.assertEqual(fullJustify(words, max_width), output)


if __name__ == '__main__':
    unittest.main()
