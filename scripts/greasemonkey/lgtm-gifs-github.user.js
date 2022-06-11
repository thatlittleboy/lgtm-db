// ==UserScript==
// @name         lgtm-gifs-github
// @namespace    https://www.github.com/thatlittleboy
// @version      1.0
// @author       thatlittleboy
// @include      https://github.com/*/*/pull/*
// @require      https://cdnjs.cloudflare.com/ajax/libs/js-yaml/4.1.0/js-yaml.min.js
// @grant        GM.xmlHttpRequest
// ==/UserScript==

(function () {
    console.log("Greasemonkey lgtm-gifs-github running...");
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
            "click event registered. name:",
            e.target.name,
            ", value:",
            e.target.value
        );

        if (all_lgtm.length && e.target.name === "pull_request_review[event]" && e.target.value === "approve") {
            console.log("inside approved if-block");

            // user just clicked on the "Approve" button
            // find the comment box by id
            msg = document.querySelector("#pull_request_review_body");

            // select a random gif
            const selected = all_lgtm[Math.floor(Math.random() * all_lgtm.length)];

            // replace the msg value
            msg.value = `${msg.value}\n\n![${selected.name}](${selected.url})`;
        }
    });
})();
