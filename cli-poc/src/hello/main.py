import click

@click.group()
def cli():
    """Hello CLI — available commands below."""
    pass


@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
@click.option("--excited", is_flag=True, help="Add excitement")
def greet(name, excited):
    greeting = f"Hello, {name}"
    if excited:
        greeting += "!!!"
    click.echo(greeting)


@click.command()
@click.option('--name', prompt='Your name', help='The person to goodbye.')
def bye(name):
    bye = f"Goodbye, {name}!"
    click.echo(bye)


cli.add_command(greet)
cli.add_command(bye)


if __name__ == "__main__":
    cli()
