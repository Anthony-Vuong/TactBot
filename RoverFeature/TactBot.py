'''@file                    changeUtil.py
   @brief                   Brief doc for serialBot.py
   @details                 Detailed doc for serialBot.py 
   @author                  Anthony Vuong, Pedro Muñoz-Rodriguez
   @date                    June 18, 2021
'''

import serial
import RPI.gpio as GPIO








    
    
    
class TactBot:
    def __init__(self, rover, turret):
        self.rover = rover
        self.turret = turret
    
    
    def readSerial(self):
        blue = serial.Serial("/dev/serial0", baudrate=9600, timeout=2)
        
        while True:
    
            try:
                data=blue.readline()
            
                print(data)
                
                if(data == '1'):
                    #throttle straight
                    self.rover.increaseSpeed()
                elif(data == '2'):
                    #steer right
                    self.rover.steerRight()
                elif(data == '3'):
                    #throttle back
                    self.rover.decreaseSpeed()
                elif(data == '4'):
                    #steer left
                    self.rover.steerLeft()
                elif(data == '5'):
                    #STOP
                    self.rover.stop()
                else:
                    print("Command not valid")
                    
                    
                #CHANGE SPEED
                throttle.ChangeDutyCycle(direction)
                #CHANGE DIRECTION
                steering.ChangeDutyCycle(steer)
                
            except KeyboardInterrupt:
                break
        
        
        blue.close()



        
        
        
        
        
    
        
        
        
        
        
        
        