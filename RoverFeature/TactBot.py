# coding=utf-8

import serial
import Rover


class TactBot:
    def __init__(self):
        self.rov = Rover.Rover()
    
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
            
if __name__ == "__main__":



	t = TactBot()


	t.run()
