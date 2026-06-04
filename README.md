# ESP32 Single Joystick GTA V Controller

A fun project that turns a single ESP32-connected analog joystick into a virtual Xbox 360 controller for GTA V.

This project demonstrates how an ESP32, Python, vgamepad and ViGEmBus can be combined to emulate a game controller using only a single analog joystick module.

## Important

This repository is intentionally limited to a single joystick module.

It is not intended to replace a full Xbox or PlayStation controller.

A future repository may implement:

* Dual analog sticks
* Face buttons
* D-Pad
* Shoulder buttons
* Full trigger controls
* Complete gamepad functionality

This project focuses only on creating a playable GTA V experience using a single joystick and its push button.

## Features

* Virtual Xbox 360 controller
* Analog walking
* Analog steering
* Analog acceleration
* Analog braking and reverse
* Walk Mode
* Drive Mode
* Mode switching using joystick button
* Circular deadzone
* Input smoothing
* Response curves

## Hardware Required

* ESP32 Dev Board
* Analog Joystick Module
* Jumper Wires
* USB Cable

## Wiring

| Joystick Pin | ESP32 Pin |
| ------------ | --------- |
| VCC          | 3V3       |
| GND          | GND       |
| VRX          | GPIO34    |
| VRY          | GPIO35    |
| SW           | GPIO32    |

### Wiring Diagram

![Wiring Diagram](image.png)

---

# Setup Guide

## 1. Upload the ESP32 Sketch

Open:

```text
esp32_joystick.ino
```

in Arduino IDE.

Select:

```text
DOIT ESP32 DEVKIT V1
```

Upload the sketch.

## 2. Verify ESP32 Output

Open Serial Monitor.

Baud rate:

```text
115200
```

You should see values similar to:

```text
1650,1790,1
1645,1785,1
1652,1791,0
```

Format:

```text
X,Y,SW
```

## 3. Install Python Dependencies

```bash
pip install pyserial vgamepad
```

## 4. Install ViGEmBus

Download:

https://github.com/nefarius/ViGEmBus/releases

Install:

```text
ViGEmBus_1.22.0_x64_x86_arm64.exe
```

Reboot Windows after installation.

## 5. Find Your ESP32 COM Port

Arduino IDE:

```text
Tools → Port
```

Example:

```text
COM7
```

## 6. Update the COM Port

Open:

```text
gta_xbox.py
```

Update:

```python
ser = serial.Serial("COM7", 115200, timeout=1)
```

to match your ESP32 port.

## 7. Start the Controller

Open a terminal in the repository folder:

```bash
python gta_xbox.py
```

## 8. Verify the Virtual Controller

Press:

```text
Win + R
```

Run:

```text
joy.cpl
```

An Xbox 360 controller should appear.

Open Properties and verify:

* Up
* Down
* Left
* Right

all function correctly.

## 9. Disable Steam Input

This step is important.

Steam Input may prevent GTA V from recognizing the virtual controller correctly.

Steam:

```text
Library
→ Grand Theft Auto V
→ Properties
→ Controller
→ Override for Grand Theft Auto V
→ Disable Steam Input
```

Completely restart GTA V afterwards.

## 10. Launch GTA V

Before launching:

* gta_xbox.py must be running
* Controller must appear in joy.cpl
* Steam Input must be disabled

Launch GTA V.

The game should automatically detect the virtual Xbox controller.

---

# Controls

## Walk Mode

Default mode.

Joystick behaves as the Xbox left stick.

Used for:

* Walking
* Running
* Character movement

## Drive Mode

Press the joystick button.

Controls become:

| Direction | Action          |
| --------- | --------------- |
| Up        | Accelerate      |
| Down      | Brake / Reverse |
| Left      | Steer Left      |
| Right     | Steer Right     |

Press the joystick button again to return to Walk Mode.

---

# Troubleshooting

## Controller appears in joy.cpl but not GTA V

1. Disable Steam Input.
2. Close GTA V completely.
3. Start gta_xbox.py.
4. Verify controller appears in joy.cpl.
5. Launch GTA V.

## GTA V only shows keyboard prompts

Steam Input is probably still enabled.

Disable it and restart the game.

## ESP32 not detected

Check:

```text
Tools → Port
```

and update the COM port in gta_xbox.py.

## Controller Drifting

Increase the DEADZONE value in gta_xbox.py.

---

# Disclaimer

This project is intended for learning, experimentation and fun.

It is not intended to replace a real game controller.

Controller feel, compatibility and performance will vary depending on hardware quality, calibration and game support.

## License

MIT License
