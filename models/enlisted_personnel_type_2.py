from sqlalchemy import Column, DateTime, Integer, String , BigInteger, TIMESTAMP, Date, Text , Numeric
from sqlalchemy.sql import func
from database.base import Base
from sqlalchemy.orm import Session
from typing import List, Dict
import pytz
# from datetime import Datetime


tz = pytz.timezone("Asia/Bangkok")

class EnlistedPersonnelType2(Base):
    __tablename__ = "enlisted_personnel_type_2"
    __table_args__ = {"schema": "public"}
    id = Column(BigInteger, primary_key=True)

    id_cardno = Column(String(13), nullable=False)
    title = Column(String(50))
    first_name = Column(String(100))
    last_name = Column(String(100))
    previous_first_name = Column(String(100))
    previous_last_name = Column(String(100))

    birth_date = Column(Date)
    age_year = Column(Integer)
    religion = Column(String(50))
    blood_type = Column(String(10))

    weight_kg = Column(Numeric(5, 2))
    height_cm = Column(Numeric(5, 2))

    marital_status = Column(String(50))
    military_origin = Column(Text)

    military_address_no = Column(String(50))
    military_address_moo = Column(String(10))
    military_address_soi = Column(String(100))
    military_address_road = Column(String(100))
    military_province = Column(String(100))
    military_amphoe = Column(String(100))
    military_tambon = Column(String(100))

    conscription_year_be = Column(Integer)

    sd43_document_no = Column(String(50))
    reserve_class = Column(String(50))

    home_address_text = Column(Text)
    home_address_no = Column(String(50))
    home_address_moo = Column(String(10))
    home_address_soi = Column(String(100))
    home_address_road = Column(String(100))
    home_province = Column(String(100))
    home_amphoe = Column(String(100))
    home_tambon = Column(String(100))
    home_postcode = Column(String(10))
    # created_at = Column(DateTime,default=lambda: datetime.now(tz))
    # updated_at = Column(DateTime,default=lambda: datetime.now(tz), onupdate=lambda: datetime.now(tz))   
    # created_at = Column(TIMESTAMP, server_default=func.now())
    # updated_at = Column(TIMESTAMP, server_default=func.now())
    created_at = Column(DateTime(timezone=True),server_default=func.now())
    updated_at = Column(
    DateTime(timezone=True),
    server_default=func.now(),   # ตอน INSERT
    onupdate=func.now()          # ตอน UPDATE
)

    def __repr__(self):
        return (
            f"<EnlistedPersonnelType2(id={self.id}, "
            f"id_cardno='{self.id_cardno}', "
            f"first_name='{self.first_name}', "
            f"last_name='{self.last_name}')>"
        )
    @classmethod
    def bulk_create(cls, session: Session, rows: List[Dict]):
        objs = []
        cols = {c.name for c in cls.__table__.columns}
        for row in rows:
            clean = {k: v for k, v in row.items() if k in cols and k != "id"}
            objs.append(cls(**clean))

        session.add_all(objs)