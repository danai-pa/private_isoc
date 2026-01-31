import pandas as pd
import requests
import os
import time
import re

# อ่านไฟล์ CSV - ลอง encoding หลายแบบ
csv_file = 'DataDict.csv'

# ลอง encoding หลายแบบ
encodings = ['utf-8', 'utf-8-sig', 'cp874', 'tis-620', 'latin-1', 'cp1252']
df = None

for enc in encodings:
    try:
        df = pd.read_csv(csv_file, encoding=enc)
        print(f"อ่านไฟล์สำเร็จด้วย encoding: {enc}")
        break
    except:
        continue

if df is None:
    print("ไม่สามารถอ่านไฟล์ CSV ได้")
    exit(1)

# URL template
url_template = 'https://dgpc.isoc.go.th/dg-report-service/api/v1/docs/export/NSDC-DG-202-1/{id}'

# สร้างโฟลเดอร์สำหรับเก็บ PDF
output_folder = 'PDF_Downloads'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# ฟังก์ชันสำหรับทำให้ชื่อไฟล์ปลอดภัย
def sanitize_filename(name):
    if pd.isna(name) or name == '':
        return None
    # ลบตัวอักษรที่ไม่สามารถใช้ในชื่อไฟล์ได้
    name = re.sub(r'[<>:"/\\|?*]', '_', str(name))
    return name.strip()

# ดาวน์โหลด PDF
success_count = 0
fail_count = 0
skip_count = 0

print(f"เริ่มดาวน์โหลด PDF จำนวน {len(df)} รายการ...")
print("-" * 50)

for index, row in df.iterrows():
    id_value = row['id']
    name_value = row['name']
    
    # ข้ามถ้าไม่มีชื่อ
    safe_name = sanitize_filename(name_value)
    if safe_name is None:
        print(f"[{index + 1}/{len(df)}] ข้าม - ไม่มีชื่อสำหรับ ID: {id_value}")
        skip_count += 1
        continue
    
    # สร้าง URL
    url = url_template.format(id=id_value)
    
    # ชื่อไฟล์
    filename = f"{safe_name}.pdf"
    filepath = os.path.join(output_folder, filename)
    
    # ตรวจสอบว่าไฟล์มีอยู่แล้วหรือไม่
    if os.path.exists(filepath):
        print(f"[{index + 1}/{len(df)}] มีอยู่แล้ว - {filename}")
        skip_count += 1
        continue
    
    try:
        print(f"[{index + 1}/{len(df)}] กำลังดาวน์โหลด: {filename}")
        
        response = requests.get(url, timeout=60)
        
        if response.status_code == 200:
            # ตรวจสอบว่าเป็น PDF หรือไม่
            content_type = response.headers.get('Content-Type', '')
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            file_size = len(response.content) / 1024  # KB
            print(f"    ✓ สำเร็จ ({file_size:.1f} KB)")
            success_count += 1
        else:
            print(f"    ✗ ผิดพลาด - HTTP {response.status_code}")
            fail_count += 1
            
    except requests.exceptions.Timeout:
        print(f"    ✗ หมดเวลา")
        fail_count += 1
    except requests.exceptions.RequestException as e:
        print(f"    ✗ ผิดพลาด - {str(e)}")
        fail_count += 1
    
    # หน่วงเวลาเล็กน้อยเพื่อไม่ให้โหลด server หนัก
    time.sleep(0.5)

print("-" * 50)
print(f"เสร็จสิ้น!")
print(f"  สำเร็จ: {success_count}")
print(f"  ผิดพลาด: {fail_count}")
print(f"  ข้าม: {skip_count}")
print(f"  รวม: {len(df)}")
print(f"\nไฟล์ถูกบันทึกไว้ที่โฟลเดอร์: {os.path.abspath(output_folder)}")
