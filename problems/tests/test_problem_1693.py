import unittest

import pandas as pd

from problems.problem_1693 import daily_leads_and_partners


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.daily_sales = {
            "date_id": [
                pd.Timestamp("2020-12-8"),
                pd.Timestamp("2020-12-8"),
                pd.Timestamp("2020-12-8"),
                pd.Timestamp("2020-12-7"),
                pd.Timestamp("2020-12-7"),
                pd.Timestamp("2020-12-8"),
                pd.Timestamp("2020-12-8"),
                pd.Timestamp("2020-12-7"),
                pd.Timestamp("2020-12-7"),
                pd.Timestamp("2020-12-7"),
            ],
            "make_name": [
                "toyota",
                "toyota",
                "toyota",
                "toyota",
                "toyota",
                "honda",
                "honda",
                "honda",
                "honda",
                "honda",
            ],
            "lead_id": [0, 1, 1, 0, 0, 1, 2, 0, 1, 2],
            "partner_id": [1, 0, 2, 2, 1, 2, 1, 1, 2, 1],
        }
        self.expected = {
            "date_id": [
                pd.Timestamp("2020-12-7"),
                pd.Timestamp("2020-12-7"),
                pd.Timestamp("2020-12-8"),
                pd.Timestamp("2020-12-8"),
            ],
            "make_name": ["honda", "toyota", "honda", "toyota"],
            "unique_leads": [3, 1, 2, 2],
            "unique_partners": [2, 2, 2, 3],
        }

    def test_daily_leads_and_partners(self):
        actual = daily_leads_and_partners(pd.DataFrame(self.daily_sales))
        expected = pd.DataFrame(self.expected)
        self.assertEqual(actual.to_dict("records"), expected.to_dict("records"))
