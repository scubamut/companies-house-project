"""Console script for companies_house."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("companies-house-project")
    click.echo("=" * len("companies-house-project"))
    click.echo("companies house api to extract companies data")


if __name__ == "__main__":
    main()  # pragma: no cover
