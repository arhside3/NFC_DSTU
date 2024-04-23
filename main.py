import sys
import os
sys.path.append(os.path.dirname(__file__) + '/nfcpy')
import nfc
import RPi.GPIO as GPIO

def open_door():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)

    # Открытие двери
    GPIO.output(18, GPIO.HIGH)
    print("Дверь открыта!")

    # Закрытие GPIO
    GPIO.cleanup()

clf = nfc.ContactlessFrontend('usb')            #Specify only that it is a USB device
#clf = nfc.ContactlessFrontend('usb:054c:06c3')  #Specify vendor ID(Sony's PaSoRi Vendor ID)
#clf = nfc.ContactlessFrontend('usb:001')        #Specify the bus number. Choose the first one on this bus
#clf = nfc.ContactlessFrontend('usb:001:011')    #Specify bus number and device number

rdwr = {'on-connect':open_door}

print ('start')
clf.connect(rdwr=rdwr)
print ('end')
