from github_scripts.release_builder.release_builder \
    import ReleaseFactory
import argparse


def main() -> int:
    """Run all scripts needs for build a Git release"""
    parser = argparse.ArgumentParser(
        description="Build and publish a project release"
    )
    parser.add_argument(
        "project_directory",
        type=str,
        help="The root directory of the project"
    )
    args = parser.parse_args()
    project_dir = args.project_directory
    release_builder = ReleaseFactory(project_dir)
    return release_builder.build_release()


if __name__ == "__main__":
    raise SystemExit(main())
