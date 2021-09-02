'''@file                    Rover.py
   @brief                   Brief doc for Rover.py
   @details                 Detailed doc for Rover.py 
   @author                  Anthony Vuong, Pedro Muñoz-Rodriguez
   @date                    June 18, 2021
'''
import RPi.gpio as GPIO
import motor.Motor as Motor
import servo.Servo as Servo
import time

##    @var int $dir_forward 
##    An int value representing forward flag
dir_forward = 1

##    @var int $dir_backward
##    An int value representing backward flag
dir_backward = -1

##    @var int $dir_stop 
##    An int value representing stop flag
dir_stop = 0


class Rover:
    def __init__(self, steerPin, throttlePin):
        ''' @brief Rover init function
            @param throttleMotor Motor object for controlling rover throttle
            @param steeringServo Servo object for controlling rover steering
            @param currentStatus Current driving direction of rover
            @param currentSpeed Current driving speed of rover
            @details Initializes rover object with given parameters
            @return none
        '''
        self.throttleMotor = Motor()
        self.steeringServo = Servo()
        self.currentStatus = dir_stop
        self.currentSpeed = 0
        
    def stop(self):
        '''@brief Stop rover
           @param None
           @details Disables all pins, sets currentStatus=0, and set currentSpeed=0
           @return None
        '''
        self.throttleMotor.spin(0)
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
        pass
    
    def steer_left(self):
        '''@brief Turns rover left
           @param None
           @details Moves rover in a left-direction and increases turning degree every call to function
           @return None
        '''
        pass

    
    def controls(self, data):
        '''@brief Rover controls
           @param data An int value indicating specific control
           @details Controls rover direction and speed upon every call
           @return None
        '''
        valid_flag = 0 
         
        if(data == '1'):
            #throttle straight
            self.forward()
        elif(data == '2'):
            #steer right
            self.steer_right()
        elif(data == '3'):
            #throttle back
            self.backward()
        elif(data == '4'):
            #steer left
            self.steer_left()
        elif(data == '5'):
            #STOP
            self.stop()
        else:
            valid_flag = 1
            print("Rover controls(): valid flag : false")

        return valid_flag

        
        
        
            
