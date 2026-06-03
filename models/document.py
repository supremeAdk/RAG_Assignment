from sqlalchemy import Column, Integer, String

from db.sqlite_db import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    chunk_strategy = Column(String)