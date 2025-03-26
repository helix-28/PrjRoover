# Python Script
import time
import math
import pygame
from pygame.locals import *
import os, sys
import threading
import time
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/



import RPi.GPIO as GPIO

from time import sleep



moteurF_AVNT_DRT = 23

moteurR_AVNT_DRT = 24

moteurF_AVNT_GCH = 25

moteurR_AVNT_GCH = 5

moteurF_ARR_DRT = 4

moteurR_ARR_DRT = 17

moteurF_ARR_GCH = 27

moteurR_ARR_GCH = 22

temp1 = 1

NSLEEP1 = 18

NSLEEP2 = 13

NSLEEP3 = 12

NSLEEP4 = 19

GPIO.setmode(GPIO.BCM)

GPIO.setup(NSLEEP1,GPIO.OUT)

GPIO.setup(NSLEEP2,GPIO.OUT)

GPIO.setup(NSLEEP3,GPIO.OUT)

GPIO.setup(NSLEEP4,GPIO.OUT)

GPIO.setup(moteurF_AVNT_DRT, GPIO.OUT)

GPIO.setup(moteurR_AVNT_DRT, GPIO.OUT)

GPIO.setup(moteurF_AVNT_GCH, GPIO.OUT)

GPIO.setup(moteurR_AVNT_GCH, GPIO.OUT)

GPIO.setup(moteurF_ARR_DRT, GPIO.OUT)

GPIO.setup(moteurR_ARR_DRT, GPIO.OUT)

GPIO.setup(moteurF_ARR_GCH, GPIO.OUT)

GPIO.setup(moteurR_ARR_GCH, GPIO.OUT)

GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)  # roue avant droite avance

GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)	# roue avant gauche avance

GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)	# roue avant droite recule

GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)  # roue avant gauche recule

GPIO.output(moteurF_ARR_DRT, GPIO.LOW)  # roue arriere droite avance

GPIO.output(moteurR_ARR_DRT, GPIO.LOW)  # roue arriere droite recule

GPIO.output(moteurF_ARR_GCH, GPIO.LOW)  # roue arriere gauche avance

GPIO.output(moteurR_ARR_GCH, GPIO.LOW)  # roue arriere gauche recule

p1=GPIO.PWM(NSLEEP1,1000)

p2=GPIO.PWM(NSLEEP2,1000)

p3=GPIO.PWM(NSLEEP3,1000)

p4=GPIO.PWM(NSLEEP4,1000)

p1.start(25)

p2.start(25)

p3.start(25)

p4.start(25)

print("\n")

print("r-run s-stop f-forward b-backward l-low m-medium h-high lt-lefttranslation rt-righttranslation e-exit")

print("\n")




