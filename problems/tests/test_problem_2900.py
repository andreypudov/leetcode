import unittest

from problems.problem_2900 import Solution

class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_getLongestSubsequence(self):
        assert self.solution.getLongestSubsequence(["e","a","b"], [0,0,1]) == ["e","b"]
        assert self.solution.getLongestSubsequence(["a","b","c","d"], [1,0,1,1]) == ["a","b","c"]
