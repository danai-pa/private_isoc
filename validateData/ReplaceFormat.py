import pandas as pd
import pathlib
import os
import re
curPath = pathlib.Path(__file__).resolve().parents[1]
print("Current path:", curPath)
chiPath = curPath / "csv"
print("chiPath:", chiPath)
csv = chiPath / "ข้าราชการกลาโหมพลเรือน_mock.csv"
out_path = chiPath / "ข้าราชการกลาโหมพลเรือน_mock_valid.csv"
df = pd.read_csv(csv)
print(df)
# print(df)
# for i , j in df.iterrows():
#     print(j)
#     break
# print(df.columns.tolist())
new_cols = [
   "id_cardno",
    "title",
    "first_name",
    "last_name",
    "first_name_old",
    "last_name_old",
    "birth_date_be",
    "birth_date",
    "age",
    "nationality",
    "gender",
    "religion",
    "blood_type",
    "marital_status",
    "level",
    "employee_id_10_digit",
    "department",
    "unit",
    "position",
    "rate",
    "reg_house_no",
    "reg_village_no",
    "reg_soi",
    "reg_road",
    "reg_province",
    "reg_district",
    "reg_subdistrict",
    "reg_postcode",
    "education_level",
    "major",
    "contact_house_no",
    "contact_village_no",
    "contact_soi",
    "contact_road",
    "contact_province",
    "contact_district",
    "contact_subdistrict",
    "contact_postcode",
    "phone",
    "email",
    "line_id",
    "facebook",
    "other_social_media",
]

df.columns = new_cols

df = df.replace("-", "")
df = df.drop(columns="birth_date_be")
print(len(df.columns))
df["id_cardno"] = (
    df["id_cardno"]
    .astype(str)
    .str.replace(r"\D+", "", regex=True)   # ลบทุกอย่างที่ไม่ใช่ตัวเลข
)
print(df["id_cardno"])

df = df.replace("-", "")
df["birth_date"] = pd.to_datetime(
    df["birth_date"],
    dayfirst=True,
    errors="coerce"
).dt.strftime("%Y-%m-%d")
df["xlock"] = ""
df["created_at"] = ""
df["updated_at"] = ""
for i , j in df.iterrows():
    print(j)
    break
# print(df.columns.tolist())
# # print(df)

df.to_csv(out_path, index=False, encoding="utf-8-sig")