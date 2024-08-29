import unittest

from problems.helpers.list import ListHelper
from problems.problem_23 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_mergeKLists(self):
        self.__merge_k_lists([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6])
        self.__merge_k_lists([], [])
        self.__merge_k_lists([[]], [])
        self.__merge_k_lists([[], [1]], [1])

    def __merge_k_lists(self, lists: list[list[int]], expected: list[int]):
        helper = ListHelper()

        lists = helper.make_list2(lists)
        expected = helper.make_list(expected)

        actual = self.solution.mergeKLists(lists)

        assert helper.compare_lists(expected, actual)
