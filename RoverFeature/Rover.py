'''@file                    Rover.py
   @brief                   Brief doc for Rover.py
   @details                 Detailed doc for Rover.py 
   @author                  Anthony Vuong, Pedro Muñoz-Rodriguez
   @date                    June 18, 2021
'''
import RPI.gpio as GPIO
import motor.motor as motor


class Rover:
    def __init__(self, steerPin, throttlePin):
        self.steer = GPIO.PWM(steerPin, 50)
        self.throttle = GPIO.PWM(throttlePin, 50)
        self.steer.start(0)
        self.throttle.start(0)
        
        self.throttleVelocity = 0
        self.steerDirection = 0
        
    
    def controls(self, data):
         
        if(data == '1'):
            #throttle straight
            self.rover.increaseSpeed()
        elif(data == '2'):
            #steer right
            self.rover.steerRight()
        elif(data == '3'):
            #throttle back
            self.rover.decreaseSpeed()
        elif(data == '4'):
            #steer left
            self.rover.steerLeft()
        elif(data == '5'):
            #STOP
            self.rover.stop()
        else:
            print("Command not valid")
            
            
    def run(self, data):
        
        self.controls(data)
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
        
