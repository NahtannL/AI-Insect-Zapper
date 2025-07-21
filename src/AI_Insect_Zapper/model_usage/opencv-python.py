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
from ai_insect_zapper.model_usage.gpio_utils import SimpleGPIO

g_streamer = (
    'v4l2src device=/dev/video0 ! '
    'image/jpeg, width=3840, height=2160, framerate=30/1 ! '
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

    cv2.namedWindow('camera', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('camera', 1920, 1080)

    # SIO = SimpleGPIO()
    # SIO.setup_gpio([12])
    # SIO.setup_pwm({33: 1000.00})

    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret:
            results = model(frame)

            for result in results:
                class_ids = result.boxes.cls.tolist()
                for class_id in class_ids:
                    if model.names[class_id] == 'People':
                        print('FOUND')

            # draw boxes around detected objects
            annotated_frame = results[0].plot()

            cv2.imshow('camera', annotated_frame)

            if (cv2.waitKey(1) & 0xFF == ord('q')):
                break

    SIO.clean()
    cap.release()
    cv2.destroyAllWindows()

if (__name__ == '__main__'):
    image_detection_annotation(gstreamer_cli=g_streamer, model_path='../../../models/rev2/best.pt')