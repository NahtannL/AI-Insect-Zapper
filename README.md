# Laser Insect Detection and Zapper with AI Vision
With the many annoyances in our daily lives, certain insects are at the top of
the list, such as mosquitoes and flies. To combat this, this project aims to
detect the presence of such insects in a certain area in front of the device,
and zap the insect if the right conditions are met.

## Materials
* NVIDIA Jetson Orin Nano
* 4W Laser Module
* 12MP Camera Module w/ Auto Focus
* Laser Stage Galvanometer
* N-MOSFET (e.g. IRLZ44N)

## Installation
There are some requirements that need to be met before you can run the model.
The following should be installed on your computer:

* Pyenv (not required)
* Poetry
* Ultralytics
* OpenCV (w/ GStreamer support)

### Python Version
This project was built using Python 3.10.12, which can be installed with pyenv,
or a similar service.

### Poetry Configuration
After cloning the repo into a folder, ensure poetry is using the correct version
of Python (3.10.12) with the following line:
```
$ poetry env use python3.10.12
```
After verifying poetry is using the right version of python, run
```
$ poetry install
```
to install the version of Ultralytics defined in `pyproject.toml`. Torch should
also be installed with their guide 
([torch](https://pytorch.org/get-started/locally/)).

## Computer Vision and Deep Learning
To ensure only insects are zapped and humans that enter the field of vision are
kept safe, artificial intelligence is trained on a custom YOLO11 model for
multi-object tracking. YOLO11 is one of Ultralytic's many models that provides
efficient object detection, tracking, etc.

## NVIDIA Jetson Orin Nano
With the many devices out there that can be used for AI deployment, there were
many options that we could have chosen. The Jetson was ultimately chosen given
its unrivaled software support with Artificial Intelligence.