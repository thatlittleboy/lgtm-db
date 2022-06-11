// ==UserScript==
// @name         lgtm-gifs-gitlab
// @namespace    https://www.github.com/thatlittleboy
// @version      1.0
// @author       thatlittleboy
// @include      https://gitlab.com/*/*/-/merge_requests/*
// @require      https://cdnjs.cloudflare.com/ajax/libs/js-yaml/4.1.0/js-yaml.min.js
// @grant        GM.xmlHttpRequest
// ==/UserScript==

(function () {
    console.log("Greasemonkey lgtm-gifs-gitlab running...");
    let all_lgtm;

    GM.xmlHttpRequest({
        method: "GET",
        url: "https://raw.githubusercontent.com/thatlittleboy/lgtm-db/main/lgtm_db/data/db.yaml",
        onload: function (resp) {
            if (resp.status === 200) {
                try {
                    const ymldoc = jsyaml.load(resp.response);
                    all_lgtm = ymldoc["gifs"].concat(ymldoc["images"]);
                } catch (e) {
                    console.log("error", e);
                    all_lgtm = [];
                }
                // console.log(all_lgtm);
            }
        },
    });

    document.body.addEventListener("click", function (e) {
        let msg;
        console.log(
            "click event registered. className:",
            e.target.className,
            ", innerText:",
            e.target.innerText
        );

        if (all_lgtm.length && e.target.className === "gl-button-text" && e.target.innerText === "Approve") {
            console.log("inside approved if-block");

            // user just clicked on the "Approve" button
            // find the comment box by id
            msg = document.querySelector("#note-body");

            // select a random gif
            const selected = all_lgtm[Math.floor(Math.random() * all_lgtm.length)];

            // replace the msg value
            msg.value = `${msg.value}\n\n![${selected.name}](${selected.url})`;
            msg.dispatchEvent(new Event("change"));
        }
    });
})();
