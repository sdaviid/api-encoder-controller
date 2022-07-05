from sqlalchemy import(
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.types import(
    Date,
    Boolean,
    Time,
    DateTime
)
from sqlalchemy.orm import(
    relationship,
    backref
)
from app.models.base import ModelBase
from app.core.database import Base
from datetime import datetime



class File(ModelBase, Base):
    __tablename__ = "file"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    server = Column(Integer)
    date_created = Column(DateTime, default=datetime.utcnow())


    @classmethod
    def add_file(cls, session, name, server):
        file = File()
        file.name = name
        file.server = server
        session.add(file)
        session.commit()
        session.refresh(file)
        return File.find_by_id(session=session, id=file.id)



    @classmethod
    def add(cls, session, data):
        file = File()
        file.name = data.name
        file.server = data.server
        session.add(file)
        session.commit()
        session.refresh(file)
        return File.find_by_id(session=session, id=file.id)


    @classmethod
    def find_by_id(cls, session, id):
        try:
            return session.query(File).filter_by(id=id).one()
        except Exception as err:
            print(f'model.file.find_by_id exception - {err}')
        return False

    @classmethod
    def find_by_name(cls, session, name):
        try:
            return session.query(File).filter_by(name=name).one()
        except Exception as err:
            print(f'model.file.find_by_name exception - {err}')
        return False