import RPi.GPIO as GPIO
from time import sleep

# Motor Speed (Duty Cycle [0.0, 100.0] for PWM pins)
MAX_SPEED       = 95
MIN_SPEED       = 33
TURN_SPEED      = 50
SLOW_TURN_SPEED = 33
BACK_SPEED      = 50

# Motor speed Pins; PWM Pins for H-Bridge enable
speed_pin_FR = 18         # Front
speed_pin_FL = 12         # Front
speed_pin_BR = 13         # Back
speed_pin_BL = 19         # Back


# Motor direction pins
right_motor_dir_pin1F = 23 # Front
right_motor_dir_pin2F = 24 # Front
left_motor_dir_pin1F  = 25 # Front
left_motor_dir_pin2F  = 8  # Front


right_motor_dir_pin1B = 11 # Back
right_motor_dir_pin2B = 0  # Back
left_motor_dir_pin1B  = 5  # Back
left_motor_dir_pin2B  = 6  # Back

# Set up and Initialize pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# H-bridge enA and enB pins for respective motors (PWM pins)
GPIO.setup(speed_pin_FR, GPIO.OUT)
GPIO.setup(speed_pin_FL, GPIO.OUT)
GPIO.setup(speed_pin_BR, GPIO.OUT)
GPIO.setup(speed_pin_BL, GPIO.OUT)

# Direction pins for H-bridge (2 per motor)

#     Front motors
GPIO.setup(right_motor_dir_pin1F, GPIO.OUT)
GPIO.setup(right_motor_dir_pin2F, GPIO.OUT)
GPIO.setup(left_motor_dir_pin1F,  GPIO.OUT)
GPIO.setup(left_motor_dir_pin2F,  GPIO.OUT)
#     Rear motors
GPIO.setup(right_motor_dir_pin1B, GPIO.OUT)
GPIO.setup(right_motor_dir_pin2B, GPIO.OUT)
GPIO.setup(left_motor_dir_pin1B,  GPIO.OUT)
GPIO.setup(left_motor_dir_pin2B,  GPIO.OUT)

# Create PWM instance for each motor

#     Front motors
front_right_motor = GPIO.PWM(speed_pin_FR, 1000)
front_left_motor  = GPIO.PWM(speed_pin_FL, 1000)

#     Rear motors
back_right_motor  = GPIO.PWM(speed_pin_BR, 1000)
back_left_motor   = GPIO.PWM(speed_pin_BL, 1000)




# Motor functions

def FR_fwd(speed):
    GPIO.output(right_motor_dir_pin1F, GPIO.LOW)
    GPIO.output(right_motor_dir_pin2F, GPIO.HIGH)

def FR_bck(speed):
    GPIO.output(right_motor_dir_pin1F, GPIO.HIGH)
    GPIO.output(right_motor_dir_pin2F, GPIO.LOW)

def FL_fwd(speed):
    GPIO.output(left_motor_dir_pin1F, GPIO.LOW)
    GPIO.output(left_motor_dir_pin2F, GPIO.HIGH)

def FL_bck(speed):
    GPIO.output(left_motor_dir_pin1F, GPIO.HIGH)
    GPIO.output(left_motor_dir_pin2F, GPIO.LOW)

def BR_fwd(speed):
    GPIO.output(right_motor_dir_pin1B, GPIO.LOW)
    GPIO.output(right_motot_dir_pin2B, GPIO.HIGH)

def BR_bck(speed):
    GPIO.output(right_motor_dir_pin1B, GPIO.HIGH)
    GPIO.output(right_motor_dir_pin2B, GPIO.LOW)

def BL_fwd(speed):
    GPIO.output(left_motor_dir_pin1B, GPIO.LOW)
    GPIO.output(left_motot_dir_pin2B, GPIO.HIGH)

def Bl_bck(speed):
    GPIO.output(left_motor_dir_pin1B, GPIO.HIGH)
    GPIO.output(left_motor_dir_pin2B, GPIO.LOW)

def stop_stop():
    front_right_motor.stop()
    front_left_motor.stop()
    back_right_motor.stop()
    back_left_motor.stop()

while(1):
    FR_fwd(90)
    front_right_motor.start(50)
    print("moving fwd front right")
    sleep(2)
    stop_stop();

    FL_fwd(90)
    front_left_motor.start(90)
    print("moving fwd front left")
    sleep(2)
    stop_stop();

    FL_bck(90)
    front_left_motor.start(90)
    print("moving bck front left")
    sleep(2)
    stop_stop();

    FR_bck(90)
    front_right_motor.start(50);
    print("moving bck front right")
    sleep(2)
    stop_stop;


