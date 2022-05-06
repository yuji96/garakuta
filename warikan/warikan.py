import json
import math
from typing import NamedTuple

import pandas as pd


class Row(NamedTuple):
    payer: str
    amount: float
    note: str


def round(x, unit=100):
    d = math.log10(unit)
    offset = int(10**d + 0.5)
    return int((x + 0.5 * offset) // offset * offset)


# members = list("ABCDE")
# balance = pd.Series([-2000, -1500, 1000, 1000, 1500], index=members)

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
init_balance = balance.copy()

pay_unit = 500
last_eps = 250
while True:
    highest_member = balance.idxmax()
    lowest_member = balance.idxmin()
    lowest_amount = balance[lowest_member]
    highest_amount = balance[highest_member]

    if not (lowest_amount < 0 < highest_amount):
        break
    if -lowest_amount <= last_eps:
        break
    pay = min(-lowest_amount, highest_amount)
    round_pay = round(pay, unit=pay_unit)
    # FIXME: round(25) = 50 で無限ループ
    if round_pay == 0:
        break

    account_df.loc[highest_member, lowest_member] += round_pay
    balance[highest_member] -= round_pay
    balance[lowest_member] += round_pay

print(pd.DataFrame(dict(init=init_balance, result=balance)))
print(account_df, end="\n\n")
