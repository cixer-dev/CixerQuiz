from typing import Optional
import subprocess
import platform
import shutil


def run_bash(
    script_path: str,
    arguments: Optional[tuple] = None,
) -> Optional[bool]:
    """Run a Bash script and print its output.
    Return True if the Bash is executed correctly"""

    if platform.system() == "Windows":
        bash_executable = shutil.which("bash")
        if bash_executable is None:
            raise FileNotFoundError(
                "bash not found in PATH. "
                "Ensure Git Bash is installed and in PATH."
            )
        command = [bash_executable, script_path]
    else:
        command = ["bash", script_path]

    if isinstance(arguments, tuple):
        command.extend(arguments)

    try:
        subprocess.run(
            command,
            text=True,
            check=True,
        )
        return True
    except Exception:
        raise
