import pyb

## Motor driver object
#
#  Details
#  @author Anthony Vuong
#  @date April 21, 2020
#  @note https://bitbucket.org/avuong04/me405_labs/src/master/LAB_2/

class MotorDriver:

    def __init__(self, enable, pin1, pin2, timer):
        print('Creating a motor driver')
        self.pin1 = pyb.Pin(pin1, pyb.Pin.OUT_PP)
        self.pin2 = pyb.Pin(pin2, pyb.Pin.OUT_PP)
        self.timer = pyb.Timer(timer, freq = 1000)
        self.enable = pyb.Pin(enable, pyb.Pin.OUT_PP)
        
    def enable(self):
        print('Enabling motor')
        self.enable.high()
       
    def disable(self):
        print('Disabling motor')
        self.enable.low()

    def set_duty(self, duty):
        print('Running motor')
        if duty > 99 or duty < 1:
            print("Not a valid pulse width percent");
        else:
            self.timer.channel(1, pyb.Timer.PWM, pin=self.pin1).pulse_width_percent(duty)
        

if __name__ == '__main__':

    
    testMotor = MotorDriver('PA10', 'PB4', 'PB5', 3)

    testMotor.enable()

    testMotor.set_duty(100)

    pyb.delay(10000)

    testMotor.disable()






