import unittest

from problems.problem_205 import Solution as Solution1
from problems.problem_205_2 import Solution as Solution2


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution_1 = Solution1()
        self.solution_2 = Solution2()

    def test_isIsomorphic(self):
        for solution in [self.solution_1, self.solution_2]:
            self.assertTrue(solution.isIsomorphic("egg", "add"))
            self.assertFalse(solution.isIsomorphic("foo", "bar"))
            self.assertTrue(solution.isIsomorphic("paper", "title"))
            self.assertFalse(solution.isIsomorphic("bbbaaaba", "aaabbbba"))
            self.assertFalse(solution.isIsomorphic("badc", "baba"))
