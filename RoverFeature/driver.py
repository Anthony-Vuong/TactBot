'''@file                    driver.py
   @brief                   Brief doc for driver.py
   @details                 Detailed doc for driver.py 
   @author                  Anthony Vuong, Pedro Muñoz-Rodriguez
   @date                    June 18, 2021
'''
import TactBot as TactBot
import Rover as Rover
import serial

def openSerial():
        blue = serial.Serial("/dev/serial0", baudrate=9600, timeout=2)
        return blue    

if __name__=="__main__":
    
    
    port = openSerial()
    
    if not port:
        ##If serialPort cannot not be opened then we need to trip a signal on the rc car to signal communication is bad
        print("Could not open Serial Port")
    else:
        print("Opening serial port is successful")
        
        
    rover = Rover(12 , 13)
    tactbot = TactBot(rover)
    msg = None
    
    while msg != 'Q':
        msg = tactbot.readSerial(port)
        print("Success")
    
    
    
    
    

