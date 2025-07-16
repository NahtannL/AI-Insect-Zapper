# Laser Insect Detection and Zapper with AI Vision
With the many annoyances in our daily lives, certain insects are at the top of
the list, such as mosquitoes and flys. To combat this, this project aims to
detect the presence of such insects in a certain area in front of the device,
and zap the insect if the right conditions are met.

## Materials
* NVIDIA Jetson Orin Nano
* 4W Laser Module
* 12MP Camera Module w/ Auto Focus

## Installation
There are some requirements that need to be met before you can run the model.
The following should be installed on your computer:

* Pyenv (not required)
* Poetry

### Python Version
This project was built using Python 3.13.5, which can be installed with pyenv,
or a similar service.

### Poetry Configuration
After cloning the repo into a folder, install ultralytics and its dependencies
with their [guide](https://docs.ultralytics.com/quickstart/).

## Computer Vision and Deep Learning
To ensure only insects are zapped and humans that enter the field of vision are
kept safe, artificial intelligence is trained on a custom YOLO11 model for
multi-object tracking. YOLO11 is one of Ultralytic's many models that provides
efficient object detection, tracking, etc.

## NVIDIA Jetson Orin Nano
With the many devices out there that can be used for AI deployment, there were
many options that we could have chosen. The Jetson was ultimately chosen given
its unrivaled software support with Artificial Intelligence.