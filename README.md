# L.A.R.S  
**Lunar Attachment for Regolith Sublimation**

[Spinning Model](Render.png)

## Table of Contents
- [Overview](#overview)
  - [Key Features](#key-features)
  - [Project Goal](#project-goal)
- [Installation & Setup](#installation-setup)
  - [Flashing Raspberry Pi Pico W](#flashing-raspberry-pi-pico-w)
  - [Thonny Basics](#thonny-basics)
  - [Bluetooth Electronics App](#bluetooth-electronics)
  - [Wiring Schematic](#wiring-schematic)
- [Parts List](#parts-list)
- [Resources](#resources)

## Overview
This repository supports the **Lunar Attachment for Regolith Sublimation** (LARS), a prototype designed to extract pure water from icy lunar regolith deposits. The system uses heated drive screws powered by induction coils to penetrate and vaporize the regolith, with a steam collection system that condenses the vapor into liquid water. The LARS system is intended for integration with a lunar rover platform for autonomous operation in challenging lunar environments.

### Key Features
- **Inductive Heating**: Induction coils heat drive screws, which penetrate and sublimate regolith.
- **Steam Collection System**: Collects the vaporized regolith and condenses it into liquid water.
- **Rover Attachment**: Designed for integration with a rover platform.
- **Modular Components**: The system is designed for scalability and upgrades.

### Project Goal
The goal of LARS is to provide a reliable and efficient method of extracting pure water from the icy lunar regolith, supporting future human missions and robotic exploration.

## Installation & Setup
This section explains how to set up the LARS system on your hardware and software environment.

### Flashing Raspberry Pi Pico W
1. Download the latest firmware for Raspberry Pi Pico W.
2. Use [Raspberry Pi Imager](https://www.raspberrypi.org/software/) to flash the firmware onto the device.

### Thonny Basics
1. Download and install [Thonny IDE](https://thonny.org/) to start programming the Raspberry Pi Pico.
2. Set the correct interpreter to your Pico device.

### Bluetooth Electronics App
1. Install the Bluetooth Electronics app on your mobile device to communicate with the Raspberry Pi Pico.
2. Pair it with the Pico to test Bluetooth communication.

### Wiring Schematic
The schematic for the system can be found in the `docs/` folder for detailed instructions on connecting the components.

## Parts List
- Raspberry Pi Pico W
- Heating element
- Drive screws
- Regolith sample containers
- Bluetooth communication module
- Power supply

## Resources
- [Pico Documentation](https://www.raspberrypi.org/documentation/pico/)
- [Lunar Regolith Sublimation Research](https://www.example-link-to-research.com)
- [ROAR Website](https://www.example-roar.com)
- [ARCh Rules & Regulations](https://www.example-arch-rules.com)

## Contributions
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch for your changes
3. Submit a pull request

## License
This project is open-source under the MIT License.
