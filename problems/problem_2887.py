# 2887. Fill Missing Data
#
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | quantity    | int    |
# | price       | int    |
# +-------------+--------+
#
# Write a solution to fill in the missing value as 0 in the quantity column.
#
# The result format is in the following example.

import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"] = products["quantity"].fillna(0)
    return products
