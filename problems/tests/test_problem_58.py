import unittest

from problems.problem_58 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_lengthOfLastWord(self):
        self.assertEqual(self.solution.lengthOfLastWord("Hello World"), 5)
        self.assertEqual(
            self.solution.lengthOfLastWord("   fly me   to   the moon  "), 4
        )
        self.assertEqual(
            self.solution.lengthOfLastWord("luffy is still joyboy"), 6
        )
