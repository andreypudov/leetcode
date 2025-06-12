import unittest

from problems.helpers.list import ListHelper
from problems.problem_206 import Solution as Solution1
from problems.problem_206_2 import Solution as Solution2
from problems.problem_206_3 import Solution as Solution3
from problems.protocols.problem_206 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution_1 = Solution1()
        self.solution_2 = Solution2()
        self.solution_3 = Solution3()

    def test_reverseList(self):
        for solution in [self.solution_1, self.solution_2, self.solution_3]:
            self.reverseList(solution, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
            self.reverseList(solution, [1, 2], [2, 1])
            self.reverseList(solution, [], [])

    def reverseList(
        self, solution: Solution, head: list[int], expected: list[int]
    ):
        helper = ListHelper()

        head = helper.make_list(head)
        expected = helper.make_list(expected)
        actual = solution.reverseList(head)

        assert helper.compare_lists(expected, actual)
