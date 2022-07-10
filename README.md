<h1 align="center">~~~ LGTM db ~~~</h1>

<p align="center">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/thatlittleboy/lgtm-db/actions"><img alt="Actions Status" src="https://github.com/thatlittleboy/lgtm-db/actions/workflows/tests.yml/badge.svg"></a>
</p>

A repository containing LGTM-related gifs and images for PR approvals and merges.

<img alt="wwe-referee-thumbsup" src="https://c.tenor.com/JS6Vtap-SYEAAAAC/wwe-wrestling.gif" width="500">

---

View all the available images and gifs in the [gallery page](https://thatlittleboy.github.io/lgtm-db/).

---

## ⬇️ Installation
This project is just for personal use, so it is not published on PyPI.

Using [pipx](https://pypa.github.io/pipx/) to install directly from github:
```shell
$ pipx install git+https://github.com/thatlittleboy/lgtm-db
```

## 🚀 Usage
### CLI
This project exposes a simple CLI API that prints out the HTML img tag of a randomly selected gif/image in the db.

```shell
$ lgtm-db
<img alt="wwe-referee-thumbsup" src="https://c.tenor.com/JS6Vtap-SYEAAAAC/wwe-wrestling.gif" width="500" height="390">
```
You can then pipe the result into `pbcopy` etc. to copy the result into your clipboard.

**NOTE**: API is very much subject to change.

### Browser user script
Integration with the browser is experimental.
You need to install Greasemonkey / Tampermonkey, and invoke a user script to insert a random gif into the message box (upon PR approval, or any other Javascript event you like).

Sample user scripts for Gitlab and Github are found in the [scripts folder](scripts/greasemonkey).

Demo:
<img src="./docs/assets/greasemonkey-demo-gh.mp4">

## 👷 Development
Pip install in editable mode (in a virtualenv).
```shell
(venv) $ pip install -e ".[dev]"
```

### 📌 Release
1. Bump the version number in `setup.cfg` and commit with a commit message `release: v1.0.1`
1. And tag the ref, `git tag v1.0.1`, for example.

## ⚡️ Inspiration
Inspiration from the following repositories:
* https://github.com/seantomburke/shipit.gifs
* https://github.com/chriskuehl/shipit
* https://github.com/maludecks/take-my-approval
