'''
MS Robotics Camp 2021
Meghan Jimenez
Forward, Backward, Left, Right robot control
'''

import time
import board
import pwmio
from adafruit_motor import servo
from analogio import AnalogIn

# create a PWMOut object on Pin A2.
pwmLeft = pwmio.PWMOut(board.A3, frequency=50)
pwmRight = pwmio.PWMOut(board.A4, frequency=50)

# Create a servo object, my_servo.
leftServo = servo.ContinuousServo(pwmLeft)
rightServo = servo.ContinuousServo(pwmRight)

rightEye = AnalogIn(board.A1)
leftEye = AnalogIn(board.A0)

def backward(t, speed):
    print("backward")
    leftServo.throttle = speed
    rightServo.throttle = -1*speed
    time.sleep(t)

def forward(t, speed):
    print("forward")
    leftServo.throttle = -1 * speed
    rightServo.throttle = speed
    time.sleep(t)


def left(t, speed):
    print("left")
    leftServo.throttle = speed
    rightServo.throttle = speed
    time.sleep(t)

def right(t, speed):
    print("left")
    leftServo.throttle = -1*speed
    rightServo.throttle = -1*speed
    time.sleep(t)


while True:
    #print("rightEye: " + str(rightEye.value) + "     leftEye: " + str(leftEye.value))
    time.sleep(0.1)

    if (rightEye.value < 1000):
        right(0.01,1)
    elif (leftEye.value < 1500):
        left(0.01,1)
    else:
        forward(0.01,1)

