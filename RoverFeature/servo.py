'''@file                    servo.py
   @brief                   Brief doc for servo.py
   @details                 Detailed doc for servo.py 
   @author                  Anthony Vuong, Pedro Muñoz-Rodriguez
   @date                    August 12, 2021
'''
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Servo:
    def __init__(self, steeringPin):
        ''' @brief Servo init function
            @param steer Steering pin for motor controller
            @param steerAngle pin input signal
            @details Initializes servo driver object with given parameters
            @return none
        '''
        self.steeringPin = steeringPin
        self.steer = GPIO(steeringPin, GPIO.OUT)
        self.steerAngle = GPIO.PWM(self.steer, 50)
        self.steerAngle.start(0)
        
    def calc_angle(self, angle):
        '''@brief Calculate servo angle
           @param angle The desired servo angle
           @details Calculates the position of the servo by computing the angle
           @return None
        '''
        duty = angle / 18 + 3
        GPIO.output(self.steeringPin, True)
        self.steerAngle.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(self.steeringPin, False)
        self.steerAngle.ChangeDutyCycle(duty)
        
        
        