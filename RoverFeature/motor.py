import RPi.GPIO as GPIO
import numpy as np
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ForwardPin = 12
BackwardPin = 13
EnablePin = 14

class Motor:
    ''' Methods and parameters needed to operate motor '''
    
    def __init__(self, EN_pin, IN1_pin, IN2_pin, timer):
        ''' Initializes motor driver object with given parameters
            @param EN_pin enable pin for motor controller
            @param IN1_pin input signal
            @param IN2_pin input signal'''
        self.En_pin = GPIO(EnablePin, GPIO.OUT)
        self.forward_pin = GPIO(ForwardPin, GPIO.OUT)
        self.backward_pin = GPIO(BackwardPin, GPIO.OUT)
        self.speed = GPIO.PWM(self.En_pin, 1000)
        self.speed.start(0)
        
        
    def enable(self):
        ''' Set enable pin high, and sets one MD pin low '''
        GPIO.output(self.En_pin, GPIO.HIGH)
        
    def disable(self):
        ''' Sets enable pin low '''
        GPIO.output(self.En_pin, GPIO.LOW)
        
    def hold(self):
        self.disable()
        GPIO.output(self.forward_pin, GPIO.LOW)
        GPIO.output(self.backward_pin, GPIO.LOW)
        
    def cw(self, duty):
        self.enable()
        GPIO.output(self.backward_pin, GPIO.LOW)
        GPIO.output(self.forward_pin, GPIO.HIGH)
        self.speed.ChangeDutyCycle(duty)

     
    def ccw(self, duty):
        self.enable()
        GPIO.output(self.backward_pin, GPIO.HIGH)
        GPIO.output(self.forward_pin, GPIO.LOW)
        self.speed.ChangeDutyCycle(duty)

        
    def spin(self, direction, duty = 0):
        if direction == 1:
            self.cw(duty)
        elif direction == -1
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
    
      
