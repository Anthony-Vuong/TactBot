import pyb, time

class Encoder:
    
    def __init__(self, pinCH1, pinCH2, timer):
        self.timer = pyb.Timer(timer, prescaler = 0, period = 65535)
        self.channel1 = self.timer.channel(1, pyb.Timer.ENC_AB, pin = pinCH1)
        self.channel2 = self.timer.channel(2, pyb.Timer.ENC_AB, pin = pinCH2)
        self.period = 65535
        self.halfPeriod = 65535 / 2
        self.count = 0
        self.currentPos = 0
        self.delta = 0
    
    def update(self):
        self.delta = self.timer.counter() - self.count
        
        #Underflow
        if self.delta < -self.halfPeriod:
            self.delta = self.delta + self.period
        #Overflow
        elif self.delta > self.halfPeriod:
            self.delta = self.delta - self.period
            
        self.currentPos = self.currentPos + self.delta
        self.count = self.timer.counter()            
              
    def get_position(self):
        print("The current position is: " + str(self.currentPos))
        return self.currentPos
    
    def set_position(self, newPosition):
        self.currentPos = newPosition
        print("New position is: " + str(newPosition))
    
    def get_delta(self):
        print("The current delta is: " + str(self.delta))
        return self.delta
       
  