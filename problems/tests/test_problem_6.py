import unittest

from problems.problem_6 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_twoSum(self):
        self.assertEqual(
            self.solution.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR"
        )
        self.assertEqual(
            self.solution.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI"
        )
        self.assertEqual(self.solution.convert("A", 1), "A")
