# Auto-generated SQLAlchemy models
# DO NOT EDIT MANUALLY

from sqlalchemy import Column, ForeignKey, text
from sqlalchemy import Integer, BigInteger, SmallInteger, String, Text, Boolean, Float, Numeric, Date, DateTime, Time, LargeBinary
try:
    from sqlalchemy.orm import declarative_base
except Exception:  # pragma: no cover
    from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RefOrgSubRegionUnitCode(Base):
    __tablename__ = 'ref_org_sub_region_unit_code'
    __table_args__ = {'schema': 'core'}
    unit_id = Column(INTEGER(), primary_key=True, nullable=False)
    province_code = Column(String(2), ForeignKey('master.province.province_code'), nullable=False)
    sub_region_id = Column(INTEGER(), ForeignKey('core.ref_sub_regions.sub_region_id'), nullable=False)
    unit_code = Column(String(50))
    updated_at = Column(DateTime())
