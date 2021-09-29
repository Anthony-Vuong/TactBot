'''@file                    camera.py
   @brief                   Brief doc for camera.py
   @details                 Detailed doc for camera.py. This code could not be without the help of author mjrovai
                            whose instructable can be found here: https://www.instructables.com/Automatic-Vision-Object-Tracking/
                            Our code is an adaption of the author's original code. All original code belongs to the author.
   @author                  Anthony Vuong, Pedro Munoz-Rodriguez
   @date                    September 18, 2021
'''
from __future__ import print_function
from imutils.video import VideoStream
import imutils
import cv2
import time
import RPi.GPIO as GPIO
import servo



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)



class Camera:
    ''' @brief      This class allows TactBot to utilize computer vision library OpenCV as well as the RPI camera streaming
                    services. With the ability to locate assigned targets, TactBot can be on the offensive.
    '''
    
    def __init__(self):
        ''' @brief camera init function
            @param panAngle The initial pan angle for pan tilt hat
            @param tiltAngle The initial tilt angle for pan tilt hat
            @param located The current status of target located
            @param temp Keeps track of how many times the pan tilt has been on target
            @param temp2 Keeps track of how many times the pan tilt has been off target
            @param prevX The previous recorded pan angle
            @param prevY The previous recorded tilt angle
            @param pan Setting the up the GPIO pin for pan servo
            @param panServo A servo object for panning the camera
            @param tilt Setting the up the GPIO pin for tilt servo
            @param tiltServo A servo object for tilting the camera
            @param colorLow Lower range value for BGH color: dark purple   
            @param colorUpp Upper range value for BGH color: dark purple                     
            @details Initializes camera object with given object variables
            @return none
        '''
        self.panAngle = 90
        self.tiltAngle = 90
        self.located = 0
        self.temp = 0
        self.temp2 = 0
        self.prevX = 0
        self.prevY = 0
        self.pan = GPIO.setup(19, GPIO.OUT)
        self.panServo = servo.Servo(19, self.panAngle, True)
        self.tilt = GPIO.setup(26, GPIO.OUT)
        self.tiltServo = servo.Servo(26, self.tiltAngle, True)
        self.colorLow = (110, 100, 100)
        self.colorUpp = (130, 255, 255)

    def posServo(self, servo, angle):
        '''@brief Positioning servo
           @param servo The desired servo 
           @param angle The desired servo angle
           @details Changes the servo's angle based on calculated pwm and prints new angle to screen
           @return None
        '''
        servo.turret_angle(angle)
        print("Positioning servo {0} to {1} degrees".format(servo.turretServoPin, angle))
    
    def mapServoPos(self, x, y):
        '''@brief Increments/decrements servo angles
           @param x The pan angle
           @param y The tilt angle
           @details Calculates the servo angle to keep object centered
           @return None
        '''

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
        '''@brief Increments/decrements servo angles
           @param x The pan angle
           @param y The tilt angle
           @details Prints the servo angle to keep object centered
           @return None
        '''
        print("x0 = {0} and y0 = {1}".format(x, y))
    
    def start(self):
        '''@brief Camera and openCV driver
           @details This function starts off by initiating the video stream of Pi Cam. Following this we set the initial pan tilt 
                    angles so Pi Cam is facing forward. In an endless loop, openCV is configured to frame the Pi Cam capture in 
                    specified parameters. Then an computer vision overlay is configured to detect the color dark purple - called a mask.
                    With frame and mask setup openCV is ready to detect color and pinpoint the area of interest using contours.
                    Using openCV tools and with the setup specified, a purple cup is ready to be detected. Once detected a red dot with
                    a yellow outer circle is drawn in the center of mask. Using coordinates from frame and color detection of mask
                    we can move pan tilt hat to center object in front of camera. 
           @return True or false, if object is detected or not.
        '''
        
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


                    if self.prevY == int(y) and self.prevX == int(x):
                        self.temp = self.temp + 1
                        if self.temp == 2:
                            self.temp = 0
                            self.located = 1
                            break

                    self.prevX = int(x)
                    self.prevY = int(y)

                    

                    if not ledOn:
                        ledOn = True
    
            elif ledOn:
                self.temp2 = self.temp2 + 1
            
                ledOn = False
                if self.temp2 == 100:
                   self.temp2 = 0
                   break
    
    
            cv2.imshow("Frame", frame)
            
            key = cv2.waitKey(1) & 0xFF
    
            if key == ord('a'):
                break
    
    
        #self.posServo(self.panServo, 90)
        #self.posServo(self.tiltServo, 90)
        vs.stop()
        #GPIO.cleanup()
        cv2.destroyAllWindows()

        return self.located

#if __name__ == "__main__":
#    c = camera()
    
#    c.start()
