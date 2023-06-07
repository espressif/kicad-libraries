# Espressif KiCad Library

[![GitHub stars](https://img.shields.io/github/stars/espressif/kicad-libraries)](https://github.com/espressif/kicad-libraries/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/espressif/kicad-libraries)](https://github.com/espressif/kicad-libraries/network)
[![GitHub issues](https://img.shields.io/github/issues/espressif/kicad-libraries)](https://github.com/espressif/kicad-libraries/issues)

> Notice: A major update from version 1.0.1 was made to be compliant to the [KLC](https://klc.kicad.org/). Please consider updating your library and checking the symbols and footprints.

> From the version 2.0.0, the library instalation process is done by the PCM.

This repository contains the Symbols, Footprint, and 3D Models for the Espressif SoC and Modules family.


* Notice: The libraries are provided in the hope that they will be useful but without a warranty of any kind.

**The libraries in this repository are intended to be used with KiCad version 7.**

For the KiCad 6 legacy library, please use [this branch](https://github.com/espressif/kicad-libraries/tree/legacy_kicad6) instead.

Each footprint library is stored as a directory with the .pretty suffix. The footprint files are .kicad_mod files within.

## Hardware Design Guidelines

Before designing your hardware, be sure to check all recommendations at:

* [Espressif Hardware Design Guidelines](https://www.espressif.com/sites/default/files/documentation/esp32_hardware_design_guidelines_en.pdf)
* [Espressif Product Selector](https://products.espressif.com/#/)

## Symbols and Footprints

All footprints were designed according to the Recommended PCB Land Pattern section present on each module datasheet.

### SoC

The following SoC are included in this library

| SoC               | Symbol | Footprint | Resource                                                                                               |
|:-----------------:|:------:|:---------:|:------------------------------------------------------------------------------------------------------:|
|ESP32              |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)         |
|ESP32-PICO-V3      |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-pico-v3_datasheet_en.pdf) |
|ESP32-S2           |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_en.pdf)      |
|ESP32-C3           |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)      |
|ESP32-C6           |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c6_datasheet_en.pdf)      |
|ESP32-S3           |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf)      |
|ESP8286            |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf)  |
|ESP8285            |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/0a-esp8285_datasheet_en.pdf)    |
|ESP8684 (ESP32-C2) |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp8684_datasheet_en.pdf)       |
|ESP8685            |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp8685_datasheet_en.pdf)       |

### Modules

| Module           | Symbol | Footprint | Resource                                                                                                                    |
|:----------------:|:------:|:---------:|:---------------------------------------------------------------------------------------------------------------------------:|
|ESP32-WROOM-32E   |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.pdf)   |
|ESP32-WROOM-32UE  |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.pdf)   |
|ESP32-WROOM-DA    |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-da_datasheet_en.pdf)                     |
|ESP32-WROVER-E    |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wrover-e_esp32-wrover-ie_datasheet_en.pdf)     |
|ESP32-MINI-1      |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-mini-1_datasheet_en.pdf)                       |
|ESP32-MINI-1U     |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-mini-1_datasheet_en.pdf)                       |
|ESP32-C3-MINI-1   |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3-mini-1_datasheet_en.pdf)                    |
|ESP32-C3-WROOM-02 |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3-wroom-02_datasheet_en.pdf)                  |
|ESP32-C6-MINI-1   |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c6-mini-1_datasheet_en.pdf)                    |
|ESP32-C6-MINI-1U  |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c6-mini-1_datasheet_en.pdf)                    |
|ESP32-C6-WROOM-1  |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c6-wroom-1_datasheet_en.pdf)                   |
|ESP32-S2-MINI-1   |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s2-mini-1_esp32-s2-mini-1u_datasheet_en.pdf)   |
|ESP32-S2-MINI-1U  |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s2-mini-1_esp32-s2-mini-1u_datasheet_en.pdf)   |
|ESP32-S2-SOLO     |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s2-solo_esp32-s2-solo-u_datasheet_en.pdf)      |
|ESP32-S2-WROOM    |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s2-wroom_esp32-s2-wroom-i_datasheet_en.pdf)    |
|ESP32-S2-WROVER   |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s2-wrover_esp32-s2-wrover-i_datasheet_en.pdf)  |
|ESP32-S3-MINI-1   |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3-mini-1_mini-1u_datasheet_en.pdf)            |
|ESP32-S3-MINI-1U  |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3-mini-1_mini-1u_datasheet_en.pdf)            |
|ESP32-S3-WROOM-1  |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf)          |
|ESP32-S3-WROOM-1U |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf)          |
|ESP32-S3-WROOM-2  |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-2_datasheet_en.pdf)                   |

### Development Boards

| Dev Board       | Symbol | Footprint | Resource                                                                                    |
|:---------------:|:------:|:---------:|:-------------------------------------------------------------------------------------------:|
|ESP32-S2-Saola-1 |Yes     |Yes        |[Schematic](https://dl.espressif.com/dl/schematics/ESP32-S2-SAOLA-1_V1.1_schematics.pdf)     |
|ESP32-S2-DevKitC-1|Yes    |Yes        |[Schematic](https://dl.espressif.com/dl/schematics/esp-idf/SCH_ESP32-S2-DEVKITC-1_V1_20220817.pdf) |
|ESP32-DevKitC    |Yes     |Yes        |[Schematic](https://dl.espressif.com/dl/schematics/esp32_devkitc_v4-sch.pdf)                 |
|ESP32-S3-DevKitC |Yes     |Yes        |[Schematic](https://dl.espressif.com/dl/schematics/SCH_ESP32-S3-DevKitC-1_V1.1_20220413.pdf) |
|ESP32-S2-DevKitM |Yes     |Yes        |[Schematic](https://dl.espressif.com/dl/schematics/ESP32-S2-DevKitM-1_V1_Schematics.pdf)     |
|ESP32-C6-DevKitC-1|Yes    |Yes        |[Schematic](https://docs.espressif.com/projects/espressif-esp-dev-kits/en/latest/_static/esp32-c6-devkitc-1/schematics/esp32-c6-devkitc-1-schematics_v1.2.pdf)     |

## Manual Installation - PCM

The Espressif KiCad library is distributed via the Pluguin and Content Manager (PCM) and the installation is done automatically.

To install the library, you need to download the **"espressif-kicad-addon.zip"** file from the latest release. For legacy support, please visit the legacy branch and follow the instructions from there.

* [Latest Release](https://github.com/espressif/kicad-libraries/releases/latest)

For KiCad 6 and 7, you can use the following steps:

1. On KiCad, open the PCM in the main KiCad window.

![First Step](resources/pcm_install_step-1.png)

2. The PCM window will display a list of available plugins, libraries, and color themes. You can browse through the categories or use the search bar to find a specific package.

![First Step](resources/pcm_install_step-2.png)

3. To install the library manually using the ZIP file from the latest release, you need to select the file from **"Install from file..."**

![First Step](resources/pcm_install_step-3.png)

4. Once the package is installed, you will see the Espressif Library listed on the Installed tab.

![First Step](resources/pcm_install_step-4.png)

5. Now you are ready to use the library. Note that the library will be listed as **PCM_Espressif** in the Symbol and Footprint.

## Contributing

If you want to contribute, please consider sending us a Pull Request (PR).

### About KiCad

KiCad is a Cross-Platform and Open Source Electronics Design Automation Suite. See [KiCad EDA](https://kicad.org/) for more information.
