import RPi.GPIO as GPIO
import motorControl.motor as motor
from time import sleep

class Rover:
    
    def __init__(self, motor1, motor2, motor3, motor4):
        self.leftRearWheel = motor1     
        self.rightRearWheel = motor2
        self.leftFrontWheel = motor3     #strictly used for turning
        self.rightFrontWheel = motor4    #strictly used for turning
        
    def forward(self):
        self.leftRearWheel.counterClockWise()
        self.rightRearWheel.clockWise()
        
    def backWard(self):
        self.rightRearWheel.counterClockWise()
        self.leftRearWheel.clockWise()
    
    def stop(self):
        self.rightRearWheel.disable()
        self.leftRearWheel.disable()
        
    def leftTurn(self):
        #not sure how to do this yet
        
    def rightTurn(self):
        #not sure how to do this yet
             