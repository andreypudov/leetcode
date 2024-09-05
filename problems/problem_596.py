# 596. Classes More Than 5 Students
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | student     | varchar |
# | class       | varchar |
# +-------------+---------+
# (student, class) is the primary key (combination of columns with unique
# values) for this table.
# Each row of this table indicates the name of a student and the class in which
# they are enrolled.
#
# Write a solution to find all the classes that have at least five students.
#
# Return the result table in any order.
#
# The result format is in the following example.

import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # courses = courses.groupby("class").count().reset_index()
    # return courses[(courses["student"] >= 5)][["class"]]
    class_counts = courses["class"].value_counts()
    return class_counts[class_counts >= 5].index.to_frame(index=False)
