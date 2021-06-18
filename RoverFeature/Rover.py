'''@file                    Rover.py
   @brief                   Brief doc for Rover.py
   @details                 Detailed doc for Rover.py 
   @author                  Anthony Vuong, Pedro Muñoz-Rodriguez
   @date                    June 18, 2021
'''
import RPI.gpio as GPIO


class Rover:
    def __init__(self, steerPin, throttlePin):
        self.steer = GPIO.PWM(steerPin, 50)
        self.throttle = GPIO.PWM(throttlePin, 50)
        self.steer.start(0)
        self.throttle.start(0)
        
        self.throttleVelocity = 0
        self.steerDirection = 0
        
    
    def run(self):
        self.steer.ChangeDutyCycle(self.steerDirection)
        self.throttle.ChangeDutyCycle(self.throttleVelocity)
        
        
    def increaseSpeed(self):
        self.throttleVelocity = self.throttleVelocity + 1
    
    def decreaseSpeed(self):
        self.throttleVelocity = self.throttleVelocity - 1
        
    def steerRight(self):
        self.steerDirection = self.steerDirection + 1
        
    def steerLeft(self):
        self.steerDirection = self.steerDirection - 1
        
    def stop(self):
        self.throttleVelocity = 0
        
# #STEERING PWM PIN
# steering = GPIO.PWM(12, 50)
# steering.start(0)

# #THROTTLE PWM PIN
# throttle = GPIO.PWM(13, 50)
# throttle.start(0)

# #INCREMENT VARIABLES FOR DIRECTION AND SPEED
# steer = 0
# direction = 0