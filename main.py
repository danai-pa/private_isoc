from loader.csv_loader import load_csv_to_db , validate_columns
# from models.military_personnel import MilitaryPersonnel
# from models.defense_civil_servant import DefenseCivilServant
# from models.defense_civil_officer import DefenseCivilOfficer
from models_isoc360.datasets import clsDatasets
# from models.employee_contract import EmployeeContrac
from pathlib import Path
from database.init_db import init_db
import pandas as pd


curPath = Path(__file__).resolve().parent
chiPath = curPath / "csv_isoc360"
csv = chiPath / "การบริหารจัดการภาวะฉุกเฉินด้านสาธารณสุขและโรคติดต่ออุบัติใหม่.csv"

def main():
    
    db_key = "ISOC_360"
    df = pd.read_csv(csv, sep=",", dtype=str)
    init_db(db_key=db_key) 
    validate_columns(df=df, model=clsDatasets)  
    load_csv_to_db(
        file_path=csv,
        db_key=db_key,  
        model_class=clsDatasets
    )

if __name__ == "__main__":
    main()


