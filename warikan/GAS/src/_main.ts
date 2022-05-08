import { Forms } from "./form";

export function main(event: GoogleAppsScript.Events.FormsOnFormSubmit) {
  // const ENV = getEnv();

  const form = FormApp.getActiveForm();
  const folder = DriveApp.getFileById(form.getId()).getParents().next();
  const itemDict = Forms.generateItemDict(form);

  // TODO: answerDict を定義する。

  const answerDict = Forms.generateAnswerDict(event.response);

  switch (answerDict["なにする？"]) {
    case "初期化をする":
      Forms.init(answerDict, form, folder, itemDict);
      break;
    case "後で N 等分したい支払い記録をする":
      Forms.recordUniformPayment(answers);
      break;
    case "後で個別会計したい支払い記録をする":
      Forms.recordIndividualPayment(answers);
      break;
    case "割り勘精算をする":
      Forms.settle(answers);
      break;
  }
}
