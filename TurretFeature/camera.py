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



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)



class camera:
    
    def __init__(self):
        self.panAngle = 0
        self.tiltAngle = 0
        self.panServo = servo.Servo(19, 8, True)
        self.tiltServo = servo.Servo(26, 8, True)
        self.ledPin = 21
        self.redLed = GPIO.setup(self.ledPin, GPIO.OUT)
        self.colorLow = (110, 100, 100)
        self.colorUpp = (130, 255, 255)

    def posServo(self, servo, angle):
    	servo.calc_angle(angle)
    	print("Positioning servo {0} to {1} degrees".format(servo.servoPin, angle))
    
    def mapServoPos(self, x, y):
    	
    
    	if(x < 220):
    		self.panAngle += 10
    		if self.panAngle > 140:
    			self.panAngle = 140
    		self.posServo(self.panServo, self.panAngle)	
    
    	if(x > 280):
            self.panAngle -= 10
            if self.panAngle < 40:
                self.panAngle = 40
                self.posServo(self.panServo, self.panAngle) 
    
    	if(y < 160):
    		self.tiltAngle -= 10
    		if self.tiltAngle > 140:
    			self.tiltAngle = 140
    		self.posServo(self.tiltServo, self.tiltAngle)
    
    	if(y > 210):
            self.tiltAngle += 10
            if self.tiltAngle < 40:
                    self.tiltAngle = 40
            self.posServo(self.tiltServo, self.tiltAngle)
    
    
    def mapObjectPos(self, x, y):
    	print("x0 = {0} and y0 = {1}".format(x, y))
    
    def start(self):
        #print("Camera starting...")
        vs = VideoStream(0).start()
        time.sleep(2.0)
    
        ledOn = False
    
        self.panAngle = 90
        self.tiltAngle = 90
    
        self.posServo(self.panServo, self.panAngle)
        self.posServo(self.tiltServo, self.tiltAngle)
    
        while(True):
            
    
            frame = vs.read()
            frame = imutils.resize(frame, width=500)
            frame = imutils.rotate(frame, angle=180)
    
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
            mask = cv2.inRange(hsv, self.colorLow, self.colorUpp)
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
                        GPIO.output(self.redLed, GPIO.HIGH)
                        ledOn = True
    
            elif ledOn:
                GPIO.output(self.redLed, GPIO.LOW)	
                ledOn = False
    
    
            cv2.imshow("Frame", frame)
            
            key = cv2.waitKey(1) & 0xFF
    
            if key == ord("q"):
                break
    
    
        self.posServo(self.panServo, 90)
        self.posServo(self.tiltServo, 90)
        vs.stop()
        GPIO.cleanup()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    c = camera()
    
    c.start()
