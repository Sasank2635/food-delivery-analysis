from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.core.config import CORS_ORIGINS
from api.core.errors import AppError, app_error_handler
from api.routes.analysis import router

app = FastAPI(title="Food Delivery Analysis API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(AppError, app_error_handler)
app.include_router(router)
