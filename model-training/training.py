from ultralytics import YOLO

model = YOLO('yolo11n.yaml')

results = model.train(data='data.yaml', epochs=100, imgsz=640, device=0)