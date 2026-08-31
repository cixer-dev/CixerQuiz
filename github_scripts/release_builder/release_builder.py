import platform
import traceback

from github_scripts.release_builder.builders.linux_builder import \
    LinuxReleaseBuilder
from github_scripts.release_builder.builders.windows_builder import \
    WindowsReleaseBuilder


class ReleaseFactory:
    """Build a release using the builder for the current operating system."""

    def __init__(self, project_dir: str) -> None:
        """Initialize the release factory"""
        self.project_dir = project_dir
        self.actual_platform = platform.system()

    def build_release(self) -> int:
        """Build the project release for the current operating system.
        Return 0 if the release is built successfully; otherwise, 1.
        """
        try:
            if self.actual_platform == "Linux":
                release_builder = LinuxReleaseBuilder(self.project_dir)
                release_builder.build_release()
            elif self.actual_platform == "Windows":
                release_builder = WindowsReleaseBuilder(self.project_dir)
                release_builder.build_release()
            else:
                print(
                    "This script is running on an unsupported platform. "
                    f"{self.actual_platform} is not supported."
                )
                return 1

            return 0
        except Exception:
            print(traceback.format_exc())
            return 1
