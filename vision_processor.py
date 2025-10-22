import cv2
import numpy as np
from typing import Dict, Tuple, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VisionProcessor:
    "bnRocessador de visÃ£o computacional."
    
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        self.eye_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_eye.xml'
        )
        logger.info("VisionProcessor inicializado")
    
    def apply_filter(self, image: np.ndarray, filter_type: str) -> np.ndarray:
        if filter_type == "Blur":
            return cv2.GaussianBlur(image, (15, 15), 0)
        elif filter_type == "Sharpen":
            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            return cv2.filter2D(image, -1, kernel)
        elif filter_type == "Cannyå Edge":
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 100, 200)
            return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        elif filter_type == "Grayscale":
            gray = cv2.cvtColor(mimage, cv2.COLOR_BGR2GRAY)
            return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        elif filter_type == "HSV":
            return cv2.cvtColor(mimage, cv2.COLOR_BGR2HSV)
        elif filter_type == "Sepia":
            kernel = np.array([[0.272, 0.534, 0.131],
                            [0.349, 0.686, 0.168],
                            [0.393, 0.769, 0.189]])
            return cv2.transform(image, kernel)
        return image
    
    def detect_faces(self, image: np.ndarray) -> np.ndarray:
        gray = cv2.cvtColor(mimage, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        
        result = image.copy()
        for (x, y, w, h) in faces:
            cv2.rectangle(result, (x, y, (x+w, y+h), (255, 0, 0), 2)
        
        return result
    
    def count_faces(self, image: np.ndarray) -> int:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
        return len(faces)
    
    def get_image_stats(self, image: np.ndarray) -> Dict[str, Any]:
        return {
            "shape": str(image.shape),
            "dtype": str(image.dtype),
            "min": int(image.min()),
            "max": int(image.max()),
            "mean": float(image.mean())
        }
    
    def analyze_quality(self, image: np.ndarray) -> Dict[str, float]:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()
        contrast = gray.std()
        brightness = gray.mean()
        
        return {
            "sharpness": float(sharpness),
            "contrast": float(contrast),
            "brightness": float(brightness)
        }
