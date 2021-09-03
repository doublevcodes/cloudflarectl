import typer

user = typer.Typer(name="user")


@user.command()
def user_hi():
    typer.echo("Hello!")


def load(cli):
    cli.add_typer(user)
