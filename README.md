# Codex Project

A small Python command-line interface (CLI) built to showcase basic skills with
[Click](https://click.palletsprojects.com/) and `requests`. Use it to greet
someone or fetch data from the internet.

## Features

- `greet NAME` - display a personalized greeting
- `fetch URL` - print the first part of a web page's content

## Getting Started

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Run the CLI

```bash
python -m codex.cli greet "World"
python -m codex.cli fetch https://example.com --chars 200
```

Feel free to extend the tool with your own commands!

