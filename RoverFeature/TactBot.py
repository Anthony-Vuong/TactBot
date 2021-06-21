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
        
    def controls(self, data):
        
        while True:
    
            try:
            
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
                    
                    
                self.rover.run()
                
            except KeyboardInterrupt:
                break
        
        
        blue.close()



        
        
        
        
        
    
        
        
        
        
        
        
        