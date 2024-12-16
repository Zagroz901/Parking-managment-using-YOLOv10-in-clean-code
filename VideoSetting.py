import cv2
class VideoSetting:
    def __init__(self, video_path, output_path='output.avi', frame_size=(640, 480), fps=20.0):
        self.area=[(26,433),(9,516),(389, 492),(786,419),(720,368)]
        self.video_path=video_path
        self.output_path=output_path
        self.frame_size= frame_size
        self.fps=fps
        self.cap = None
        self.out = None
    def load_video(self):
        fourcc = cv2.VideoWriter_fourcc(*'XVID') #use any fourcc type to improve quality for the saved video
        self.out = cv2.VideoWriter(self.output_path, fourcc, self.fps ,self.frame_size) #Video settings
        self.cap=cv2.VideoCapture(self.video_path)
    def release_resources(self):
        if self.cap:
            self.cap.release()
        if self.out:
            self.out.release()
        cv2.destroyAllWindows()        