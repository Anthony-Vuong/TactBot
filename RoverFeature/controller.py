import time

class Controller:
    '''Methods and parameters needed to control system '''
    
    ## 
    #
    # @param start_time real time clock
    # @param kp gain variable
    # @param kd derivative gain variable
    # @param ki integral gain variable
    # @param setPoint number of ticks 
    # @param time_list[] list of time points
    # @param pos_list[] list of position points
    #
    # Method used to initialize the Controller class.
    def __init__(self, motor, encoder, kp=1, kd=1, ki=1):
        
        self.kp = kp
        self.kd = kd
        self.ki = ki
        self.motor = motor
        self.encoder = encoder
        self.setPoint = None
        self.error = 0
        self.previousError = 0
        self.sumError = 0
               
    def run(self, newPosition):
                
        self.setPoint = newPosition
        self.motor.enable()
        
        #Ask for gain values - tweaking gain values
        #.26
        self.kp = float(input("Enter proportional gain(KP): "))
        #.020
        self.kd = float(input("Enter derivative gain(KD): "))
        #The closer to 0 the better - feel like there's something missing.
        self.ki = float(input("Enter integral gain(KI): "))
        
        while True:
            
            try:               
                self.encoder.update()
                self.adjustSig(self.encoder.get_position())
                          
            except KeyboardInterrupt:
                print("Exiting system control")
                break;
        
        self.motor.disable()

        
      
    ##Adjusting pwm method
    #
    def adjustSig(self, position):
        #Error - difference between desired point and current point
        self.error = self.setPoint - position
        
        #Set sum of errors for derivative calculation
        self.sumError += self.error
    
        #New adjust pwm percentage, must be a value between 0 and 1
        output = (self.kp * self.error) + (self.kd * self.previousError) + (self.ki * self.sumError)
        print(output)
        #Filters bad pwm calculations, no less than 0, no more than 1
        pwm = output
        if pwm > 100:
            pwm = 100
        elif pwm < -100:
            pwm = -100
        #Set motor to new pwm
        self.motor.set_duty(pwm)
        
        #Rest encoder to new position value
        self.encoder.set_position(0)
        
        #Let system sleep and sample encoder tick values
        #time.sleep(1)
        
        #Set previous error for integral calculations
        self.previousError = self.error
      
    def setKPGain(self, newGain):
        '''A method to set a new gain'''
        self.kp = newGain
        
    def setKDGain(self, newGain):
        '''A method to set a new gain'''
        self.kd = newGain
    
    def setKDGain(self, newGain):
        '''A method to set a new gain'''
        self.ki = newGain
    
    def setSetPoint(self, newSP):
        '''A method to set a set point'''
        self.set = newSP