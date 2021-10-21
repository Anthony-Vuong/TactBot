import RPi.GPIO as GPIO
import numpy as np
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Motor:
    ''' Methods and parameters needed to operate motor '''
    
    def __init__(self, EN_pin, IN1_pin, IN2_pin):
        ''' @brief Motor init function
            @param EN_pin enable pin for motor controller
            @param IN1_pin input signal
            @param IN2_pin input signal
            @details Initializes motor driver object with given parameters
            @return none
        '''
        self.enable_pin = EN_pin
        self.in1_pin = IN1_pin
        self.in2_pin = IN2_pin
        GPIO.setup(EN_pin, GPIO.OUT)
        GPIO.setup(IN1_pin, GPIO.OUT)
        GPIO.setup(IN2_pin, GPIO.OUT)
        self.inMotion = 0
        self.speed = GPIO.PWM(EN_pin, 50)
        self.speed.start(0)
        
        
    def enable(self):
        '''@brief Enable pwm pin
           @param None
           @details Set enable pin high, and sets one MD pin low
           @return None
        '''
        GPIO.output(self.enable_pin, GPIO.HIGH)
        
    def disable(self):
        '''@brief Disable pwm pin
           @param None
           @details  Sets enable pin low 
           @return None
        '''
        GPIO.output(self.enable_pin, GPIO.LOW)
        
    def hold(self):
        '''@brief Stops motor
           @param None
           @details  Disables all pins for motor
           @return None
        '''
        self.disable()
        GPIO.output(self.in1_pin, GPIO.LOW)
        GPIO.output(self.in2_pin, GPIO.LOW)
        self.inMotion = 0
        
    def cw(self, duty):
        '''@brief Spins motor
           @param duty Speed represented by duty cycle
           @details  Setup for motor to spin clockwise(cw)
           @return None
        '''
        
        if self.inMotion == 0:
            self.enable()
            GPIO.output(self.in1_pin, GPIO.LOW)
            GPIO.output(self.in2_pin, GPIO.HIGH)
            self.inMotion = 1
            
        self.speed.ChangeDutyCycle(duty)

     
    def ccw(self, duty):
        '''@brief Spins motor
           @param duty Speed represented by duty cycle
           @details  Setup for motor to spin counter-clockwise(ccw)
           @return None
        '''
        if self.inMotion == 0:
            self.enable()
            GPIO.output(self.in1_pin, GPIO.HIGH)
            GPIO.output(self.in2_pin, GPIO.LOW)
            self.inMotion = 1
            
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
    
      
