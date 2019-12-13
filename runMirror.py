import threading
import subprocess
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) # set board numbering
GPIO.setup(11, GPIO.IN) # set PIR input pin
GPIO.setup(13, GPIO.OUT) # set LED (on/off relay) output pin


def startAlexa():
    subprocess.Popen("sudo bash /home/pi/startsample.sh", shell=True) 

def startMirror():
    subprocess.Popen("pm2 start mm.sh", shell=True)

#def closeMirror():
    #subprocess.Popen("pm2 stop all", shell=True) results in pi loggin out
    
close = 1
startMirror() # call function to start MagicMirror module
startAlexa() # call function to start Alexa
GPIO.output(13,GPIO.LOW) # set LED off

while True:
    
    i = GPIO.input(11)   # get current motion
        
    if (i == 1): # while there is motion keep LED off
	# GPIO.output(13,GPIO.HIGH) #  uncomment if using on/off relay
	GPIO.output(13,GPIO.LOW)
	time.sleep(0.5)
        
    elif (i == 0):  # while there is no motion keep LED on
	print("I should shut off..")
	# GPIO.output(13,GPIO.LOW) #  uncomment if using on/off relay
        GPIO.output(13,GPIO.HIGH)
	time.sleep(0.5)

    
