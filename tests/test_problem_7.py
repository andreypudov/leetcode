import unittest

from problems.problem_7 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_reverse(self):
        assert self.solution.reverse(123) == 321
        assert self.solution.reverse(-123) == -321
        assert self.solution.reverse(120) == 21


if __name__ == "__main__":
    unittest.main()
