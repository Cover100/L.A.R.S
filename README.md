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
- **Steam Collection System**: Collects the steam offput and condenses it into liquid water.
- **Rover Attachment**: Designed for integration with a rover platform.

### Project Goal
The goal of LARS is to provide a reliable and efficient method of extracting pure water from the icy lunar regolith, supporting future human missions and robotic exploration.

## Installation & Setup
This section explains how to set up the LARS system on your hardware and software environment.

### Flashing Raspberry Pi Pico W
1. Go to the official [MicroPython dowload page](https://micropython.org/download/RPI_PICO/)
2. Download the latest `.uf2` file for the Raspberry Pi Pico W.
3. Hold down the `BOOTSEL` button on the Pico W.
4. While holding `BOOTSEL`, plug the Pico W into your computer via USB.
5. Release the `BOOTSEL` button.
6. The Pico W should appear as a USB mass storage device called `RPI-RP2`.
7. Copy the downloaded `.uf2` file to the RPI-RP2 drive.
8. The Pico W will automatically reboot and run MicroPython.

### Thonny Basics
1. Download from [https://thonny.org.](https://thonny.org/)
2. Open Thonny, select `Tools > Options > Interpreter`.
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
- [12V Relay Module](https://www.amazon.com.au/dp/B0D14LXTW7?ref=ppx_yo2ov_dt_b_fed_asin_title) - **Quantity**: 2  
- [ZVS Induction Heating Power Supply Module](https://www.amazon.com.au/Treedix-Voltage-Induction-Heating-Supply/dp/B086V6CYM6/ref=sr_1_6?crid=2UZY8DQV3H39S&dib=eyJ2IjoiMSJ9.r-7KYd4Ku1HqRXxeYk78R2MpZubueKdt2c_AfjAzzMo8u9cTIPdUqh2DHLuysDQ-vsUPCzN5x3ibvHwxcshE9ZfpFlvxy0HidLuVsjyYFaxb02HoRFYhjdif3garCzIkx9YLa_Nk7GB9UW0tV-ZifX_5hgG-gRjKewfhhskuer4NyQZ_fNS4pFsOutsNm-gfoh0OlPa8R9tKK9bZP8F846eLtPKWo_62xv8BTTyWthJKQeylpQYJ8qOkJI9cu3CY27PWN_aZEoXkFlM1h3W0Ysi-bXrebhweggBPl7x3bw0qY-bESMmdepsbNJsU9GSXy8SOE2NH-_iEuYykmuQir4r7QcJKg4y8Dbcq7_9PvGz8grlt77lxnyjt2ZZOMlI6VNEJgEpnGVDCzgRWg9aCj-q6F0zFvvO8W_E7jT9jPl6GKt0tyXz1JmlhPiiohkY9.KOzNB1a2GwTO2axgxSWAVOkT82kqt-a6-sj9cNGM6Rw&dib_tag=se&keywords=ZVS+Induction+Heating+Power+Supply+Module&qid=1743330911&sprefix=zvs+induction+heating+power+supply+module%2Caps%2C210&sr=8-6) - **Quantity**: 2  
- [Constant Current CC CV Buck Converter Module](https://www.amazon.com.au/dp/B07R832BRX?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1) - **Quantity**: 1  
- [DC Brushless Cooling Fan (60mm x 15mm)](https://www.amazon.com.au/dp/B0BZKY4GF2?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1) - **Quantity**: 2  
- [Raspberry Pi Pico W](https://www.raspberrypi.org/products/pico-w/) - **Quantity**: 1  
- [DRV8825 Stepper Motor Drivers](https://www.amazon.com.au/s?k=drv8825+stepper+motor+driver+module&crid=3GQNG3UQVVLKM&sprefix=DRV%2Caps%2C375&ref=nb_sb_ss_fb_1_3_mvt-t2-ranker) - **Quantity**: 2  
- [HC-05 Bluetooth Module](https://www.amazon.com.au/Bluetooth-Pass-Through-Wireless-Communication-Arduino/dp/B01G9KSAF6/ref=sr_1_1_sspa?crid=23JE590149PV4&dib=eyJ2IjoiMSJ9.oNxKH5uQWhTXEtgL0-6BRVUuIhmGMRQTqUThdUZu4QIV0Fv0ySr-fKAFUnphAAwpK-wmRjS97g5Rck6Y5ot0CkhJpfO3OukR8ez0EirAsHx9H1swwvzNCZZpHKbKlTSx1YFrIF1MJddPijgqpKMyQbO24OaYTdFHCD5P-ANaKAYSPJZgds5wVGWQPpyYzFk_Lv-vq6NpCsbLytcvKWSbDfoMn26E1L_d8F6SCNQyjC6utkJIav3B5x4YAMdlgnHOay6YeJcKBGZZkQsGlYchB8he9DqkIuPMVzQZ3ao9tBc.tU_JPQzowbaPArojsSuJTjxWZPDa6_irtrSATgvpuQQ&dib_tag=se&keywords=HC-05&qid=1743330817&sprefix=hc-05%2Caps%2C240&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1) - **Quantity**: 1  
- [DC Brushless Cooling Fan (40mm x 10mm)](https://www.amazon.com.au/ANVISION-2-Pack-Brushless-Cooling-Bearing/dp/B08HXZYQKJ/ref=sr_1_2_sspa?crid=N3RG5NSGR2CI&dib=eyJ2IjoiMSJ9.1Y8nc3c5WVyP7m1A_CaFhdJ9H4ibT4jqxU-yzkEep4hdVSoyKp731tqnSo3i_vcglXPeRXvXWJearTSRXiodlTCfJQM4cDlt8LTKreWPgQarUXXhwK2sdahSALs9OBhD77c9pn_IlmCPsjO-cLWYKXYY_GNMSjxljMkpsyAF0jI2miDoTriMrWdITQc3q2PuoBvnsrP_VAMydqcRA2fUJWr1nOesrFlwF22qtdp4Qu7nR3p7-falBAU-_OAfimWjrsWXu1RPIja2zeBywzh23013oOwGecipsJBB5XKi0lM.QNSIm-Qh6mCmCkjnh8BgBQN3bwOwtjf8PJ4TcqYgXw0&dib_tag=se&keywords=40MM+dc+FAN&qid=1743330864&sprefix=40mm+dc+fan%2Caps%2C230&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1) - **Quantity**: 2  


## Resources
- [Pico Documentation](https://www.raspberrypi.org/documentation/pico/)
- [ROAR Website](https://www.example-roar.com)
- [ARCh Rules & Regulations](https://www.example-arch-rules.com)
