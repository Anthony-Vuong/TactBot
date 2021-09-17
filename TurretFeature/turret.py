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


