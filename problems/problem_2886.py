# 2886. Change Data Type
#
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# | grade       | float  |
# +-------------+--------+
#
# Write a solution to correct the errors:
#
# The grade column is stored as floats, convert it to integers.
#
# The result format is in the following example.

import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({"grade": int})
