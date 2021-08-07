'''
    Raspberry Pi Pico - PWP - MicroPython

    Servo motor 360° "Kookye EAEC100300" 

    Frequency : 50 Hz
    Volt : 4,8 - 6V DC
     
    Forward : 1 ms to 1,5 ms
    Stop : 1,5 ms
    Backward : 1,5 ms to 2 ms
'''
from machine import Pin,PWM
from utime import sleep

FORWARD_FAST = 3000
FORWARD_SLOW = 3500
STOP = 4500
BACKWARS_MEDIUM = 5250
BACKWARD_FAST = 5500

pwmMotor = PWM(Pin(16)) 
pwmMotor.freq(50)

while True:
    pwmMotor.duty_u16(FORWARD_FAST)
    sleep(2)
    pwmMotor.duty_u16(FORWARD_SLOW)
    sleep(2)
    pwmMotor.duty_u16(STOP)
    sleep(2)
    pwmMotor.duty_u16(BACKWARS_MEDIUM)
    sleep(2)
    pwmMotor.duty_u16(BACKWARD_FAST)
    sleep(2)
    pwmMotor.duty_u16(STOP)
    sleep(2)


