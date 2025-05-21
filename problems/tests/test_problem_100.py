import unittest
from typing import List

from problems.helpers.tree import TreeHelper
from problems.problem_100 import Solution


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution = Solution()

    def test_isSameTree(self):
        self.assertTrue(self.__isSameTree([1, 2, 3], [1, 2, 3]))
        self.assertFalse(self.__isSameTree([1, 2], [1, None, 2]))

    def __isSameTree(self, p: List[int], q: List[int]):
        helper = TreeHelper()

        p = helper.make_tree(p)
        q = helper.make_list(q)

        return self.solution.isSameTree(p, q)
