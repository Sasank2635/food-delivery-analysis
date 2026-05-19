import os

MAX_UPLOAD_BYTES = 10 * 1024 * 1024  # 10 MB
ALLOWED_EXT = {".csv"}
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
