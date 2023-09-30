import unittest

from problems.problem_9 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_findMedianSortedArrays(self):
        self.assertTrue(self.solution.isPalindrome(121))
        self.assertFalse(self.solution.isPalindrome(-121))
        self.assertFalse(self.solution.isPalindrome(10))


if __name__ == "__main__":
    unittest.main()
