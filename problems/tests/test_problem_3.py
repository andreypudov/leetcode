import unittest

from problems.problem_3 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_lengthOfLongestSubstring(self):
        assert self.solution.lengthOfLongestSubstring("abcabcbb") == 3
        assert self.solution.lengthOfLongestSubstring("bbbbb") == 1
        assert self.solution.lengthOfLongestSubstring("pwwkew") == 3
