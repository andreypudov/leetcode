import unittest

import pandas as pd

from problems.problem_1148 import article_views


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.views = {
            "article_id": [1, 1, 2, 2, 4, 3, 3],
            "author_id": [3, 3, 7, 7, 7, 4, 4],
            "viewer_id": [5, 6, 7, 6, 1, 4, 4],
            "view_date": [
                "2019-08-01",
                "2019-08-02",
                "2019-08-01",
                "2019-08-02",
                "2019-07-22",
                "2019-07-21",
                "2019-07-21",
            ],
        }
        self.expected = {
            "id": [4, 7],
        }

    def test_article_views(self):
        actual = article_views(pd.DataFrame(self.views))
        expected = pd.DataFrame(self.expected)
        self.assertEqual(actual.to_dict("records"), expected.to_dict("records"))
