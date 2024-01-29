import argparse
import tensorflow as tf
from model.domino_detector import DominoDetector
from utils.data_loader import load_dataset
from utils.evaluator import evaluate_model

def train_model():
    # Load dataset
    train_data, val_data = load_dataset('data/train', 'data/val')

    # Initialize the model
    model = DominoDetector()

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(train_data, validation_data=val_data, epochs=10)

def evaluate_model():
    # Load dataset
    test_data = load_dataset('data/test')

    # Initialize the model
    model = DominoDetector()

    # Load weights
    model.load_weights('path/to/saved_model')

    # Evaluate the model
    return evaluate_model(model, test_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train and Evaluate Domino Dot Counting Model')
    parser.add_argument('--train', action='store_true', help='Train the model')
    parser.add_argument('--evaluate', action='store_true', help='Evaluate the model')

    args = parser.parse_args()

    if args.train:
        train_model()
    elif args.evaluate:
        evaluate_model()
