'''@file                    servo.py
   @brief                   Brief doc for servo.py
   @details                 Detailed doc for servo.py 
   @author                  Anthony Vuong, Pedro Munoz-Rodriguez
   @date                    August 12, 2021
'''
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Servo:
    ''' @brief      This class gives functionality to the Turret System (SG90 Servos) and MG996 Servo for the steering system.
    '''
    def __init__(self, servoPin, startDuty=0, turret=False):
        ''' @brief Servo init function
            @param steer Steering pin for motor controller
            @param steerAngle pin input signal
            @details Initializes servo driver object with given parameters
            @return none
        '''
        if turret == False:
            self.steeringPin = servoPin
            self.steer = GPIO.setup(servoPin, GPIO.OUT)
            self.steerAngle = GPIO.PWM(self.steeringPin, 50)
            self.steerAngle.start(startDuty)
        else:
            self.turretServoPin = servoPin
            self.turretAngle = GPIO.PWM(servoPin, 50)
            self.turretAngle.start(90)

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

    def turret_angle(self, angle):
        '''@brief Calculate servo angle for turret system
           @param angle The desired servo angle
           @details Calculates the position of the servo by computing the angle
           @return None
        '''
        dutyCycle = angle / 18. + 3.
        self.turretAngle.ChangeDutyCycle(dutyCycle)
        time.sleep(0.3)

