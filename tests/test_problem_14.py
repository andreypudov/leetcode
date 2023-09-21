import unittest

from problems.problem_14 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_longestCommonPrefix(self):
        assert self.solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
        assert self.solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""


if __name__ == "__main__":
    unittest.main()
