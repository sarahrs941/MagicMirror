import threading
import subprocess
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
GPIO.setup(13, GPIO.OUT)


def startAlexa():
    subprocess.Popen("sudo bash /home/pi/startsample.sh", shell=True)

def startMirror():
    subprocess.Popen("pm2 start mm.sh", shell=True)

def closeMirror():
    subprocess.Popen("pm2 stop all", shell=True)
    
close = 0
startMirror()
startAlexa()
GPIO.output(13,GPIO.LOW)

while True:
    
    i = GPIO.input(11)   
        
    if (i == 1 and close == 1):	
	GPIO.output(13,GPIO.LOW)          
        
    elif (i == 0):
	print("I should shut off..")
        GPIO.output(13,GPIO.HIGH)
	close = 1
	
    
