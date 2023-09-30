import unittest

from problems.problem_5 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_twoSum(self):
        assert self.solution.longestPalindrome("babad") == "bab"
        assert self.solution.longestPalindrome("cbbd") == "bb"


if __name__ == "__main__":
    unittest.main()
