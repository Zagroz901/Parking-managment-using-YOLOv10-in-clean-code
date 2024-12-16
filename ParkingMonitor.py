import VideoSetting
import ModelProcessor 
import cv2
import numpy as np
class ParkingMonitor:
    def __init__(self,video_path,model_path,area):
        self.video_setting =VideoSetting.VideoSetting(video_path)
        self.model_processor =ModelProcessor.ModelProcessor(model_path)
        self.area=area
    def monitor_parking(self):
        self.video_setting.load_video()
        cap = self.video_setting.cap
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, (1020, 600))
            frame, car_count = self.model_processor.process_frame(frame, self.area)

            cv2.polylines(frame, [np.array(self.area, np.int32)], True, (0, 255, 0), 2)
            cv2.putText(frame, f'Number of cars in parking: {car_count}', (50, 80),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
            cv2.imshow("Parking Monitor", frame)
            self.video_setting.out.write(frame)
            if cv2.waitKey(1) == 27:  # Escape key to exit
                break
        self.video_setting.release_resources()    