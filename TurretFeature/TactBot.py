# coding=utf-8

import serial
import RPi.GPIO as GPIO
import turret
import Rover
import time


class TactBot:
    def __init__(self):
        self.tur = turret()
        self.rov = Rover()
        self.targetFound = 0
        self.msg = ""
    
    def run(self):
        
        comms = serial.Serial("/dev/serial0", baudrate=9600, timeout=0)
        
        while True:
            
            try:
                ctrl = ord(comms.readline())
		                
                
                if ctrl == 9:
                   self.rov.controls(5)
                   self.targetFound = self.tur.locate()
                   if self.targetFound == 1:
                       self.msg += "Target Found. Engage?"
                       comms.write(self.msg.encode())
                       self.msg = ""

                if ctrl == 8:
                    self.tur.laser()
                    time.sleep(3)
                    self.msg += "Target Destroyed"
                    comms.write(self.msg.encode())
                    self.msg = ""

                if ctrl == 7:
                    self.msg += "Fire mission aborted"
                    comms.write(self.msg.encode())
                    self.msg = ""

                if ctrl > 0 and ctrl < 6:
                    rover_flag = self.rov.controls(ctrl)

                if rover_flag == 1:
                    print("")


            except KeyboardInterrupt:
                comms.close()
                break

if __name__ == "__main__":



	t = TactBot()


	t.run()

	GPIO.cleanup()

