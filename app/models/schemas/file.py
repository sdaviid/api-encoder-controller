from datetime import date
from pydantic import Field
from datetime import datetime
from app.models.schemas.base import baseSchema


class FileAddUpload(baseSchema):
    url: str


class FileAdd(baseSchema):
    name: str
    url: str
    server: int



class FileDetail(baseSchema):
    id: int
    name: str
    url: str
    server: int
    date_created: datetime
