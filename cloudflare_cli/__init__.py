from cloudflare_cli.cli import CloudflareCLI

APP_NAME: str = "Cloudflare CLI"
COMMANDS_DIRECTORY: str = "commands"

CLI: CloudflareCLI = CloudflareCLI(app_name=APP_NAME, commands_dir=COMMANDS_DIRECTORY)

__version__: str = "0.1.0"
__all__: tuple[str, ...] = ("__version__", "CLI")
