import unittest

from problems.problem_70 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_climbStairs(self):
        assert self.solution.climbStairs(2) == 2
        assert self.solution.climbStairs(3) == 3


if __name__ == "__main__":
    unittest.main()
