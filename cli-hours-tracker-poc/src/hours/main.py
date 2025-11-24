import click
import hours.datasource as datasource

LOGO = click.style(r"""
  ██████╗   ██████╗ 
  ██╔══██╗  ██╔══██╗
  ██║  ██║  ██████╔╝
  ██║  ██║  ██╔══██╗
  ██████╔╝  ██████╔╝
  ╚═════╝   ╚═════╝ 
""", fg="bright_cyan")


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(LOGO)
        welcome_display()


def welcome_display():
    datasource_data = datasource.get_or_create_datasource()
    if "name" in datasource_data and "last_name" in datasource_data and "contract_hours" in datasource_data:
        name = datasource_data["name"]
        last_name = datasource_data["last_name"]
        click.echo(f"Welcome back, {name} {last_name}!")
        click.echo(f"Contract hours per month: {datasource_data['contract_hours']}")
    else:
        click.echo("Welcome! Let's set up your hours tracker.")
        collect_user_data.main(args=[], standalone_mode=False)
        click.echo("Thank You! Setup hours tracker done successfully.")


@click.command()
@click.option('--name', prompt='Your name', help='The name to store.')
@click.option('--last-name', prompt='Your last name', help='The last name to store.')
@click.option('--contract-hours', type=int, prompt='Your contract monthly hours', help='The contract hours per month to store.')
def collect_user_data(name, last_name, contract_hours):
    data = {
        "name": name,
        "last_name": last_name,
        "contract_hours": contract_hours
    }
    datasource.update_datasource(data)


if __name__ == "__main__":
    cli()
