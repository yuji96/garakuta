import json
import math
from typing import List, NamedTuple

import pandas as pd

DF = pd.DataFrame


class Row(NamedTuple):
    payer: str
    amount: float
    note: str


def round(x, unit=100):
    d = math.log10(unit)
    offset = int(10**d + 0.5)
    return int((x + 0.5 * offset) // offset * offset)


def calc_balance(members: List[str]):
    transition_df = pd.DataFrame(data=0, index=members, columns=members)
    for row in log_df.itertuples():
        row: Row
        if pd.isna(row.note):
            transition_df.loc[row.payer] += row.amount / len(members)
        else:
            transition_df.loc[row.payer] += pd.Series(json.loads(row.note))

    borrowing = transition_df.sum(axis="rows")
    lending = transition_df.sum(axis="columns")
    balance = borrowing - lending
    return balance


def account(initial_balance: DF, pay_unit=100):
    balance = initial_balance.copy()
    account_df = pd.DataFrame(data=0, index=members, columns=members)

    while True:
        highest_member = balance.idxmax()
        lowest_member = balance.idxmin()
        lowest_amount = balance[lowest_member]
        highest_amount = balance[highest_member]

        if not (lowest_amount < 0 < highest_amount):
            break

        pay = min(-lowest_amount, highest_amount)
        if pay < pay_unit:
            break
        round_pay = round(pay, unit=pay_unit)

        account_df.loc[highest_member, lowest_member] += round_pay
        balance[highest_member] -= round_pay
        balance[lowest_member] += round_pay

    return account_df, balance


if __name__ == "__main__":
    log_df = pd.read_csv("data.csv")
    members = list("ABCD")

    initial_balance = calc_balance(list("ABCD"))
    account_df, balance = account(initial_balance)
    print(pd.DataFrame(dict(init=initial_balance, result=balance)))
    print(account_df, end="\n\n")
