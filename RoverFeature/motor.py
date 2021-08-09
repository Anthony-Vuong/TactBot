import pyb

class Motor:
    ''' Methods and parameters needed to operate motor '''
    
    def __init__(self, EN_pin, IN1_pin, IN2_pin, timer):
        ''' Initializes motor driver object with given parameters
            @param EN_pin enable pin for motor controller
            @param IN1_pin input signal
            @param IN2_pin input signal
            @param timer Used for to regulate PWM signal'''
        print('Creating a motor driver')
        self.En_pin = pyb.Pin(EN_pin, pyb.Pin.OUT_PP)
        self.pin_IN1 = pyb.Pin(IN1_pin, pyb.Pin.OUT_PP)        
        self.pin_IN2 = pyb.Pin(IN2_pin, pyb.Pin.OUT_PP)
        self.timer = pyb.Timer(timer, freq = 20000)
        self.ch1 = self.timer.channel(1, pyb.Timer.PWM, pin=self.pin_IN1)
        self.ch2 = self.timer.channel(2, pyb.Timer.PWM, pin=self.pin_IN2)

    
    def enable(self):
        ''' Set enable pin high, and sets one MD pin low '''
        print('Enabling motor')
        self.En_pin.high()
        
    def disable(self):
        ''' Sets enable pin low '''
        self.En_pin.low()
        
        
    
    def set_duty(self, duty):
        ''' Control the duty cycle of the motor and direction '''
        if (duty <= 100 and duty >= -100):
            if (duty < 0):
                self.ch1.pulse_width_percent(0)
                self.ch2.pulse_width_percent(abs(duty))
            else:
                self.ch2.pulse_width_percent(0)
                self.ch1.pulse_width_percent(abs(duty))
        else:
            print("Not a valid input")


if __name__ == '__main__':

        
    testMotor = MotorDriver('PA10', 'PB4', 'PB5', 3)

    testMotor.enable()
    
    testMotor.set_duty(10)
    
    pyb.delay(10000)
    
    testMotor.disable()
    
    pyb.delay(5000)

    testMotor.enable()
    
    testMotor.set_duty(-10)
    
    pyb.delay(10000)
      
