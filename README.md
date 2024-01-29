# Domino Dot Counting Model

## Overview
This project develops a machine learning model to detect dominoes in images and count the number of dots on each. It utilizes YOLO (You Only Look Once) for domino detection and OpenCV for image processing.

## Dataset
The dataset should consist of annotated images of dominoes. Each image must have bounding box annotations around each domino and labels indicating the number of dots.

## Requirements
- Python 3.x
- OpenCV
- PyTorch and Torchvision
- NumPy
- Pillow
- Other dependencies listed in `requirements.txt`

## Installation
1. Clone the repository:
   
```git clone [repository URL]```

2. Install the required packages:

```pip install -r requirements.txt```

## Usage
To process images and count domino dots, run:

```python main.py --process```

To evaluate the model, run:

```python main.py --evaluate```

## Summary
- The project uses OpenCV for preprocessing images to prepare them for object detection.
- YOLO (You Only Look Once), implemented in `yolo_detector.py`, is used for accurate and efficient domino detection in the images.
- Once dominoes are detected, `image_processor.py` applies image processing techniques to count the dots on each detected domino.
- `main.py` serves as the orchestration script, leveraging both the YOLO model and the image processing functionality to process images and count domino dots.
- `data_loader.py` has been adapted to load and handle images using OpenCV, ensuring compatibility with the YOLO model's input requirements.
- The TensorFlow-based `evaluator.py` is no longer needed in this workflow, as the project has transitioned to a focus on YOLO and OpenCV.

## Project Structure
- `main.py`: Entry point for processing images.
- `model/yolo_detector.py`: YOLO-based domino detection.
- `utils/image_processor.py`: Image processing for dot counting.
- `utils/data_loader.py`: Utility for loading images.
- `data/`: Directory to store the dataset.

## Contributing
Contributions to this project are welcome. Please follow the standard fork-and-pull request workflow.

## Contributing
Contributions to this project are welcome. Please follow the standard fork-and-pull request workflow.
