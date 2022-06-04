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
* supporting cli args
  * default with no args should print help message
  * selecting random static imgs or gifs
  * selecting random based on name
* support alternative outputs (not just HTML tags)
  * markdown `![alt-text](url)` syntax

## Inspiration
Inspiration from the following repositories:
* https://github.com/seantomburke/shipit.gifs.git
