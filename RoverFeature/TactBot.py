'''@file                    TactBot.py
   @brief                   Brief doc for serialBot.py
   @details                 Detailed doc for serialBot.py 
   @author                  Anthony Vuong, Pedro Muñoz-Rodriguez
   @date                    June 18, 2021
'''

import serial
import Rover
import Turret

class TactBot:
    def __init__(self, rover, turret):
        self.rover = rover
        self.turret = turret
        
    def run(self):
        
        comms = serial.Serial("/dev/serial0", baudrate=9600)
        
        while True:
            
            try:
                ctrl = comms.readline()
                
                rover_flag = Rover.controls(ctrl)
                
                if rover_flag == 1:
                    print("Send message to app")
                
                
                
                
                
                
                
                
                
            except KeyboardInterrupt:
                break
            