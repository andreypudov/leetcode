import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_1741 import total_time


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.employees = {
            "emp_id": [1, 1, 1, 2, 2],
            "event_day": [
                "2020-11-28",
                "2020-11-28",
                "2020-12-03",
                "2020-11-28",
                "2020-12-09",
            ],
            "in_time": [4, 55, 1, 3, 47],
            "out_time": [32, 200, 42, 33, 74],
        }
        self.expected = {
            "day": ["2020-11-28", "2020-11-28", "2020-12-03", "2020-12-09"],
            "emp_id": [1, 2, 1, 2],
            "total_time": [173, 30, 41, 27],
        }

    def test_total_time(self):
        actual = total_time(pd.DataFrame(self.employees))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
