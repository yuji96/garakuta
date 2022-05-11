chrome.runtime.onInstalled.addListener(function () {
  chrome.contextMenus.create({
    id: "tangoTown",
    title: "丹後町",
    type: "normal",
    contexts: ["selection"],
  });
});

chrome.contextMenus.onClicked.addListener((info, tab) => {
  addWord(info.selectionText, tab.title, tab.url);
});

chrome.browserAction.onClicked.addListener(() => {
  chrome.tabs.create({ url: chrome.extension.getURL("main.html") });
});

chrome.commands.onCommand.addListener((command) => {
  if (command === "add-word") {
    // this is not working in pdf viewer.
    // chrome.tabs.executeScript({
    //   code: `document.execCommand("copy");`,
    // });
    let pasteText = $("#paste-text");
    pasteText.show().focus();
    document.execCommand("paste");
    const copiedText = pasteText[0].value;
    pasteText.hide();
    pasteText[0].value = "";

    chrome.tabs.query({ active: true }, (tabs) => {
      addWord(copiedText, tabs[0].title, tabs[0].url);
    });
  }
});

function addWord(selectionText, pageTitle, pageUrl) {
  chrome.storage.local.get("data", (response) => {
    let data = response["data"] || {};
    let page = data[pageUrl] || { title: pageTitle, words: {} };
    page["words"][selectionText] = "not yet";
    data[pageUrl] = page;
    chrome.storage.local.set({ data: data }); // 気まぐれで失敗する
  });
  let wrapper = $(`.page-title[href="${pageUrl}"]`).parent().parent();
  if (!wrapper.length) {
    wrapper = $("#template .page-wrapper").clone().appendTo("main");
    wrapper.find("a").attr({ href: pageUrl }).text(pageTitle);
    wrapper.find(".template").remove();
  }
  let termCard = $(".template.term-card")
    .clone()
    .removeClass("template")
    .appendTo(wrapper.find("dl"));
  termCard.find("dt").text(selectionText);
  termCard.find("dd").text("not yet");
}
