'''@file                    Rover.py
   @brief                   Brief doc for Rover.py
   @details                 Detailed doc for Rover.py 
   @author                  Anthony Vuong, Pedro Muñoz-Rodriguez
   @date                    June 18, 2021
'''
import RPi.gpio as GPIO
import motor.Motor as Motor
import servo.Servo as Servo


dir_forward = 1
dir_backward = -1
dir_stop = 0


class Rover:
    def __init__(self, steerPin, throttlePin):
        self.throttleMotor = Motor()
        self.steeringServo = Servo()
        self.currentStatus = dir_stop
        self.currentSpeed = 0
        
    def stop(self):
        self.throttleMotor.spin(0)
        self.currentStatus = dir_stop
        self.currentSpeed = 0

    def forward(self):
        if self.currentStatus == dir_backward or self.currentStatus == dir_stop:
            self.stop()
            time.sleep(1)
            self.currentStatus = dir_forward
        
        self.currentSpeed = self.currentSpeed + 5
        self.throttleMotor.spin(dir_forward, self.currentSpeed)
        
    def backward(self):
        if self.currentStatus == dir_forward or self.currentStatus == dir_stop:
            self.stop()
            time.sleep(1)
            self.currentStatus = dir_backward
        
        self.currentSpeed = self.currentSpeed + 5
        self.throttleMotor.spin(dir_backward, self.currentSpeed)
    
    def steer_right(self):
        pass
    
    def steer_left(self):
        pass

    
    def controls(self, data):
         
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
            print("Command not valid")
            
