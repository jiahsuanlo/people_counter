import cv2
from enum import Enum

class DisplayType(Enum):
    SourceImage=0,
    Gray=1,
    ColorMask= 2

cap= cv2.VideoCapture(0)
display_type= DisplayType.SourceImage
while True:
    # get a frame
    ret, img= cap.read()

    # convert to gray image
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # color mask for source img
    mask= (img[...,2]>150) & \
        (img[...,1]<100) & \
        (img[...,0]<150) 
    
   
    # make gray => bgr
    gray_bgr= cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    gray_bgr[mask,:] = img[mask,:]
        

    if display_type== DisplayType.SourceImage:
        cv2.imshow("webcam", img)
    elif display_type== DisplayType.Gray:
        cv2.imshow("webcam", gray)
    elif display_type== DisplayType.ColorMask:
        cv2.imshow("webcam", gray_bgr)


    key= cv2.waitKey(1) # wait for 1 ms
    if key== ord('q'):
        break
    elif key== ord("g"):
        display_type= DisplayType.Gray
    elif key== ord("s"):
        display_type= DisplayType.SourceImage
    elif key== ord("m"):
        display_type= DisplayType.ColorMask
    

cap.release()
cv2.destroyAllWindows()

