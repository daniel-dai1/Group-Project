from machine import Pin,PWM
import time
from Servo_Angle_Translator import translate

#Defines Shoulder servo as pin 0
servo_S = PWM(Pin(0))
#Shoulder servo has a frequency of 50hz
servo_S.freq(50)
#Defines Elbow servo as pin 1
servo_E = PWM(Pin(1))
#Elbow servo has a frequency of 50hz
servo_E.freq(50)
#Defines Wrist servo as pin 2
servo_W = PWM(Pin(2))
#Wrist servo has a frequency of 50hz
servo_W.freq(50)

servo_W.duty_u16(translate(30))