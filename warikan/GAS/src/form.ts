import { getEnv } from "./utils";

type AnswerType = (string | string[] | string[][])[][];
type ItemDict = { [title: string]: GoogleAppsScript.Forms.Item };

export namespace Forms {
  export function init(answers: AnswerType, itemDict: ItemDict) {
    console.log("initialize");

    let [[title, members], ...others] = answers.filter(
      ([title, answer]) => title === "参加者を入力する"
    );
    members = (members as string).split(/\s+/).filter((s) => s);
    console.log(members);

    itemDict["支払った人"].asListItem().setChoiceValues(members);
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

export function copyBaseForm(folder: GoogleAppsScript.Drive.Folder) {
  const formFiles = folder.searchFiles(
    `mimeType="${GoogleAppsScript.Base.MimeType.GOOGLE_FORMS}"`
  );
  const DEBUG = getEnv() === "DEBUG";
  if (DEBUG) {
    console.log("in debug");
    while (formFiles.hasNext()) {
      const formFile = formFiles.next();
      if (formFile.getName() === "支払い記録フォーム") {
        return FormApp.openById(formFile.getId());
      }
    }
  }

  while (formFiles.hasNext()) {
    const formFile = formFiles.next();
    if (formFile.getName() === "base") {
      return FormApp.openById(formFile.makeCopy("支払い記録フォーム").getId());
    }
  }
  throw "base form is not found.";
}

export function generateBaseForm(
  baseForm: GoogleAppsScript.Forms.Form,
  members: string[]
) {
  for (const item of baseForm.getItems()) {
    const title = item.getTitle();
    switch (title) {
      case "支払った人":
        item.asListItem().setChoiceValues(members);
        break;
      case "X さんの購入額":
        for (const member of members) {
          const itemPerMember = item.duplicate().setTitle(`${member} さんの購入額`);
          baseForm.moveItem(itemPerMember.getIndex(), item.getIndex());
        }
        baseForm.deleteItem(item);
        break;
    }
  }
  return baseForm;
}
