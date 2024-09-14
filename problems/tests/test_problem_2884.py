import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_2884 import modifySalaryColumn


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.employees = {
            "name": ["Jack", "Piper", "Mia", "Ulysses"],
            "salary": [19666, 74754, 62509, 54866],
        }
        self.expected = {
            "name": ["Jack", "Piper", "Mia", "Ulysses"],
            "salary": [39332, 149508, 125018, 109732],
        }

    def test_modifySalaryColumn(self):
        actual = modifySalaryColumn(pd.DataFrame(self.employees))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
