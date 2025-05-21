import unittest

from problems.problem_2900 import Solution as Solution1
from problems.problem_2900_2 import Solution as Solution2


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution_1 = Solution1()
        self.solution_2 = Solution2()

    def test_getLongestSubsequence(self):
        for solution in [self.solution_1, self.solution_2]:
            assert solution.getLongestSubsequence(
                ["e", "a", "b"], [0, 0, 1]
            ) == ["e", "b"]
            assert solution.getLongestSubsequence(
                ["a", "b", "c", "d"], [1, 0, 1, 1]
            ) == ["a", "b", "c"]
