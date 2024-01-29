import cv2
import torch

class YoloDetector:
    def __init__(self):
        # Load the pre-trained YOLO model
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    def preprocess_for_yolo(self, img):
        # YOLO expects BGR images
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img_rgb

    def detect_dominoes(self, img):
        # Preprocess the image for YOLO
        processed_img = self.preprocess_for_yolo(img)
        
        # Perform detection
        results = self.model(processed_img)
        
        # Extract detected dominoes
        detected_dominoes = []
        for *xyxy, conf, cls in results.pred[0]:
            if cls == your_domino_class_id:  # Replace with the class ID for dominoes
                x1, y1, x2, y2 = map(int, xyxy)
                domino_img = img[y1:y2, x1:x2]
                detected_dominoes.append(domino_img)
        return detected_dominoes