while True:



    x = input()
    def arret():

        # Arrêt du robot
        GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)
        GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)
        GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)
        GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)
        GPIO.output(moteurF_ARR_DRT, GPIO.LOW)
        GPIO.output(moteurR_ARR_DRT, GPIO.LOW)
        GPIO.output(moteurF_ARR_GCH, GPIO.LOW)
        GPIO.output(moteurR_ARR_GCH, GPIO.LOW)


    def direction_mecanum(vitesse, angle):
        vx = vitesse * math.cos(math.radians(angle))
        vy = vitesse * math.sin(math.radians(angle))

        v_AVNT_DRT = vx + vy
        v_AVNT_GCH = vx - vy
        v_ARR_DRT = vx - vy
        v_ARR_GCH = vx + vy

        maximum = max(abs(v_AVNT_DRT),abs(v_AVNT_GCH) , abs(v_ARR_GCH), abs(v_ARR_DRT))

        if maximum > 100 :
            v_ARR_DRT = v_ARR_DRT/maximum*100
            v_ARR_GCH = v_ARR_GCH/maximum*100
            v_AVNT_DRT = v_AVNT_DRT/maximum*100
            v_AVNT_GCH = v_AVNT_GCH/maximum*100


        if v_AVNT_DRT > 0:
            GPIO.output(moteurF_AVNT_DRT, GPIO.HIGH)
            GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)
        elif v_AVNT_DRT < 0:
            GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)
            GPIO.output(moteurR_AVNT_DRT, GPIO.HIGH)
        else:
            GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)
            GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)

        p1.ChangeDutyCycle(abs(v_AVNT_DRT))

        if v_AVNT_GCH > 0:
            GPIO.output(moteurF_AVNT_GCH, GPIO.HIGH)
            GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)
        elif v_AVNT_GCH < 0:
            GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)
            GPIO.output(moteurR_AVNT_GCH, GPIO.HIGH)
        else:
            GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)
            GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)

        p2.ChangeDutyCycle(abs(v_AVNT_GCH))

        if v_ARR_DRT > 0:
            GPIO.output(moteurF_ARR_DRT, GPIO.HIGH)
            GPIO.output(moteurR_ARR_DRT, GPIO.LOW)
        elif v_ARR_DRT < 0:
            GPIO.output(moteurF_ARR_DRT, GPIO.LOW)
            GPIO.output(moteurR_ARR_DRT, GPIO.HIGH)
        else:
            GPIO.output(moteurF_ARR_DRT, GPIO.LOW)
            GPIO.output(moteurR_ARR_DRT, GPIO.LOW)

        p4.ChangeDutyCycle(abs(v_ARR_DRT))

        if v_ARR_GCH > 0:
            GPIO.output(moteurF_ARR_GCH, GPIO.HIGH)
            GPIO.output(moteurR_ARR_GCH, GPIO.LOW)
        elif v_ARR_GCH < 0:
            GPIO.output(moteurF_ARR_GCH, GPIO.LOW)
            GPIO.output(moteurR_ARR_GCH, GPIO.HIGH)
        else:
            GPIO.output(moteurF_ARR_GCH, GPIO.LOW)
            GPIO.output(moteurR_ARR_GCH, GPIO.LOW)

        p3.ChangeDutyCycle(abs(v_ARR_GCH))

    def rotation(vitesse, horaire):
        if (horaire) :
            GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)
            GPIO.output(moteurF_AVNT_GCH, GPIO.HIGH)
            GPIO.output(moteurR_AVNT_DRT, GPIO.HIGH)
            GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)
            GPIO.output(moteurF_ARR_DRT, GPIO.LOW)
            GPIO.output(moteurR_ARR_DRT, GPIO.HIGH)
            GPIO.output(moteurF_ARR_GCH, GPIO.HIGH)
            GPIO.output(moteurR_ARR_GCH, GPIO.LOW)
        else :
            GPIO.output(moteurF_AVNT_DRT, GPIO.HIGH)
            GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)
            GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)
            GPIO.output(moteurR_AVNT_GCH, GPIO.HIGH)
            GPIO.output(moteurF_ARR_DRT, GPIO.HIGH)
            GPIO.output(moteurR_ARR_DRT, GPIO.LOW)
            GPIO.output(moteurF_ARR_GCH, GPIO.LOW)
            GPIO.output(moteurR_ARR_GCH, GPIO.HIGH)

        p1.ChangeDutyCycle(abs(vitesse))
        p2.ChangeDutyCycle(abs(vitesse))
        p3.ChangeDutyCycle(abs(vitesse))
        p4.ChangeDutyCycle(abs(vitesse))


    class Controller:
        def __init__(self):
            pygame.init()
            pygame.joystick.init()

            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

            print(f"Controller detected: {self.joystick.get_name()}")

        def read(self):
            """Read the state of the Xbox controller"""
            if not self.joystick:
                return [0, 0, 0, 0, 0]

            # Get the joystick values (assuming axes 0 and 1 are for the left stick, 2 and 3 for the right stick)
            left_x = self.joystick.get_axis(0)  # Left stick horizontal (X)
            left_y = self.joystick.get_axis(1)  # Left stick vertical (Y)
            right_x = self.joystick.get_axis(2)  # Right stick horizontal (X)
            right_y = self.joystick.get_axis(3)  # Right stick vertical (Y)
            z_axis = self.joystick.get_axis(4)  # Rotation (e.g., triggers or other axis)

            # Return the joystick values as separate axes
            return left_x, left_y, z_axis, right_x, right_y


    class RobotControl:
        def __init__(self):
            self.controller = XboxController()

        def rotation(self, vitesse, horaire):
            # Simulate rotation logic (clockwise or counterclockwise)
            direction = "Clockwise" if horaire else "Counterclockwise"
            print(f"Rotating {direction} with speed: {vitesse}")

        def handle_events(self):
            # Get the current state of the Xbox controller
            left_x, left_y, z_axis, right_x, right_y = self.controller.read()

            # Left joystick input handling for mecanum drive
            if left_x != 0 or left_y != 0:  # Handle left joystick movement
                angleManette = math.degrees(math.atan2(left_y, left_x))  # atan2 to handle correct quadrants
                vitesseManette = math.sqrt(left_x ** 2 + left_y ** 2) * 100  # Magnitude for speed (scaled)
                self.direction_mecanum(vitesseManette, angleManette)

            # Right joystick (right_x) input handling for rotation
            horaire = False
            if right_x >= 0:  # Right joystick X (used for rotation direction)
                horaire = True  # Clockwise rotation
            self.rotation(abs(right_x) * 100, horaire)

            # Handling the Z-axis rotation or triggers (optional)
            if z_axis != 0:
                print(f"Rotation Z-Axis: {z_axis}")

        def run(self):
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False  # Quit if the window is closed

                # Handle joystick inputs and control the robot
                self.handle_events()

                pygame.time.wait(50)  # Small delay to reduce CPU usage


    if x == 'r':

        print("run")

        if (temp1 == 1):

            GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)

            GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)

            GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)

            GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)

            GPIO.output(moteurF_ARR_DRT, GPIO.LOW)

            GPIO.output(moteurR_ARR_DRT, GPIO.LOW)

            GPIO.output(moteurF_ARR_GCH, GPIO.HIGH)

            GPIO.output(moteurR_ARR_GCH, GPIO.LOW)

            print("forward")
            #sleep(2)
            #arret()
            x = 'z'


        else:

            GPIO.output(moteurF_AVNT_DRT, GPIO.HIGH)

            GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)

            GPIO.output(moteurF_AVNT_GCH, GPIO.HIGH)

            GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)

            GPIO.output(moteurF_ARR_DRT, GPIO.LOW)

            GPIO.output(moteurR_ARR_DRT, GPIO.HIGH)

            GPIO.output(moteurF_ARR_GCH, GPIO.LOW)

            GPIO.output(moteurR_ARR_GCH, GPIO.HIGH)

            print("backward")

            x = 'z'
    elif x == 'tr':
        print("turn right")
        GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)
        GPIO.output(moteurF_AVNT_GCH, GPIO.HIGH)
        GPIO.output(moteurR_AVNT_DRT, GPIO.HIGH)
        GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)
        GPIO.output(moteurF_ARR_DRT, GPIO.LOW)
        GPIO.output(moteurR_ARR_DRT, GPIO.HIGH)
        GPIO.output(moteurF_ARR_GCH, GPIO.HIGH)
        GPIO.output(moteurR_ARR_GCH, GPIO.LOW)
    elif x == 'tl':
        print("turn left")
        GPIO.output(moteurF_AVNT_DRT, GPIO.HIGH)
        GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)
        GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)
        GPIO.output(moteurR_AVNT_GCH, GPIO.HIGH)
        GPIO.output(moteurF_ARR_DRT, GPIO.HIGH)
        GPIO.output(moteurR_ARR_DRT, GPIO.LOW)
        GPIO.output(moteurF_ARR_GCH, GPIO.LOW)
        GPIO.output(moteurR_ARR_GCH, GPIO.HIGH)
    elif x == 's':

        print("stop")

        arret()

        x = 'z'
    elif x == 'f':

        print("forward")

        GPIO.output(moteurF_AVNT_DRT, GPIO.HIGH)

        GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)

        GPIO.output(moteurF_AVNT_GCH, GPIO.HIGH)

        GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)

        GPIO.output(moteurF_ARR_DRT, GPIO.HIGH)

        GPIO.output(moteurR_ARR_DRT, GPIO.LOW)

        GPIO.output(moteurF_ARR_GCH, GPIO.HIGH)

        GPIO.output(moteurR_ARR_GCH, GPIO.LOW)

        temp1 = 1

        x = 'z'
    elif x == 'b':

        print("backward")

        GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)

        GPIO.output(moteurR_AVNT_DRT, GPIO.HIGH)

        GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)

        GPIO.output(moteurR_AVNT_GCH, GPIO.HIGH)

        GPIO.output(moteurF_ARR_DRT, GPIO.LOW)

        GPIO.output(moteurR_ARR_DRT, GPIO.HIGH)

        GPIO.output(moteurF_ARR_GCH, GPIO.LOW)

        GPIO.output(moteurR_ARR_GCH, GPIO.HIGH)

        temp1 = 0

        x = 'z'
    elif x == 'rt':

        print("right translation")

        GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)

        GPIO.output(moteurR_AVNT_DRT, GPIO.HIGH)

        GPIO.output(moteurF_AVNT_GCH, GPIO.HIGH)

        GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)

        GPIO.output(moteurF_ARR_DRT, GPIO.HIGH)

        GPIO.output(moteurR_ARR_DRT, GPIO.LOW)

        GPIO.output(moteurF_ARR_GCH, GPIO.LOW)

        GPIO.output(moteurR_ARR_GCH, GPIO.HIGH)

        temp1 = 0

        x = 'z'
    elif x == 'lt':

        print("left translation")

        GPIO.output(moteurF_AVNT_DRT, GPIO.HIGH)

        GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)

        GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)

        GPIO.output(moteurR_AVNT_GCH, GPIO.HIGH)

        GPIO.output(moteurF_ARR_DRT, GPIO.LOW)

        GPIO.output(moteurR_ARR_DRT, GPIO.HIGH)

        GPIO.output(moteurF_ARR_GCH, GPIO.HIGH)

        GPIO.output(moteurR_ARR_GCH, GPIO.LOW)

        temp1 = 0

        x = 'z'
    elif x == 'rd':

        print("right diagonale")

        GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)

        GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)

        GPIO.output(moteurF_AVNT_GCH, GPIO.HIGH)

        GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)

        GPIO.output(moteurF_ARR_DRT, GPIO.HIGH)

        GPIO.output(moteurR_ARR_DRT, GPIO.LOW)

        GPIO.output(moteurF_ARR_GCH, GPIO.LOW)

        GPIO.output(moteurR_ARR_GCH, GPIO.LOW)

        temp1 = 0

        x = 'z'
    elif x == 'ld':

        print("left diagonale")

        GPIO.output(moteurF_AVNT_DRT, GPIO.HIGH)

        GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)

        GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)

        GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)

        GPIO.output(moteurF_ARR_DRT, GPIO.LOW)

        GPIO.output(moteurR_ARR_DRT, GPIO.LOW)

        GPIO.output(moteurF_ARR_GCH, GPIO.HIGH)

        GPIO.output(moteurR_ARR_GCH, GPIO.LOW)

        temp1 = 0

        x = 'z'
    elif x == 'ldb':

        print("left diagonale backward")

        GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)

        GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)

        GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)

        GPIO.output(moteurR_AVNT_GCH, GPIO.HIGH)

        GPIO.output(moteurF_ARR_DRT, GPIO.LOW)

        GPIO.output(moteurR_ARR_DRT, GPIO.HIGH)

        GPIO.output(moteurF_ARR_GCH, GPIO.LOW)

        GPIO.output(moteurR_ARR_GCH, GPIO.LOW)

        temp1 = 0

        x = 'z'
    elif x == 'rdb':

        print("right diagonale backward")

        GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)

        GPIO.output(moteurR_AVNT_DRT, GPIO.HIGH)

        GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)

        GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)

        GPIO.output(moteurF_ARR_DRT, GPIO.LOW)

        GPIO.output(moteurR_ARR_DRT, GPIO.LOW)

        GPIO.output(moteurF_ARR_GCH, GPIO.LOW)

        GPIO.output(moteurR_ARR_GCH, GPIO.HIGH)

        temp1 = 0

        x = 'z'
    elif x=='l':

        print("low")

        p1.ChangeDutyCycle(25)

        p2.ChangeDutyCycle(25)
        p3.ChangeDutyCycle(25)

        p4.ChangeDutyCycle(25)

        x='z'
    elif x=='m':

        print("medium")

        p1.ChangeDutyCycle(50)

        p2.ChangeDutyCycle(50)
        
        p3.ChangeDutyCycle(50)

        p4.ChangeDutyCycle(50)

        x='z'
    elif x=='h':

        print("high")

        p1.ChangeDutyCycle(75)

        p2.ChangeDutyCycle(75)
        p3.ChangeDutyCycle(75)

        p4.ChangeDutyCycle(75)

        x='z'
    elif x == 'e':

        GPIO.cleanup()

        print("GPIO Clean up")

        break
    elif x == 'test':
        angle = int(input("Entrez l'angle: "))
        vitesse = float(input("Entrez la vitesse: "))
        print("angle: ", angle)
        print("vitesse:", vitesse)
        direction_mecanum(vitesse,angle)
        sleep(1.5)
        arret()
    elif x == 'manette' :
        xboxController = Controller()
        xboxController.run()

        tab = xboxController.read()

        if tab[0] != 0 :
            angleManette = math.arctan(tab[1]/tab[0])
        elif tab[1] >= 0 :
            angleManette = 0
        else :
            angleManette = 180

        vitesseManette = math.sqrt(tab[0]**2 + tab[1]**2) * 100

        print(angleManette)
        direction_mecanum(vitesseManette,angleManette)

        horaire = False
        if tab[2] >= 0 :
            horaire = True

        rotation(abs(tab[2]) * 100, horaire)

    elif x == "test2" :
        robot_control = RobotControl()
        robot_control.run()


    else:

        print("<<<  wrong data  >>>")

        print("please enter the defined data to continue.....")

