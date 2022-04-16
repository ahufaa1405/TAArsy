from enum import Flag
from json import load
from tkinter.font import names
import cv2
from cv2 import imshow	
import pyzbar.pyzbar as pyzbar

from pygame import mixer

mixer.init()

cap = cv2.VideoCapture(0)
cap2 = None
detected = None
load = None
is_detecting = False

track = None

while True:
    _, frame = cap.read()
    decode_QR = pyzbar.decode(frame)
    for barcode in decode_QR:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255),2)
        cv2.putText(frame, str(barcode.data), (100, 100), cv2.FONT_HERSHEY_PLAIN, 2,(255, 0, 0), 3)
        if not is_detecting and barcode.data.decode('UTF-8') != detected:
            detected = barcode.data.decode('UTF-8')
            cap2 = cv2.VideoCapture(detected+'.mp4')
            
            mixer.music.load(detected+".mp3")
            mixer.music.play()

    cv2.imshow('QR Code', frame)
    if detected:

        is_detecting, load = cap2.read()
        if is_detecting:
            cv2.imshow('LOAD', load)
        else:
            detected = None
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()