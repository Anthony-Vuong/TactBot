#!/usr/bin/python

import serial, sys
import RPI.gpio as GPIO

blue = serial.Serial("/dev/serial0", baudrate=9600, timeout=2)

#STEERING PWM PIN
steering = GPIO.PWM(12, 100)
steering.start(0)

#THROTTLE PWM PIN
throttle = GPIO.PWM(13, 100)
throttle.start(0)

#INCREMENT VARIABLES FOR DIRECTION AND SPEED
steer = 0
direction = 0


while True:
    
    try:
        data=blue.readline()
       
        print(data)
        
        if(data == '1'):
            #throttle straight
            direction += 1
        elif(data == '2'):
            #steer right
            steer += 1
        elif(data == '3'):
            #throttle back
            direction -= 1
        elif(data == '4'):
            #steer left
            steer -= 1
        elif(data == '5'):
            #STOP
            direction = 0
        else:
            print("Command not valid")
            
            
        #CHANGE SPEED
        throttle.ChangeDutyCycle(direction)
        #CHANGE DIRECTION
        steering.ChangeDutyCycle(steer)
        
    except KeyboardInterrupt:
        sys.exit(0)
    
    
    
blue.close()