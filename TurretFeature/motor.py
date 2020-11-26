''''@file main.py

    Motor Driver Python File '''

import pyb

## Motor driver object
#
#  Details
#  @author Anthony Vuong
#  @date April 21, 2020
#  @note https://bitbucket.org/avuong04/me405_labs/src/master/LAB_2/

class MotorDriver:
    ''' Methods and parameters needed to operate motor '''

    def __init__(self, EN_pin, IN1_pin, IN2_pin, timer, direction):
        ''' Initializes motor driver object with given parameters
            @param EN_pin enable pin for motor controller
            @param IN1_pin input signal
            @param IN2_pin input signal
            @param timer Used for to regulate PWM signal'''
        print('Creating a motor driver')
        self.EN_pin = EN_pin
        self.IN1_pin = IN1_pin
        self.IN2_pin = IN2_pin
        self.timer = timer
        self.direction = direction

    def enable(self):
        ''' Set enable pin high, and sets one MD pin low '''
        print('Enabling motor')
        self.EN_pin.high()
        if (self.direction == 'CCW'):
            self.IN2_pin.low()
        else:
            self.IN1_pin.low()


    def disable(self):
        ''' Sets enable pin low '''
        self.EN_pin.low()


    def set_duty(self, duty):
        ''' Control the duty cycle of the motor and direction '''
        if (self.direction == 'CCW'):
            self.timer.channel(1, pyb.Timer.PWM, pin=self.IN1_pin).pulse_width_percent(duty)
        else:
            self.timer.channel(2, pyb.Timer.PWM, pin=self.IN2_pin).pulse_width_percent(duty)

if __name__ == '__main__':

    pin_En = pyb.Pin('PA10', pyb.Pin.OUT_PP)
    pin_IN1 = pyb.Pin('PB4', pyb.Pin.OUT_PP)
    pin_IN2 = pyb.Pin('PB5', pyb.Pin.OUT_PP)
    tim = pyb.Timer(3, freq = 1000)

    testMotor = MotorDriver(pin_En, pin_IN1, pin_IN2, tim, 'CW')

    testMotor.enable()

    testMotor.set_duty(100)

    pyb.delay(10000)

    testMotor.disable()






