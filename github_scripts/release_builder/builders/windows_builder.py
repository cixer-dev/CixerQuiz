import os
from zipfile import ZipFile, ZIP_DEFLATED

from github_scripts.common_scripts import run_bash
from src.model.configurators.assets_paths_configurator \
    import assets_paths_reader
from src.model.configurators.general_configurator import general_reader


class WindowsReleaseBuilder:
    """Build a Windows release archive."""

    def __init__(self, project_dir: str) -> None:
        """Initialize the Windows release builder."""
        self.project_dir = project_dir
        self.app_name = general_reader.read_general_config("app_domain")

        self.dist_path = os.path.join(self.project_dir, "dist")
        self.app_logo_path = os.path.join(
            self.project_dir,
            assets_paths_reader.read_asset_path("reduced_game_logo_ico"),
        )
        self.exe_path = os.path.join(
            self.dist_path,
            f"{self.app_name}.exe",
        )
        self.zip_path = os.path.join(
            self.dist_path,
            f"{self.app_name}_windows-amd64.zip",
        )

    def build_release(self) -> None:
        """Build the Windows executable and release archive."""
        self._build_exe()
        self._create_release_zip_file((self.exe_path,))

    def _build_exe(self) -> None:
        """Build the Windows executable with PyInstaller."""
        arguments = (
            self.app_name,
            self.exe_path,
            self.app_logo_path,
        )
        build_exe_path = os.path.join(
            self.project_dir,
            "github_scripts",
            "release_builder",
            "build_exe.sh",
        )

        run_bash.run_bash(build_exe_path, arguments)

    def _create_release_zip_file(
        self,
        additional_paths: tuple[str, ...],
    ) -> None:
        """Create the archive containing the Windows release files."""
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
