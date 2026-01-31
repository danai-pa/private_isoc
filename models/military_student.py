from sqlalchemy import Column, Integer, String , BigInteger, TIMESTAMP, Date, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from database.base import Base  
from typing import List, Dict

class MilitaryStudent(Base):
    __tablename__ = "military_student"  # 👉 เปลี่ยนชื่อ table ให้ตรงของจริง
    __table_args__ = {"schema": "public"}
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    id_cardno = Column(String(13), nullable=False)
    title = Column(String(50))
    first_name = Column(String(100))
    last_name = Column(String(100))
    previous_first_name = Column(String(100))
    previous_last_name = Column(String(100))
    birth_date = Column(Date)
    age_year = Column(Integer)
    gender = Column(String(20))
    nationality = Column(String(50))
    religion = Column(String(50))
    ror_dor_student_code = Column(String(50))
    ror_dor_enroll_date = Column(Date)
    ror_dor_enroll_academy = Column(Integer)
    military_force = Column(String(100))
    status = Column(String(50))
    study_year = Column(String(50))
    institution_name = Column(String(255))
    institution_address_text = Column(Text)
    institution_address_no = Column(String(50))
    institution_address_moo = Column(String(10))
    institution_address_soi = Column(String(100))
    institution_address_road = Column(String(100))
    institution_province = Column(String(100))
    institution_district = Column(String(100))
    institution_subdistrict = Column(String(100))
    institution_postcode = Column(String(10))
    rd25_document_no = Column(String(50))
    current_academic_year = Column(Integer)
    transferred_institution_name = Column(String(255))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    def __repr__(self):
        return (
            f"<MilitaryStudent(id={self.id}, "
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
