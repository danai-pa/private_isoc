import pandas as pd
from pathlib import Path

# path ของไฟล์ปัจจุบัน (change_csv.py)
curPath = Path(__file__).resolve().parent
print("Current path:", curPath)

# path ไฟล์ xlsx
xlsx_path = curPath / "ทหารกองเกิน_mock_excel.xlsx"
if xlsx_path.exists():
    print("File exists")
else:
    print("File not found")

# path โฟลเดอร์ csv (อยู่ระดับเดียวกับ Change_xlsxTo_CSV)
csv_dir = curPath.parent / "csv"
print("csv dir:", csv_dir)
csv_dir.mkdir(parents=True, exist_ok=True)

# # path ไฟล์ csv
csv_path = csv_dir / "ทหารกองเกิน_mock_excel.csv"
print("csv path:", csv_path)

# แปลงไฟล์
df = pd.read_excel(xlsx_path)
df.to_csv(csv_path, index=False, encoding="utf-8-sig")

print("Saved csv to:", csv_path)

