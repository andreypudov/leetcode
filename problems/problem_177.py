# 177. Nth Highest Salary
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
# Write a solution to find the nth highest salary from the Employee table. If
# there is no nth highest salary, return null.
#
# The result format is in the following example.

import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    column_name = "getNthHighestSalary(" + str(N) + ")"
    if N <= 0 or len(employee["salary"].unique()) < N:
        return pd.DataFrame({column_name: [None]})
    salary = pd.Series(employee["salary"].unique()).nlargest(N).iloc[N - 1]
    return pd.DataFrame({column_name: [salary]})
