import os
from fastapi import APIRouter, UploadFile, File
from api.schemas.analysis import AnalysisResult
from api.services.pipeline import run_full_pipeline
from api.core.config import MAX_UPLOAD_BYTES, ALLOWED_EXT
from api.core.errors import AppError

router = APIRouter(prefix="/api")


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.post("/analyze", response_model=AnalysisResult)
async def analyze(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in ALLOWED_EXT:
        raise AppError("INVALID_EXT", f"File must be .csv, got '{ext}'")

    csv_bytes = await file.read()

    if len(csv_bytes) > MAX_UPLOAD_BYTES:
        raise AppError("FILE_TOO_LARGE", "File exceeds 10 MB limit", status=413)

    try:
        result = run_full_pipeline(csv_bytes)
    except ValueError as e:
        raise AppError("INVALID_SCHEMA", str(e))

    return result
