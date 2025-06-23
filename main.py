from assembly import Assembly
import time
import serial
import joystick
import pipeline as pl


def main():
    assembly = Assembly()
    while True:
        assembly.update_motor_command()

if __name__ == "__main__":
    try:
        main()
    except serial.SerialException as e:
        print(f"An error occurred: {e}")