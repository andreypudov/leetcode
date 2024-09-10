import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from problems.problem_607 import sales_person


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.sales_person = {
            "sales_id": [1, 2, 3, 4, 5],
            "name": ["John", "Amy", "Mark", "Pam", "Alex"],
            "commission_rate": [6, 5, 12, 25, 10],
            "hire_date": ["4/1/2006", "5/1/2010", "12/25/2008", "1/1/2005", "2/3/2007"],
        }
        self.company = {
            "com_id": [1, 2, 3, 4],
            "name": ["RED", "ORANGE", "BLUE", "GREEN"],
            "city": ["Boston", "New York", "Boston", "Austin"],
        }
        self.orders = {
            "order_id": [1, 2, 3, 4],
            "order_date": ["1/1/2014", "2/1/2014", "3/1/2014", "4/1/2014"],
            "com_id": [3, 4, 1, 1],
            "sales_id": [4, 5, 1, 4],
            "amount": [10000, 5000, 50000, 25000],
        }
        self.expected = {
            "name": ["Amy", "Mark", "Alex"],
        }

    def test_sales_person(self):
        actual = sales_person(
            pd.DataFrame(self.sales_person),
            pd.DataFrame(self.company),
            pd.DataFrame(self.orders),
        )
        expected = pd.DataFrame(self.expected)
        assert_frame_equal(
            actual.reset_index(drop=True), expected.reset_index(drop=True)
        )
