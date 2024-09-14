import unittest

import pandas as pd

from problems.problem_2878 import getDataframeSize


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.players = {
            "player_id": [846, 749, 155, 583, 388, 883, 355, 247, 761, 642],
            "name": [
                "Mason",
                "Riley",
                "Bob",
                "Isabella",
                "Zachary",
                "Ava",
                "Violet",
                "Thomas",
                "Jack",
                "Charlie",
            ],
            "age": [21, 30, 28, 32, 24, 23, 18, 27, 33, 36],
            "position": [
                "Forward",
                "Winger",
                "Striker",
                "Goalkeeper",
                "Midfielder",
                "Defender",
                "Striker",
                "Striker",
                "Midfielder",
                "Center-back",
            ],
            "team": [
                "RealMadrid",
                "Barcelona",
                "ManchesterUnited",
                "Liverpool",
                "BayernMunich",
                "Chelsea",
                "Juventus",
                "ParisSaint-Germain",
                "ManchesterCity",
                "Arsenal",
            ],
        }
        self.expected = [10, 5]

    def test_getDataframeSize(self):
        actual = getDataframeSize(pd.DataFrame(self.players))
        self.assertEqual(actual, self.expected)
