import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_2891 import findHeavyAnimals


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.animals = {
            "name": [
                "Tatiana",
                "Khaled",
                "Alex",
                "Jonathan",
                "Stefan",
                "Tommy",
            ],
            "species": [
                "Snake",
                "Giraffe",
                "Leopard",
                "Monkey",
                "Bear",
                "Panda",
            ],
            "age": [98, 50, 6, 45, 100, 26],
            "weight": [464, 41, 328, 463, 50, 349],
        }
        self.expected = {
            "name": [
                "Tatiana",
                "Jonathan",
                "Tommy",
                "Alex",
            ],
        }

    def test_findHeavyAnimals(self):
        actual = findHeavyAnimals(pd.DataFrame(self.animals))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True),
            expected.reset_index(drop=True),
        )
