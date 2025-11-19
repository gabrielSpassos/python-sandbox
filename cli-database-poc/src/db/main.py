import click
import db.datasource as datasource

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
        collect_user_data.main(args=[], standalone_mode=False)


@click.command()
@click.option('--name', prompt='Your name', help='The name to store.')
@click.option('--last-name', prompt='Your last name', help='The last name to store.')
@click.option('--contract-hours', prompt='Your contract monthly hours', help='The contract hours per month to store.')
def collect_user_data(name, last_name, contract_hours):
    data = {
        "name": name,
        "last_name": last_name,
        "contract_hours": contract_hours
    }
    datasource.update_datasource(data)
    datasource_data = datasource.get_or_create_datasource()
    click.echo(datasource_data)


@click.command()
def read():
    datasource_data = datasource.get_or_create_datasource()
    click.echo(datasource_data)


cli.add_command(collect_user_data)
cli.add_command(read)


if __name__ == "__main__":
    cli()
