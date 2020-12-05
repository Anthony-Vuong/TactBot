''''@file main.py

    Encoder Python File '''

import pyb
import os
import sys


class Encoder:
    
    def __init__(self, pin1, pin2, timer):
        
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
           
        self.currentReading = 0
        self.previousReading = 0
        self.currentPosition = 0
        self.delta = 0
        self.EncTimer.counter(0) 
         
    def update(self):
        self.currentPosition = self.currentPosition + self.delta
      
    def get_position(self):
        return self.currentPosition
    
    def set_position(self, newPosition):
        self.EncTimer.counter(newPosition)
        
    def get_delta(self):
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