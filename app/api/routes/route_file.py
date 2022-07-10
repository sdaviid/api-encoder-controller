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

from app.models.domain.server import Server
from app.models.schemas.file import(
    FileAddUpload,
    FileAdd,
    FileDetail
)


from app.core.database import get_db

from app.api.deps import(
    allow_create_resource
)


from app.service.server import get_instance_server_manager


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
    temp_upload = get_instance_server_manager().upload_server(data.url)
    if temp_upload:
        return temp_upload
    else:
        return {
            "error": True,
            "message": "Failed add file"
        }



@router.get(
    '/status',
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(allow_create_resource)]
)
def status_by_id(
    id: int,
    response: Response,
    db: Session = Depends(get_db)
):
    temp_file = File.find_by_id(session=db, id=id)
    if temp_file:
        temp_server = Server.find_by_id(session=db, id=temp_file.server)
        if temp_server:
            temp_status = get_instance_server_manager().status_file(name=temp_file.name, server_uri=temp_server.uri)
            if temp_status:
                return temp_status
            else:
                return {
                    "error": True,
                    "message": "Couldnt get status from file"
                }
        else:
            return {
                "error": True,
                "message": "Couldnt get server"
            }
    else:
        return {
            "error": True,
            "message": "Couldnt find file"
        }


@router.delete(
    '/delete/{hash}',
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(allow_create_resource)]
)
def delete_by_name(
    hash: str,
    response: Response,
    db: Session = Depends(get_db)
):
    temp_file = File.find_by_name(session=db, name=hash)
    if temp_file:
        temp_server = Server.find_by_id(session=db, id=temp_file.server)
        if temp_server:
            temp_status = get_instance_server_manager().delete_file(name=temp_file.name, server_uri=temp_server.uri)
            if temp_status:
                if File.delete(session=db, id=temp_file.id):
                    return temp_status
                else:
                    return {
                        "error": True,
                        "message": "Failed delete id from database"
                    }
            else:
                return {
                    "error": True,
                    "message": "Couldnt get server"
                }
        else:
            return {
                "error": True,
                "message": "Couldnt find file"
            }



@router.get(
    '/status/{hash}',
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(allow_create_resource)]
)
def status_by_name(
    hash: str,
    response: Response,
    db: Session = Depends(get_db)
):
    temp_file = File.find_by_name(session=db, name=hash)
    if temp_file:
        temp_server = Server.find_by_id(session=db, id=temp_file.server)
        if temp_server:
            temp_status = get_instance_server_manager().status_file(name=temp_file.name, server_uri=temp_server.uri)
            if temp_status:
                return temp_status
            else:
                return {
                    "error": True,
                    "message": "Couldnt get status from file"
                }
        else:
            return {
                "error": True,
                "message": "Couldnt get server"
            }
    else:
        return {
            "error": True,
            "message": "Couldnt find file"
        }