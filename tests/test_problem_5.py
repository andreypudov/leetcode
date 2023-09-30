import unittest

from problems.problem_5 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_twoSum(self):
        self.assertEqual(self.solution.longestPalindrome("babad"), "bab")
        self.assertEqual(self.solution.longestPalindrome("cbbd"), "bb")


if __name__ == "__main__":
    unittest.main()
