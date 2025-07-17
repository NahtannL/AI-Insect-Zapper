# Used for converting the custom YOLO11 model to a TensorRT model for better
# performance when used on the Jetson Orin Nano.

from ultralytics import YOLO

model = YOLO('../runs/detect/train5/weights/best.pt')

model.export(format='engine')

tensorrt_model = YOLO('../runs/detect/train5/weights/best.engine')