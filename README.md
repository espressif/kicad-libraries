# Espressif KiCad Library

This repository contains the Symbols, Footprint, and 3D Models for the Espressif SoC and Modules family.


![Library Downloads](https://img.shields.io/github/downloads/espressif/kicad-libraries/total?style=flat-square)

> Notice: The libraries are provided in the hope that they will be useful but without a warranty of any kind.

**The libraries in this repository are intended to be used with KiCad version 6.**

Each footprint library is stored as a directory with the .pretty suffix. The footprint files are .kicad_mod files within.

## Hardware Design Guidelines

Before designing your own hardware, be sure to check all recommendations at:

[Espressif Hardware Design Guidelines](https://www.espressif.com/sites/default/files/documentation/esp32_hardware_design_guidelines_en.pdf)

## Symbols and Footprints

All footprints were designed according to the Recommended PCB Land Pattern section present on each module datasheet.

### SoC

The following SoC are included in this library

| SoC          | Symbol | Footprint | Resource                                                                                               |
|:------------:|:------:|:---------:|:------------------------------------------------------------------------------------------------------:|
|ESP32         |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)         |
|ESP32-C3      |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)      |
|ESP32-PICO-V3 |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-pico-v3_datasheet_en.pdf) |
|ESP32-S2      |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s2_datasheet_en.pdf)      |
|ESP32-S3      |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s3_datasheet_en.pdf)      |
|ESP8286       |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/0a-esp8266ex_datasheet_en.pdf)  |
|ESP8285       |Yes     |No         |[Datasheet](https://www.espressif.com/sites/default/files/documentation/0a-esp8285_datasheet_en.pdf)    |

### Modules

| Module           | Symbol | Footprint | Resource                                                                                                                    |
|:----------------:|:------:|:---------:|:---------------------------------------------------------------------------------------------------------------------------:|
|ESP32-C3-MINI-1   |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3-mini-1_datasheet_en.pdf)                    |
|ESP32-C3-WROOM-02 |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3-wroom-02_datasheet_en.pdf)                  |
|ESP32-S2-MINI-1   |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s2-mini-1_esp32-s2-mini-1u_datasheet_en.pdf)   |
|ESP32-S2-MINI-1U  |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s2-mini-1_esp32-s2-mini-1u_datasheet_en.pdf)   |
|ESP32-S2-SOLO     |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s2-solo_esp32-s2-solo-u_datasheet_en.pdf)      |
|ESP32-S2-WROOM    |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s2-wroom_esp32-s2-wroom-i_datasheet_en.pdf)    |
|ESP32-S2-WROVER   |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-s2-wrover_esp32-s2-wrover-i_datasheet_en.pdf)  |
|ESP32-S3-MINI-1   |Yes     |Yes        |[Datasheet](https://products.espressif.com/)                                                                                 |
|ESP32-S3-MINI-1U  |Yes     |Yes        |[Datasheet](https://products.espressif.com/)                                                                                 |
|ESP32-S3-WROOM-1  |Yes     |Yes        |[Datasheet](https://products.espressif.com/)                                                                                 |
|ESP32-S3-WROOM-1U |Yes     |Yes        |[Datasheet](https://products.espressif.com/)                                                                                 |
|ESP32-WROOM-32E   |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.pdf)   |
|ESP32-WROOM-32UE  |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32e_esp32-wroom-32ue_datasheet_en.pdf)   |
|ESP32-WROVER-E    |Yes     |Yes        |[Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wrover-e_esp32-wrover-ie_datasheet_en.pdf)     |

### Development Boards

|    Dev Board     | Symbol | Footprint |                           Resource                           |
| :--------------: | :----: | :-------: | :----------------------------------------------------------: |
| ESP32-S2-Saola-1 |  Yes   |    Yes    | [Schematic](https://dl.espressif.com/dl/schematics/ESP32-S2-SAOLA-1_V1.1_schematics.pdf) |
|  ESP32-DevKitC   |  Yes   |    Yes    | [Schematic](https://dl.espressif.com/dl/schematics/esp32_devkitc_v4-sch.pdf) |
| ESP32-S3-DevKitC |  Yes   |    Yes    |                                                              |
| ESP32-S2-DevKitM |  Yes   |    Yes    | [Schematic](https://dl.espressif.com/dl/schematics/ESP32-S2-DevKitM-1_V1_Schematics.pdf) |

### Contributing

If you want to contribute, please consider sending us a Pull Request (PR).

### 3D Models

Espressif provides some 3D models to help you with your project inside the ``3d`` folder.
To use the files, you need to create an environment variable add the ``3d`` folder path.

* Open ``Open Preferences`` -> ``Configure Paths...``
* Create the new variable:
    * Name: ``ESPRESSIF_3DMODELS``
    * Path: ``<PATH_TO_THE_3D_FOLDER>``

### About KiCad

KiCad is a Cross-Platform and Open Source Electronics Design Automation Suite. See [KiCad EDA](https://kicad.org/) for more information.
