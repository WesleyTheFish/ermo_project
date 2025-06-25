import motor
import joystick
import math
import pipeline as pl


class Assembly:
    def __init__(self, joystick_deadzone=0.2):
        self.motor1 = motor.Motor(id=1)

        # self.motor2 = motor.Motor(id=2)
        self.joystick = joystick.Joystick()
        self.joystick_pipeline_x = pl.Pipeline(transform_funcs=[pl.make_deadzone_transform(0,joystick_deadzone),
                               pl.make_expo_transform(1),
                               pl.make_window_filter_transform(30)])
        
        self.joystick_pipeline_y = pl.Pipeline(transform_funcs=[pl.make_deadzone_transform(0,joystick_deadzone),
                                pl.make_expo_transform(1),
                                pl.make_window_filter_transform(5)])



    def update_motor_command(self):
        x_sample, y_sample = self.joystick.read()
        x_sample = self.joystick_pipeline_x.run_pipeline(x_sample)
        y_sample = self.joystick_pipeline_y.run_pipeline(y_sample)


        
        #! Convert joystick values to motor commands
        self.motor1.change_velocity(x_sample*200,1)
        

    
        # print(f"{x_sample:>8.3f}, {y_sample:>8.3f}")

   