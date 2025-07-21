"""Train a custom YOLO model using Ultralytics YOLO and a YAML dataset.

Exports:
    model_train() - Train YOLO model from a base YOLO model.

Example:
    $ python3 training.py 11 path/to/dataset.yaml
"""

import sys
from ultralytics import YOLO

def model_train(yolo_version, yaml_file_path):
    """Train a custom model based on a specified base YOLO model and dataset.
    
    Keyword arguments:
        yolo_version -- YOLO base model version number (eg. 11 for YOLO11)
        yaml_file_path -- relative path to yaml file
    """
    model = YOLO(f'yolo{yolo_version}n.pt')

    model.train(data=yaml_file_path, epochs=100, imgsz=640, device=0)

if (__name__ == '__main__'):
    if (len(sys.argv) < 3):
        print('Invalid arguments (Ex. training.py 11 "path/to/file")')
        exit()
    model_train(sys.argv[1], sys.argv[2])