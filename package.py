# Some samples are in here:https://gitlab.com/kicad/addons/metadata
import json
from os import path, walk as os_walk
import zipfile
import os
import re
import hashlib
import sys
import time
from datetime import datetime, timezone

directories_to_zip = [
    "3dmodels",
    "footprints",
    "symbols",
    "resources"
]


ZIP_FILE_NAME = "espressif-kicad-addon.zip"
DOWNLOAD_URL = "https://github.com/espressif/kicad-libraries/releases/download/{VERSION}/{ZIP_FILE_NAME}"


def create_json_string(zip_internal_metadata_json: dict):
    return json.dumps(zip_internal_metadata_json, indent=4)


def read_template_json_file():
    with open('metadata.template.json', mode='r') as metadata_file:
        metadat_template = json.load(metadata_file)
        metadata_file.close()

        return metadat_template


def create_zip_internal_metadata_json(version: str):
    template = read_template_json_file()
    version_item = {
        "version": version,
        "status": "stable",
        "kicad_version": "9.0"
    }

    template["versions"] = [version_item]

    return template


def create_full_metadata_file(version: str, existing_versions: [], zip_size: int, zip_internal_size: int,
                              zip_file_sha256: str):
    template = read_template_json_file()

    download_url = DOWNLOAD_URL.replace("{VERSION}", version).replace("{ZIP_FILE_NAME}", ZIP_FILE_NAME)

    version_item = {
        "version": version,
        "status": "stable",
        "kicad_version": "9.0",
        "download_sha256": zip_file_sha256,
        "download_size": zip_size,
        "download_url": download_url,
        "install_size": zip_internal_size
    }
    existing_versions.insert(0, version_item)

    template['versions'] = existing_versions

    with open('metadata.json', mode='w') as metadata_file:
        metadata_file.write(create_json_string(template))


def zip_directory(target: str, zip_handle: zipfile.ZipFile):
    for root, dirs, files in os_walk(target):
        for file in files:
            current_file_path = path.join(root, file)
            zip_handle.write(current_file_path, path.relpath(current_file_path, path.join(target, '..')))


def package_directories_to_zip(zip_handle: zipfile.ZipFile):
    for directory_to_zip in directories_to_zip:
        zip_directory(directory_to_zip, zip_handle)


def add_zip_internal_metadata_json(zip_handle: zipfile.ZipFile, version: str):
    zip_internal_metadata_json = create_zip_internal_metadata_json(version)
    zip_handle.writestr('metadata.json', create_json_string(zip_internal_metadata_json))


def calculate_zip_content_size(zip_handle: zipfile.ZipFile) -> int:
    zip_content_size = 0
    for entry in zip_handle.infolist():
        if not entry.is_dir():
            zip_content_size += entry.file_size

    return zip_content_size


# Return internal size
def generate_release_zip_file(zip_file_path: str, version: str) -> int:
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_handle:
        package_directories_to_zip(zip_handle)
        add_zip_internal_metadata_json(zip_handle, version)

        return calculate_zip_content_size(zip_handle)


def generate_sha256(zip_file_path: str):
    hash_gen = hashlib.sha256()

    with open(zip_file_path, mode='rb') as zip_file:
        while True:
            data = zip_file.read(65536)
            if not data:
                break
            hash_gen.update(data)

    return hash_gen.hexdigest()


def read_all_existing_versions():
    if os.path.isfile('metadata.json'):
        with open('metadata.json') as f:
            metadata_file = json.load(f)
            f.close()
            if 'versions' in metadata_file:
                return metadata_file['versions']
    return []


def check_version_already_exist(version, existing_versions):
    for version_data in existing_versions:
        if version_data["version"] == version:
            return True

    return False


def get_version_from_user():
    version = input("Enter the new addon version (required format: major[.minor[.patch]]): ")
    return version.strip()


def package():
    print('This script helps to generate a new kicad addon release. \n')
    print('It generates the release zip file and the metadata.json \n\n')

    if len(sys.argv) < 2:
        version = get_version_from_user()
    else:
        version = sys.argv[1]

    if not re.match('^\d{1,4}(\.\d{1,4}(\.\d{1,6})?)?$', version):
        raise Exception(
            "Version string is invalid. Required format: major[.minor[.patch]] (major, minor, patch are numbers)")

    existing_versions = read_all_existing_versions()
    if check_version_already_exist(version, existing_versions):
        raise Exception("The specified version " + version + " already exists")

    print("Start packaging documents to zip\n")
    if not os.path.isdir('build/'):
        os.mkdir('build')

    zip_file_path = os.path.join('build', ZIP_FILE_NAME)

    if os.path.isfile(zip_file_path):
        os.remove(zip_file_path)

    zip_internal_size = generate_release_zip_file(zip_file_path, version)
    zip_sha256 = generate_sha256(zip_file_path)
    zip_size = os.stat(zip_file_path).st_size

    print('Generated addon zip at path: ' + zip_file_path + '\n')

    print('Starting to generate metadata.json\n')
    create_full_metadata_file(version, existing_versions, zip_size, zip_internal_size, zip_sha256)

    print('Starting to update PCM index (packages.json & repository.json)\n')
    download_url = DOWNLOAD_URL.replace("{VERSION}", version).replace("{ZIP_FILE_NAME}", ZIP_FILE_NAME)
    update_pcm_index(version, zip_size, zip_internal_size, zip_sha256, download_url)

    print('All necessary files are generated. Now follow the steps on release-kicad-addons.md')


def update_pcm_index(version, zip_size, zip_internal_size, zip_sha256, download_url):
    """Update packages.json and repository.json for the self-hosted PCM repository."""
    packages_file = 'packages.json'
    repository_file = 'repository.json'

    # Read the current kicad_version from the template
    template = read_template_json_file()
    # Extract kicad_version from the template's version item pattern
    kicad_version = "9.0"  # Default

    # Update packages.json
    if os.path.isfile(packages_file):
        with open(packages_file, 'r') as f:
            packages_data = json.load(f)

        new_version = {
            "version": version,
            "status": "stable",
            "kicad_version": kicad_version,
            "download_sha256": zip_sha256,
            "download_size": zip_size,
            "download_url": download_url,
            "install_size": zip_internal_size
        }

        for package in packages_data.get("packages", []):
            if package["identifier"] == "com.github.espressif.kicad-libraries":
                # Check if version exists
                version_updated = False
                for i, v in enumerate(package.get("versions", [])):
                    if v["version"] == version:
                        package["versions"][i] = new_version
                        version_updated = True
                        break
                if not version_updated:
                    package.setdefault("versions", []).insert(0, new_version)
                break

        with open(packages_file, 'w') as f:
            json.dump(packages_data, f, indent=4, ensure_ascii=False)
            f.write("\n")

        print(f'Updated {packages_file} with version {version}\n')
    else:
        print(f'Warning: {packages_file} not found - skipping PCM index update\n')

    # Update repository.json timestamps
    if os.path.isfile(repository_file):
        with open(repository_file, 'r') as f:
            repo_data = json.load(f)

        timestamp = int(time.time())
        time_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

        for section in ["packages", "resources"]:
            if section in repo_data:
                repo_data[section]["update_time_utc"] = time_utc
                repo_data[section]["update_timestamp"] = timestamp

        with open(repository_file, 'w') as f:
            json.dump(repo_data, f, indent=4, ensure_ascii=False)
            f.write("\n")

        print(f'Updated {repository_file} timestamps\n')
    else:
        print(f'Warning: {repository_file} not found - skipping timestamp update\n')



if __name__ == "__main__":
    package()
