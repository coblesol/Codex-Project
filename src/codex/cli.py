import sys
from typing import Optional

import click
import requests

@click.group()
def main():
    """Codex command line interface."""


@main.command()
@click.argument("name")
def greet(name: str):
    """Greet NAME with a friendly message."""
    click.echo(f"Hello, {name}! Welcome to the Codex CLI.")


@main.command()
@click.argument("url")
@click.option("--chars", default=100, help="Number of characters to display from the response.")
def fetch(url: str, chars: int):
    """Fetch URL and print the first CHARS characters of the response."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as exc:
        click.echo(f"Error fetching {url}: {exc}", err=True)
        sys.exit(1)

    click.echo(response.text[:chars])


if __name__ == "__main__":
    main()
