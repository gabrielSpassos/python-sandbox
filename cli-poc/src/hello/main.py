import click

LOGO = click.style(r"""
   _____ _      _____ 
  / ____| |    |_   _|
 | |    | |      | |  
 | |    | |      | |  
 | |____| |____ _| |_ 
  \_____|______|_____|
""", fg="bright_cyan")


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(LOGO)
        click.echo(ctx.get_help())


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
@click.option('--last-name', prompt='Your last name', help='The person to goodbye.')
def bye(name, last_name):
    bye = f"Goodbye, {name} {last_name}!"
    click.echo(bye)


cli.add_command(greet)
cli.add_command(bye)


if __name__ == "__main__":
    cli()
