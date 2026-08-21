from typing import Any, Optional
import re
import tomllib


class PyProjectParser:
    def __init__(self, project_path) -> None:
        self.project_path = project_path
        self.project_content = self._get_project_content()
        self.version = self._get_project_version()

    def _get_project_content(self) -> dict[str, Any]:
        with open(self.project_path, "rb") as toml_file:
            pyproject_content = tomllib.load(toml_file)
            project_content = pyproject_content["project"]
        return project_content

    def _get_project_version(self) -> str:
        project_version = self.project_content["version"]
        return project_version

    @staticmethod
    def get_version_tuple(
        version_string: str
            ) -> Optional[tuple[int, int, int]]:
        match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", version_string)
        print(f"Match: {match}")
        if match:
            versions_unformatted = tuple(match.group().split("."))
            if len(versions_unformatted) == 3:
                major, minor, patch \
                    = (int(version) for version in versions_unformatted)
                return major, minor, patch
        else:
            raise RuntimeError(
                f"The project version '{version_string}' is not formatted "
                "properly using semantic var style"
                )
