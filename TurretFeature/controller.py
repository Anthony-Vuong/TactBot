## @file controller.py
#  Controller Driver 
#
#  Details
#  @author Anthony Vuong
#  @date May 12, 2020

## Controller class
#
#
class Controller:
    '''Methods and parameters needed to control system '''
    
    ## 
    #
    # @param start_time real time clock
    # @param kp gain variable 
    # @param setPoint number of ticks 
    # @param time_list[] list of time points
    # @param pos_list[] list of position points
    #
    # Method used to initialize the Controller class.
    def __init__(self, kp, setpoint):
        
        self.start_time = int(utime.ticks_ms())
        self.kp = kp
        self.setPoint= setpoint
        self.time_list = []
        self.pos_list = []
      
    ##Adjusting pwm method
    #
    def adjustSig(self, position):
        self.error = self.setPoint - position
        self.output = self.kp * self.error

        # saturation
        if (self.output > 100) :
            self.output = 100
        elif (self.output < -100) :
            self.output = -100

        return self.output
    
    ##Printing time and position list method
    def printList(self):
        '''A method to print time and position elements '''
        print("[")
        for i in range(len(self.time_list)):
            print(str(self.time_list[i]), end=", ")
        print("]")
        print("\n[")
        for i in range(len(self.pos_list)):
            print(str(self.pos_list[i]), end = ", ")
        print("]")
 
    ## Clear the lists method
    def emptyList(self):
        ''' A method to clear time and position lists'''
        self.time_list = []
        self.pos_list = []
        self.start_time = int(utime.ticks_ms())
    
    def addToPositionList(self, position):
        '''A method to add an element to position list'''
        self.pos_list.append(position)
        
    def addToTimeList(self, timeLeft):
        '''A method to add an element to time list'''
        self.time_list.append(timeLeft)
        
    def setGain(self, newGain):
        '''A method to set a new gain'''
        self.kp = newGain
    
    def setSetPoint(self, newSP):
        '''A method to set a set point'''
        self.set = newSP