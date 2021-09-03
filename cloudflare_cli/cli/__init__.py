import runpy
from pathlib import Path
from typing import Callable, Optional

from typer import Typer, get_app_dir


class CloudflareCLI(Typer):
    """
    The base class for the Cloudflare CLI.

    This class subclasses typer.Typer and ensures Cloudflare CLI's cache files
    are available and also loads all command groups upon initiation.
    """

    def __init__(self, app_name: str, commands_dir: str) -> None:
        super().__init__(name=app_name, no_args_is_help=True)

        # Create cache file to store stateful data
        app_dir: Path = Path(get_app_dir(app_name))
        cache: Path = Path(app_dir / ".cache.json")
        cache.touch(exist_ok=True)

        # Dynamically load all files:
        # Each file should define it's own load() function which
        # interacts with the CloudflareCLI instance
        commands_path: Path = Path(__file__).parent.resolve() / commands_dir
        for file in commands_path.glob("*.py"):
            load_function: Optional[Callable] = runpy.run_path(file).get("load")
            if load_function is None:
                pass  # TODO: setup logging and have a warning that the file does not define `load`
            else:
                load_function(self)


__all__ = "CloudflareCLI"
