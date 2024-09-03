import unittest

from problems.helpers.list import ListHelper
from problems.problem_23 import Solution as Solution1
from problems.problem_23_2 import Solution as Solution2
from protocols.problem_23 import SolutionProto


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution_1 = Solution1()
        self.solution_2 = Solution2()

    def test_mergeKLists(self):
        for solution in [self.solution_1, self.solution_2]:
            self.__merge_k_lists(
                solution, [[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]
            )
            self.__merge_k_lists(solution, [], [])
            self.__merge_k_lists(solution, [[]], [])
            self.__merge_k_lists(solution, [[], [1]], [1])

    def __merge_k_lists(
        self, solution: SolutionProto, lists: list[list[int]], expected: list[int]
    ):
        helper = ListHelper()

        lists = helper.make_list2(lists)
        expected = helper.make_list(expected)

        actual = solution.mergeKLists(lists)

        assert helper.compare_lists(expected, actual)
