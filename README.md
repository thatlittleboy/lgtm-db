A repository containing LGTM-related gifs and images.

<img alt="wwe-referee-thumbsup" src="https://c.tenor.com/JS6Vtap-SYEAAAAC/wwe-wrestling.gif" width="500">

## Installation
This is just for personal use, so it is not published on PyPI.

Using [pipx](https://pypa.github.io/pipx/):
```shell
pipx install git+https://github.com/thatlittleboy/lgtm-db
```

## Usage
API very much subject to change.

```shell
$ lgtm-db
<img alt="wwe-referee-thumbsup" src="https://c.tenor.com/JS6Vtap-SYEAAAAC/wwe-wrestling.gif" width="500">
```

## Todo
Things that I may or may not get around to doing...
* autogeneration of img/gif gallery markdown file so I can see easily view all the gifs/imgs i have
  * via github actions
  * display name, and the img
  * support lazy loading, if possible
* supporting cli args
  * default with no args should print help message
  * selecting random static imgs or gifs
  * selecting random based on name
* support alternative outputs (not just HTML tags)
  * markdown `![alt-text](url)` syntax
* automating the release process with some tool (Makefile? doit?)

## Release
1. Bump the version number in `setup.cfg` and commit with a commit message `release: v1.0.1`
1. And tag the ref, `git tag v1.0.1`, for example.

## Inspiration
Inspiration from the following repositories:
* https://github.com/seantomburke/shipit.gifs.git
