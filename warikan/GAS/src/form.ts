type AnswerType = (string | string[] | string[][])[][];
type ItemDict = { [title: string]: GoogleAppsScript.Forms.Item };

export namespace Forms {
  export function init(
    answers: AnswerType,
    form: GoogleAppsScript.Forms.Form,
    itemDict: ItemDict
  ) {
    console.log("start initializing");

    let [[title, members], ...others] = answers.filter(
      ([title, answer]) => title === "参加者を入力する"
    );
    members = (members as string).trim().split(/\s+/);
    console.log(members);

    itemDict["支払った人"].asListItem().setChoiceValues(members);

    for (const title in itemDict) {
      if (title.includes(" さんの購入額")) {
        form.deleteItem(itemDict[title]);
      }
    }
    const sectionHeadIndex =
      itemDict["後で個別会計したい支払い記録をする"].getIndex() + 1;
    for (const member of members.reverse()) {
      const item = form
        .addTextItem()
        .setTitle(`${member} さんの購入額`)
        .setRequired(true)
        // @ts-ignore
        .setValidation(FormApp.createTextValidation().requireNumber().build());
      form.moveItem(item.getIndex(), sectionHeadIndex);
    }

    // TODO: 確認ボタンがOKだったら回答を全削除する。
    form.deleteAllResponses();
    console.log("complete initializing");
  }
  export function recordUniformPayment(answers: AnswerType) {
    console.log("uniform");
  }
  export function recordIndividualPayment(answers: AnswerType) {
    console.log("individual");
  }
  export function settle(answers: AnswerType) {
    console.log("settle");
  }

  export function generateItemDict(form: GoogleAppsScript.Forms.Form) {
    let out: ItemDict = {};
    for (const item of form.getItems()) {
      out[item.getTitle()] = item;
    }
    return out;
  }
}
