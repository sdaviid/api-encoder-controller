from fastapi import APIRouter
from app.api.routes import route_server
from app.api.routes import route_file


api_router = APIRouter()
api_router.include_router(route_server.router, prefix="/server", tags=["server"])
api_router.include_router(route_file.router, prefix="/file", tags=["file"])
