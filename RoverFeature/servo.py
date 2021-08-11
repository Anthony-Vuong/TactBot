import RPi.GPIO as GPIO


class Servo:
    def __init__(self):
        self.spinPin = GPIO(12, GPIO.OUT)