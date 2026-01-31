import pandas as pd
from database.engine import get_session
from models.enlisted_personnel_type_2 import EnlistedPersonnelType2
from models.military_student import MilitaryStudent
from models.female_reserve_soldier import female_reserve_soldier
NUMBERIC_COLUMNS = [
    "age_yaer",
    "ror_dor_enroll_academy",
    "current_academic_year"
]

DATE_COLUMNS = [
    "birth_date",
    "ror_dor_enroll_date",
]


def validate_columns(df, model):
    csv_cols = set(df.columns)

    model_cols = {
        c.name
        for c in model.__table__.columns
        if c.name != "id"
    }

    missing_in_csv = model_cols - csv_cols
    extra_in_csv = csv_cols - model_cols

    if not missing_in_csv and not extra_in_csv:
        print("✅ Columns match with out \"id\")")
        return True

    if missing_in_csv:
        print("❌ Missing columns in CSV:")
        for c in sorted(missing_in_csv):
            print("  -", c)

    if extra_in_csv:
        print("⚠️ Extra columns in CSV:")
        for c in sorted(extra_in_csv):
            print("  -", c)

    return False
                                             
def load_csv_to_db(file_path: str, db_key: str, model_class):
    df = pd.read_csv(file_path, sep=",", dtype=str)
    df.columns = df.columns.str.replace('"', '', regex=False)

    # if "id" in df.columns:
    #     df.drop(columns=["id"], inplace=True)

    # cast numeric
    for col in NUMBERIC_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # cast date
    for col in DATE_COLUMNS:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce").dt.date

    df = df.replace({pd.NA: None})

    records = df.to_dict(orient="records")

    session = get_session(db_key)
    try:
        model_class.bulk_create(session, records)
        session.commit()
        print(
            f"✅ Loaded {len(records)} rows into "
            f"{model_class.__tablename__} ({db_key})"
        )
    except Exception as e:
        session.rollback()
        print("❌ Error loading data:", e)
    finally:
        session.close()
