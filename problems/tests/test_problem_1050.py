import unittest

import pandas as pd

from problems.problem_1050 import actors_and_directors


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.views = {
            "actor_id": [1, 1, 1, 1, 1, 2, 2],
            "director_id": [1, 1, 1, 2, 2, 1, 1],
            "viewer_id": [5, 6, 7, 6, 1, 4, 4],
            "timestamp": [0, 1, 2, 3, 4, 5, 6],
        }
        self.expected = {
            "actor_id": [1],
            "director_id": [1],
        }

    def test_actors_and_directors(self):
        actual = actors_and_directors(pd.DataFrame(self.views))
        expected = pd.DataFrame(self.expected)
        self.assertEqual(actual.to_dict("records"), expected.to_dict("records"))
