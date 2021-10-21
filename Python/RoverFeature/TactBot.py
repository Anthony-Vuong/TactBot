
import serial
import Rover
import RPi.GPIO as GPIO


class TactBot:
    def __init__(self):
        self.rov = Rover.Rover()
    
    def run(self):
        
        comms = serial.Serial("/dev/serial0", baudrate=9600, timeout=0)
        
        while True:
            
            try:
                ctrl = comms.readline()
		                

                rover_flag = self.rov.controls(ctrl)
                
                #if rover_flag == 1:
                   # print("Send message to app")
                
                
            except KeyboardInterrupt:
                comms.close()
		print("break")
                break
            
if __name__ == "__main__":



	t = TactBot()


	t.run()

	GPIO.cleanup()

