import time
import board
import neopixel




class flashlight:
    def __init__(self):
        self.numPixels = 1
        self.pixelPin = board.D18
        self.pixels = (self.pixelPin, self.numPixels)
        
    
    def flash(self):
        #white light flash on and off repeatedly
        pass
    
    def on(self):
        #white light stays on
        pass
        
    
    def off(self):
        #white stays off
        pass
    
    def emergencyLigts(self):
        #flashes yellow when stopped in dark area or potential traffic hazard
        pass
    
    def medicalLights(self):
        #Flashed red and white lights like an ambulance
        pass
    
    
    def lightControls(self, ctrl):
        if ctrl == 11:
            self.on()
        elif ctrl == 12:
            self.off()
        elif ctrl == 13:
            self.flash()
        elif ctrl == 14:
            self.emergencyLigts()
        elif ctrl == 15:
            self.medicalLights()
        else:
            print("Ctrl not recognized")