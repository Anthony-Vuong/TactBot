import sys
import os
from motor import MotorDriver
from encoder import Encoder
import pyb
import utime

## @file main.py
#  Control loop driver
#
#  @author Anthony Vuong
#  @date May 12, 2020
#  @note https://bitbucket.org/avuong04/me405_labs/src/master/LAB_3/
#  @note https://www.youtube.com/watch?v=6Y9zB3bX2XA
#

## Main method
#  Method used to control loop. User asked for gain and program for float type.  If float type not found, the program prompts user invalid input and exits.
def main():
    
     
    ##  Variable to hold controller object. KP or gain is initially set to 1.#  Setpoint is set to 1000.
    con1 = Controller(1, 1000)
     
    ##  Variable to hold motor object
    #  Pin PA10 for ENABLE pin of motor.
    #  Pin PB4 for M+ of motor component.
    #  Pin PB5 for M- of motor component.
    #  Timer 3 is compatible with these pins.
    motor1 = MotorDriver('PA10', 'PB4', 'PB5', 3)
    
    ##  Variable to hold encoder object
    #  Pin PB6 for channel 1 of encoder.
    #  Pin PB7 for channel 2 of encoder.
    #  Timer 4 is compatible with these pins.
    enc1 = Encoder('PB6' , 'PB7', 4)
    
    ##  Variable constant for 1 second.
    time = 1000
    
    motor1.enable()
    
    while True:
        try:
            
            ##  Variable to hold user input, can be >0 and < 1.
            gain = float(input("Enter gain value: "))
            
            
            ## Variable to hold real time
            start_time = utime.ticks_ms()
            
            con1.setGain(gain)
            enc1.reset()
            con1.emptyList()
            while (start_time + time) > utime.ticks_ms():
                con1.addToTimeList(int(utime.ticks_ms()) - start_time)
                enc1.get_delta()
                utime.sleep_ms(10)
                enc1.update()
                
               
                ##  Variable to position of motor in ticks
                pos = enc1.get_position()
                con1.addToPositionList(pos)
                
                ##  Variable to hold newly calculated PWM signal
                pwm = con1.adjustSig(pos)
                motor1.set_duty(pwm)
            
            con1.printList()
            con1.emptyList()
            print("List printed and emptied")
        except ValueError:
            print("Not a valid input")
            break;

           
        
    motor1.disable()



    