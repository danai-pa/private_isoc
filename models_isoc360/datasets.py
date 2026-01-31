from sqlalchemy import Column, Integer, String , BigInteger, TIMESTAMP, Date, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from database.base import Base  
from typing import List, Dict
from datetime import datetime
class clsDatasets(Base):
    __tablename__ = "datasets"
    __table_args__ = {"schema": "public"}

    id = Column(Text, primary_key=True)

    name = Column(Text, nullable=False)
    detail = Column(Text)

    unit_owner_id = Column(Text, nullable=False)
    category_id = Column(Text, nullable=False)

    createdBy = Column(Text, nullable=False,default="sqlachemy")
    createdAt = Column(
    TIMESTAMP(timezone=False),
    server_default=func.now(),
    nullable=False
)

    updatedBy = Column(Text, nullable=False,default="danai.p")
    updatedAt = Column(
    TIMESTAMP(timezone=False),
    server_default=func.now(),   # ✅ เพิ่ม default
    onupdate=func.now(),         # ✅ เวลา update ให้เปลี่ยนเอง
    nullable=False
)

    deletedBy = Column(Text)
    deletedAt = Column(TIMESTAMP(timezone=False))

    metadata_json = Column("metadata", Text)

    type_id = Column(Text, nullable=False)
    security_level = Column(Text)

    def __repr__(self):
        return (
            f"<MilitaryStudent(id={self.id}, "
            f"name='{self.name}', "
            f"detail='{self.detail}', "
            f"createdBy='{self.createdBy}')>"
        )


    @classmethod
    def bulk_create(cls, session: Session, rows: List[Dict]):
        objs = []
        cols = {c.name for c in cls.__table__.columns}

        now = datetime.now()

        for row in rows:
            clean = {k: v for k, v in row.items() if k in cols}

            # ถ้าไม่มี createdAt / updatedAt ให้เติมให้เอง
            if "createdAt" in cols and not clean.get("createdAt"):
                clean["createdAt"] = now

            if "updatedAt" in cols and not clean.get("updatedAt"):
                clean["updatedAt"] = now

            objs.append(cls(**clean))

        session.add_all(objs)
        session.commit()

