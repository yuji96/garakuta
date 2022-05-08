type ItemDict = { [title: string]: GoogleAppsScript.Forms.Item };
type AnswerDict = { [title: string]: string[][] | string[] | string };

export namespace Forms {
  export function init(
    answerDict: AnswerDict,
    form: GoogleAppsScript.Forms.Form,
    folder: GoogleAppsScript.Drive.Folder,
    itemDict: ItemDict
  ) {
    console.log("start initializing");

    // 参加者を取得する
    const members = (answerDict["参加者を入力する"] as string).trim().split(/\s+/);

    // 古いフォームを削除する
    for (const title in itemDict) {
      if (title.includes(" さんの購入額")) {
        form.deleteItem(itemDict[title]);
      }
    }

    // 参加者を設定する
    itemDict["支払った人（N等分）"].asListItem().setChoiceValues(members);
    itemDict["支払った人（個別会計）"].asListItem().setChoiceValues(members);
    const sectionHeadIndex =
      itemDict["後で個別会計したい支払い記録をする"].getIndex();
    for (const member of members.reverse()) {
      const item = form
        .addTextItem()
        .setTitle(`${member} さんの購入額`)
        .setRequired(true)
        .setValidation(
          FormApp.createTextValidation()
            .requireTextMatchesPattern("[1-9][0-9]*")
            // @ts-ignore
            .setHelpText("自然数を入力してください。")
            .build()
        );
      form.moveItem(item.getIndex(), sectionHeadIndex + 3);
    }

    // TODO: 確認ボタンがOKだったら回答を全削除する。
    form.deleteAllResponses();

    // スプレッドシートを作成する。
    // TODO: スプレッドシートは削除時に前回のバックアップ用に作成するものとして、今回分は作成しない。
    // const oldSheets = folder.searchFiles(
    //   // @ts-ignore
    //   `title contains "割り勘精算フォーム" and mimeType = "${MimeType.GOOGLE_SHEETS}"`
    // );
    // while (oldSheets.hasNext()) {
    //   oldSheets.next().setTrashed(true);
    // }
    // const ss = SpreadsheetApp.create("割り勘精算フォーム");
    // form.setDestination(FormApp.DestinationType.SPREADSHEET, ss.getId());
    // DriveApp.getFileById(ss.getId()).moveTo(folder);

    console.log("complete initializing");
  }
  export function recordUniformPayment(answerDict: AnswerDict) {
    console.log("uniform");
  }
  export function recordIndividualPayment(answerDict: AnswerDict) {
    console.log("individual");
  }
  export function settle(form: GoogleAppsScript.Forms.Form, itemDict: ItemDict) {
    console.log("settle");

    const members = itemDict["支払った人（N等分）"]
      .asListItem()
      .getChoices()
      .map((choice) => choice.getValue());
    const balance: { [title: string]: number } = {};
    for (const member of members) {
      balance[member] = 0;
    }

    // TODO move to warikan.ts
    for (const response of form.getResponses()) {
      const answerDict = generateAnswerDict(response);
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
    console.log(balance);
    itemDict["掲示板"].setHelpText(
      JSON.stringify(balance, null, 2) + "\n\n" + itemDict["掲示板"].getHelpText()
    );
  }

  export function generateItemDict(form: GoogleAppsScript.Forms.Form) {
    const out: ItemDict = {};
    for (const item of form.getItems()) {
      out[item.getTitle()] = item;
    }
    return out;
  }
  export function generateAnswerDict(
    response: GoogleAppsScript.Forms.FormResponse
  ) {
    const out: AnswerDict = {};
    for (const item of response.getItemResponses()) {
      out[item.getItem().getTitle()] = item.getResponse();
    }
    return out;
  }
}
