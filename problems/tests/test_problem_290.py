import unittest

from problems.problem_290 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_containsDuplicate(self):
        self.assertTrue(self.solution.wordPattern("abba", "dog cat cat dog"))
        self.assertFalse(self.solution.wordPattern("abba", "dog cat cat fish"))
        self.assertFalse(self.solution.wordPattern("aaaa", "dog cat cat dog"))
        self.assertFalse(self.solution.wordPattern("aaa", "aa aa aa aa"))
