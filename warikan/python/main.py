import pandas as pd

from warikan import account


def csv2balance(path):
    df = pd.read_csv(path)
    members = [c.split()[0] for c in map(str, df.columns) if c.endswith(" さんの購入額")]
    balance = {m: 0 for m in members}

    for _, answer_dict in df.iterrows():
        if answer_dict["なにする？"] == "後で N 等分したい支払い記録をする":
            total_price = answer_dict["支払った合計金額を入力する"]
            price_per_member = total_price / len(members)
            for member in members:
                if member == answer_dict["支払った人（N等分）"]:
                    balance[member] -= total_price
                balance[member] += price_per_member
        elif answer_dict["なにする？"] == "後で個別会計したい支払い記録をする":
            for member in members:
                balance[
                    answer_dict["支払った人（個別会計）"]] -= answer_dict[f"{member} さんの購入額"]
                balance[member] += answer_dict[f"{member} さんの購入額"]

    return balance


if __name__ == "__main__":
    balance = csv2balance("割り勘精算フォーム.csv")
    print(balance)
    print(*account(pd.Series(balance)), sep="\n" * 2)
