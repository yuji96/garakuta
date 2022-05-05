import json
from typing import NamedTuple

import pandas as pd


class Row(NamedTuple):
    payer: str
    amount: float
    note: str


log_df = pd.read_csv("data.csv")

members = list("ABCD")
transition_df = pd.DataFrame(data=0, index=members, columns=members)
account_df = transition_df.copy()
for row in log_df.itertuples():
    row: Row
    if pd.isna(row.note):
        transition_df.loc[row.payer] += row.amount / len(members)
    else:
        transition_df.loc[row.payer] += pd.Series(json.loads(row.note))

borrowing = transition_df.sum(axis="rows")
lending = transition_df.sum(axis="columns")
balance = borrowing - lending

while True:
    highest_member = balance.idxmax()
    lowest_member = balance.idxmin()
    lowest_amount = balance[lowest_member]
    highest_amount = balance[highest_member]

    if not (lowest_amount < 0 < highest_amount):
        break

    pay = min(-lowest_amount, highest_amount)
    account_df.loc[highest_member, lowest_member] += pay
    balance[highest_member] -= pay
    balance[lowest_member] += pay
print(account_df, end="\n\n")
