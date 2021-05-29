#!/usr/bin/python

import serial
import RPI.gpio as GPIO

blue = serial.Serial("/dev/serial0", baudrate=9600, timeout=2)


while True:
    data=blue.readline()
   
    print(data)
    
    if(data == '1'):
        #go straight
        pass
    elif(data == '2'):
        #go right
        pass
    elif(data == '3'):
        #go back
        pass
    elif(data == '4'):
        #go left
        pass
    else:
        print("Command not valid")
    
    
    
blue.close()