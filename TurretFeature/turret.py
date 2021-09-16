import RPi.GPIO as GPIO
import camera
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


redLed = 21


class Turret:

    def __init__(self):
        self.redLed = redLed
        self.cam = camera.Camera()
        self.onTarget = 0
        self.led = redLed
        GPIO.setup(redLed, GPIO.OUT)

        
    def locate(self):
        self.onTarget = self.cam.start()
        if self.onTarget == 1:
           print("Located")
        return self.onTarget
    
    def laser(self):
        GPIO.OUTPUT(redLed, GPIO.HIGH)
        time.sleep(1)
        GPIO.OUTPUT(redLed, GPIO.LOW)
        time.sleep(1)
        GPIO.OUTPUT(redLed, GPIO.HIGH)
        time.sleep(1)
        GPIO.OUTPUT(redLed, GPIO.LOW)
       
        
        
        

    
    

