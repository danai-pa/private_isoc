from sqlalchemy import Column, DateTime, Integer, String , BigInteger, TIMESTAMP, Date, Text , Numeric
from sqlalchemy.sql import func
from database.base import Base
from sqlalchemy.orm import Session
from typing import List, Dict
import pytz
# from datetime import Datetime


tz = pytz.timezone("Asia/Bangkok")

class DefenseCivilServant(Base):
    __tablename__ = "defense_civil_servant"
    __table_args__ = {"schema": "public"}

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    id_cardno = Column(String(13), nullable=False)
    title = Column(String(50))
    first_name = Column(String(100))
    last_name = Column(String(100))
    previous_first_name = Column(String(100))
    previous_last_name = Column(String(100))

    birth_date = Column(Date)
    age = Column(Integer)

    nationality = Column(String(50))
    gender = Column(String(20))
    religion = Column(String(50))
    blood_type = Column(String(20))
    marital_status = Column(String(50))

    employee_type = Column(String(100))
    employee_group = Column(String(100))
    employee_no_10 = Column(String(10))

    department = Column(String(255))
    unit = Column(String(255))
    position = Column(String(255))
    rate = Column(String(100))

    home_address_no = Column(String(50))
    home_address_moo = Column(String(10))
    home_address_soi = Column(String(100))
    home_address_road = Column(String(100))
    home_province = Column(String(100))
    home_amphoe = Column(String(100))
    home_tambon = Column(String(100))
    home_zipcode = Column(String(10))

    education_level = Column(String(255))
    major = Column(String(255))

    contact_address_no = Column(String(50))
    contact_address_moo = Column(String(10))
    contact_address_soi = Column(String(100))
    contact_address_road = Column(String(100))
    contact_province = Column(String(100))
    contact_amphoe = Column(String(100))
    contact_tambon = Column(String(100))
    contact_postcode = Column(String(10))

    phone = Column(String(20))
    email = Column(String(255))
    line_id = Column(String(100))
    facebook = Column(Text)
    other_social_media = Column(Text)

    xlock = Column(String(4), default="x")

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())       # ตอน UPDATE


    def __repr__(self):
        return (
            f"<EnlistedPersonnelType2(id={self.id}, "
            f"id_cardno='{self.citizen_id}', "
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
