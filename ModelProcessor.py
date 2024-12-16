from ultralytics import YOLO
import cv2
import numpy as np
class ModelProcessor:
    def __init__(self,model_path):
        self.model=YOLO(model_path)
        self.names=self.model.names
    def process_frame(self, frame, area):
        results=self.model(frame)
        points = []
        for result in results:
            for box in result.boxes:
                x1,y1,x2,y2=map(int,box.xyxy[0])
                d=self.names[int(box.cls)]
                cx=int(x1+x2)//2
                cy=int(y1+y2)//2
                if 'car' in d:
                    results = cv2.pointPolygonTest(np.array(area,np.int32),(cx,cy),False)
                    if results>=0:
                        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),3)
                        cv2.putText(frame,str(d),(x1,y1),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
                        points.append([cx])
        return frame,len(points)
        a = len(points)
        cv2.polylines(frame,[np.array(area,np.int32)],True,(0,255,0),2)
        cv2.putText(frame,'number of cars in parking ='+str(a),(50,80),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)  