import RPi.GPIO as GPIO
import time
from pynput import keyboard
import os

IN1 = 24
IN2 = 23
ENA = 25
temp1 = 1


GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
p = GPIO.PWM(ENA, 1000)

p.start(25)
print("Starting motor is LOW and Forward")


while True:
    try:
        key = input()
        
        if x=='r':
            print("run")
            if(temp1==1):
                GPIO.output(IN1,GPIO.HIGH)
                GPIO.output(IN2,GPIO.LOW)
                print("forward")
                x='z'
            else:
                GPIO.output(IN1,GPIO.LOW)
                GPIO.output(IN2,GPIO.HIGH)
                print("backward")
                x='z'


        elif x=='s':
            print("stop")
            GPIO.output(IN1,GPIO.LOW)
            GPIO.output(IN2,GPIO.LOW)
            x='z'

        elif x=='f':
            print("forward")
            GPIO.output(IN1,GPIO.HIGH)
            GPIO.output(IN2,GPIO.LOW)
            temp1 = 1
            x='z'

        elif x=='b':
            print("backward")
            GPIO.output(IN1,GPIO.LOW)
            GPIO.output(IN2,GPIO.HIGH)
            temp1 = 0
            x='z'

        elif x=='l':
            print("low")
            p.ChangeDutyCycle(25)
            x='z'

        elif x=='m':
            print("medium")
            p.ChangeDutyCycle(50)
            x='z'

        elif x=='h':
            print("high")
            p.ChangeDutyCycle(75)
            x='z'
        
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        break
