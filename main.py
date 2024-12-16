import ParkingMonitor
if __name__ == "__main__":
    area = [(26, 433), (9, 516), (389, 492), (786, 419), (720, 368)]
    video_path = 'parking1.mp4'
    model_path = 'yolov10s.pt'
    monitor = ParkingMonitor.ParkingMonitor(video_path, model_path, area)
    monitor.monitor_parking()