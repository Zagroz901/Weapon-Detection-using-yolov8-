# app/model.py
from ultralytics import YOLO
import io
import cv2
import numpy as np
class WeaponDetectionModel:
    def __init__(self, model_path: str):
        self.model = YOLO(model_path)

    def predict(self, image_data: bytes):
        try:
            image_array = np.frombuffer(image_data, np.uint8)
            image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

            results = self.model(image)

            detections = []
            for box in results[0].boxes:
                label = results[0].names[int(box.cls)]
                confidence = float(box.conf)
                bbox = box.xyxy.cpu().numpy().astype(int).tolist()

                if len(bbox[0]) == 4:
                    x_min, y_min, x_max, y_max = bbox[0][0],bbox[0][1],bbox[0][2],bbox[0][3]
                    detections.append({
                        "label": label,
                        "confidence": confidence,
                        "bbox": bbox
                    })

                    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)
                    text = f"{label} {confidence:.2f}"
                    cv2.putText(image, text, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                else:
                    print(f"Unexpected bbox format: {bbox}")

            _, buffer = cv2.imencode('.jpg', image)
            output_image = io.BytesIO(buffer)

            return detections, output_image
        except Exception as e:
            print(f"Prediction error: {e}")
            return [], None

weapon_detector = WeaponDetectionModel("app/Weights/wepon_weight.pt")
