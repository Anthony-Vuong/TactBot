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
        
        
    def locate(self):
        #not sure how to do this
        self.cam.start()
        
    def located(self):
        pass
        
    def launchPayload(self):
        #not sure how to do this
        pass
        

