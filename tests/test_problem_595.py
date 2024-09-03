import unittest

import pandas as pd

from problems.problem_595 import big_countries


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.input = {
            "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
            "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
            "area": [652230, 28748, 2381741, 468, 1246700],
            "population": [25500100, 2831741, 37100000, 78115, 20609294],
            "gdp": [20343000000, 12960000000, 188681000000, 3712000000, 100990000000],
        }
        self.expected = {
            "name": ["Afghanistan", "Algeria"],
            "population": [25500100, 37100000],
            "area": [652230, 2381741],
        }

    def test_big_countries(self):
        actual = big_countries(pd.DataFrame(self.input))
        expected = pd.DataFrame(self.expected)
        self.assertEqual(actual.to_dict("records"), expected.to_dict("records"))