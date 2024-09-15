import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_2890 import meltTable


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.report = {
            "product": [
                "Umbrella",
                "SleepingBag",
            ],
            "quarter_1": [
                417,
                800,
            ],
            "quarter_2": [
                224,
                936,
            ],
            "quarter_3": [
                379,
                93,
            ],
            "quarter_4": [
                611,
                875,
            ],
        }
        self.expected = {
            "product": [
                "Umbrella",
                "SleepingBag",
                "Umbrella",
                "SleepingBag",
                "Umbrella",
                "SleepingBag",
                "Umbrella",
                "SleepingBag",
            ],
            "quarter": [
                "quarter_1",
                "quarter_1",
                "quarter_2",
                "quarter_2",
                "quarter_3",
                "quarter_3",
                "quarter_4",
                "quarter_4",
            ],
            "sales": [417, 800, 224, 936, 379, 93, 611, 875],
        }

    def test_meltTable(self):
        actual = meltTable(pd.DataFrame(self.report))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True),
            expected.reset_index(drop=True),
        )
