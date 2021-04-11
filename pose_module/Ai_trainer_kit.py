import cv2
import mediapipe as mp
import time
import pose_module as pm

#cap=cv2.VideoCapture(r"C:\Users\Annie_Unplugged\my\dataset\fingure\cv2module\pose_sample2.mp4")

detector=pm.poseDetector()
#resize = cv2.resize(image, (640, 480))

while True:
    #img=cv2.imread(r"C:\Users\Annie_Unplugged\my\dataset\fingure\cv2module\pose_module\images2.jpg")
    cap=cv2.VideoCapture(0)
    success,img=cap.read()
    #make below line true for whole body lines
    detector.findpose(img,False)
    lmlist=detector.getpos(img,False)
    #print(lmlist)
    if len(lmlist)!=0:
        #right arm
        #detector.findangle(img,12,14,16)
        #left arm
        detector.findangle(img,11,13,15)
        #percentage=np.interp(angle,(210,310),0,100)
        #print(angle, percentage)

    
    cv2.imshow("image",img)
    cv2.waitKey(1)