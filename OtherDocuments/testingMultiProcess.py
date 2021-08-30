from multiprocessing import Process
import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led1 = 23
led2 = 24


def ledon(led, t):
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.HIGH)
    time.sleep(t)
    GPIO.output(led, GPIO.LOW)

    
    
if __name__ == '__main__':
    jobs = []

    p1 = multiprocessing.Process(target=ledon, args=(led1, 2,))
    jobs.append(p1)
    p1.start()
    
    p2 = multiprocessing.Process(target=ledon, args=(led2, 3,))
    jobs.append(p2)
    p2.start()
    
    p1.join() 
    p2.join()
    
    
    GPIO.cleanup()
        

    

