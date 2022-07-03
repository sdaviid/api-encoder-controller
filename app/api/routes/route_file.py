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


from app.models.domain.file import(
    File
)
from app.models.schemas.file import(
    FileAddUpload,
    FileAdd,
    FileDetail
)


from app.core.database import get_db

from app.api.deps import(
    allow_create_resource
)


#from app.service.server import upload_server


router = APIRouter()




@router.post(
    '/add',
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(allow_create_resource)]
)
def add(
    data: FileAddUpload,
    response: Response,
    db: Session = Depends(get_db)
):
    return File.add(session=db, data=data)
   

# @router.post(
#     '/add',
#     status_code=status.HTTP_200_OK,
#     dependencies=[Depends(allow_create_resource)]
# )
# def add(
#     data: FileAddUpload,
#     response: Response,
#     db: Session = Depends(get_db)
# ):
#     temp_file = File.add(session=db, data=data)
#     if temp_file:
#         return temp_file
#     else:
#         return {
#             "error": True,
#             "message": "Failed add file"
#         }