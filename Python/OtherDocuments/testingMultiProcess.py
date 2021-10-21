from multiprocessing import Process
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led1 = 23
led2 = 24

motorA = 17
motorA_in1 = 27
motorA_in2 = 22
motorB = 26
motorB_in1 = 5
motorB_in2 = 6


def motorMove(enPin, in1, in2, duty, t):
    GPIO.setup(enPin, GPIO.OUT)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    p = GPIO.PWM(enPin, 1000)
    p.start(0)
    
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    p.ChangeDutyCycle(duty)
    
    time.sleep(t)
    
    GPIO.output(in2, GPIO.LOW)

    
def ledon(led, t):
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(led, GPIO.LOW)

    
    
if __name__ == '__main__':
    jobs = []

    p1 = multiprocessing.Process(target=motorMove, args=(motorA, motorA_in1, motorA_in2,  10, 5))
    jobs.append(p1)
    p1.start()
    
    p2 = multiprocessing.Process(target=motorMove, args=(motorB, motorB_in1, motorB_in2,  20, 3))
    jobs.append(p2)
    p2.start()
    
    p1.join() 
    p2.join()
    
    
    GPIO.cleanup() 
        

    

