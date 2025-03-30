import machine
import time

# Initialize Pins
r_en_pin = machine.Pin(13, machine.Pin.OUT, value=1)
l_en_pin = machine.Pin(10, machine.Pin.OUT, value=1)
r_dir_pin = machine.Pin(15, machine.Pin.OUT)
l_dir_pin = machine.Pin(12, machine.Pin.OUT)
r_step_pin = machine.Pin(14, machine.Pin.OUT)
l_step_pin = machine.Pin(11, machine.Pin.OUT)

# Define rail step limits (calibrate these values for your system)
MAX_STEPS = 1800
MIN_STEPS = 0

# Track current positions
current_position = {"r": 0, "l": 0}


def move_both_to_position(target_r, target_l):
    """
    Moves both stepper motors at the same time to their respective target positions.

    :param target_r: Target step position for the right stepper.
    :param target_l: Target step position for the left stepper.
    """

    # Enable both motors
    r_en_pin.value(0)
    l_en_pin.value(0)

    # Calculate step counts
    steps_r = abs(target_r - current_position["r"])
    steps_l = abs(target_l - current_position["l"])

    # Determine movement direction
    r_dir_pin.value(1 if target_r > current_position["r"] else 0)
    l_dir_pin.value(0 if target_l > current_position["l"] else 1)

    # Find the larger step count
    max_steps = max(steps_r, steps_l)

    # Move both motors together
    for i in range(max_steps):
        if i < steps_r:
            r_step_pin.value(1)
        if i < steps_l:
            l_step_pin.value(1)

        time.sleep_us(5000)  # Adjust this for speed

        if i < steps_r:
            r_step_pin.value(0)
        if i < steps_l:
            l_step_pin.value(0)

        time.sleep_us(5000)  # Adjust this for speed

    # Update positions
    current_position["r"] = target_r
    current_position["l"] = target_l

    # Disable both motors
    r_en_pin.value(1)
    l_en_pin.value(1)


