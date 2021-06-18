'''@file                    changeUtil.py
   @brief                   Brief doc for serialBot.py
   @details                 Detailed doc for serialBot.py 
   @author                  Anthony Vuong, Pedro Muñoz-Rodriguez
   @date                    June 18, 2021
'''

import serial
import RPI.gpio as GPIO

blue = serial.Serial("/dev/serial0", baudrate=9600, timeout=2)

#STEERING PWM PIN
steering = GPIO.PWM(12, 50)
steering.start(0)

#THROTTLE PWM PIN
throttle = GPIO.PWM(13, 50)
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
            steer = 0
        else:
            print("Command not valid")
            
            
        #CHANGE SPEED
        throttle.ChangeDutyCycle(direction)
        #CHANGE DIRECTION
        steering.ChangeDutyCycle(steer)
        
    except KeyboardInterrupt:
        break
    
    
    
blue.close()