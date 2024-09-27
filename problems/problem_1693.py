# 1693. Daily Leads and Partners
#
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | date_id     | date    |
# | make_name   | varchar |
# | lead_id     | int     |
# | partner_id  | int     |
# +-------------+---------+
# There is no primary key (column with unique values) for this table. It may
# contain duplicates.
# This table contains the date and the name of the product sold and the IDs of
# the lead and partner it was sold to.
# The name consists of only lowercase English letters.
#
# For each date_id and make_name, find the number of distinct lead_id's and
# distinct partner_id's.
#
# Return the result table in any order.
#
# The result format is in the following example.

import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return (
        daily_sales.groupby(["date_id", "make_name"], as_index=False)
        .nunique()
        .rename(
            columns={"lead_id": "unique_leads", "partner_id": "unique_partners"}
        )
    )
