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
    return balance;
  }
  export function account(_balance: { [title: string]: number }, pay_unit = 100) {
    const balance: { [title: string]: number } = JSON.parse(
      JSON.stringify(_balance)
    );
    let result = "";
    while (true) {
      const summary = getHighAndLow(balance);
      if (!(summary.min < 0 && 0 < summary.max)) {
        break;
      }

      const pay = Math.min(-summary.min, summary.max);
      if (pay < pay_unit) {
        break;
      }
      const round_pay = round(pay, pay_unit);

      balance[summary.argmax] -= round_pay;
      balance[summary.argmin] += round_pay;

      result += `${summary.argmax} → ${summary.argmin}: ${round_pay}\n`;
      console.log(balance);
    }
    return result;
  }

  function round(x: number, unit = 100) {
    const offset = Math.floor(10 ** Math.log10(unit) + 0.5);
    return Math.floor((x + 0.5 * offset) / offset) * offset;
  }

  function getHighAndLow(balance: { [title: string]: number }) {
    const fistKey = Object.keys(balance)[0];
    let max = balance[fistKey];
    let min = balance[fistKey];
    let argmax = fistKey;
    let argmin = fistKey;

    for (const member in balance) {
      if (max < balance[member]) {
        max = balance[member];
        argmax = member;
      } else if (min > balance[member]) {
        min = balance[member];
        argmin = member;
      }
    }
    return { max: max, min: min, argmax: argmax, argmin: argmin };
  }
}
