from typing import List
import unittest

"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    prefix_product = 1
    postfix_product = 1
    result = [0] * n
    for i in range(n):
        result[i] = prefix_product
        prefix_product *= nums[i]

    for i in range(n - 1, -1, -1):
        result[i] *= postfix_product
        postfix_product *= nums[i]
    return result


class TestProductExceptSelf(unittest.TestCase):

    def test_productExceptSelf(self):

        input_nums_1 = [1, 2, 3, 4]
        expected_output_1 = [24, 12, 8, 6]
        self.assertEqual(productExceptSelf(input_nums_1), expected_output_1)

        input_nums_2 = [5, 2, 3, 1, 4]
        expected_output_2 = [24, 60, 40, 120, 30]
        self.assertEqual(productExceptSelf(input_nums_2), expected_output_2)


if __name__ == '__main__':
    unittest.main()
