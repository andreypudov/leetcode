# 178. Rank Scores
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | score       | decimal |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table contains the score of a game. Score is a floating
# point value with two decimal places.
#
# Write a solution to find the rank of the scores. The ranking should be
# calculated according to the following rules:
#
#    - The scores should be ranked from the highest to the lowest.
#    - If there is a tie between two scores, both should have the same ranking.
#    - After a tie, the next ranking number should be the next consecutive
#      integer value. In other words, there should be no holes between ranks.
#
# Return the result table ordered by score in descending order.
#
# The result format is in the following example.

import pandas as pd


def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    return (
        scores.assign(
            rank=scores["score"].rank(method="dense", ascending=False)
        )
        .sort_values(by="score", ascending=False)
        .drop("id", axis=1)
    )
