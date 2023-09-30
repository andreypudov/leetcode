import unittest

from problems.problem_13 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_romanToInt(self):
        self.assertEqual(self.solution.romanToInt("III"), 3)
        self.assertEqual(self.solution.romanToInt("LVIII"), 58)
        self.assertEqual(self.solution.romanToInt("MCMXCIV"), 1994)


if __name__ == "__main__":
    unittest.main()
