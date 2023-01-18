import keyboard
import movement_code

class rover():
    MAX_SPEED = 90
    MIN_SPEED = 0
    SPEED_INCREMENT = 10

    def __init__(self):
        self.speed     = 0
        self.direction = 0                                                           # 0 equals forward | 1 equals backwards
        self.left_wheels = self.speed
        self.right_wheels = self.speed
        movement_code.initialize_robot()                            # Starts RPi pins

    def speed_up(self, direction):                                  # direction is function object
        adjustment = rover.SPEED_INCREMENT
        if(self.speed + rover.SPEED_INCREMENT >= rover.MAX_SPEED): 
            adjustment = 0
        
        self.speed += adjustment 
        self.left_wheels += adjustment 
        self.right_wheels += adjustment 


        print(f"l: {self.left_wheels} r: {self.right_wheels} s: {self.speed}")

        direction(self.speed)
        
    def slow_down(self, direction):                                 # dir is a function object.
        adjustment = rover.SPEED_INCREMENT
        if(self.speed - rover.SPEED_INCREMENT <= rover.MIN_SPEED):
            self.direction = not self.direction
            adjustment = 0
        
        self.speed -= adjustment 
        self.left_wheels -= adjustment 
        self.right_wheels -= adjustment 

        print(f"l: {self.left_wheels} r: {self.right_wheels} s: {self.speed}")

        direction(self.speed)

    def turn_left(self):
        if self.left_wheels - rover.SPEED_INCREMENT < rover.MIN_SPEED: 
            self.left_wheels = rover.MIN_SPEED
        else:
            self.left_wheels -= rover.SPEED_INCREMENT
        print(f"Left wheel speed: {self.left_wheels}")
        movement_code.turn_left_wheels(self.left_wheels)

    def turn_right(self):
        if self.right_wheels - rover.SPEED_INCREMENT < rover.MIN_SPEED: 
            self.right_wheels = rover.MIN_SPEED
        else:
            self.right_wheels -= rover.SPEED_INCREMENT
        print(f"Right wheel speed: {self.right_wheels}")
        movement_code.turn_right_wheels(self.right_wheels)
    
    def straighten(self):
        max_speed = max(self.left_wheels, self.right_wheels)
        self.left_wheels = max_speed
        self.right_wheels = max_speed
        print(f"Straightening with speed: {max_speed}")
        movement_code.straighten(max_speed)
        
    def turn_on(self):
        print("Robot on...")
        while 1:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                key = event.name

                if key == 'q':
                    print("Turning off engine.")
                    break

                if key == 'up' or key == 'i':
                    print("Accelerate\n")
                    if not self.direction:
                        self.speed_up(movement_code.move_fwd)
                    else:
                        self.slow_down(movement_code.move_bwd)
                if key == 'down':
                    print("Slowing down\n")
                    if not self.direction:
                        self.slow_down(movement_code.move_fwd)
                    else:
                        self.speed_up(movement_code.move_bwd)
                if key == 'left':
                    print("Turning left\n")
                    self.turn_left()
                if key == 'right':
                    print("Turning right\n")
                    self.turn_right()
                if key == 's':
                    print("Stopping.\n")
                    self.speed = rover.MIN_SPEED
                    movement_code.stop_stop()
                if key == 't':
                    self.straighten()

robot = rover()
robot.turn_on()
# while 1:
#     event = keyboard.read_event()
#     if event.event_type == keyboard.KEY_DOWN:
#         key = event.name
#         print(f"Pressed: {key}")
