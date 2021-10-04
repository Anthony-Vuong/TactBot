import serial
import RPi.GPIO as GPIO
import turret
import Rover
#import time


safe = "Green"
onAlert = "Yellow"
inDanger = "Red"

class TactBot:
    def __init__(self):
        self.tur = turret.Turret()
        self.rov = Rover.Rover()
        self.targetFound = 0
        self.msg = ""
        self.currentCtrl = None
        self.comms = serial.Serial("/dev/serial0", baudrate=9600, timeout=0)
        self.awareness = safe
        
    
    def getAwareness(self):
        return self.awareness
        
    def decodeMessage(self, msg):
        #expects a 2 digit number
        #list() turns the message which is a string into a list
        self.currentCtrl = list(msg)
    
    
    #assign 0 to rover controls
    #assign 1 to turret controls
    def TactBotControls(self, msgList):
        if msgList[0] == 0:
            #rover
            self.rov.controls(msgList[1])
        elif msgList[0] == 1:
            #turret
            self.msg = self.tur.controls(msgList[1], self.rov)
            self.comms.write(self.msg.encode())

        else:
            print("{0}: Ctrl not recoginized", msgList)
        
    
    
    def run(self):
        
        while True:
            
            try:
                
                #Use serial python to read message from RPI port serial0 
                ctrl = self.comms.readline().decode("utf-8", errors='replace')
                
                #turn the string into a list
                #the first element branches into 2 control choices: rover or turret
                self.currentCtrl = self.currentCtrl(ctrl)
                
                #sends the ctrl List to tactbot command control
                self.TactBotControls(self.currentCtrl())


            except KeyboardInterrupt:
                self.comms.close()
                break


if __name__ == "__main__":

    t = TactBot()

    t.run()


    GPIO.cleanup()
