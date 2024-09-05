import unittest

import pandas as pd

from problems.problem_511 import game_analysis


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.activity = {
            "player_id": [1, 1, 2, 3, 3],
            "device_id": [2, 2, 3, 1, 4],
            "event_date": [
                pd.Timestamp("2016-03-01"),
                pd.Timestamp("2016-05-02"),
                pd.Timestamp("2017-06-25"),
                pd.Timestamp("2016-03-02"),
                pd.Timestamp("2018-07-03"),
            ],
            "games_played": [5, 6, 1, 0, 5],
        }
        self.expected = {
            "player_id": [1, 2, 3],
            "first_login": [
                pd.Timestamp("2016-03-01"),
                pd.Timestamp("2017-06-25"),
                pd.Timestamp("2016-03-02"),
            ],
        }

    def test_game_analysis(self):
        actual = game_analysis(pd.DataFrame(self.activity))
        expected = pd.DataFrame(self.expected)
        self.assertEqual(actual.to_dict("records"), expected.to_dict("records"))
