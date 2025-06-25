import serial
import threading
import time
# DDSM115 motor controller
# https://www.waveshare.com/wiki/DDSM_Driver_HAT_(A)#Example_Demo

                
class Motor:
    def __init__(self, id, port="/dev/ttyAMA0", baudrate=115200, heartbeat=1000):
        self.port = port
        self.baudrate = baudrate
        self.ser = self.init_serial()
        self.start_serial()

    
        self.id = self.set_id(id)
        self.set_heartbeat(heartbeat)


    
    def read_serial(self):
        while True:
            data = self.ser.readline().decode('utf-8')
            if data:
                print(f"Received: {data}", end='')

    def init_serial(self):
        ser = serial.Serial(self.port, self.baudrate, dsrdtr=None)
        ser.setRTS(False)
        ser.setDTR(False)        
        return ser
    
    def start_serial(self):
        serial_recv_thread = threading.Thread(target=self.read_serial)
        serial_recv_thread.daemon = True
        serial_recv_thread.start()

    # velocity given in rpm
    # the acceleration time per revolution is measured in 0.1 milliseconds. The larger the act value, the smoother the speed change.
    def change_velocity(self, vel, acc):
        try:
            self.ser.write(f'{{"T":10010,"id":{self.id},"cmd":{vel},"act":{acc}}}\n'.encode() + b'\n')
        except KeyboardInterrupt:
            print("Error changing velocity")

    # cmd values is 0 to 32767 (0 to 360°). motor will pick shortest path to reach position
    def change_position(self, pos, acc):
        try:
            self.ser.write(f'{{"T":10010,"id":{self.id},"cmd":{pos},"act":{acc}}}\n'.encode() + b'\n')
        except KeyboardInterrupt:
            print("Error changing position")

    # -32767 to 32767, corresponding to -8A to 8A, but DDSM115 only supports up to 2.7A.
    def change_current(self, current, acc):
        try:
            self.ser.write(f'{{"T":10010,"id":{self.id},"cmd":{current},"act":{acc}}}\n'.encode() + b'\n')
        except KeyboardInterrupt:
            print("Error changing current")

    # only one motor can be plugged in at a time for this
    def set_id(self, id):
        try:
            self.ser.write(f'{{"T":10011,"id":{id}}}\n'.encode() + b'\n')
            return id
        except KeyboardInterrupt:
            print("Error setting id")

    # Time given in milliseconds
    # -1 means dont stop
    def set_heartbeat(self, time):
        try:
            self.ser.write(f'{{"T":11001,"time":{time}}}\n'.encode() + b'\n')
        except KeyboardInterrupt:
            print("Error setting heartbeat")

    # 1: current mode. 
    # 2: velocity mode. (default)
    # 3: position mode. 
    def change_mode(self, mode):
        try:
            self.ser.write(f'{{"T":10012,"id":{self.id},"mode":{mode}}}\n'.encode() + b'\n')
        except KeyboardInterrupt:
            print("Error changing mode")

    def get_id(self):
        try:
            self.ser.write(f'{{"T":10031}}\n'.encode() + b'\n')
            id = self.ser.readline().decode('utf-8')
            return id
        except KeyboardInterrupt:
            print("Error getting id")
    
    def get_info(self):
        try:
            self.ser.write(f'{{"T":10032}}\n'.encode() + b'\n')
            info = self.ser.readline().decode('utf-8')
            return info
        except KeyboardInterrupt:
            print("Error getting info")
