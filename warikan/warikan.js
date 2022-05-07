var DEBUG = false;

// TODO: フォームを統合したい。
function submitForm(event) {
  const initForm = FormApp.getActiveForm();
  const members = !DEBUG
    ? event.response.getItemResponses().pop().getResponse().split("\n")
    : ["a", "b"];
  const folder = DriveApp.getFileById(initForm.getId()).getParents().next();
  const baseForm = copyBaseForm(folder);
  generateBaseForm(baseForm, members);
  console.log(baseForm.getPublishedUrl());
  initForm.setConfirmationMessage(
    `支払い記録フォームを作成しました。\n${baseForm.getPublishedUrl()}`
  );
}

function copyBaseForm(folder) {
  const formFiles = folder.searchFiles(`mimeType="${MimeType.GOOGLE_FORMS}"`);
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

function generateBaseForm(baseForm, members) {
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
