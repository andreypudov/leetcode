import unittest

from problems.problem_12 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_intToRoman(self):
        self.assertEqual(self.solution.intToRoman(3), "III")
        self.assertEqual(self.solution.intToRoman(58), "LVIII")
        self.assertEqual(self.solution.intToRoman(1994), "MCMXCIV")

        self.assertEqual(self.solution.intToRoman(1), "I")
        self.assertEqual(self.solution.intToRoman(3999), "MMMCMXCIX")

        self.assertEqual(self.solution.intToRoman(49), "XLIX")
        self.assertEqual(self.solution.intToRoman(99), "XCIX")
        self.assertEqual(self.solution.intToRoman(494), "CDXCIV")
        self.assertEqual(self.solution.intToRoman(999), "CMXCIX")
