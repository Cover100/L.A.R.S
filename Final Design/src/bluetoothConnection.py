from machine import Pin, UART
from time import sleep
import re

# Initialize the Bluetooth STATE pin
bt_state = Pin(2, Pin.IN)

# Initialize UART for Bluetooth communication
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

def is_connected():
    return bt_state.value() == 1

def get_uart_command():
    if uart.any():
        data = uart.read().decode().strip()

        # Split data by '-' and extract valid commands
        parts = data.split('-')
        commands = [part for part in parts if part.strip()] 

        if commands:
            last_command = commands[-1] 
            print(f"Command: {last_command}")
            return last_command.strip()

    return None 


