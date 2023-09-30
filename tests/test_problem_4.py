import unittest

from problems.problem_4 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_findMedianSortedArrays(self):
        self.assertEqual(self.solution.findMedianSortedArrays([1, 3], [2]), 2.0)
        self.assertEqual(self.solution.findMedianSortedArrays([1, 2], [3, 4]), 2.5)


if __name__ == "__main__":
    unittest.main()
