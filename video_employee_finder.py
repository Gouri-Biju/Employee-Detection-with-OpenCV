import cv2
from employee_finder import employee_finder

vs = cv2.VideoCapture('./video/green_tshirt_on_floor.mov')
while True:
    grabbed, frame = vs.read()
    cv2.imshow('input', frame)
    cv2.waitKey(1)
    if grabbed == False:
        break
    else:
        frame = employee_finder(frame)
        cv2.imshow('output', frame)
        cv2.waitKey(1)
