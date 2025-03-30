import bluetoothConnection
import servo_control
from machine import Pin
from time import sleep

# -------------------- Pin Initialisation -------------------- 
led = Pin(6, Pin.OUT, value=0)

r_relay = Pin(3, Pin.OUT, value=0)  # Active HIGH
l_relay = Pin(4, Pin.OUT, value=0)  # Active HIGH

try:
    while True:
        if bluetoothConnection.is_connected():
            led.on()
            command = bluetoothConnection.get_uart_command()  # Get the command from UART
            
            # Ensure the command is not None
            if command:
                if command == "On":
                    print("Turning relays ON...")
                    r_relay.value(1)
                    l_relay.value(1)
                    
                elif command == "Off":
                    print("Turning relays OFF...")
                    r_relay.value(0)
                    l_relay.value(0)
                    
                elif command.startswith("S:"):  # Handle slider updates
                    try:
                        slider_value = int(command.split(":")[1])  # Extract slider value (0 to 100)
                        print(f"Slider updated to: {slider_value}")

                        # Map slider value (0-100) to step range (MIN_STEPS to MAX_STEPS)
                        target_steps = int((slider_value / 100) * servo_control.MAX_STEPS)

                        # Move both servos to the target position **simultaneously**
                        servo_control.move_both_to_position(target_steps, target_steps)

                    except ValueError:
                        print("Invalid slider value received.")
                        
                elif command == "Exit":
                    print("Exit command received. Breaking the loop...")
                    break
                else:
                    print(f"Unknown command: {command}")
        else:
            led.off()
            sleep(0.5)
            led.on()
            sleep(0.5)

except KeyboardInterrupt:
    print("Keyboard Interrupt detected. Cleaning up...")

finally:
    # Clean Exit
    print("Performing cleanup before exiting...")
    led.off()
    r_relay.value(0)
    l_relay.value(0)
    servo_control.r_en_pin.value(1)
    servo_control.l_en_pin.value(1)
    print("Exiting program.")

