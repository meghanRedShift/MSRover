'''
Meghan Jimenez
Robotics Camp 2021
'''

import time
import board
import pwmio
from adafruit_motor import servo
from analogio import AnalogIn

#Connect Servos
pwmLeft = pwmio.PWMOut(board.A3, frequency=50)
pwmRight = pwmio.PWMOut(board.A2, frequency=50)

#Make Servos
leftServo = servo.ContinuousServo(pwmLeft)
rightServo = servo.ContinuousServo(pwmRight)

while True:
    leftServo.throttle = 1
    rightServo.throttle = -1
    time.sleep(1)

    leftServo.throttle = -1
    rightServo.throttle = 1
    time.sleep(1)

    leftServo.throttle = -1
    rightServo.throttle = -1
    time.sleep(1)

    leftServo.throttle = 1
    rightServo.throttle = 1
    time.sleep(1)















