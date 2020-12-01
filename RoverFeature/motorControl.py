import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)

class motor:
    
    def __init__(self, pin1, pin2, pin3):
        self.motor1A = pin1
        self.motor1B = pin2
        self.enableMotor = pin3
        self.setup()
               
    def setup(self):
        GPIO.setup(self.motor1A,GPIO.OUT)  
        GPIO.setup(self.motor1B,GPIO.OUT)
        GPIO.setup(self.enableMotor,GPIO.OUT)
        
    def clockWise(self, speed):
        #GPIO.output(self.motor1A,GPIO.HIGH)  
        GPIO.output(self.motor1B,GPIO.LOW)
        GPIO.output(self.enableMotor,GPIO.HIGH)
        pwm = GPIO.PWM(self.motor1A, 1000)
        pwm.start(speed)        
        
    def counterClockWise(self, speed):
        #GPIO.output(self.motor1B,GPIO.HIGH)
        GPIO.output(self.motor1A,GPIO.LOW)    
        GPIO.output(self.enableMotor,GPIO.HIGH)
        pwm = GPIO.PWM(self.motor1B, 1000)
        pwm.start(speed) 
        
    def disable(self):
        GPIO.output(self.enableMotor,GPIO.LOW)

        
        
