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



class Server(ModelBase, Base):
    __tablename__ = "server"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    uri = Column(String(255))
    date_created = Column(DateTime, default=datetime.utcnow())


    @classmethod
    def add(cls, session, data):
        server = Server()
        server.name = data.name
        server.uri = data.uri
        session.add(server)
        session.commit()
        session.refresh(server)
        return Server.find_by_id(session=session, id=server.id)



    @classmethod
    def find_by_id(cls, session, id):
        try:
            return session.query(Server).filter_by(id=id).one()
        except Exception as err:
            print(f'model.server.find_by_id exception - {err}')
        return False




