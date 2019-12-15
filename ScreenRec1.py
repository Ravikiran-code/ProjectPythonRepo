import cv2
import numpy as np
import pyautogui

screen_size=(1920,1080)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
ip = input("Enter video name with .extension: ")
out=cv2.VideoWriter("E:/Python codes/FMSVideos/"+ip,fourcc,20.0,(screen_size))

##key = input("Press s to start : ")
##print ("Press q to stop")

while True:
    img=pyautogui.screenshot()
    frame=np.array(img)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("show",frame)
    if cv2.waitKey(1) == ord('q'):
        break
##    key = str(input())
##    if key == 'q':
##        print ('Video capture stopped and saved')
##        break
    
