# 570. Managers with at Least 5 Direct Reports
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | department  | varchar |
# | managerId   | int     |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the name of an employee, their department,
# and the id of their manager.
# If managerId is null, then the employee does not have a manager.
# No employee will be the manager of themself.
#
# Write a solution to find managers with at least five direct reports.
#
# Return the result table in any order.
#
# The result format is in the following example.

import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    """return (
        employee.groupby("managerId")
        .size()
        .reset_index(name="employee_count")
        .query("employee_count >= 5")
        .drop("employee_count", axis=1)
        .merge(employee, left_on="managerId", right_on="id")[["name"]]
    )"""
    grouped = employee.groupby("managerId").count()
    manager_ids = grouped[grouped["id"] >= 5].index.to_list()
    return employee[employee["id"].isin(manager_ids)][["name"]]
