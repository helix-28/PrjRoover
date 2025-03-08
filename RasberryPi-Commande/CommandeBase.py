# Python Script

# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/



import RPi.GPIO as GPIO

from time import sleep



in1 = 23

in2 = 24

in3 = 25

in4 = 18

in5 = 4

in6 = 17

in7 = 27

in8 = 22

temp1 = 1

NSLEEP1 = 12

NSLEEP2 = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(NSLEEP1,GPIO.OUT)

GPIO.setup(NSLEEP2,GPIO.OUT)

GPIO.setup(in1, GPIO.OUT)

GPIO.setup(in2, GPIO.OUT)

GPIO.setup(in3, GPIO.OUT)

GPIO.setup(in4, GPIO.OUT)

GPIO.setup(in5, GPIO.OUT)

GPIO.setup(in6, GPIO.OUT)

GPIO.setup(in7, GPIO.OUT)

GPIO.setup(in8, GPIO.OUT)

GPIO.output(in1, GPIO.LOW)  # roue avant droite avance

GPIO.output(in2, GPIO.LOW)	# roue avant gauche avance

GPIO.output(in3, GPIO.LOW)	# roue avant droite recule

GPIO.output(in4, GPIO.LOW)  # roue avant gauche recule 

GPIO.output(in5, GPIO.LOW)  # roue arriere droite avance

GPIO.output(in6, GPIO.LOW)  # roue arriere droite recule

GPIO.output(in7, GPIO.LOW)  # roue arriere gauche avance

GPIO.output(in8, GPIO.LOW)  # roue arriere gauche recule

p1=GPIO.PWM(NSLEEP1,1000)

p2=GPIO.PWM(NSLEEP2,1000)

p1.start(25)

p2.start(25)

print("\n")

print("The default speed & direction of motor is LOW & Forward.....")

print("r-run s-stop f-forward b-backward l-low m-medium h-high lt-lefttranslation rt-righttranslation e-exit")

print("\n")



