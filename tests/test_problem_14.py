import unittest

from problems.problem_14 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_longestCommonPrefix(self):
        self.assertEqual(
            self.solution.longestCommonPrefix(["flower", "flow", "flight"]), "fl"
        )
        self.assertEqual(
            self.solution.longestCommonPrefix(["dog", "racecar", "car"]), ""
        )
