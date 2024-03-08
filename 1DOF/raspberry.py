import RPi.GPIO as GPIO
import time
from pynput import keyboard
import os

IN1 = 24
IN2 = 23
ENA = 25
TEST = 16
temp1 = 1


GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(TEST, GPIO.OUT)
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(TEST, GPIO.HIGH)    # Debug RaspberryPi


p = GPIO.PWM(ENA, 1000)

p.start(25)
print("Starting motor is LOW and Forward")


while True:
    try:
        key = input()

        if key=='r':
            print("run")
            if(temp1==1):
                GPIO.output(IN1,GPIO.HIGH)
                GPIO.output(IN2,GPIO.LOW)
                print("forward")
                key='z'
            else:
                GPIO.output(IN1,GPIO.LOW)
                GPIO.output(IN2,GPIO.HIGH)
                print("backward")
                key='z'


        elif key=='s':
            print("stop")
            GPIO.output(IN1,GPIO.LOW)
            GPIO.output(IN2,GPIO.LOW)
            key='z'

        elif key=='f':
            print("forward")
            GPIO.output(IN1,GPIO.HIGH)
            GPIO.output(IN2,GPIO.LOW)
            temp1 = 1
            key='z'

        elif key=='b':
            print("backward")
            GPIO.output(IN1,GPIO.LOW)
            GPIO.output(IN2,GPIO.HIGH)
            temp1 = 0
            key='z'

        elif key=='l':
            print("low")
            p.ChangeDutyCycle(25)
            key='z'

        elif key=='m':
            print("medium")
            p.ChangeDutyCycle(50)
            key='z'

        elif key=='h':
            print("high")
            p.ChangeDutyCycle(75)
            key='z'
        else:
            print("<<<  wrong data  >>>")
        
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        break
