# Domino Dot Counting Model

## Overview
This project aims to develop a machine learning model capable of detecting dominoes in images and counting the number of dots on each. The model will be trained on a dataset of annotated images of dominoes.

## Dataset
The dataset should consist of annotated images of dominoes. Each image must have bounding box annotations around each domino and labels indicating the number of dots.

## Requirements
- Python 3.x
- PyTorch (for YOLO)
- YOLOv3 or YOLOv5 pre-trained weights
- OpenCV
- NumPy
- Pandas
- Other dependencies listed in `requirements.txt`

## Installation
1. Clone the repository:
   
```git clone [repository URL]```

2. Install the required packages:

```pip install -r requirements.txt```

## Usage
To train the model, run:

```python main.py --train```

To evaluate the model, run:

```python main.py --evaluate```

## Summary
- First, use OpenCV for preprocessing images, and then apply the YOLO model for domino detection.
- After detecting dominoes, count the dots on each domino using image processing techniques.

- The YOLO model (yolo_detector.py) is responsible for detecting dominoes in the images.
- The image processor (image_processor.py) applies additional image processing to count the dots on each detected domino.
- The main.py script orchestrates the process, calling the YOLO detector and the image processor for each image.
- The data_loader.py is updated to load images using OpenCV, suitable for the YOLO model input.

## Structure
- `main.py`: Entry point for the entire process.
- `model/yolo_detector.py`: Script for the YOLO-based domino detection.
- `utils/image_processor.py`: Utility for image preprocessing and dot counting.

## Contributing
Contributions to this project are welcome. Please follow the standard fork-and-pull request workflow.
