# Python Script
import time
from inputs import get_gamepad
import math
import threading
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


class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()


    def read(self): # return the buttons/triggers that you care about in this methode
        x = self.LeftJoystickX
        y = self.LeftJoystickY
        rot = self.RightJoystickX

        return [x, y, rot]


    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.Y = event.state #previously switched with X
                elif event.code == 'BTN_WEST':
                    self.X = event.state #previously switched with Y
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY1':
                    self.LeftDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY2':
                    self.RightDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY3':
                    self.UpDPad = event.state
                elif event.code == 'BTN_TRIGGER_HAPPY4':
                    self.DownDPad = event.state


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
        xboxController = XboxController1()

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



    else:

        print("<<<  wrong data  >>>")

        print("please enter the defined data to continue.....")
class XboxController1(threading.Thread):
    # internal ids for the xbox controls
    class XboxControls():
        LTHUMBX = 0
        LTHUMBY = 1
        RTHUMBX = 2
        RTHUMBY = 3
        RTRIGGER = 4
        LTRIGGER = 5
        A = 6
        B = 7
        X = 8
        Y = 9
        LB = 10
        RB = 11
        BACK = 12
        START = 13
        XBOX = 14
        LEFTTHUMB = 15
        RIGHTTHUMB = 16
        DPAD = 17

    # pygame axis constants for the analogue controls of the xbox controller
    class PyGameAxis():
        LTHUMBX = 0
        LTHUMBY = 1
        RTHUMBX = 2
        RTHUMBY = 3
        RTRIGGER = 4
        LTRIGGER = 5

    # pygame constants for the buttons of the xbox controller
    class PyGameButtons():
        A = 0
        B = 1
        X = 2
        Y = 3
        LB = 4
        RB = 5
        BACK = 6
        START = 7
        XBOX = 8
        LEFTTHUMB = 9
        RIGHTTHUMB = 10

    # map between pygame axis (analogue stick) ids and xbox control ids
    AXISCONTROLMAP = {PyGameAxis.LTHUMBX: XboxControls.LTHUMBX,
                      PyGameAxis.LTHUMBY: XboxControls.LTHUMBY,
                      PyGameAxis.RTHUMBX: XboxControls.RTHUMBX,
                      PyGameAxis.RTHUMBY: XboxControls.RTHUMBY}

    # map between pygame axis (trigger) ids and xbox control ids
    TRIGGERCONTROLMAP = {PyGameAxis.RTRIGGER: XboxControls.RTRIGGER,
                         PyGameAxis.LTRIGGER: XboxControls.LTRIGGER}

    # map between pygame buttons ids and xbox contorl ids
    BUTTONCONTROLMAP = {PyGameButtons.A: XboxControls.A,
                        PyGameButtons.B: XboxControls.B,
                        PyGameButtons.X: XboxControls.X,
                        PyGameButtons.Y: XboxControls.Y,
                        PyGameButtons.LB: XboxControls.LB,
                        PyGameButtons.RB: XboxControls.RB,
                        PyGameButtons.BACK: XboxControls.BACK,
                        PyGameButtons.START: XboxControls.START,
                        PyGameButtons.XBOX: XboxControls.XBOX,
                        PyGameButtons.LEFTTHUMB: XboxControls.LEFTTHUMB,
                        PyGameButtons.RIGHTTHUMB: XboxControls.RIGHTTHUMB}

    # setup xbox controller class
    def __init__(self,
                 controllerCallBack=None,
                 joystickNo=0,
                 deadzone=0.1,
                 scale=1,
                 invertYAxis=False):

        # setup threading
        threading.Thread.__init__(self)

        # persist values
        self.running = False
        self.controllerCallBack = controllerCallBack
        self.joystickNo = joystickNo
        self.lowerDeadzone = deadzone * -1
        self.upperDeadzone = deadzone
        self.scale = scale
        self.invertYAxis = invertYAxis
        self.controlCallbacks = {}

        # setup controller properties
        self.controlValues = {self.XboxControls.LTHUMBX: 0,
                              self.XboxControls.LTHUMBY: 0,
                              self.XboxControls.RTHUMBX: 0,
                              self.XboxControls.RTHUMBY: 0,
                              self.XboxControls.RTRIGGER: 0,
                              self.XboxControls.LTRIGGER: 0,
                              self.XboxControls.A: 0,
                              self.XboxControls.B: 0,
                              self.XboxControls.X: 0,
                              self.XboxControls.Y: 0,
                              self.XboxControls.LB: 0,
                              self.XboxControls.RB: 0,
                              self.XboxControls.BACK: 0,
                              self.XboxControls.START: 0,
                              self.XboxControls.XBOX: 0,
                              self.XboxControls.LEFTTHUMB: 0,
                              self.XboxControls.RIGHTTHUMB: 0,
                              self.XboxControls.DPAD: (0, 0)}

        # setup pygame
        self._setupPygame(joystickNo)

    # Create controller properties
    @property
    def LTHUMBX(self):
        return self.controlValues[self.XboxControls.LTHUMBX]

    @property
    def LTHUMBY(self):
        return self.controlValues[self.XboxControls.LTHUMBY]

    @property
    def RTHUMBX(self):
        return self.controlValues[self.XboxControls.RTHUMBX]

    @property
    def RTHUMBY(self):
        return self.controlValues[self.XboxControls.RTHUMBY]

    @property
    def RTRIGGER(self):
        return self.controlValues[self.XboxControls.RTRIGGER]

    @property
    def LTRIGGER(self):
        return self.controlValues[self.XboxControls.LTRIGGER]

    @property
    def A(self):
        return self.controlValues[self.XboxControls.A]

    @property
    def B(self):
        return self.controlValues[self.XboxControls.B]

    @property
    def X(self):
        return self.controlValues[self.XboxControls.X]

    @property
    def Y(self):
        return self.controlValues[self.XboxControls.Y]

    @property
    def LB(self):
        return self.controlValues[self.XboxControls.LB]

    @property
    def RB(self):
        return self.controlValues[self.XboxControls.RB]

    @property
    def BACK(self):
        return self.controlValues[self.XboxControls.BACK]

    @property
    def START(self):
        return self.controlValues[self.XboxControls.START]

    @property
    def XBOX(self):
        return self.controlValues[self.XboxControls.XBOX]

    @property
    def LEFTTHUMB(self):
        return self.controlValues[self.XboxControls.LEFTTHUMB]

    @property
    def RIGHTTHUMB(self):
        return self.controlValues[self.XboxControls.RIGHTTHUMB]

    @property
    def DPAD(self):
        return self.controlValues[self.XboxControls.DPAD]

    # setup pygame
    def _setupPygame(self, joystickNo):
        # set SDL to use the dummy NULL video driver, so it doesn't need a windowing system.
        os.environ["SDL_VIDEODRIVER"] = "dummy"
        # init pygame
        pygame.init()
        # create a 1x1 pixel screen, its not used so it doesnt matter
        screen = pygame.display.set_mode((1, 1))
        # init the joystick control
        pygame.joystick.init()
        # how many joysticks are there
        # print pygame.joystick.get_count()
        # get the first joystick
        joy = pygame.joystick.Joystick(joystickNo)
        # init that joystick
        joy.init()

    # called by the thread
    def run(self):
        self._start()

    # start the controller
    def _start(self):

        self.running = True

        # run until the controller is stopped
        while (self.running):
            # react to the pygame events that come from the xbox controller
            for event in pygame.event.get():

                # thumb sticks, trigger buttons
                if event.type == JOYAXISMOTION:
                    # is this axis on our xbox controller
                    if event.axis in self.AXISCONTROLMAP:
                        # is this a y axis
                        yAxis = True if (
                                    event.axis == self.PyGameAxis.LTHUMBY or event.axis == self.PyGameAxis.RTHUMBY) else False
                        # update the control value
                        self.updateControlValue(self.AXISCONTROLMAP[event.axis],
                                                self._sortOutAxisValue(event.value, yAxis))
                    # is this axis a trigger
                    if event.axis in self.TRIGGERCONTROLMAP:
                        # update the control value
                        self.updateControlValue(self.TRIGGERCONTROLMAP[event.axis],
                                                self._sortOutTriggerValue(event.value))

                # d pad
                elif event.type == JOYHATMOTION:
                    # update control value
                    self.updateControlValue(self.XboxControls.DPAD, event.value)

                # button pressed and unpressed
                elif event.type == JOYBUTTONUP or event.type == JOYBUTTONDOWN:
                    # is this button on our xbox controller
                    if event.button in self.BUTTONCONTROLMAP:
                        # update control value
                        self.updateControlValue(self.BUTTONCONTROLMAP[event.button],
                                                self._sortOutButtonValue(event.type))

    # stops the controller
    def stop(self):
        self.running = False

    # updates a specific value in the control dictionary
    def updateControlValue(self, control, value):
        # if the value has changed update it and call the callbacks
        if self.controlValues[control] != value:
            self.controlValues[control] = value
            self.doCallBacks(control, value)

    # calls the call backs if necessary
    def doCallBacks(self, control, value):
        # call the general callback
        if self.controllerCallBack != None: self.controllerCallBack(control, value)

        # has a specific callback been setup?
        if control in self.controlCallbacks:
            self.controlCallbacks[control](value)

    # used to add a specific callback to a control
    def setupControlCallback(self, control, callbackFunction):
        # add callback to the dictionary
        self.controlCallbacks[control] = callbackFunction

    # scales the axis values, applies the deadzone
    def _sortOutAxisValue(self, value, yAxis=False):
        # invert yAxis
        if yAxis and self.invertYAxis: value = value * -1
        # scale the value
        value = value * self.scale
        # apply the deadzone
        if value < self.upperDeadzone and value > self.lowerDeadzone: value = 0
        return value

    # turns the trigger value into something sensible and scales it
    def _sortOutTriggerValue(self, value):
        # trigger goes -1 to 1 (-1 is off, 1 is full on, half is 0) - I want this to be 0 - 1
        value = max(0, (value + 1) / 2)
        # scale the value
        value = value * self.scale
        return value

    # turns the event type (up/down) into a value
    def _sortOutButtonValue(self, eventType):
        # if the button is down its 1, if the button is up its 0
        value = 1 if eventType == JOYBUTTONDOWN else 0
        return value