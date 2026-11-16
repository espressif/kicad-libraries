# Release process

## Automated Release (Recommended)

When you create a new GitHub Release with a version tag, the CI workflow automatically:

1. Builds the `espressif-kicad-addon.zip` package
2. Uploads it as a release asset
3. Updates `metadata.json` on the main branch
4. Updates the self-hosted PCM index (`packages.json` and `repository.json`)

Steps:

1. Create a release on GitHub with an appropriate version tag (e.g. `3.2.0`)
2. The `release.yml` workflow will run automatically and handle everything
3. (Optional) Fork https://gitlab.com/kicad/addons/metadata and submit `metadata.json` to the official KiCad PCM

## Manual Release

1. Run `python package.py`
2. Enter an appropriate version number
3. This generates:
   - `build/espressif-kicad-addon.zip` — the addon package
   - `metadata.json` — updated version history for the official KiCad PCM
   - `packages.json` — updated self-hosted PCM index
   - `repository.json` — updated timestamps
4. Create a release on GitHub, entering the same version number as the tag, and uploading the zip file in the `build/` directory as the binary
5. Commit and push the updated `metadata.json`, `packages.json`, and `repository.json` to main
6. (Optional) Submit `metadata.json` to the official KiCad PCM at https://gitlab.com/kicad/addons/metadata

## Self-Hosted PCM Repository

Users can add the Espressif PCM repository directly to KiCad:

1. Open KiCad → **Plugin and Content Manager** → **Manage**
2. Click **Add Repository**
3. Add URL: `https://raw.githubusercontent.com/espressif/kicad-libraries/main/repository.json`
4. Install the **Espressif Library** from the list

## Manual PCM Index Update

You can also manually trigger the PCM index update workflow from the GitHub Actions tab:

1. Go to **Actions** → **Update PCM Index**
2. Click **Run workflow**
3. Fill in the plugin details (identifier, version, status, kicad_version, download_url)
