# Auto-generated SQLAlchemy models
# DO NOT EDIT MANUALLY

from sqlalchemy import Column, ForeignKey, text
from sqlalchemy import Integer, BigInteger, SmallInteger, String, Text, Boolean, Float, Numeric, Date, DateTime, Time, LargeBinary
try:
    from sqlalchemy.orm import declarative_base
except Exception:  # pragma: no cover
    from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EnlistedPersonnelType2(Base):
    __tablename__ = 'enlisted_personnel_type_2'
    __table_args__ = {'schema': 'public'}
    id = Column(BIGINT(), primary_key=True, nullable=False, server_default=text('nextval(\'"public".enlisted_personnel_type_2_id_seq\'::regclass)'))
    id_cardno = Column(String(13), nullable=False)
    title = Column(String(50))
    first_name = Column(String(100))
    last_name = Column(String(100))
    previous_first_name = Column(String(100))
    previous_last_name = Column(String(100))
    birth_date = Column(Date())
    age_year = Column(INTEGER())
    religion = Column(String(50))
    blood_type = Column(String(10))
    weight_kg = Column(Numeric(precision=5, scale=2))
    height_cm = Column(Numeric(precision=5, scale=2))
    marital_status = Column(String(50))
    military_origin = Column(String())
    military_address_no = Column(String(50))
    military_address_moo = Column(String(10))
    military_address_soi = Column(String(100))
    military_address_road = Column(String(100))
    military_province = Column(String(100))
    military_amphoe = Column(String(100))
    military_tambon = Column(String(100))
    conscription_year_be = Column(INTEGER())
    sd43_document_no = Column(String(50))
    reserve_class = Column(String(50))
    home_address_text = Column(String())
    home_address_no = Column(String(50))
    home_address_moo = Column(String(10))
    home_address_soi = Column(String(100))
    home_address_road = Column(String(100))
    home_province = Column(String(100))
    home_amphoe = Column(String(100))
    home_tambon = Column(String(100))
    home_postcode = Column(String(10))
    created_at = Column(DateTime(timezone=True), server_default=text('now()'))
    updated_at = Column(DateTime(timezone=True), server_default=text('now()'))
