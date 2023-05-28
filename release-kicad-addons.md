# Release process

- Run `python package.py`
- Enter an appropriate version number - It will be the number that the maintainer just about to release
- Create a release on Github, with the following details:
  - The same version number as the tag in the above step
  - In the `build/` directory, a zip file was created by the Python script - Upload it as the binary release.
- In Gitlab, fork https://gitlab.com/kicad/addons/metadata
- Create a new branch
- If it doesn't exist, create a folder in `packages` called `com.github.espressif.kicad-libraries`
- In that folder, add the `metadata.json` in the root Espressif library directory, and the `icon.png` file located in `resources`
- Commit, and then wait for CI to complete without errors
- Create a merge request
