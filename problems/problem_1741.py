# 1741. Find Total Time Spent by Each Employee
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | emp_id      | int  |
# | event_day   | date |
# | in_time     | int  |
# | out_time    | int  |
# +-------------+------+
# (emp_id, event_day, in_time) is the primary key (combinations of columns
# with unique values) of this table.
# The table shows the employees' entries and exits in an office.
# event_day is the day at which this event happened, in_time is the minute at
# which the employee entered the office, and out_time is the minute at which
# they left the office.
# in_time and out_time are between 1 and 1440.
# It is guaranteed that no two events on the same day intersect in time, and
# in_time < out_time.
#
# Write a solution to calculate the total time in minutes spent by each
# employee on each day at the office. Note that within one day, an employee
# can enter and leave more than once. The time spent in the office for a
# single entry is out_time - in_time.
#
# Return the result table in any order.
#
# The result format is in the following example.

import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.assign(
        total_time=lambda row: row["out_time"] - row["in_time"]
    )
    return (
        employees.groupby(["emp_id", "event_day"], as_index=False)
        .sum()
        .sort_values(by=["event_day"])
        .rename(columns={"event_day": "day"})[["day", "emp_id", "total_time"]]
    )
