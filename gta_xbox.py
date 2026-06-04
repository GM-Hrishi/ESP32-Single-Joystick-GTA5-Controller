import serial
import vgamepad as vg
import time
import math

ser = serial.Serial("COM7", 115200, timeout=1)

time.sleep(2)

gamepad = vg.VX360Gamepad()

CENTER_X = 1650
CENTER_Y = 1790

DEADZONE = 3500

drive_mode = False
last_button = 1

smooth_x = 0
smooth_y = 0

print("Xbox Controller Started")
print("Click joystick to toggle WALK/DRIVE mode")

while True:
    try:
        line = ser.readline().decode(errors="ignore").strip()

        parts = line.split(",")

        if len(parts) != 3:
            continue

        x = int(parts[0])
        y = int(parts[1])
        sw = int(parts[2])

        # ==========================
        # MODE SWITCH
        # ==========================

        if last_button == 1 and sw == 0:

            drive_mode = not drive_mode

            if drive_mode:
                print("DRIVE MODE")
            else:
                print("WALK MODE")

            time.sleep(0.25)

        last_button = sw

        # ==========================
        # RAW -> STICK RANGE
        # ==========================

        if x >= CENTER_X:
            lx = int(((x - CENTER_X) / (3300 - CENTER_X)) * 32767)
        else:
            lx = int(-((CENTER_X - x) / CENTER_X) * 32767)

        if y >= CENTER_Y:
            ly = int(((y - CENTER_Y) / (4095 - CENTER_Y)) * 32767)
        else:
            ly = int(-((CENTER_Y - y) / CENTER_Y) * 32767)

        # ==========================
        # ORIENTATION
        # ==========================

        xbox_x = -ly
        xbox_y = -lx

        # ==========================
        # CIRCULAR DEADZONE
        # ==========================

        magnitude = math.sqrt(
            xbox_x * xbox_x +
            xbox_y * xbox_y
        )

        if magnitude < DEADZONE:
            xbox_x = 0
            xbox_y = 0

        # ==========================
        # RESPONSE CURVE
        # ==========================

        nx = xbox_x / 32767.0
        ny = xbox_y / 32767.0

        nx = nx * abs(nx)
        ny = ny * abs(ny)

        xbox_x = int(nx * 32767)
        xbox_y = int(ny * 32767)

        # ==========================
        # SMOOTHING
        # ==========================

        smooth_x = int(
            smooth_x * 0.75 +
            xbox_x * 0.25
        )

        smooth_y = int(
            smooth_y * 0.75 +
            xbox_y * 0.25
        )

        # ==========================
        # WALK MODE
        # ==========================

        if not drive_mode:

            gamepad.left_joystick(
                x_value=smooth_x,
                y_value=smooth_y
            )

            gamepad.left_trigger(value=0)
            gamepad.right_trigger(value=0)

        # ==========================
        # DRIVE MODE
        # ==========================

        else:

            steer = int(smooth_x * 0.85)

            gamepad.left_joystick(
                x_value=steer,
                y_value=0
            )

            if smooth_y > 0:

                throttle = int(
                    (smooth_y / 32767.0) * 255
                )

                throttle = max(
                    0,
                    min(255, throttle)
                )

                gamepad.right_trigger(
                    value=throttle
                )

                gamepad.left_trigger(
                    value=0
                )

            elif smooth_y < 0:

                brake = int(
                    (abs(smooth_y) / 32767.0) * 255
                )

                brake = max(
                    0,
                    min(255, brake)
                )

                gamepad.left_trigger(
                    value=brake
                )

                gamepad.right_trigger(
                    value=0
                )

            else:

                gamepad.left_trigger(value=0)
                gamepad.right_trigger(value=0)

        gamepad.update()

    except Exception as e:
        print("ERROR:", e)
