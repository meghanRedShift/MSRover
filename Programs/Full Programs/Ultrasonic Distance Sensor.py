'''
Meghan Jimenez
Robotics Summer Camp 2021
'''

import time
import board
import pwmio
from adafruit_motor import servo
from analogio import AnalogIn

#Connect Servos
pwmLeft = pwmio.PWMOut(board.A3, frequency=50)
pwmRight = pwmio.PWMOut(board.A2, frequency = 50)

#Make Servos
leftServo = servo.ContinuousServo(pwmLeft)
rightServo = servo.ContinuousServo(pwmRight)



def forward(t,speed, speed2):
    leftServo.throttle = speed
    rightServo.throttle = -speed2
    time.sleep(t)
    
rightEye = AnalogIn(board.A0)

import adafruit_hcsr04
sonarFront = adafruit_hcsr04.HCSR04(trigger_pin=board.D1, echo_pin=board.D0)
sonarRight = adafruit_hcsr04.HCSR04(trigger_pin=board.D2, echo_pin=board.D3)

while True:
    try:
        print("Front: " + str(sonarFront.distance) + "     Right: " + str(sonarRight.distance))
        if (sonarFront.distance > 100):
            leftServo.throttle = 0
            print("off")
        else:
            leftServo.throttle = 1
            print("servoOn")
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)



















