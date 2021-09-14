from __future__ import print_function
from imutils.video import VideoStream
import numpy as np
import argparse 
import imutils
import cv2
import time
import os
import RPi.GPIO as GPIO
import servo

panServo = servo.Servo(27)
tiltServo = servo.Servo(17)
redLed = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(redLed, GPIO.OUT)


class camera:
    
    def __init__(self):
        self.panAngle = 0
        self.tiltAngle = 0

    def posServo(self, servo, angle):
    	servo.calc_angle(angle)
    	print("Positioning servo {0} to {1} degrees".format(servo, angle))
    
    def mapServoPos(self, x, y):
    	
    
    	if(x < 220):
    		self.panAngle += 10
    		if self.panAngle > 140:
    			self.panAngle = 140
    		self.posServo(panServo, self.panAngle)	
    
    	if(x > 280):
            self.panAngle -= 10
            if self.panAngle < 40:
                self.panAngle = 40
                self.posServo(panServo, self.panAngle) 
    
    	if(y < 160):
    		self.tiltAngle += 10
    		if self.tiltAngle > 140:
    			self.tiltAngle = 140
    		self.posServo(tiltServo, self.tiltAngle)
    
    	if(y > 210):
            self.tiltAngle -= 10
            if self.tiltAngle < 40:
                    self.tiltAngle = 40
            self.posServo(tiltServo, self.tiltAngle)
    
    
    def mapObjectPos(self, x, y):
    	print("x0 = {0} and y0 = {1}".format(x, y))
    
    def start(self):
        #print("Camera starting...")
        vs = VideoStream(0).start()
        time.sleep(2.0)
    
        colorLow = (110, 100, 100)
        colorUpp = (130, 255, 255)
    
        GPIO.output(redLed, GPIO.LOW)
        ledOn = False
    
        self.panAngle = 90
        self.tiltAngle = 90
    
        self.posServo(panServo, self.panAngle)
        self.posServo(tiltServo, self.tiltAngle)
    
        while(True):
            
    
            frame = vs.read()
            frame = imutils.resize(frame, width=500)
            frame = imutils.rotate(frame, angle=180)
    
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
            mask = cv2.inRange(hsv, colorLow, colorUpp)
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)
    
    
            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if imutils.is_cv2 else cnts[1]
            center=None
    
            if len(cnts) > 0:
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    
                if radius > 10:
                    cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)
    
                    self.mapServoPos(int(x), int(y))
                    
                    if not ledOn:
                        GPIO.output(redLed, GPIO.HIGH)
                        ledOn = True
    
            elif ledOn:
                GPIO.output(redLed, GPIO.LOW)	
                ledOn = False
    
    
            cv2.imshow("Frame", frame)
            
            key = cv2.waitKey(1) & 0xFF
    
            if key == ord("q"):
                break
    
    
        self.posServo(panServo, 90)
        self.posServo(tiltServo, 90)
        vs.stop()
        GPIO.cleanup()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    c = camera()
    
    c.start()
