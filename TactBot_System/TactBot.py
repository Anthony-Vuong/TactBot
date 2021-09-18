'''@file                    TactBot.py
   @brief                   Brief doc for TactBot.py
   @details                 Detailed doc for TactBot.py 
   @author                  Anthony Vuong, Pedro Munoz-Rodriguez
   @date                    August 12, 2021
'''
import serial
import RPi.GPIO as GPIO
import turret
import Rover
import time


class TactBot:
    ''' @brief This class contains the driver function to run TactBot'''

    def __init__(self):
        ''' @brief Servo init function
            @param steer Steering pin for motor controller
            @param steerAngle pin input signal
            @details Initializes servo driver object with given parameters
            @return none
        '''
        self.tur = turret.Turret()
        self.rov = Rover.Rover()
        self.targetFound = 0
        self.msg = ""
    
    def run(self):
        '''@brief Driver function for TactBot
           @details Initializes the serial port to communicate over UART pins 14/15 tx/rx. With the serial class we read until a null character is 
                    read . Using if we determine what the TactBot based off the app user inputs. Once the user decides to turn off the TactBot system
                    ctrl-c is pressed end the program thus closing UART port and clearing all GPIO pins.
           @return None
        '''
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
