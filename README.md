# Domino Dot Counting Model

## Overview
This project aims to develop a machine learning model capable of detecting dominoes in images and counting the number of dots on each. The model will be trained on a dataset of annotated images of dominoes.

## Dataset
The dataset should consist of annotated images of dominoes. Each image must have bounding box annotations around each domino and labels indicating the number of dots.

## Requirements
- Python 3.x
- TensorFlow 2.x
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

## Structure
- `main.py`: Entry point for training and evaluating the model.
- `model/`: Contains the scripts for the model architecture and data processing.
- `data/`: Directory for storing the dataset.
- `utils/`: Utility scripts for various tasks like data loading and preprocessing.

## Contributing
Contributions to this project are welcome. Please follow the standard fork-and-pull request workflow.