while(1):



    x = input()



    if x == 'r':

        print("run")

        if (temp1 == 1):

            GPIO.output(in1, GPIO.LOW)

            GPIO.output(in2, GPIO.HIGH)

            GPIO.output(in3, GPIO.LOW)

            GPIO.output(in4, GPIO.HIGH)

            GPIO.output(in5, GPIO.HIGH)

            GPIO.output(in6, GPIO.LOW)

            GPIO.output(in7, GPIO.HIGH)

            GPIO.output(in8, GPIO.LOW)

            print("forward")

            x = 'z'

        else:

            GPIO.output(in1, GPIO.HIGH)

            GPIO.output(in2, GPIO.LOW)

            GPIO.output(in3, GPIO.HIGH)

            GPIO.output(in4, GPIO.LOW)

            GPIO.output(in5, GPIO.LOW)

            GPIO.output(in6, GPIO.HIGH)

            GPIO.output(in7, GPIO.LOW)

            GPIO.output(in8, GPIO.HIGH)

            print("backward")

            x = 'z'

    elif x == 't':

        GPIO.output(in7, GPIO.HIGH)  # roue avant droite avance

        GPIO.output(in8, GPIO.LOW)

        x = 'z'

    elif x == 's':

        print("stop")

        GPIO.output(in1, GPIO.LOW)

        GPIO.output(in2, GPIO.LOW)

        GPIO.output(in3, GPIO.LOW)

        GPIO.output(in4, GPIO.LOW)

        GPIO.output(in5, GPIO.LOW)

        GPIO.output(in6, GPIO.LOW)

        GPIO.output(in7, GPIO.LOW)

        GPIO.output(in8, GPIO.LOW)

        x = 'z'



    elif x == 'f':

        print("forward")

        GPIO.output(in1, GPIO.HIGH)

        GPIO.output(in2, GPIO.HIGH)

        GPIO.output(in3, GPIO.LOW)

        GPIO.output(in4, GPIO.LOW)

        GPIO.output(in5, GPIO.HIGH)

        GPIO.output(in6, GPIO.LOW)

        GPIO.output(in7, GPIO.HIGH)

        GPIO.output(in8, GPIO.LOW)

        temp1 = 1

        x = 'z'



    elif x == 'b':

        print("backward")

        GPIO.output(in1, GPIO.LOW)

        GPIO.output(in2, GPIO.LOW)

        GPIO.output(in3, GPIO.HIGH)

        GPIO.output(in4, GPIO.HIGH)

        GPIO.output(in5, GPIO.LOW)

        GPIO.output(in6, GPIO.HIGH)

        GPIO.output(in7, GPIO.LOW)

        GPIO.output(in8, GPIO.HIGH)

        temp1 = 0

        x = 'z'



    elif x == 'rt':

        print("right translation")

        GPIO.output(in1, GPIO.LOW)

        GPIO.output(in2, GPIO.HIGH)

        GPIO.output(in3, GPIO.HIGH)

        GPIO.output(in4, GPIO.LOW)

        GPIO.output(in5, GPIO.HIGH)

        GPIO.output(in6, GPIO.LOW)

        GPIO.output(in7, GPIO.LOW)

        GPIO.output(in8, GPIO.HIGH)

        temp1 = 0

        x = 'z'



    elif x == 'lt':

        print("left translation")

        GPIO.output(in1, GPIO.HIGH)

        GPIO.output(in2, GPIO.LOW)

        GPIO.output(in3, GPIO.LOW)

        GPIO.output(in4, GPIO.HIGH)

        GPIO.output(in5, GPIO.LOW)

        GPIO.output(in6, GPIO.HIGH)

        GPIO.output(in7, GPIO.HIGH)

        GPIO.output(in8, GPIO.LOW)

        temp1 = 0

        x = 'z'

        

    elif x == 'rd':

        print("right diagonale")

        GPIO.output(in1, GPIO.LOW)

        GPIO.output(in2, GPIO.HIGH)

        GPIO.output(in3, GPIO.LOW)

        GPIO.output(in4, GPIO.LOW)

        GPIO.output(in5, GPIO.HIGH)

        GPIO.output(in6, GPIO.LOW)

        GPIO.output(in7, GPIO.LOW)

        GPIO.output(in8, GPIO.LOW)

        temp1 = 0

        x = 'z'

        

    elif x == 'ld':

        print("left diagonale")

        GPIO.output(in1, GPIO.HIGH)

        GPIO.output(in2, GPIO.LOW)

        GPIO.output(in3, GPIO.LOW)

        GPIO.output(in4, GPIO.LOW)

        GPIO.output(in5, GPIO.LOW)

        GPIO.output(in6, GPIO.LOW)

        GPIO.output(in7, GPIO.HIGH)

        GPIO.output(in8, GPIO.LOW)

        temp1 = 0

        x = 'z'

        

    elif x == 'ldb':

        print("left diagonale backward")

        GPIO.output(in1, GPIO.LOW)

        GPIO.output(in2, GPIO.LOW)

        GPIO.output(in3, GPIO.LOW)

        GPIO.output(in4, GPIO.HIGH)

        GPIO.output(in5, GPIO.LOW)

        GPIO.output(in6, GPIO.HIGH)

        GPIO.output(in7, GPIO.LOW)

        GPIO.output(in8, GPIO.LOW)

        temp1 = 0

        x = 'z'     

    

    elif x == 'rdb':

        print("right diagonale backward")

        GPIO.output(in1, GPIO.LOW)

        GPIO.output(in2, GPIO.LOW)

        GPIO.output(in3, GPIO.HIGH)

        GPIO.output(in4, GPIO.LOW)

        GPIO.output(in5, GPIO.LOW)

        GPIO.output(in6, GPIO.LOW)

        GPIO.output(in7, GPIO.LOW)

        GPIO.output(in8, GPIO.HIGH)

        temp1 = 0

        x = 'z'

        

    elif x=='l':

        print("low")

        p1.ChangeDutyCycle(25)

        p2.ChangeDutyCycle(25)

        x='z'

        

    elif x=='m':

        print("medium")

        p1.ChangeDutyCycle(50)

        p2.ChangeDutyCycle(50)

        x='z'

        

    elif x=='h':

        print("high")

        p1.ChangeDutyCycle(75)

        p2.ChangeDutyCycle(75)

        x='z'

        

    elif x == 'e':

        GPIO.cleanup()

        print("GPIO Clean up")

        break



    else:

        print("<<<  wrong data  >>>")

        print("please enter the defined data to continue.....")


































































































































































