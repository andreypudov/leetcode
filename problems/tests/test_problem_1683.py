import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_1683 import invalid_tweets


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.tweets = {
            "tweet_id": [1, 2],
            "content": ["Vote for Biden", "Let us make America great again!"],
        }
        self.expected = {
            "tweet_id": [2],
        }

    def test_invalid_tweets(self):
        actual = invalid_tweets(pd.DataFrame(self.tweets))
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
