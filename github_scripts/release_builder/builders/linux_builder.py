import platform
import os

from zipfile import ZipFile, ZIP_DEFLATED

from github_scripts.common_scripts.run_bash import run_bash

from src.model.configurators.general_configurator.\
    general_reader import read_general_config


class LinuxReleaseBuilder:
    """Build a Linux release and package its required files."""

    def __init__(
        self,
        project_dir: str,
    ) -> None:
        """Initialize the Linux release builder with project paths."""
        self.project_dir = project_dir
        self.actual_platform = platform.system()
        self.app_name = read_general_config("app_domain")

        self.dist_path = os.path.join(self.project_dir, "dist")
        self.linux_binary_path = os.path.join(
            self.dist_path,
            self.app_name,
        )
        self.launcher_path = os.path.join(
            self.dist_path,
            f"{self.app_name}.sh",
        )
        self.zip_path = os.path.join(
            self.dist_path,
            f"{self.app_name}_linux-amd64.zip",
        )

    def build_release(self) -> None:
        """Build the Linux executable and create its release archive."""
        self._build_executable()
        self._create_release_zip_file(
            additional_paths=(self.linux_binary_path, self.launcher_path)
        )

    def _build_executable(self) -> None:
        """Build the Linux executable and launcher with a Bash script."""
        arguments = (self.app_name, self.dist_path, self.launcher_path)
        build_executable_path = os.path.join(
            "github_scripts",
            "release_builder",
            "build_executable.sh",
        )

        run_bash(
            build_executable_path,
            arguments,
        )

    def _create_release_zip_file(
        self,
        additional_paths: tuple[str, ...],
    ) -> None:
        """Create a release archive containing the required project files."""
        fixed_paths = (
            "assets",
            "config",
            "docs",
            "translations",
            "user_data",
            "README.md",
            "LICENSE",
        )
        all_paths = fixed_paths + additional_paths

        with ZipFile(
            self.zip_path, "w", compression=ZIP_DEFLATED, compresslevel=9
                ) as archive:
            for path in all_paths:
                if os.path.isdir(path):
                    for root, _, files in os.walk(path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            archive.write(file_path, file_path)
                elif os.path.isfile(path):
                    archive.write(path, os.path.basename(path))
