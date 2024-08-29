import unittest

from problems.helpers.list import ListHelper
from problems.problem_2 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_addTwoNumbers(self):
        self.__add_two_numbers([2, 4, 3], [5, 6, 4], [7, 0, 8])
        self.__add_two_numbers([0], [0], [0])
        self.__add_two_numbers(
            [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]
        )

    def __add_two_numbers(self, l1: list[int], l2: list[int], expected: list[int]):
        helper = ListHelper()

        l1 = helper.make_list(l1)
        l2 = helper.make_list(l2)

        expected = helper.make_list(expected)
        actual = self.solution.addTwoNumbers(l1, l2)

        assert helper.compare_lists(expected, actual)
