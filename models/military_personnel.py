from sqlalchemy import Column, Integer, String , BigInteger, TIMESTAMP, Date, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from database.base import Base  
from typing import List, Dict

class MilitaryPersonnel(Base):
    __tablename__ = "military_personnel"
    __table_args__ = {"schema": "public"}

    id = Column(Integer, primary_key=True, autoincrement=True)

    citizen_id = Column(String(20))
    title = Column(String(50))
    first_name = Column(String(100))
    last_name = Column(String(100))

    previous_first_name = Column(String(100))
    previous_last_name = Column(String(100))

    birth_date_be = Column(Date)
    birth_date_ce = Column(Date)
    age_year = Column(Integer)

    nationality = Column(String(50))
    religion = Column(String(50))
    basic_education = Column(String(255))
    occupation = Column(String(255))
    special_skills = Column(Text)
    notable_mark = Column(Text)

    home_address_no = Column(String(50))
    home_address_moo = Column(String(10))
    home_address_soi = Column(String(100))
    home_address_road = Column(String(100))
    home_province = Column(String(100))
    home_amphor = Column(String(100))
    home_tambon = Column(String(100))
    home_postcode = Column(String(10))

    phone_number = Column(String(20))

    father_citizen_id = Column(String(20))
    father_title = Column(String(50))
    father_first_name = Column(String(100))
    father_last_name = Column(String(100))
    father_nationality = Column(String(50))

    mother_citizen_id = Column(String(20))
    mother_first_name = Column(String(100))
    mother_last_name = Column(String(100))
    mother_nationality = Column(String(50))

    military_domicile_type = Column(String(100))

    military_address_no = Column(String(50))
    military_address_moo = Column(String(10))
    military_address_soi = Column(String(100))
    military_address_road = Column(String(100))
    military_province = Column(String(100))
    military_amphor = Column(String(100))
    military_tambon = Column(String(100))

    sd9_document_no = Column(String(50))
    sd9_received_date = Column(Date)

    sd9_enroll_year = Column(Integer)
    sd9_enroll_date = Column(Date)

    conscription_result_status = Column(String(100))

    sd43_issue_no = Column(String(50))
    sd43_document_no = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    def __repr__(self):
        return (
            f"<MilitaryStudent(id={self.id}, "
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
