'''@file                    TactBot.py
   @brief                   Brief doc for serialBot.py
   @details                 Detailed doc for serialBot.py 
   @author                  Anthony Vuong, Pedro Muñoz-Rodriguez
   @date                    June 18, 2021
'''

import serial

class TactBot:
    def __init__(self, rover, turret):
        self.rover = rover
        self.turret = turret
        
        
    def readSerial(self, serialPort):
        data = serialPort.readline()
        return data
        

        