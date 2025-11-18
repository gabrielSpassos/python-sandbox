import click

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
@click.option("--excited", is_flag=True, help="Add excitement")
def greet(name, excited):
    greeting = f"Hello, {name}"
    if excited:
        greeting += "!!!"
    click.echo(greeting)

if __name__ == "__main__":
    greet()
