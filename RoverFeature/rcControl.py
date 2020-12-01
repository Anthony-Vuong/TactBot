import RPi.GPIO as GPIO
import motorControl.motor as motor
from time import sleep

class Rover:
    
    def __init__(self, motor1, motor2, motor3, motor4):
        self.leftRearWheel = motor1     
        self.rightRearWheel = motor2
        self.leftFrontWheel = motor3     #strictly used for turning
        self.rightFrontWheel = motor4    #strictly used for turning
        
    def forward(self, duty):
        if duty < 100 and duty > 0:
            self.leftRearWheel.counterClockWise(duty)
            self.rightRearWheel.clockWise(duty)
        else:
            print("Speed input not valid")
        
    def backWard(self, duty):
        if duty < 100 and duty > 0:
            self.rightRearWheel.counterClockWise(duty)
            self.leftRearWheel.clockWise(duty)
        else:
            print("Speed input not valid")
    
    def stop(self):
        self.rightRearWheel.disable()
        self.leftRearWheel.disable()
        
    def speedUp(self, duty):
        #change the duty cycle to go faster
    
    def slowDown(self, duty):
        #change the duty cycle to go slower
        
    def straightenOut(self):
        #wheel straighten out
        
    def leftTurn(self, angle):
        #not sure how to do this yet
        
    def rightTurn(self, angle):
        #not sure how to do this yet
             