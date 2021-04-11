import cv2
import mediapipe as mp
import time

mppose=mp.solutions.pose
pose=mppose.Pose()
mpdraw=mp.solutions.drawing_utils
cap=cv2.VideoCapture(r"C:\Users\Annie_Unplugged\my\dataset\fingure\cv2module\pose_sample2.mp4")
pertime=0
#resize = cv2.resize(image, (640, 480))
while True:
    success,img=cap.read()
    imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=pose.process(imgrgb)
    print(results.pose_landmarks)
    if results.pose_landmarks:
        mpdraw.draw_landmarks(img,results.pose_landmarks,mppose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = img.shape
            print(id,lm)
            cx,cy=int(lm.x*w),int(lm.y*h)
            cv2.circle(img,(cx,cy),4,(255,0,0),cv2.FILLED)

    curtime=time.time()
    fps=1/(curtime-pertime)
    pertime=curtime
    cv2.putText(img,str(int(fps)),(70,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("image",img)
    cv2.waitKey(1)