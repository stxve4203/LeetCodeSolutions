import unittest
from typing import List


def trap(height: List[int]) -> int:
    water = 0
    for i in range(1, len(height)):
        min_height = min(max(height[0:i]), max(height[i:len(height)]))
        if (min_height - height[i]) > 0:
            water += (min_height - height[i])
    return water


class TrapTest(unittest.TestCase):

    def test_trap(self):
        height_1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        expected_1 = 6
        self.assertEqual(trap(height_1), expected_1)

        height_2 = [4, 2, 0, 3, 2, 5]
        expected_2 = 9
        self.assertEqual(trap(height_2), expected_2)


if __name__ == '__main__':
    unittest.main()
