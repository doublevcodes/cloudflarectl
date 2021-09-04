# Contributing to `cloudflarectl`

We thank you for your interest in contributing to the
`cloudflarectl` project. Must know information:

- `cloudflarectl` is written in [Python 3.9](https://python.org)
- The CLI is built using [Typer](https://typer.tiangolo.com)
- Core interaction with Cloudflare is done through [Pydantic](https://pydantic.readthedocs.io) and [Requests](https://docs.python-requests.org/en/master/)

## Setting up `cloudflarectl`

1. Install [Poetry](https://python-poetry.com) if you haven't already
2. Fork this repository using the instructions [here](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository)
3. Clone your fork onto your local machine using:
```zsh
$ git clone https://github.com/<YOUR_USERNAME>/cloudflarectl && cd cloudflarectl
```
4. Install all of `cloudflarectl`'s dependencies with Poetry through:
```zsh
$ poetry install
```
5. Enter the virtual environment created by Poetry:
```zsh
$ poetry shell
```
5. Make your changes!
6. Try out your new `cloudflarectl` by making sure you are inside the virtual environment (`poetry shell`) and then running:
```zsh
$ poetry install
$ cloudflarectl --help  # This is your local cloudflarectl!
```
