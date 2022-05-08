import math
from typing import NamedTuple

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


def account(initial_balance: pd.Series, pay_unit=100):
    balance = initial_balance.copy()
    members = initial_balance.index
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
