import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
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

# Serve React build — only if ui/dist exists (production)
_UI_DIST = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ui", "dist")

if os.path.isdir(_UI_DIST):
    app.mount("/assets", StaticFiles(directory=os.path.join(_UI_DIST, "assets")), name="assets")

    @app.get("/{full_path:path}", include_in_schema=False)
    async def serve_spa(_: str):
        return FileResponse(os.path.join(_UI_DIST, "index.html"))
