# 2880. Select Data
#
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+
#
# Write a solution to select the name and age of the student with
# student_id = 101.
#
# The result format is in the following example.

import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students["student_id"] == 101][["name", "age"]]