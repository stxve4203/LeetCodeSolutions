from typing import List
import unittest

def candy(ratings: List[int]) -> int:
    if not ratings:
        return 0

    ret, up, down, peak = 1, 0, 0, 0

    for prev, curr in zip(ratings[:-1], ratings[1:]):
        if prev < curr:
            up, down, peak = up +1, 0, up + 1
            ret += 1 + up
        elif prev == curr:
            up = down = peak = 0
            ret += 1
        else:
            up, down = 0, down + 1
            ret += 1 + down - int(peak >= down)
    return ret

class CandyTest(unittest.TestCase):

    def test_candy(self):
        ratings_input_1 = [1, 0, 2]
        expected_1 = 5
        self.assertEqual(candy(ratings_input_1), expected_1)

        ratings_input_2 = [1, 2, 2]
        expected_2 = 4
        self.assertEqual(candy(ratings_input_2), expected_2)

if __name__ == '__main__':
    unittest.main()