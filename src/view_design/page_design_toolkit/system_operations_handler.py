import os
import sys


def restart_program():
    """Restart the current program with the same command-line arguments."""
    executable = sys.executable

    if getattr(sys, "frozen", False):
        arguments = [executable, *sys.argv[1:]]
    else:
        arguments = [executable, sys.argv[0], *sys.argv[1:]]

    os.execv(executable, arguments)
