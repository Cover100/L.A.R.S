# L.A.R.S  
**Lunar Attachment for Regolith Sublimation**

![Render](Render.png)

## Table of Contents
- [Overview](#overview)
  - [Key Features](#key-features)
  - [Project Goal](#project-goal)
- [Installation & Setup](#installation--setup)
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
1. Go to the official [MicroPython dowload page](https://micropython.org/download/RPI_PICO/)
2. Download the latest '.uf2' file for the Raspberry Pi Pico W.
3. Hold down the 'BOOTSEL' button on the Pico W.
4. While holding 'BOOTSEL', plug the Pico W into your computer via USB.
5. Release the 'BOOTSEL' button.
6. The Pico W should appear as a USB mass storage device called 'RPI-RP2'.
7. Copy the downloaded '.uf2' file to the RPI-RP2 drive.
8. The Pico W will automatically reboot and run MicroPython.

### Thonny Basics
1. Download from [https://thonny.org.](https://thonny.org/)
2. Open Thonny, select 'Tools > Options > Interpreter'.
3. Choose MicroPython (Raspberry Pi Pico).
4. Select the correct COM/Serial port and click OK.
5. Write and run Micropython scripts on the Pico W
```python
print("Hello World!")
```

### Bluetooth Electronics App
1. Open the Google Play Store on your Android phone or tablet.
2. Search for "Bluetooth Electronics" by keuwlsoft or click [here](https://play.google.com/store/apps/details?id=com.keuwl.arduinobluetooth&hl=en_AU&pli=1).
3. Tap Install and wait for the app to download.
4. Open the app and grant the necessary Bluetooth permissions.

### Wiring Schematic
The schematic for the system can be found in the `docs/` folder for detailed instructions on connecting the components.

## Parts List
- [12V Relay Module](https://www.amazon.com/dp/B01D5H6XUE) - **Quantity**: 2  
- [ZVS Induction Heating Power Supply Module](https://www.amazon.com/dp/B08DJ9NT74) - **Quantity**: 2  
- [Constant Current CC CV Buck Converter Module](https://www.amazon.com/dp/B07ZL7N2QY) - **Quantity**: 1  
- [DC Brushless Cooling Fan (60mm x 15mm)](https://www.amazon.com/dp/B08BBNDDJ3) - **Quantity**: 2  
- [Raspberry Pi Pico W](https://www.raspberrypi.org/products/pico-w/) - **Quantity**: 1  
- [DRV8825 Stepper Motor Drivers](https://www.amazon.com/dp/B07ZVKP9P9) - **Quantity**: 2  
- [HC-05 Bluetooth Module](https://www.amazon.com/dp/B07Z2C8V9L) - **Quantity**: 1  
- [DC Brushless Cooling Fan (40mm x 10mm)](https://www.amazon.com/dp/B08BBNDDJ3) - **Quantity**: 2  


## Resources
- [Pico Documentation](https://www.raspberrypi.org/documentation/pico/)
- [ROAR Website](https://www.example-roar.com)
- [ARCh Rules & Regulations](https://www.example-arch-rules.com)
