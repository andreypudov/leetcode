import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_1667 import fix_names


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.users = {
            "user_id": [1, 222, 2],
            "name": ["aLice", "MaRRy aNN", "bOB"],
        }
        self.expected = {
            "user_id": [1, 2, 222],
            "name": ["Alice", "Bob", "Marry ann"],
        }

    def test_fix_names(self):
        actual = fix_names(pd.DataFrame(self.users))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
