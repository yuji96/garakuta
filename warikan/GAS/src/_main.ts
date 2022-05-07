import { Forms } from "./form";

// TODO: フォームを統合する。
export function main(event: GoogleAppsScript.Events.FormsOnFormSubmit) {
  // const ENV = getEnv();

  // const form = FormApp.getActiveForm();
  const response = event.response;

  const [[_, answerType], ...answer] = response
    .getItemResponses()
    .map((ir) => [ir.getItem().getTitle(), ir.getResponse()]);
  // [ [ 'なにする？', '初期化をする' ], [ '参加者を入力する', 'a b' ] ]

  switch (answerType) {
    case "初期化をする":
      Forms.init(answer);
      break;
    case "後で N 等分したい支払い記録をする":
      Forms.recordUniformPayment(answer);
      break;
    case "後で個別会計したい支払い記録をする":
      Forms.recordIndividualPayment(answer);
      break;
    case "割り勘精算をする":
      Forms.settle(answer);
      break;
  }

  // const folder = DriveApp.getFileById(form.getId()).getParents().next();
  // const baseForm = copyBaseForm(folder);
  // generateBaseForm(baseForm, members);
  // console.log(baseForm.getPublishedUrl());
  // form.setConfirmationMessage(
  //   `支払い記録フォームを作成しました。\n${baseForm.getPublishedUrl()}`
  // );
}
