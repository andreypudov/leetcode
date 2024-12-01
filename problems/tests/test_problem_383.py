import unittest

from problems.problem_383 import Solution as Solution1
from problems.problem_383_2 import Solution as Solution2


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution_1 = Solution1()
        self.solution_2 = Solution2()

    def test_canConstruct(self):
        for solution in [self.solution_1, self.solution_2]:
            self.assertFalse(solution.canConstruct("a", "b"))
            self.assertFalse(solution.canConstruct("aa", "ab"))
            self.assertTrue(solution.canConstruct("aa", "aab"))
