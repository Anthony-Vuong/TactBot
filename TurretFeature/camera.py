from __future__ import print_function
from imutils.video import VideoStream
#from collections import deque
import numpy as np
import argparse 
import imutils
import cv2
import time
import os
import RPi.GPIO as GPIO

panServo = 27
tiltServo = 17
redLed = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(redLed, GPIO.OUT)

def posServo(servo, angle):
	os.system("python panTiltTest.py " + str(servo) + " " + str(angle))
	print("Positioning servo {0} to {1} degrees".format(servo, angle))

def mapServoPos(x, y):
	global panAngle
	global tiltAngle

	if(x < 220):
		panAngle += 10
		if panAngle > 140:
			panAngle = 140
		posServo(panServo, panAngle)	

	if(x > 280):
                panAngle -= 10
                if panAngle < 40:
                        panAngle = 40
                posServo(panServo, panAngle) 

	if(y < 160):
		tiltAngle += 10
		if tiltAngle > 140:
			tiltAngle = 140
		posServo(tiltServo, tiltAngle)

	if(y > 210):
                tiltAngle -= 10
                if tiltAngle < 40:
                        tiltAngle = 40
                posServo(tiltServo, tiltAngle)


def mapObjectPos(x, y):
	print("x0 = {0} and y0 = {1}".format(x, y))

def start():
    print("Camera starting...")
    vs = VideoStream(0).start()
    time.sleep(2.0)

    colorLow = (110, 100, 100)
    colorUpp = (130, 255, 255)

    GPIO.output(redLed, GPIO.LOW)
    ledOn = False

    global panAngle
    panAngle = 90
    global tiltAngle
    tiltAngle = 90

    posServo(panServo, panAngle)
    posServo(tiltServo, tiltAngle)

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

                mapServoPos(int(x), int(y))
                
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


    posServo(panServo, 90)
    posServo(tiltServo, 90)
    vs.stop()
    GPIO.cleanup()
    cv2.destroyAllWindows()
