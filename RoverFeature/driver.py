'''@file                    driver.py
   @brief                   Brief doc for driver.py
   @details                 Detailed doc for driver.py 
   @author                  Anthony Vuong, Pedro Muñoz-Rodriguez
   @date                    June 18, 2021
'''
import TactBot as TactBot
import Rover as Rover
import serial
import sys


def openSerial():
    
    try:
        blue = serial.Serial("/dev/serial0", baudrate=9600)
    except serial.SerialException:
        print("Unsuccesful attempt to open serial0")
        sys.exit(0)
    
    return blue
        

if __name__=="__main__":
    
    
    port = openSerial()
    
    rover = Rover(12 , 13)
    tactbot = TactBot(rover)
    msg = None
    
    while msg != 'Q':
        msg = tactbot.readSerial(port)
        
        tactbot.rover.run(msg)
        
        
        
        
    port.close()
        
    
    
    
    
    

