'''@file                    Rover.py
   @brief                   Brief doc for Rover.py
   @details                 Detailed doc for Rover.py 
   @author                  Anthony Vuong, Pedro Munoz-Rodriguez
   @date                    June 18, 2021
'''
import RPi.GPIO as GPIO
import motor
import servo 
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
##    @var int $dir_forward 
##    An int value representing forward flag
dir_forward = 1

##    @var int $dir_backward
##    An int value representing backward flag
dir_backward = -1

##    @var int $dir_stop 
##    An int value representing stop flag
dir_stop = 0

throttle_En = 25
throttle_in1 = 23
throttle_in2 = 24

steering_pin = 17


class Rover():
    def __init__(self):
        ''' @brief Rover init function
            @param throttleMotor Motor object for controlling rover throttle
            @param steeringServo Servo object for controlling rover steering
            @param currentStatus Current driving direction of rover
            @param currentSpeed Current driving speed of rover
            @details Initializes rover object with given parameters
            @return none
        '''
        self.throttleMotor = motor.Motor(throttle_En, throttle_in1, throttle_in2)
        self.steeringServo = servo.Servo(steering_pin, 45)
        self.currentStatus = dir_stop
        self.currentSpeed = 10
        self.currentDirection = 45
        
    
    def controls(self, data):
        '''@brief Rover controls
           @param data An int value indicating specific control
           @details Controls rover direction and speed upon every call
           @return None
        '''
        valid_flag = 0 
         
        if(data == "1"):
            #throttle straight
            print("1")
            self.forward()
        elif(data == "2"):
            #steer right
            print("2")
            self.steer_right()
        elif(data == "3"):
            #throttle back
            print("3")
            self.backward()
        elif(data == "4"):
            #steer left
            print("4")
            self.steer_left()
        elif(data == "5"):
            #STOP
            print("5")
            self.stop()
        else:
            valid_flag = 1
            #print("Rover controls(): valid flag : false")

        return valid_flag
        
    def stop(self):
        '''@brief Stop rover
           @param None
           @details Disables all pins, sets currentStatus=0, and set currentSpeed=0
           @return None
        '''
        self.throttleMotor.hold()
        self.currentStatus = dir_stop
        self.currentSpeed = 0

    def forward(self):
        '''@brief Move rover forward
           @param None
           @details Starts rover moving forward or increases speed if already doing so
           @return None
        '''
        if self.currentStatus == dir_backward or self.currentStatus == dir_stop:
            self.stop()
            time.sleep(1)
            self.currentStatus = dir_forward
        
        self.currentSpeed = self.currentSpeed + 5
        self.throttleMotor.spin(dir_forward, self.currentSpeed)
        
    def backward(self):
        '''@brief Move rover backward
           @param None
           @details Starts rover moving forward or increases speed if already doing so
           @return None
        '''
        if self.currentStatus == dir_forward or self.currentStatus == dir_stop:
            self.stop()
            time.sleep(1)
            self.currentStatus = dir_backward
        
        self.currentSpeed = self.currentSpeed + 5
        self.throttleMotor.spin(dir_backward, self.currentSpeed)
    
    def steer_right(self):
        '''@brief Turns rover right
           @param None
           @details Moves rover in a right-direction and increases turning degree every call to function
           @return None
        '''
        if self.currentDirection < 65:
            self.currentDirection = self.currentDirection + 10
            self.steeringServo.calc_angle(self.currentDirection)
    
    def steer_left(self):
        '''@brief Turns rover left
           @param None
           @details Moves rover in a left-direction and increases turning degree every call to function
           @return None
        '''
        if self.currentDirection > 25:
            self.currentDirection = self.currentDirection - 10
            self.steeringServo.calc_angle(self.currentDirection)
