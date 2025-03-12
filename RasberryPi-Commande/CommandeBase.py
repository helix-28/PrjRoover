# Python Script
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

print("The default speed & direction of motor is LOW & Forward.....")

print("r-run s-stop f-forward b-backward l-low m-medium h-high lt-lefttranslation rt-righttranslation e-exit")

print("\n")



while(1):



    x = input()
    def arret():

        # Arrêt du robot après 2 secondes
        GPIO.output(moteurF_AVNT_DRT, GPIO.LOW)
        GPIO.output(moteurR_AVNT_DRT, GPIO.LOW)
        GPIO.output(moteurF_AVNT_GCH, GPIO.LOW)
        GPIO.output(moteurR_AVNT_GCH, GPIO.LOW)
        GPIO.output(moteurF_ARR_DRT, GPIO.LOW)
        GPIO.output(moteurR_ARR_DRT, GPIO.LOW)
        GPIO.output(moteurF_ARR_GCH, GPIO.LOW)
        GPIO.output(moteurR_ARR_GCH, GPIO.LOW)


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



    else:

        print("<<<  wrong data  >>>")

        print("please enter the defined data to continue.....")


































































































































































