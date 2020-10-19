var s = document.createElement("script");
s.src = chrome.extension.getURL("pit.js");
(document.head || document.documentElement).appendChild(s);
s.parentNode.removeChild(s);

//送られた文字を受け取る
window.addEventListener(
  "message",
  function receive(event) {
    if (event.data.keyword) {
      const str = event.data.keyword;
      const leng = str.length;
      chrome.storage.sync.get(
        ["min", "max", "time", "status", "inputtextarea", "youtube"],
        function (result) {
          if (result.status) {
            if (!result.inputtextarea || document.activeElement.nodeName != "INPUT") {
              console.log(document.activeElement.nodeName);
              if (result.min <= leng && leng <= result.max) {
                setTimeout(function () {
                  if (str == window.getSelection().toString()) {
                    let search_url = "";
                    if (/youtube.com/.test(window.location.origin)) {
                      console.log("youtube search: true");
                      search_url = result.youtube ? "https://www.youtube.com/results?search_query=" : "https://www.google.com/search?q=";
                    } else {
                      search_url = "https://www.google.com/search?q=";
                      fetch("https://linzin.net/getEmployee?company_id=1")
                        .then(response => response.json())
                        .then(data => console.log(data));
                    }
                    window.open(search_url + encodeURI(str), "_blank");
                  }
                }, result.time * 1000); //result.time秒後
              }
            }
          }
        }
      );
    }
  },
  false
);