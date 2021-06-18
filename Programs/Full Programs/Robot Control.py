'''
MS Robotics Camp 2021
Meghan Jimenez
Forward, Backward, Left, Right robot control
'''

import time
import board
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwmLeft = pwmio.PWMOut(board.A3, frequency=50)
pwmRight = pwmio.PWMOut(board.A4, frequency=50)

# Create a servo object, my_servo.
leftServo = servo.ContinuousServo(pwmLeft)
rightServo = servo.ContinuousServo(pwmRight)

def backward():
    print("backward")
    leftServo.throttle = 1.0
    rightServo.throttle = -1.0
    time.sleep(2.0)
    print("stop")
    leftServo.throttle = 0.0
    rightServo.throttle = 0.0
    time.sleep(2.0)
    
def forward():
    print("forward")
    leftServo.throttle = -1.0
    rightServo.throttle = 1.0
    time.sleep(2.0)
    print("stop")
    leftServo.throttle = 0.0
    rightServo.throttle = 0.0
    time.sleep(2.0)
    
def left():
    print("left")
    leftServo.throttle = 1.0
    rightServo.throttle = 1.0
    time.sleep(1.0)
    print("stop")
    leftServo.throttle = 0.0
    rightServo.throttle = 0.0
    time.sleep(2.0)
    
def right():
    print("left")
    leftServo.throttle = -1.0
    rightServo.throttle = -1.0
    time.sleep(1.0)
    print("stop")
    leftServo.throttle = 0.0
    rightServo.throttle = 0.0
    time.sleep(2.0)

forward()
backward()
left()
right()
    

