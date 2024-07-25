import enum
from sqlalchemy import Boolean, BigInteger, Column, Text,DateTime, Enum, ForeignKey, Integer, String, Numeric, UniqueConstraint, text, JSON
import strawberry

from database.db_conf import Base
    

class TestTable(Base):
    __tablename__ = "test_master"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    value = Column(String , nullable = False)

    def __repr__(self) -> str:
        return "<TestTable %r>" % self.id