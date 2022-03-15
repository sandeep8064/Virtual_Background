import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os
cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
segmentor = SelfiSegmentation()
fpsReader= cvzone.FPS()
#imgBg = cv2.imread("images/1.jpg")

listimg=os.listdir("images")
print(listimg)
imglist=[]
for imgpath in listimg:
    img = cv2.imread(f'images/{imgpath}')
    imglist.append(img)
print(len(imglist))

index=0;

while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img,imglist[index], threshold=0.8)


    imgStacked=cvzone.stackImages([img,imgOut],2,1)
    _, imgStacked=fpsReader.update(imgStacked,color=(0,0,255))

    print(index)
    cv2.imshow("Virtual Background",imgStacked)
    key=cv2.waitKey(1)
    if key == ord('a'):
        if index>0:
            index -=1
    elif key == ord('d'):
        if index < len(imglist)-1:
            index +=1
    elif key == ord('q'):
        break

