import RPi.GPIO as GPIO
import numpy as np
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

##    @var int $ForwardPin
##    Pin value for forward direction
ForwardPin = 12

##    @var int $BackwardPin 
##    Pin value for backward direction
BackwardPin = 13

##    @var int $EnablePin 
##    Pin value for pwm signal
EnablePin = 14

class Motor:
    ''' Methods and parameters needed to operate motor '''
    
    def __init__(self, EN_pin, IN1_pin, IN2_pin, timer):
        ''' @brief Motor init function
            @param EN_pin enable pin for motor controller
            @param IN1_pin input signal
            @param IN2_pin input signal
            @details Initializes motor driver object with given parameters
            @return none
        '''
        self.En_pin = GPIO.setup(EnablePin, GPIO.OUT)
        self.forward_pin = GPIO.setup(ForwardPin, GPIO.OUT)
        self.backward_pin = GPIO.setup(BackwardPin, GPIO.OUT)
        self.speed = GPIO.PWM(self.En_pin, 1000)
        self.speed.start(0)
        
        
    def enable(self):
        '''@brief Enable pwm pin
           @param None
           @details Set enable pin high, and sets one MD pin low
           @return None
        '''
        GPIO.output(self.En_pin, GPIO.HIGH)
        
    def disable(self):
        '''@brief Disable pwm pin
           @param None
           @details  Sets enable pin low 
           @return None
        '''
        GPIO.output(self.En_pin, GPIO.LOW)
        
    def hold(self):
        '''@brief Stops motor
           @param None
           @details  Disables all pins for motor
           @return None
        '''
        self.disable()
        GPIO.output(self.forward_pin, GPIO.LOW)
        GPIO.output(self.backward_pin, GPIO.LOW)
        
    def cw(self, duty):
        '''@brief Spins motor
           @param duty Speed represented by duty cycle
           @details  Setup for motor to spin clockwise(cw)
           @return None
        '''
        self.enable()
        GPIO.output(self.backward_pin, GPIO.LOW)
        GPIO.output(self.forward_pin, GPIO.HIGH)
        self.speed.ChangeDutyCycle(duty)

     
    def ccw(self, duty):
        '''@brief Spins motor
           @param duty Speed represented by duty cycle
           @details  Setup for motor to spin counter-clockwise(ccw)
           @return None
        '''
        self.enable()
        GPIO.output(self.backward_pin, GPIO.HIGH)
        GPIO.output(self.forward_pin, GPIO.LOW)
        self.speed.ChangeDutyCycle(duty)

        
    def spin(self, direction, duty = 0):
        '''@brief Spins motor with speed and direction
           @param duty Speed represented by duty cycle, default is 0%
           @param direction An int representing the direction of the motor
           @details  Setup for motor control
           @return None
        '''
        if direction == 1:
            self.cw(duty)
        elif direction == -1:
            self.ccw(duty)
        else:
            self.hold()
        
    

# if __name__ == '__main__':
#     
#     m1 = Motor()
#     
#     m1.spin(1, 10)
#     time.sleep(3)
#     m1.hold()
#     
#     GPIO.cleanup()
    
      
