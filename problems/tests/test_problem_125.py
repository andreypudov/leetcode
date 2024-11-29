import unittest

from problems.problem_125 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_isPalindrome(self):
        self.assertTrue(
            self.solution.isPalindrome("A man, a plan, a canal: Panama")
        )
        self.assertTrue(self.solution.isPalindrome(" "))
        self.assertFalse(self.solution.isPalindrome("race a car"))
