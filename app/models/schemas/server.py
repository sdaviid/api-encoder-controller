from datetime import date
from pydantic import Field
from datetime import datetime
from app.models.schemas.base import baseSchema


class ServerAddUpload(baseSchema):
    uri: str
    name: str


class ServerAdd(baseSchema):
    uri: str
    name: str



class ServerDetail(baseSchema):
    id: int
    uri: str
    name: str
    date_created: datetime
