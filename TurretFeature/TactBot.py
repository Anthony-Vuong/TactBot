# coding=utf-8

import serial
import RPi.GPIO as GPIO
import turret
import Rover


class TactBot:
    def __init__(self):
        self.tur = turret()
        self.rov = Rover()
    
    def run(self):
        
        comms = serial.Serial("/dev/serial0", baudrate=9600, timeout=0)
        
        while True:
            
            try:
                ctrl = ord(comms.readline())
		                
                
                if ctrl == 9:
                    self.tur.start()

                if ctrl > 0 and ctrl < 6:
                    rover_flag = self.rov.controls(ctrl)
                
                if rover_flag == 1:
                   print("")
                
                
            except KeyboardInterrupt:
                comms.close()
                break
            
#if __name__ == "__main__":



#	t = TactBot()


#	t.run()

#	GPIO.cleanup()

