type AnswerDict = { [title: string]: string[][] | string[] | string };

export namespace Warikan {
  export function toBalance(answerDicts: AnswerDict[], members: string[]) {
    const balance: { [title: string]: number } = {};
    for (const member of members) {
      balance[member] = 0;
    }

    for (const answerDict of answerDicts) {
      switch (answerDict["なにする？"]) {
        case "後で N 等分したい支払い記録をする":
          const totalPrice = parseInt(
            answerDict["支払った合計金額を入力する"] as string
          );
          const pricePerMember = totalPrice / members.length;
          for (const member of members) {
            if (member === answerDict["支払った人（N等分）"]) {
              balance[member] -= totalPrice;
            }
            balance[member] += pricePerMember;
          }
          break;

        case "後で個別会計したい支払い記録をする":
          for (const member of members) {
            const price = parseInt(answerDict[`${member} さんの購入額`] as string);
            balance[answerDict["支払った人（個別会計）"] as string] -= price;
            balance[member] += price;
          }
      }
    }
  }

const log = [
  ["A", 10000, null],
  ["B", 7000, null],
  ["C", 3500, null],
  ["D", 12000, null],
  ["B", 3000, '"{"A": 2000, "B": 1200, "C": 1000, "D": 2000}"'],
];

const n = members.length;
let transition = zeros(n);
let account = zeros(n);

print(log);

}
}
