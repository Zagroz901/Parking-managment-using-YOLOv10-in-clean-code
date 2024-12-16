# Parking Lot Monitoring System 🅿️🚗

This project is a **Parking Lot Monitoring System** that uses **YOLO (You Only Look Once)** object detection to detect and count cars in a designated parking area. It processes video input to identify vehicles, highlight them on the video, and calculate the number of cars parked within a defined region of interest (ROI).

---

## Features ✨
- **Real-time Vehicle Detection**: Identifies cars using a pre-trained YOLO model.
- **Polygonal ROI Monitoring**: Tracks vehicles entering a specific parking area.
- **Video Processing**: Resizes video frames and overlays detection results.
- **Interactive Visualization**: Displays bounding boxes, labels, and total parked car count on the video.
- **OOP Design**: Modular object-oriented structure for better scalability and readability.
- **Output Video Saving**: Processes and saves the annotated video to disk.

---

## Project Architecture 🛠️
The project is organized into three main classes:
1. **`VideoSetting`**:
   - Handles video input, output, and resource management.
   - Encapsulates functionality to load and save video files.

2. **`ModelProcessor`**:
   - Loads the YOLO model for object detection.
   - Processes video frames to detect cars and checks if they are within the ROI.

3. **`ParkingMonitor`**:
   - Combines video settings and object detection functionalities.
   - Executes the main workflow: loads the video, detects vehicles, and tracks parking occupancy.

---

## Requirements 🧰
Before running the project, ensure you have the following installed:
- Python 3.8+
- Libraries:
  - `opencv-python`
  - `numpy`
  - `ultralytics` (for YOLO)

You can install the dependencies with:
```bash
pip install opencv-python numpy ultralytics
```

---

## Usage 🚀

### 1. Clone the Repository
```bash
git clone (https://github.com/Zagroz901/Parking-managment-using-YOLOv10-in-clean-code.git)
cd Parking-managment-using-YOLOv10-in-clean-code
```

### 2. Prepare the Model
- Download your YOLO model weights (`yolov10s.pt` or other compatible weights).
- Place the model file in the project directory.

### 3. Run the Program
```bash
python main.py
```

### 4. Output
- The processed video will be saved as `output.avi`.
- The live feed will display the parking lot with:
  - **Bounding Boxes**: Around detected cars.
  - **Polygonal ROI**: Marked parking area.
  - **Car Count**: Displayed as text on the frame.

---

## Configuration ⚙️

### Video Input
Replace the video path in `ParkingMonitor` initialization:
```python
video_path = 'path/to/your/video.mp4'
```

### Region of Interest (ROI)
Update the `area` variable with the coordinates of your parking area:
```python
area = [(x1, y1), (x2, y2), ...]
```


## File Structure 📂
```
├── main.py               # Entry point of the application
├── ModelProcessor.py     # Entry point of the application
├── ParkingMonitor.py     # Entry point of the application
├── VideoSetting.py       # Entry point of the application
├── README.md             # Project documentation
├── yolov10s.pt           # YOLO model weights
├── parking.mp4           # Example input video
└── output.avi            # Processed output video
```

---

## How It Works 🔍
1. **Load Video**: Reads the video file using OpenCV.
2. **Detect Vehicles**: Uses YOLO to identify cars in each frame.
3. **Check ROI**: Validates if the detected car is within the parking area.
4. **Overlay Results**: Draws bounding boxes, highlights the ROI, and shows the total count.
5. **Save Processed Video**: Writes the annotated frames to an output video file.

---

## Future Enhancements 🚧
- Add support for live video streams (e.g., webcam or CCTV).
- Implement a notification system for parking lot updates.
- Use additional YOLO versions (e.g., YOLOv8) for higher accuracy.
- Add multi-class detection for different vehicle types.

---

## License 📜
This project is open-source and available under the [MIT License](LICENSE).

---

## Acknowledgments 🤝
- [YOLO](https://github.com/ultralytics/ultralytics) for the powerful object detection framework.
- [OpenCV](https://opencv.org/) for video processing capabilities.
