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


    def direction_mecanum(vitesse, angle, rotation):
        vx = vitesse * math.cos(math.radians(angle))
        vy = vitesse * math.sin(math.radians(angle))

        v_AVNT_DRT = vx + vy + rotation
        v_AVNT_GCH = vx - vy - rotation
        v_ARR_DRT = vx - vy + rotation
        v_ARR_GCH = vx + vy - rotation

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
                return [0, 0, 0]

            gauche_x = self.joystick.get_axis(0)  #  joystick gauche horizontal (X)
            gauche_y = self.joystick.get_axis(1)  #  joystick gauche vertical (Y)
            droite_x = self.joystick.get_axis(3)  # joystick droit horizontal (X)

            return gauche_x, gauche_y, droite_x


    class RobotControl:
        def __init__(self):
            self.controller = Controller()

        def handle_events(self):

            gauche_x, gauche_y, droite_x = self.controller.read()

            if gauche_x != 0 or gauche_y != 0:
                angleManette = math.degrees(math.atan2(gauche_x, gauche_y))
                vitesseManette = math.sqrt(gauche_x ** 2 + gauche_y ** 2) * 100
            else :
                vitesseManette = 0
                angleManette = 0

            direction_mecanum(vitesseManette, angleManette+180, droite_x*-100)



        def run(self):
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False  # Quitter is la fenêtre est fermée

                # s'occuppe des entrées des manettes
                self.handle_events()

                pygame.time.wait(50)  # Petit délai pour l'utilisation du CPU





    if x == 'e':

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

    elif x == "test2" :
        robot_control = RobotControl()
        robot_control.run()


    else:

        print("<<<  Mauvaise entrée  >>>")

        print("Entrez une entrée valide pour continuer.....")

