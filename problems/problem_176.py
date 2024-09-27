# 176. Second Highest Salary
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | salary      | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains information about the salary of an employee.
#
# Write a solution to find the second highest distinct salary from the
# Employee table. If there is no second highest salary, return null (return
# None in Pandas).
#
# The result format is in the following example.

import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salaries = (
        employee["salary"].sort_values(ascending=False).drop_duplicates()
    )
    return pd.DataFrame(
        {
            "SecondHighestSalary": [
                None if sorted_salaries.size < 2 else sorted_salaries.iloc[1]
            ]
        }
    )
