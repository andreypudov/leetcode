import unittest

from problems.problem_189 import Solution as Solution1


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.solution_1 = Solution1()

    def test_rotate(self):
        for solution in [self.solution_1]:
            self.test_case(solution, [1, 2, 3, 4], 1, [4, 1, 2, 3])
            self.test_case(
                solution, [1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]
            )
            self.test_case(solution, [-1, -100, 3, 99], 2, [3, 99, -1, -100])

    def test_case(self, solution, nums, k, result):
        solution.rotate(nums, k)
        self.assertEqual(nums, result)
