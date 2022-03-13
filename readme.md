# Audio spectrum visualizer

Simple STM32 based audio spectrum visualizer that uses audio jack connection.

[tu będą zdjęcia i filmik]

## Specification

- 3.5 mm audio jack input
- 0-22 kHz frequency range
- voltage input range up to 3.3 Vpp
- 128x32 OLED display (I2C)

## Description

Project uses audio jack as signal input. It only uses right channel. That signal is later biased (using two resistors and capacitor) and sampled by ADC.

The data from ADC is used to calculate FFT (Fast Fourier Transform). The result is displayed on OLED, where data is sent using I2C protocol. Keep in mind that FFT result is normalized by dividing by maximum value, so if the input signal is very weak, the output will be strange.

## Hardware

- STM32F103RB
- 128x32 OLED display (I2C)
- 3.5 mm male audio jack to plug into signal source
- very simple analog frontend to bias input voltage

### Block diagram

[to do]

## Software

- IDE: STM32CubeIDE 1.5.1
- STM32 HAL library
- External libraries:
  - fix_fft.h (https://gist.github.com/Tomwi/3842231) - fixed-point FFT calculation
  - stm32-ssd1306 (https://github.com/afiskon/stm32-ssd1306) - library for communication with OLED displays that use SSD1306 chip

