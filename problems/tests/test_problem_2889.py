import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_2889 import pivotTable


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.weather = {
            "city": [
                "Jacksonville",
                "Jacksonville",
                "Jacksonville",
                "Jacksonville",
                "Jacksonville",
                "ElPaso",
                "ElPaso",
                "ElPaso",
                "ElPaso",
                "ElPaso",
            ],
            "month": [
                "January",
                "February",
                "March",
                "April",
                "May",
                "January",
                "February",
                "March",
                "April",
                "May",
            ],
            "temperature": [13, 23, 38, 5, 34, 20, 6, 26, 2, 43],
        }
        self.expected = {
            "month": ["April", "February", "January", "March", "May"],
            "ElPaso": [2, 6, 20, 26, 43],
            "Jacksonville": [5, 23, 13, 38, 34],
        }

    def test_pivotTable(self):
        actual = pivotTable(pd.DataFrame(self.weather))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.rename_axis(None, axis=1).reset_index(drop=False),
            expected.reset_index(drop=True),
        )
