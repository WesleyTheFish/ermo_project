from assembly import Assembly
import time
import serial
import joystick
import pipeline as pl


def main():
    assembly = Assembly()

    assembly.forward(speed=100, accel=2)
    time.sleep(2)
    assembly.backward(speed=100, accel=2)
    time.sleep(2)
    assembly.stop()
    # while True:
    #     assembly.update_motor_command()

if __name__ == "__main__":
    try:
        main()
    except serial.SerialException as e:
        print(f"An error occurred: {e}")