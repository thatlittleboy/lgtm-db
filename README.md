<h2 align="center">~~~ LGTM db ~~~</h2>

<p align="center">
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

A repository containing LGTM-related gifs and images.

<img alt="wwe-referee-thumbsup" src="https://c.tenor.com/JS6Vtap-SYEAAAAC/wwe-wrestling.gif" width="500">

---

View all the available images and gifs in the [gallery page](docs/gallery.md).

---

## Installation
This project is just for personal use, so it is not published on PyPI.

Using [pipx](https://pypa.github.io/pipx/) to install directly from github:
```shell
pipx install git+https://github.com/thatlittleboy/lgtm-db
```

## Usage
This project exposes a simple CLI API that prints out the HTML img tag of a randomly selected gif/image in the db.

```shell
$ lgtm-db
<img alt="wwe-referee-thumbsup" src="https://c.tenor.com/JS6Vtap-SYEAAAAC/wwe-wrestling.gif" width="500">
```

**NOTE**: API is very much subject to change.

## Todo
Things that I may or may not get around to doing...
* support lazy loading of [gallery](docs/gallery.md) markdown file
  * loading can become quite bloated if the gallery gets big
* supporting cli args
  * default with no args should print help message
  * selecting random static imgs or gifs
  * selecting random based on name
* support alternative outputs (not just HTML tags)
  * markdown `![alt-text](url)` syntax
* automating the release process with some tool (Makefile? doit?)
* write a local pre-commit hook in this repo to test:
  * if there are duplicated names (id's should be unique)
  * if there are duplicated urls

## Release
1. Bump the version number in `setup.cfg` and commit with a commit message `release: v1.0.1`
1. And tag the ref, `git tag v1.0.1`, for example.

## Inspiration
Inspiration from the following repositories:
* https://github.com/seantomburke/shipit.gifs
* https://github.com/chriskuehl/shipit
* https://github.com/maludecks/take-my-approval
