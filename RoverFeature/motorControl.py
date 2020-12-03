import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)

class motor:
    
    def __init__(self, pin1, pin2, pin3):
        self.motor1A = pin1
        self.motor1B = pin2
        self.enableMotor = pin3
        self.duty = 0
        self.pwm = GPIO.PWM(None, 0)
        self.setup()
        
    def getDuty(self):
        return self.duty
                    
    def setupGPIO(self):
        GPIO.setup(self.motor1A,GPIO.OUT)  
        GPIO.setup(self.motor1B,GPIO.OUT)
        GPIO.setup(self.enableMotor,GPIO.OUT)
        
    def setPWM(self, motor, freq):
        tempPWM = GPIO.PWM(motor, freq)
        return tempPWM
     
    def clockWise(self, speed):
        GPIO.output(self.motor1B,GPIO.LOW)
        GPIO.output(self.enableMotor,GPIO.HIGH)
        self.pwm = GPIO.PWM(self.motor1A, 1000)
        pwm.start(speed)        
        
    def counterClockWise(self, speed):
        GPIO.output(self.motor1A,GPIO.LOW)    
        GPIO.output(self.enableMotor,GPIO.HIGH)
        pwm = GPIO.PWM(self.motor1B, 1000)
        pwm.start(speed)
        
    def changeDuty(self, duty):
        self.duty = duty
        self.pwm.ChangeDutyCycle(duty)
      
    def disable(self):
        GPIO.output(self.enableMotor,GPIO.LOW)

        
        
