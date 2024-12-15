import serial
import cv2
import time, os
import pandas as pd

ser = serial.Serial('COM10', 9600)
time.sleep(2)
cap = cv2.VideoCapture(0)
image_name = []
brightness = []
SAMPLEING_RATE = 100
NUM_IMGS = 200
level = 0
count = 0
cam_loc = 5
count1 = cam_loc * NUM_IMGS
ser.write(f'{level}'.encode())
while True:
    if count % SAMPLEING_RATE == 0:
        count1 +=1
        ret, frame = cap.read()
        cv2.imwrite(f'./Reinf_learning/Final/sample_image{count1}-{level}.jpg',frame)
        # cv2.imshow('m',frame)
        image_name.append(f"sample_image{count1}-{level}.jpg")
        brightness.append(level)
        print(f'./Reinf_learning/Final/level{level}/sample_image{count1}-{level}.jpg')
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        if count1 >= ((cam_loc * NUM_IMGS)+NUM_IMGS):
            if level >=4:
                break
            level += 1
            ser.write(f'{level}'.encode())
            count1 = cam_loc * NUM_IMGS
    count += 1
cap.release()
cv2.destroyAllWindows()
