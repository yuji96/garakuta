chrome.storage.local.get("data", (response) => {
  let data = response["data"];
  for (let pageUrl in data) {
    page = data[pageUrl];

    let wrapper = $("#template .page-wrapper").clone().appendTo("main");
    wrapper.find("a").attr({ href: pageUrl }).text(page["title"]);

    for (let term in page["words"]) {
      let termCard = wrapper
        .find(".template.term-card")
        .clone()
        .removeClass("template")
        .appendTo(wrapper.find("dl"));
      termCard.find("dt").text(term);
      termCard.find("dd").text(page["words"][term]);
    }
    wrapper.find(".template").remove();
  }
});

$(document).on("click", "button.change", function () {
  let changeButton = $(this);
  let compButton = $(this).next();
  let def = $(this).parent().find("dd");
  changeButton.hide();
  compButton.show();
  def.replaceWith(`<input type="text" value="${def.text()}">`);
});

$(document).on("click", "button.complete", function () {
  let input = $(this).parent().find("input");
  let term = input.prev().text();
  const url = $(this).parent().parent().prev().find("a.page-title").attr("href");
  chrome.storage.local.get("data", (response) => {
    let data = response["data"];
    let page = data[url];
    page["words"][term] = input[0].value;
    data[url] = page;
    chrome.storage.local.set({ data: data });
  });
  input.replaceWith(`<dd>${input[0].value}</dd>`);
});

$(document).on("click", "button.delete", function () {
  let termCard = $(this).parent();
  let term = termCard.find("dt").text();
  const url = termCard.parent().prev().find("a.page-title").attr("href");
  chrome.storage.local.get("data", (response) => {
    let data = response["data"];
    let page = data[url];
    delete page["words"][term];
    if (!Object.keys(page["words"]).length) {
      delete data[url];
    } else {
      data[url] = page;
    }
    chrome.storage.local.set({ data: data });
  });
  termCard.remove();
});
