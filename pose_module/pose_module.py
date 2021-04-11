import cv2
import mediapipe as mp
import time
import math

class poseDetector():
    def __init__(self,mode=False,upbody=False,smoothmark=True,detcon=0.5,trackcon=0.5):
        self.mode=mode
        self.upbody=upbody
        self.smoothmark=smoothmark
        self.detcon=detcon
        self.trackcon=trackcon
        self.mppose=mp.solutions.pose
        self.pose=self.mppose.Pose(self.mode,self.upbody,
                                   self.smoothmark,self.detcon,self.trackcon)
        self.mpdraw=mp.solutions.drawing_utils
    
    def findpose(self,img,Draw=True):

        imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.pose.process(imgrgb)
        print(self.results.pose_landmarks)
        if self.results.pose_landmarks:
            if Draw:
                self.mpdraw.draw_landmarks(img,self.results.pose_landmarks,self.mppose.POSE_CONNECTIONS)

        return img

    def getpos(self,img,Draw=True):
        self.lmlist=[]
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = img.shape
                #print(id,lm)
                cx,cy=int(lm.x*w),int(lm.y*h)
                self.lmlist.append([id,cx,cy])
                if Draw:
                    cv2.circle(img,(cx,cy),4,(0,0,0),cv2.FILLED) 
        return self.lmlist
        
    
    def findangle(self,img,p1,p2,p3,Draw=True):
        #get the landmarks
        #_,x1,y1=self.lmlist[p1]
        x1,y1=self.lmlist[p1][1:]
        x2,y2=self.lmlist[p2][1:]
        x3,y3=self.lmlist[p3][1:]
        #get the Angles
        angle=math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x3-x2))
        #print(angle)
        if angle <0:
            angle += 360
        cv2.putText(img,str(int(angle)),(x2-50,y2+20),cv2.FONT_HERSHEY_PLAIN,3,(255,255,255),3)



        if Draw:
            cv2.line(img,(x1,y1),(x2,y2),(255,255,255),3)
            cv2.line(img,(x2,y2),(x3,y3),(255,255,255),3)
            
            cv2.circle(img,(x1,y1),8,(255,0,255),cv2.FILLED)
            cv2.circle(img,(x1,y1),15,(255,0,255),2)
            cv2.circle(img,(x2,y2),6,(255,0,255),cv2.FILLED)
            #cv2.circle(img,(x2,y2),15,(255,0,255),2 
            cv2.circle(img,(x3,y3),8,(255,0,255),cv2.FILLED) 
            cv2.circle(img,(x3,y3),15,(255,0,255),2)
        



def main():
    #cap=cv2.VideoCapture(r"C:\Users\Annie_Unplugged\my\dataset\fingure\cv2module\pose_module\pose_sample2.mp4")
    cap=cv2.VideoCapture(0)
    pertime=0
    detector=poseDetector()

    #resize = cv2.resize(image, (640, 480))
    while True:
        success,img=cap.read()
        img=cv2.resize(img,(1200,720))
        img=detector.findpose(img)
        lmlist=detector.getpos(img,Draw=True)

        if len(lmlist)!=0:
        #right arm
        #detector.findangle(img,12,14,16)
        #left arm
            detector.findangle(img,11,13,15)

        #print(lmlist[1])
        #cv2.circle(img,(lmlist[14][2],lmlist[14][1]),4,(255,255,0),cv2.FILLED) 


        curtime=time.time()
        fps=1/(curtime-pertime)
        pertime=curtime
        cv2.putText(img,str(int(fps)),(70,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        cv2.imshow("image",img)
        cv2.waitKey(1)




if __name__=="__main__":
    main()