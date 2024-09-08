# 1050. Actors and Directors Who Cooperated At Least Three Times
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | actor_id    | int     |
# | director_id | int     |
# | timestamp   | int     |
# +-------------+---------+
# timestamp is the primary key (column with unique values) for this table.
#
# Write a solution to find all the pairs (actor_id, director_id) where the
# actor has cooperated with the director at least three times.
#
# Return the result table in any order.
#
# The result format is in the following example.

import pandas as pd


def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # return actor_director.groupby(["actor_id", "director_id"])[["actor_id", "director_id"]]
    # .filter(lambda group: len(group) >= 3).drop_duplicates()
    data = actor_director.groupby(["actor_id", "director_id"], as_index=False).agg(
        count=("actor_id", "count")
    )
    return data[data["count"] >= 3][["actor_id", "director_id"]]
