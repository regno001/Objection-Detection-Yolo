from ultralytics import YOLO
import cv2
model = YOLO('../Yolo-Weights/yolov8n.pt')
result = model("../images/bikes.mp4",show=True)
cv2.waitKey(0)