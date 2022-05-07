import { getEnv } from "./utils";

type AnswerType = (string | string[] | string[][])[][];

export namespace Forms {
  export function init(answers: AnswerType) {
    console.log("initialize");
    for (const [[title, ans], ..._] of answers) {
      if (title === "参加者を入力する") {
        const members = (ans as string).split(/\s+/);
        console.log(members);
      }
    }
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
