import os
import sys


def reset_program():
    """Restart the current Python process with the same arguments."""
    os.execl(sys.executable, sys.executable, *sys.argv)
