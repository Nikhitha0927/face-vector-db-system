from sqlalchemy import Column, Integer, Text
from pgvector.sqlalchemy import Vector
from db import Base

class Face(Base):
    __tablename__ = "faces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    encoding = Column(Vector(128))