import time
import board
import neopixel




class flashlight:
    def __init__(self):
        self.numPixels = 10
        self.pixelPin = board.D18
        self.currentBrightness = 0.1
        self.pixels = (self.pixelPin, self.numPixels, self.brightness)
        
    
    def flash(self, cycles=3):
        #white light flash on and off repeatedly
        i = 0
        while i < cycles:
            self.on()
            time.sleep(0.5)
            self.off()
    
    def on(self):
        #white light stays on
        for i in range(10):
            self.pixels[i] = (255, 255, 255)
    
    def off(self):
        #white light stays off
        for i in range(10):
            self.pixels[i] = (0, 0, 0)
    
    def emergencyLigts(self):
        #flashes yellow when stopped in dark area or potential traffic hazard
        pass
    
    def medicalLights(self):
        #Flashed red and white lights like an ambulance
        pass
    
    
    def lightControls(self, ctrl):
        if ctrl == 21:
            self.on()
        elif ctrl == 22:
            self.off()
        elif ctrl == 23:
            self.flash()
        elif ctrl == 24:
            self.emergencyLigts()
        elif ctrl == 25:
            self.medicalLights()
        else:
            print("Ctrl not recognized")