import serial
import RPi.GPIO as GPIO
import turret
import Rover
import time


class TactBot:
    def __init__(self):
        self.tur = turret.Turret()
        self.rov = Rover.Rover()
        self.targetFound = 0
        self.msg = ""
    
    def run(self):
        
        comms = serial.Serial("/dev/serial0", baudrate=9600, timeout=0)
        
        while True:
            
            try:
                ctrl = comms.readline().decode("utf-8", errors='replace')

                if ctrl == "9":
                   self.rov.controls(5)
                   self.targetFound = self.tur.locate()
                   time.sleep(1)
                   if self.targetFound == 1:
                       self.msg += "Target Found. Engage?"
                       comms.write(self.msg.encode())
                       self.msg = ''

                if ctrl == '8':
                    self.tur.laser()
                    time.sleep(3)
                    self.msg += "Target Destroyed"
                    comms.write(self.msg.encode())
                    self.msg = ''

                if ctrl == '7':
                    self.msg += "Fire mission aborted"
                    comms.write(self.msg.encode())
                    self.msg = ''


                else:
                    rover_flag = self.rov.controls(ctrl)

               

            except KeyboardInterrupt:
                comms.close()
                break


if __name__ == "__main__":

    t = TactBot()

    t.run()


    GPIO.cleanup()
