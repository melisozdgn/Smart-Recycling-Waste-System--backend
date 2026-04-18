# fastapi_ai/services/ai_service.py
# Sadece 5 kategori: Plastic | Paper & Cardboard | Metal | Battery | Glass
import io
import random
from PIL import Image
import numpy as np

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

_model = None

def load_model():
    global _model
    try:
        # TensorFlow modeli hazir olunca:
        # import tensorflow as tf
        # _model = tf.keras.models.load_model("models/waste_classifier.h5")
        # Sinif sirasi egitimde kullanilan sirayla ayni olmali:
        # 0=Battery, 1=Glass, 2=Metal, 3=Paper & Cardboard, 4=Plastic

        # PyTorch modeli hazir olunca:
        # import torch
        # _model = torch.load("models/waste_classifier.pt", map_location="cpu")
        # _model.eval()
        print("Model dosyasi bulunamadi - MOCK mod aktif")
    except Exception as e:
        print(f"Model yuklenemedi: {e} - MOCK mod aktif")

load_model()


async def classify_waste_image(image_bytes: bytes):
    try:
        img     = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img_arr = np.array(img.resize((224, 224))) / 255.0

        if _model is not None:
            pass  # Gercek inference buraya gelecek

        # MOCK mod
        category_name = random.choice(list(CATEGORIES.keys()))
        confidence    = round(random.uniform(0.78, 0.98), 4)

        if confidence < 0.40:
            return None

        info = CATEGORIES[category_name]
        return {
            "category":      category_name,
            "confidence":    confidence,
            "description":   info["description"],
            "recycling_bin": info["recycling_bin"],
            "color_hex":     info["color_hex"],
        }
    except Exception as e:
        print(f"classify error: {e}")
        return None
