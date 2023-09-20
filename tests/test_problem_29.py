import unittest

from problems.problem_29 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_divide(self):
        assert self.solution.divide(-1, 1) == -1
        assert self.solution.divide(1, -1) == -1
        assert self.solution.divide(-1, -1) == 1

        assert self.solution.divide(7, 2) == 3
        assert self.solution.divide(4, 3) == 1
        assert self.solution.divide(1, 2) == 0

        assert self.solution.divide(1024, 3) == 341
        assert self.solution.divide(2037, 3) == 679
        assert self.solution.divide(2**32, 6) == 715827882

        assert self.solution.divide(2147483648, 1) == 2147483647
        assert self.solution.divide(-2147483648, -1) == 2147483647
        assert self.solution.divide(-2147483648, 1) == -2147483648


if __name__ == "__main__":
    unittest.main()
