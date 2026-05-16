# fastapi_ai/services/ai_service.py

import io
from PIL import Image
from ultralytics import YOLO

CATEGORIES = {
    "Plastic": {
        "description": "This is a plastic item. Rinse it and place in the yellow recycling bin.",
        "recycling_bin": "Yellow bin",
        "color_hex": "#FFC107",
    },
    "Paper & Cardboard": {
        "description": "This is paper or cardboard. Flatten boxes and place in the blue paper bin.",
        "recycling_bin": "Blue bin",
        "color_hex": "#2196F3",
    },
    "Metal": {
        "description": "This is a metal item. Rinse it and place in the grey metal bin.",
        "recycling_bin": "Grey bin",
        "color_hex": "#9E9E9E",
    },
    "Battery": {
        "description": "HAZARDOUS! Never put in regular trash. Take to a designated red battery collection point.",
        "recycling_bin": "Red bin",
        "color_hex": "#F44336",
    },
    "Glass": {
        "description": "This is glass. Remove lids, rinse, and place in the blue glass bin.",
        "recycling_bin": "Blue bin",
        "color_hex": "#00BCD4",
    },
}

# Veri setindeki class id sırası
CLASS_NAMES = ["Battery", "Cardboard", "Glass", "Metal", "Paper", "Plastic"]

CONF_THRESHOLD = 0.25

_model = None

def load_model():
    global _model
    try:
        _model = YOLO("models/best.pt")
        print("✅ YOLO modeli yüklendi.")
    except Exception as e:
        print(f"❌ Model yüklenemedi: {e}")
        _model = None

load_model()


async def classify_waste_image(image_bytes: bytes):
    try:
        if _model is None:
            print("Model yüklü değil.")
            return None

        img = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        results = _model.predict(img, imgsz=640, conf=CONF_THRESHOLD, verbose=False)

        if not results or len(results[0].boxes) == 0:
            return None

        # En yüksek confidence'lı tespiti al
        boxes       = results[0].boxes
        confidences = boxes.conf.tolist()
        class_ids   = boxes.cls.tolist()

        best_idx    = confidences.index(max(confidences))
        best_conf   = round(confidences[best_idx], 4)
        best_cls_id = int(class_ids[best_idx])
        best_cls    = CLASS_NAMES[best_cls_id]

        # Paper ve Cardboard'u frontend için birleştir
        if best_cls in ["Cardboard", "Paper"]:
            best_cls = "Paper & Cardboard"

        info = CATEGORIES[best_cls]

        return {
            "category":      best_cls,
            "confidence":    best_conf,
            "description":   info["description"],
            "recycling_bin": info["recycling_bin"],
            "color_hex":     info["color_hex"],
        }

    except Exception as e:
        print(f"classify error: {e}")
        return None
