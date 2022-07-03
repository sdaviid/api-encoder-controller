import os
from typing import List
from sqlalchemy.orm import Session
from fastapi import(
    Depends,
    Response,
    status,
    APIRouter,
    HTTPException
)
from fastapi.responses import JSONResponse


from app.models.domain.server import(
    Server
)
from app.models.schemas.server import(
    ServerAddUpload,
    ServerAdd,
    ServerDetail
)


from app.core.database import get_db

from app.api.deps import(
    allow_create_resource
)



router = APIRouter()



@router.post(
    '/add',
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(allow_create_resource)]
)
def add(
    data: ServerAddUpload,
    response: Response,
    db: Session = Depends(get_db)
):
    temp_server = Server.add(session=db, data=data)
    if temp_server:
        return temp_server
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Failed add server"
        )

