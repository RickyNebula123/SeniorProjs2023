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

# Create PWM instance for each motor
# Set up and Initialize pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)




def initialize_robot():
    
    global front_right_motor
    global front_left_motor
    global back_right_motor
    global back_left_motor

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

    # start PWM
    #     Front motors
    front_right_motor = GPIO.PWM(speed_pin_FR, 1000)
    front_left_motor  = GPIO.PWM(speed_pin_FL, 1000)

    #     Rear motors
    back_right_motor  = GPIO.PWM(speed_pin_BR, 1000)
    back_left_motor   = GPIO.PWM(speed_pin_BL, 1000)
    
    back_right_motor.start(0)
    back_left_motor.start(0)
    front_right_motor.start(0)
    front_left_motor.start(0)



# Motor functions

def FR_fwd():
    GPIO.output(right_motor_dir_pin1F, GPIO.LOW)
    GPIO.output(right_motor_dir_pin2F, GPIO.HIGH)

def FR_bck():
    GPIO.output(right_motor_dir_pin1F, GPIO.HIGH)
    GPIO.output(right_motor_dir_pin2F, GPIO.LOW)

def FL_fwd():
    GPIO.output(left_motor_dir_pin1F, GPIO.LOW)
    GPIO.output(left_motor_dir_pin2F, GPIO.HIGH)

def FL_bck():
    GPIO.output(left_motor_dir_pin1F, GPIO.HIGH)
    GPIO.output(left_motor_dir_pin2F, GPIO.LOW)

def BR_fwd():
    GPIO.output(right_motor_dir_pin1B, GPIO.LOW)
    GPIO.output(right_motor_dir_pin2B, GPIO.HIGH)

def BR_bck():
    GPIO.output(right_motor_dir_pin1B, GPIO.HIGH)
    GPIO.output(right_motor_dir_pin2B, GPIO.LOW)

def BL_fwd():
    GPIO.output(left_motor_dir_pin1B, GPIO.LOW)
    GPIO.output(left_motor_dir_pin2B, GPIO.HIGH)

def BL_bck():
    GPIO.output(left_motor_dir_pin1B, GPIO.HIGH)
    GPIO.output(left_motor_dir_pin2B, GPIO.LOW)

def stop_stop():
    global front_right_motor, front_left_motor
    global back_right_motor, back_left_motor
    #global front_left_motor
    #global back_left_motor

    front_right_motor.stop()
    front_left_motor.stop()
    back_right_motor.stop()
    back_left_motor.stop()

    back_right_motor.start(0)
    back_left_motor.start(0)
    front_right_motor.start(0)
    front_left_motor.start(0)

def move_fwd(speed):
    global front_right_motor
    global front_left_motor
    global back_right_motor
    global back_left_motor

    BR_fwd()
    BL_fwd()
    FR_fwd()
    FL_fwd()
    back_right_motor.ChangeDutyCycle(speed)
    back_left_motor.ChangeDutyCycle(speed)
    front_right_motor.ChangeDutyCycle(speed)
    front_left_motor.ChangeDutyCycle(speed)

def move_bwd(speed):
    global front_right_motor
    global front_left_motor
    global back_right_motor
    global back_left_motor

    BR_bck()
    BL_bck()
    FR_bck()
    FL_bck()
    back_right_motor.ChangeDutyCycle(speed)
    back_left_motor.ChangeDutyCycle(speed)
    front_right_motor.ChangeDutyCycle(speed)
    front_left_motor.ChangeDutyCycle(speed)

def turn_left_wheels(speed):
    global front_left_motor
    global back_left_motor

    front_left_motor.ChangeDutyCycle(speed)
    back_left_motor.ChangeDutyCycle(speed)

def turn_right_wheels(speed):
    global front_right_motor
    global back_right_motor

    front_right_motor.ChangeDutyCycle(speed)
    back_right_motor.ChangeDutyCycle(speed)

def straighten(speed):
    turn_right_wheels(speed)
    turn_right_wheels(speed)