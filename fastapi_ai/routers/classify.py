# fastapi_ai/routers/classify.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
from services.ai_service import classify_waste_image

router = APIRouter()

class ClassificationResult(BaseModel):
    category:     str
    confidence:   float
    description:  str
    recycling_bin: str
    color_hex:    str

@router.post("/classify", response_model=ClassificationResult)
async def classify_image(file: UploadFile = File(...)):
    """
    Görüntüyü AI modeli ile sınıflandırır.
    - JPEG veya PNG kabul eder
    - Kategori, güven skoru, açıklama ve doğru çöp kutusu bilgisini döndürür
    """
    # Dosya format kontrolü (FR-2)
    if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        raise HTTPException(
            status_code=400,
            detail="Only JPEG or PNG images are accepted."
        )

    contents = await file.read()

    
    if len(contents) > 10 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File size exceeds 10MB.")

    result = await classify_waste_image(contents)

    if result is None:
        raise HTTPException(
            status_code=422,
            detail="Could not identify this item. Please take a clearer photo."
        )

    return result
