# database/init_db.py
from database.base import Base
from database.engine import get_engine

# ⚠️ ต้อง import model ทั้งหมด
from models.military_student import MilitaryStudent
from models.female_reserve_soldier import female_reserve_soldier  
from models.enlisted_personnel_type_2 import EnlistedPersonnelType2  
from models.military_personnel import MilitaryPersonnel
from models.active_duty_personnel import ActiveDutyPersonnel
from models.government_employee import GovernmentEmployee
from models.employee_contract import EmployeeContract
from models.defense_civil_servant import DefenseCivilServant
from models.defense_civil_officer import DefenseCivilOfficer
from models_isoc360.datasets import clsDatasets
def init_db(db_key: str):
    engine = get_engine(db_key)
    Base.metadata.create_all(bind=engine)
