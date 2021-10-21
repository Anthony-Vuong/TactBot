'''@file                    turret.py
   @brief                   Brief doc for turret.py
   @details                 Detailed doc for turret.py 
   @author                  Anthony Vuong, Pedro Munoz-Rodriguez
   @date                    August 12, 2021
'''
import RPi.GPIO as GPIO
import camera
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class Turret:
    ''' @brief This class contains the functions to operate turret System'''

    def __init__(self):
        ''' @brief Turret init function
            @details Initializes turret driver object with given parameters
            @return none
        '''
        self.cam = camera.Camera()
        self.onTarget = 0
        self.led = 21
        GPIO.setup(self.led, GPIO.OUT)
        self.laserBeam = GPIO.PWM(self.led, 100)
        self.laserBeam.start(0)

        
    def locate(self):
        '''@brief Calculate servo angle
           @details Calls the camera function to locate targets
           @return True or false if target is located or not
        '''
        self.onTarget = self.cam.start()
        if self.onTarget == 1:
           print("Located")
        return self.onTarget
    
    def laser(self):
        '''@brief Laser beam function
           @details Shoots a laser beam at the target if one is located
           @return None
        '''
        self.laserBeam.ChangeDutyCycle(20)
        time.sleep(1)
        self.laserBeam.ChangeDutyCycle(0)
        time.sleep(1)
        self.laserBeam.ChangeDutyCycle(20)
        time.sleep(1)
        self.laserBeam.ChangeDutyCycle(0)


