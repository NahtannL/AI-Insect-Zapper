"""Object Detection with OpenCV and Gstreamer.

Utilizes Gstreamer and its integration with OpenCV to enable object detection
via an Ultralytics trained (custom) model.

Exports:
    image_detection_annotation() - Capture video stream, run YOLO model, and
        display annotations

Example:
    image_detection_annotation('gstreamer pipeline', 'path/to/model')
"""


import cv2
from ultralytics import YOLO

g_streamer = (
    'v4l2src device=/dev/video0 ! '
    'image/jpeg, width=1920, height=1080, framerate=60/1 ! '
    'jpegdec ! '
    'videoconvert ! '
    'video/x-raw, format=BGR ! '
    'appsink drop=1'
)

def image_detection_annotation(gstreamer_cli, model_path):
    """Captures a video stream in gstreamer and performs object detection.

    Keyword arguments:
        gstreamer_cli -- gstreamer cli component
        model_path -- relative path to model
    """

    model = YOLO(model_path)
    cap = cv2.VideoCapture(gstreamer_cli, cv2.CAP_GSTREAMER)

    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret:
            results = model(frame)

            # draw boxes around detected objects
            annotated_frame = results[0].plot()

            cv2.imshow('camera', annotated_frame)

            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break

    cap.release()
    cv2.destroyAllWindows()

if (__name__ == '__main__'):
    image_detection_annotation(gstreamer_cli=g_streamer, model_path='../../models/best.pt')