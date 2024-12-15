import serial
import cv2
import time
import pandas as pd

ser = serial.Serial('COM10', 9600)
time.sleep(2)
cap = cv2.VideoCapture(1)
image_name = []
brightness = []
count = 0
while True:
    if count % 200 == 0:
        try:
            data = ser.readline().decode('utf-8').rstrip()
            print(data)
            ret, frame = cap.read()
            cv2.imwrite(f'./Reinf_learning/sample_image{count}-{int(data)}.jpg',frame)
            cv2.imshow('m',frame)
            image_name.append(f"sample_image{count}-{data}.jpg")
            brightness.append(data)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except:
            continue
    count += 1
ser.close()
cap.release()
cv2.destroyAllWindows()
df = pd.DataFrame({"Image Name":image_name,"Brightness":brightness})
df.to_csv('./Reinf_learning/labels.csv')
