<h1 align="center">~~~ LGTM db ~~~</h1>

<p align="center">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://github.com/charliermarsh/ruff"><img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json"></a>
<a href="https://github.com/pre-commit/pre-commit"><img alt="pre-commit" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" style="max-width:100%;"></a>
<a href="https://github.com/thatlittleboy/lgtm-db/actions"><img alt="Actions Status" src="https://github.com/thatlittleboy/lgtm-db/actions/workflows/tests.yml/badge.svg"></a>
<a href="https://thatlittleboy.github.io/lgtm-db/"><img alt="GIF count" src="https://byob.yarr.is/thatlittleboy/lgtm-db/count"></a>
</p>

A repository containing LGTM-related gifs and images for PR approvals and merges.

<img alt="wwe-referee-thumbsup" src="https://c.tenor.com/JS6Vtap-SYEAAAAC/wwe-wrestling.gif" width="500">

---

View all the available images and gifs in the [gallery page](https://thatlittleboy.github.io/lgtm-db/).

---

## ⬇️ Installation

This project is just for personal use, so it is not published on PyPI.

Using [pipx](https://pypa.github.io/pipx/) (Python 3.8+ only) to install directly from github:

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

**WARNING**: API is very much subject to change.

```
usage: lgtm-db [-h] [-V] [-I PATTERN] [-E PATTERN] [-wd WIDTH]

Get a randomly-generated LGTM gif or image.

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -I PATTERN, --include PATTERN
                        Apply an inclusive filter on the list of gifs before random choice (matches
                        are included). The filter condition is treated as a regex query if it starts
                        with ^ and ends with $. For non-regex conditions, a simple substring check is
                        used. Multiple conditions are supported. Exclusions are given higher priority
                        over inclusions.
  -E PATTERN, --exclude PATTERN
                        Apply an exclusive filter on the list of gifs before random choice (matches
                        are excluded). The filter condition is treated as a regex query if it starts
                        with ^ and ends with $. For non-regex conditions, a simple substring check is
                        used. Multiple conditions are supported. Exclusions are given higher priority
                        over inclusions.
  -wd WIDTH, --width WIDTH
                        Specify the width of the output gif. A non-positive width will result in an
                        error. Only applicable for HTML.
```

### Browser user script

You need to install Greasemonkey / Tampermonkey, and invoke a user script to insert a random gif into the message box (upon PR approval, or any other Javascript event you like).

Sample user scripts for Gitlab and Github are found in the [scripts folder](scripts/greasemonkey).

**Demo usage in Github PR**

https://user-images.githubusercontent.com/30731072/178128944-bf360ded-dd8d-4b4f-acb7-56e68f28eceb.mp4

## 👷 Development

Pip install in editable mode (in a virtualenv).

```shell
(venv) $ pip install -e ".[dev]"
```

Some personal notes on creating/editing gifs are in the [Github wiki](https://github.com/thatlittleboy/lgtm-db/wiki).

### 📌 Release

1. Create a new branch called `release-v1.8.0`, for example, from the `main` branch.
1. Bump the version number in [`__version__.py`](lgtm_db/__version__.py) and commit with a commit message `release: v1.8.0`. And push up to remote.
1. Create a PR, attach the following output
   ```shell
   git log --oneline --no-decorate --perl-regexp --author='^(?!.*\[bot\]).*$' HEAD ^v1.7.0
   ```
   to the PR description. Merge this branch into `main`.
1. Then tag the ref, `git tag v1.8.0`, for example, on the `main` branch. Push the tags to remote.

## ⚡️ Inspiration

Inspiration from the following repositories:

- https://github.com/seantomburke/shipit.gifs
- https://github.com/chriskuehl/shipit
- https://github.com/maludecks/take-my-approval
