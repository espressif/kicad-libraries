# Release process

- Run `python package.py`
- Enter an appropriate version number
- Create a release on Github, entering the same version number as the tag, and uploading the zip file in the `build/` directory as the binary
- In Gitlab, fork https://gitlab.com/kicad/addons/metadata and create a new branch
- If it doesn't exist, create a folder in `packages` called `com.github.espressif.kicad-libraries`
- In that folder, add the `metadata.json` in the root Espressif library directory, and the `icon.png` file located in `resources`
- Commit, and then create a merge request
