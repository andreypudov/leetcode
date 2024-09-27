# 2891. Method Chaining
#
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | name        | object |
# | species     | object |
# | age         | int    |
# | weight      | int    |
# +-------------+--------+
#
# Write a solution to list the names of animals that weigh strictly more than
# 100 kilograms.
#
# Return the animals sorted by weight in descending order.
#
# The result format is in the following example.

import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values(
        by="weight", ascending=False
    )[["name"]]
