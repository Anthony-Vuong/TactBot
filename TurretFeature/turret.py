import RPi.GPIO as GPIO
import camera
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class Turret:

    def __init__(self):
        self.cam = camera.Camera()
        self.onTarget = 0
        self.led = 21
        GPIO.setup(self.led, GPIO.OUT)
        self.laserBeam = GPIO.PWM(self.led, 100)
        self.laserBeam.start(0)
        self.targetFound = 0
        self.msg = ''
        
    
    def controls(self, ctrl, rover):
        if ctrl == "9":
            rover.controls(5)
            self.targetFound = self.locate()
            time.sleep(1)
            if self.targetFound == 1:
                self.msg += "Target Found. Engage?"
        elif ctrl == '8':
            self.tur.laser()
            time.sleep(3)
            self.msg += "Target Destroyed"
        elif ctrl == '7':
            self.msg += "Fire mission aborted"
            
        if self.msg != None:
            return self.msg

        
    def locate(self):
        self.onTarget = self.cam.start()
        if self.onTarget == 1:
           print("Located")
        return self.onTarget
    
    def laser(self):
        self.laserBeam.ChangeDutyCycle(20)
        time.sleep(1)
        self.laserBeam.ChangeDutyCycle(0)
        time.sleep(1)
        self.laserBeam.ChangeDutyCycle(20)
        time.sleep(1)
        self.laserBeam.ChangeDutyCycle(0)


