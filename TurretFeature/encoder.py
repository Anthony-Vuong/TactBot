''''@file main.py

    Encoder Python File '''

import pyb
import os
import sys
## Encoder driver object
#
#  Details
#  @author Anthony Vuong
#  @date May 3, 2020
#  @note https://bitbucket.org/avuong04/me405_labs/src/master/LAB_2/

class Encoder:
    '''Methods and parameters needed to operate motor encoder '''
    
    def __init__(self, pin1, pin2, timer):
        '''constructor init()which does the setup, given appropriate parameters such as
        which pins and timer to use.
        @param pin1 for channel 1
        @param pin2 for channel 2
        @param timer for correct pin inputs
        '''
        if pin1 == 'PB6' and pin2 == 'PB7' and timer == 4:
            self.pin_IN1 = pyb.Pin(pin1, mode = pyb.Pin.AF_PP, af = pyb.Pin.AF2_TIM4)       
            self.pin_IN2 = pyb.Pin(pin2, mode = pyb.Pin.AF_PP, af = pyb.Pin.AF2_TIM4)
            self.EncTimer = pyb.Timer(timer, prescaler = 0, period = 0xFFFF)
            self.EncChannel = self.EncTimer.channel(2, pyb.Timer.ENC_AB)
        elif pin1 == 'PC6' and pin2 == 'PC7' and timer == 8:
            self.pin_IN1 = pyb.Pin(pin1, mode = pyb.Pin.AF_PP, af = pyb.Pin.AF3_TIM8)       
            self.pin_IN2 = pyb.Pin(pin2, mode = pyb.Pin.AF_PP, af = pyb.Pin.AF3_TIM8)
            self.EncTimer = pyb.Timer(timer, prescaler = 0, period = 0xFFFF)
            self.EncChannel = self.EncTimer.channel(3, pyb.Timer.ENC_AB)
        else:
            print("Not valid pin inputs. Use pins ")
           
        ''' @param For timer reading '''
        self.currentReading = 0
        ''' @param Previous timer reading '''
        self.previousReading = 0
        ''' @param For encoder current position '''
        self.currentPosition = 0
        ''' @param The Encoder's change of position '''
        self.delta = 0
        ''' @param Set the timer to 0 position '''
        self.EncTimer.counter(0) 
         
    def update(self):
        '''A method update()which, when called regularly, updates the recorded position of the encoder.'''
        self.currentPosition = self.currentPosition + self.delta
      
    def get_position(self):
        '''A method getposition()which returns the most recently updated position of the encoder.'''
        return self.currentPosition
    
    def set_position(self, newPosition):
        '''A method setposition()which resets the position to to a specified value.'''
        self.EncTimer.counter(newPosition)
        
    def get_delta(self):
        '''A method getdelta()which returns the difference in recorded position between the two most recent calls to update()'''
        self.previousReading = self.currentReading
        self.currentReading = self.EncTimer.counter()
        self.delta = self.currentReading - self.previousReading
        
        if self.delta < -32768:
            self.delta += 65536
        elif self.delta > 32768:
            self.delta -= 65536
            
        return self.delta
"""
if __name__ == '__main__':
    
    enc1 = Encoder('PB6' , 'PB7', 4)
        
        
    while(1):
        
        enc1.update()
        print(enc1.get_delta())
        print(enc1.get_position())

        
        pyb.delay(5000)
        
        enc1.update()
        print(enc1.get_delta())
        print(enc1.get_position())
        
        pyb.delay(5000)

    '''pin_IN1 = pyb.Pin('PB6', mode = pyb.Pin.AF_PP, af = pyb.Pin.AF2_TIM4)       
    pin_IN2 = pyb.Pin('PB7', mode = pyb.Pin.AF_PP, af = pyb.Pin.AF2_TIM4)  
    tim = pyb.Timer(4, prescaler = 0, period = 0xFFFF)
    chnl = tim.channel(2, pyb.Timer.ENC_AB)
    
    while(tim.counter() >= 0):
        pyb.delay(5000)
        t1 = tim.counter()
        c1 = chnl.capture()

        print("Channel: " + str(c1))
        print("Timer: " + str(t1))
        print("Timer RESET: ")

        pyb.delay(5000)
        t1 = tim.counter(0)
        print("Timer: " + str(t1))
        
        '''
 """