import argparse
from model.yolo_detector import YoloDetector
from utils.image_processor import process_and_count_dots
from utils.data_loader import load_dataset

def process_images():
    # Load dataset
    images = load_dataset('data/images')

    # Initialize the YOLO model
    yolo_model = YoloDetector()

    # Process each image
    for img in images:
        # Detect dominoes
        detected_dominoes = yolo_model.detect_dominoes(img)
        
        # Count dots on each domino
        total_dots = process_and_count_dots(detected_dominoes)

        # Output the results
        print(f"Total dots in image: {total_dots}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Domino Dot Counting')
    parser.add_argument('--process', action='store_true', help='Process images to count domino dots')

    args = parser.parse_args()

    if args.process:
        process_images()
