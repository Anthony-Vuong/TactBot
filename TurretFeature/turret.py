import RPi.GPIO as GPIO
import camera

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


redLed = 21

GPIO.setup(redLed, GPIO.OUT)

class Turret:

    def __init__(self):
        self.redLed = redLed
        self.cam = camera.Camera()
        self.onTarget = 0

    def locate(self):
        self.onTarget = self.cam.start()
        if self.onTarget == 1:
           print("LOcated")
        return self.onTarget

    
    def launchPayload(self):
        #not sure how to do this
        pass

