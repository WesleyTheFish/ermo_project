from assembly import Assembly
import time
import serial
import joystick
import pipeline as pl
import traceback


def main():
    
    try:
        assembly = Assembly()
        while True:
            assembly.update_motor_command()
    except Exception as e:
        print(f"An error occurred: {e}")
        # traceback.print_exc()
        

if __name__ == "__main__":
    try:
        main()
    except serial.SerialException as e:
        print(f"An error occurred: {e}")