# For training the model using YOLO11 as the base.
#
# The 'data.yaml' file contains the file paths to the dataset used for
# training. The completed model is stored in the runs folder found in the root
# of this project (AI-Insect-Zapper/runs/...)

from ultralytics import YOLO

model = YOLO('yolo11n.yaml')

results = model.train(data='data.yaml', epochs=100, imgsz=640, device=0)