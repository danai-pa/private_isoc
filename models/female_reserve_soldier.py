from sqlalchemy import Column, Integer, String , BigInteger, TIMESTAMP, Date, Text , Numeric
from sqlalchemy.sql import func
from database.base import Base
from sqlalchemy.orm import Session
from typing import List, Dict

class female_reserve_soldier(Base):
    __tablename__ = "female_reserve_soldier"
    __table_args__ = {"schema": "public"}

    id = Column(BigInteger, primary_key=True, autoincrement=True)

    id_cardno = Column(String(13), nullable=False)
    rank = Column(String(50))
    type = Column(String(50))
    first_name = Column(String(100))
    last_name = Column(String(100))
    previous_first_name = Column(String(100))
    previous_last_name = Column(String(100))

    birth_date = Column(Date)
    age_year = Column(Integer)

    religion = Column(String(50))
    blood_type = Column(String(5))
    weight_kg = Column(Numeric(5, 2))
    height_cm = Column(Numeric(5, 2))

    marital_status = Column(String(50))
    origin = Column(String(100))

    military_force = Column(String(100))
    military_party = Column(String(100))
    military_branch = Column(String(100))
    military_category = Column(String(100))

    active_service_info = Column(Text)
    last_affiliation = Column(String(255))
    last_position = Column(String(100))

    home_address_text = Column(Text)
    home_address_no = Column(String(50))
    home_address_moo = Column(String(10))
    home_address_soi = Column(String(100))
    home_address_road = Column(String(100))
    home_province = Column(String(100))
    home_amphoe = Column(String(100))
    home_tambon = Column(String(100))
    home_postcode = Column(String(10))

    education_info = Column(Text)
    education_level = Column(String(100))
    education_major = Column(String(100))

    special_skills = Column(Text)
    occupation_info = Column(Text)
    current_occupation = Column(String(100))

    workplace_position = Column(String(100))
    workplace_name = Column(String(255))
    workplace_address_no = Column(String(50))
    workplace_address_moo = Column(String(10))
    workplace_address_soi = Column(String(100))
    workplace_address_road = Column(String(100))
    workplace_province = Column(String(100))
    workplace_amphoe = Column(String(100))
    workplace_tambon = Column(String(100))
    workplace_postcode = Column(String(10))
    workplace_phone = Column(String(20))

    contact_address_text = Column(Text)
    contact_address_no = Column(String(50))
    contact_address_moo = Column(String(10))
    contact_address_soi = Column(String(100))
    contact_address_road = Column(String(100))
    contact_province = Column(String(100))
    contact_amphoe = Column(String(100))
    contact_tambon = Column(String(100))
    contact_postcode = Column(String(10))

    phone_number = Column(String(20))
    email = Column(String(255))
    line_id = Column(String(100))
    facebook_url = Column(String(255))
    other_social_media = Column(String(255))
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