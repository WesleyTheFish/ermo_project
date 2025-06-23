import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class Joystick:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        adc_ads = ADS.ADS1115(i2c)
        adc_ads.gain = 1

        # chan = AnalogIn(ads, ADS.P0, ADS.P1)
        self.horz = AnalogIn(adc_ads, ADS.P0)
        self.vert = AnalogIn(adc_ads, ADS.P1)

        # Horizontal pot values
        self.horz_middle = 16400
        self.horz_min = 8
        self.horz_max = 32767

        # Vertical pot values
        self.vert_min = 30
        self.vert_max = 32767
        self.vert_middle = 16400
        

    def read(self):
        horz_value = self.horz.value
        vert_value = self.vert.value
        horz_final_value = 0
        vert_final_value = 0

        # Normalize horizontal values
        if horz_value < self.horz_middle:
            range1 = self.horz_middle - self.horz_min
            value = horz_value - self.horz_min
            horz_final_value = -1*(1-(value / range1))
        else:
            range2 = self.horz_max - self.horz_middle
            value = horz_value - self.horz_middle
            horz_final_value = value / range2

        # Normalize vertical values
        if vert_value < self.vert_middle:
            range1 = self.vert_middle - self.vert_min
            value = vert_value - self.vert_min
            vert_final_value = -1*(1-(value / range1))
        else:
            range2 = self.vert_max - self.vert_middle
            value = vert_value - self.vert_middle
            vert_final_value = value / range2

        # return horz_value, vert_value
        return horz_final_value, vert_final_value   

