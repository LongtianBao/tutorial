# 电机主程序
from DCMotor import DCMotor
from machine import Pin, PWM
from time import sleep
 
frequency = 15000
 
pin1 = Pin(33, Pin.OUT)
pin2 = Pin(36, Pin.OUT)
enable = PWM(Pin(34), frequency)
 
dc_motor = DCMotor(pin1, pin2, enable)
 
for i in range(3):
    dc_motor.forward(10)
    sleep(0.7)
    dc_motor.stop()
    sleep(1)
    dc_motor.backwards(10)
    sleep(0.675)
    dc_motor.stop()
    sleep(1)