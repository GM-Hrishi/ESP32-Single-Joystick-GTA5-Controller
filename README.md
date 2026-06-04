# ESP32 Single Joystick GTA V Controller

A fun project that turns a single ESP32-connected analog joystick into a virtual Xbox controller for GTA V and other PC games.

The project uses:

* ESP32
* Analog Joystick Module
* Python
* vgamepad
* ViGEmBus

The ESP32 reads joystick values and sends them over serial to Python. Python then creates a virtual Xbox 360 controller that can be recognized by Windows and GTA V.

## Important

This project is intentionally designed around **one joystick only**.

It is not intended to replace a full controller and does not provide the complete functionality of an Xbox or PlayStation controller.

Features such as:

* Camera control
* Multiple face buttons
* Shoulder buttons
* Triggers
* D-Pad
* Full gamepad layout

are outside the scope of this project.

A separate repository will be created later for a **full controller implementation** with additional buttons and controls.

## Features

* Analog movement
* Analog vehicle steering
* Analog acceleration and braking
* Virtual Xbox 360 controller support
* Walk mode
* Drive mode
* Mode switching using joystick click (SW)
* Smoothing
* Response curves
* Circular deadzone

## Hardware Required

* ESP32 Dev Board
* Analog Joystick Module
* Jumper Wires
* USB Cable

## Wiring

| Joystick Pin | ESP32 Pin |
| ------------ | --------- |
| VRX          | GPIO34    |
| VRY          | GPIO35    |
| SW           | GPIO32    |
| VCC          | 3.3V      |
| GND          | GND       |

## Software Required

### Python Packages

```bash
pip install pyserial vgamepad
```

### Driver

Install ViGEmBus:

https://github.com/nefarius/ViGEmBus/releases

## How It Works

### Walk Mode

* Joystick controls the Xbox left stick.
* Used for character movement.

### Drive Mode

* Left/Right → Steering
* Up → Accelerate
* Down → Brake / Reverse

Press the joystick button to toggle between modes.

## Disclaimer

This is a hobby project created for learning and experimentation.

It is not intended to compete with or replace a real game controller.

Controller feel, precision and compatibility will vary depending on:

* Joystick quality
* Calibration
* Game support
* Windows configuration

## Future Work

A separate repository is planned that will expand this concept into a more complete controller featuring:

* Additional buttons
* Multiple joysticks
* Camera control
* D-Pad
* Trigger support
* Full gamepad functionality

## License

MIT License
