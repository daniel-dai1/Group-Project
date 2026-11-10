from machine import Pin,PWM, ADC
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

#switch to raise/lower pen
switch = Pin(12, Pin.IN, Pin.PULL_DOWN)
#iterable to register button presses for toggling
n = 0

#Left potentiometer controls X axis
adcX = ADC(Pin(27))
#Right potentiometer controls Y axis
adcY = ADC(Pin(26))

#range of potentiometer, will vary between boards
potentiometer_range = 65535 - 160
#creates integer step value for virtual grid
#denominator is the number of steps desired
potentiometer_step = potentiometer_range / 180

#variable that controls how similar results are
alpha = 0.85

def lowpass(real, post):
    return alpha * post + (1 - alpha) * real

value_X_previous = round((adcX.read_u16() / potentiometer_step), 2)
value_Y_previous = round((adcY.read_u16() / potentiometer_step), 2)

while True:
    value_X = round((adcX.read_u16() / potentiometer_step), 2)
    X_lo_band = lowpass(value_X, value_X_previous)
    value_Y = round((adcY.read_u16() / potentiometer_step), 2)
    Y_lo_band = lowpass(value_Y, value_Y_previous)
    #button toggle to raise/lower pen
    if switch.value() == 1:
        time.sleep_ms(100)
        if switch.value() == 0:
            n+=1
    if n % 2 == 0:
        #lower wrist servo to 30˚
        servo_W.duty_u16(translate(30))
    else:
        #raise wrist servo to 12.5˚, prevents stalling
        servo_W.duty_u16(translate(12.5))
    #has issues of variance in inputs, a low-pass filter would solve
    if value_X <= X_lo_band and value_Y <= Y_lo_band:
        print(f"x pos: {value_X}\t y pos:{value_Y}\n")
        #these values will be sent to calculator
        servo_E.duty_u16(translate(value_X))
        servo_S.duty_u16(translate(value_Y))
    value_X_previous = value_X
    value_Y_previous = value_Y
    #time.sleep_ms(100)


