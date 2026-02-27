#!/usr/bin/env python3
"""
KiCad PCM plugin version updater for Espressif KiCad Libraries.

This script adds or updates a plugin version in the PCM repository index.
It downloads the release artifact, calculates its metrics (SHA256, sizes),
and updates packages.json and repository.json accordingly.

Usage:
    python scripts/add_plugin_version.py <identifier> <version> <status> <kicad_version> <download_url>

Example:
    python scripts/add_plugin_version.py \
        com.github.espressif.kicad-libraries \
        3.2.0 \
        stable \
        9.0 \
        https://github.com/espressif/kicad-libraries/releases/download/3.2.0/espressif-kicad-addon.zip
"""

import argparse
import json
import logging
import sys
import tempfile
import time
import typing
import urllib.error
import urllib.request
import zipfile
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
log = logging.getLogger("pcm-updater")


def fatal(msg: str, exit_code: int = 1) -> typing.NoReturn:
    log.error(msg)
    sys.exit(exit_code)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Add or update a plugin version in KiCad PCM index"
    )
    parser.add_argument(
        "identifier",
        help="Plugin identifier (e.g. com.github.espressif.kicad-libraries)",
    )
    parser.add_argument(
        "version",
        help="Version of the plugin (e.g. 3.2.0)",
    )
    parser.add_argument(
        "status",
        choices=["stable", "testing", "development", "deprecated"],
        help="Status of the version",
    )
    parser.add_argument(
        "kicad_version",
        help="Minimum KiCad version required (e.g. 9.0)",
    )
    parser.add_argument(
        "download_url",
        help="URL to download the plugin archive",
    )
    return parser.parse_args()


def download_and_calculate_metrics(url: str) -> typing.Dict[str, typing.Any]:
    """Download the release ZIP and calculate download_size, download_sha256, and install_size."""
    log.info(f"Downloading plugin from {url}")

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        archive_path = temp_path / "plugin.zip"

        try:
            urllib.request.urlretrieve(url, archive_path)
        except Exception as e:
            fatal(f"Download error: {e}")

        if not archive_path.exists() or archive_path.stat().st_size == 0:
            fatal("Downloaded file is empty or does not exist")

        download_size = archive_path.stat().st_size

        file_hash = sha256()
        with open(archive_path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                file_hash.update(chunk)
        download_sha256 = file_hash.hexdigest()

        # Calculate install size from ZIP contents
        install_size = 0
        try:
            with zipfile.ZipFile(archive_path, "r") as zip_ref:
                for entry in zip_ref.infolist():
                    if not entry.is_dir():
                        install_size += entry.file_size
        except Exception as e:
            fatal(f"Error reading ZIP archive: {e}")

        log.info(
            f"Plugin metrics - Size: {download_size} bytes, "
            f"Install: {install_size} bytes, "
            f"SHA256: {download_sha256[:16]}..."
        )

        return {
            "download_size": download_size,
            "download_sha256": download_sha256,
            "install_size": install_size,
        }


def update_packages_json(
    args: argparse.Namespace, metrics: typing.Dict[str, typing.Any]
) -> None:
    """Find plugin by identifier and add/update version information in packages.json."""
    log.info("Updating packages.json")
    packages_file = Path("packages.json")

    if not packages_file.exists():
        fatal("packages.json not found")

    try:
        with open(packages_file, "r") as f:
            packages_data = json.load(f)

        if "packages" not in packages_data:
            fatal("Invalid packages.json structure - 'packages' key not found")

        plugin_found = False
        for package in packages_data["packages"]:
            if package["identifier"] == args.identifier:
                plugin_found = True

                new_version = {
                    "version": args.version,
                    "status": args.status,
                    "kicad_version": args.kicad_version,
                    "download_sha256": metrics["download_sha256"],
                    "download_size": metrics["download_size"],
                    "download_url": args.download_url,
                    "install_size": metrics["install_size"],
                }

                # Check if version already exists and update it
                for i, version in enumerate(package.get("versions", [])):
                    if version["version"] == args.version:
                        package["versions"][i] = new_version
                        log.info(f"Updated existing version {args.version}")
                        break
                else:
                    # Add new version at the beginning (latest first)
                    if "versions" not in package:
                        package["versions"] = []
                    package["versions"].insert(0, new_version)
                    log.info(f"Added new version {args.version}")
                break

        if not plugin_found:
            fatal(f"Plugin '{args.identifier}' not found in packages.json")

        with open(packages_file, "w") as f:
            json.dump(packages_data, f, indent=4, ensure_ascii=False)
            f.write("\n")

    except SystemExit:
        raise
    except Exception as e:
        fatal(f"Error updating packages.json: {e}")


def update_repository_json() -> None:
    """Update UTC time and Unix timestamp in repository.json for packages and resources."""
    log.info("Updating repository.json timestamps")
    repo_file = Path("repository.json")

    if not repo_file.exists():
        fatal("repository.json not found")

    try:
        timestamp = int(time.time())
        time_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

        with open(repo_file, "r") as f:
            repo_data = json.load(f)

        if "packages" not in repo_data or "resources" not in repo_data:
            fatal("Invalid repository.json structure - required sections missing")

        for section in ["packages", "resources"]:
            repo_data[section]["update_time_utc"] = time_utc
            repo_data[section]["update_timestamp"] = timestamp

        with open(repo_file, "w") as f:
            json.dump(repo_data, f, indent=4, ensure_ascii=False)
            f.write("\n")

    except SystemExit:
        raise
    except Exception as e:
        fatal(f"Error updating repository.json: {e}")


def main() -> None:
    try:
        args = parse_arguments()
        log.info(
            f"Adding version {args.version} for {args.identifier} "
            f"(status={args.status}, kicad={args.kicad_version})"
        )
        metrics = download_and_calculate_metrics(args.download_url)
        update_packages_json(args, metrics)
        update_repository_json()
        log.info(
            f"Successfully updated plugin {args.identifier} to version {args.version}"
        )
    except KeyboardInterrupt:
        log.warning("Operation cancelled")
        sys.exit(1)
    except SystemExit:
        raise
    except Exception as e:
        fatal(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
