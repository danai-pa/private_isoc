# Python Requests (HTTP) - README

เอกสารสรุปการใช้งานไลบรารี `requests` ใน Python สำหรับเรียก API / ส่ง HTTP Request

---

## 1) ติดตั้ง requests

```bash
pip install requests


เช็คว่าใช้งานได้:

import requests
print(requests.__version__)

2) HTTP Method ที่ใช้บ่อย
✅ GET (ดึงข้อมูล)

ใช้เมื่อ: ขอข้อมูลจาก server เช่น อ่านรายการสินค้า / อ่าน user

import requests

url = "https://api.example.com/users"
res = requests.get(url)

print(res.status_code)
print(res.text)       # ข้อความ raw
print(res.json())     # แปลงเป็น dict/list (ถ้า response เป็น JSON)

✅ POST (ส่งข้อมูล/สร้างข้อมูลใหม่)

ใช้เมื่อ: สร้างข้อมูลใหม่ เช่น สมัครสมาชิก / เพิ่มรายการใหม่

import requests

url = "https://api.example.com/users"
payload = {
    "name": "Tom",
    "age": 20
}

res = requests.post(url, json=payload)

print(res.status_code)
print(res.json())


📌 แนะนำใช้ json=payload แทน data=payload ถ้าปลายทางรับ JSON

✅ PUT (แก้ไขข้อมูลทั้งก้อน)

ใช้เมื่อ: แก้ไขข้อมูลทั้งหมด เช่น update user ทั้ง object

import requests

url = "https://api.example.com/users/1"
payload = {
    "name": "Tommy",
    "age": 21
}

res = requests.put(url, json=payload)

print(res.status_code)
print(res.json())

✅ PATCH (แก้ไขบางส่วน)

ใช้เมื่อ: แก้ไขเฉพาะบาง field เช่น แก้ age อย่างเดียว

import requests

url = "https://api.example.com/users/1"
payload = {
    "age": 30
}

res = requests.patch(url, json=payload)

print(res.status_code)
print(res.json())

✅ DELETE (ลบข้อมูล)

ใช้เมื่อ: ลบ resource เช่น ลบ user

import requests

url = "https://api.example.com/users/1"
res = requests.delete(url)

print(res.status_code)

3) ส่ง Query Params (พารามิเตอร์ท้าย URL)

ตัวอย่าง URL:
/users?page=1&limit=10

import requests

url = "https://api.example.com/users"
params = {
    "page": 1,
    "limit": 10
}

res = requests.get(url, params=params)
print(res.url)      # ดู URL ที่ประกอบแล้ว
print(res.json())

4) ส่ง Headers (เช่น Authorization Token)
import requests

url = "https://api.example.com/profile"
headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Accept": "application/json"
}

res = requests.get(url, headers=headers)
print(res.status_code)
print(res.json())

5) ส่ง Form Data (data=...)

ใช้เมื่อ: server รับแบบ application/x-www-form-urlencoded

import requests

url = "https://api.example.com/login"
form_data = {
    "username": "admin",
    "password": "1234"
}

res = requests.post(url, data=form_data)
print(res.status_code)
print(res.text)

6) Upload File
import requests

url = "https://api.example.com/upload"

with open("myfile.png", "rb") as f:
    files = {"file": f}
    res = requests.post(url, files=files)

print(res.status_code)
print(res.json())

7) Timeout (กันค้าง)
import requests

url = "https://api.example.com/users"
res = requests.get(url, timeout=5)  # 5 วินาที
print(res.status_code)

8) Error Handling (แนะนำใช้ try/except)
import requests

try:
    res = requests.get("https://api.example.com/users", timeout=5)
    res.raise_for_status()  # ถ้า status 4xx/5xx จะ throw error
    data = res.json()
    print(data)

except requests.exceptions.Timeout:
    print("Request timeout")

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)

except requests.exceptions.RequestException as e:
    print("Other request error:", e)

9) เช็ค Response สำคัญ ๆ
print(res.status_code)  # เช่น 200, 201, 404, 500
print(res.headers)      # header ที่ server ส่งกลับมา
print(res.text)         # response raw string
print(res.json())       # response JSON -> dict/list

10) HTTP Status Code ที่ควรรู้

200 OK สำเร็จ (GET)

201 Created สร้างสำเร็จ (POST)

204 No Content สำเร็จแต่ไม่มีข้อมูลกลับมา

400 Bad Request ส่งข้อมูลผิด format

401 Unauthorized ไม่ได้ login / token ไม่ถูก

403 Forbidden ไม่มีสิทธิ์เข้าถึง

404 Not Found ไม่เจอ endpoint หรือ resource

500 Internal Server Error server พัง

11) Session (จำค่า Cookie / Header ซ้ำ ๆ)

เหมาะกับการเรียกหลายครั้ง หรือ login ครั้งเดียวแล้วใช้ต่อ

import requests

session = requests.Session()

session.headers.update({
    "Authorization": "Bearer YOUR_TOKEN"
})

res1 = session.get("https://api.example.com/profile")
res2 = session.get("https://api.example.com/orders")

print(res1.status_code)
print(res2.status_code)

12) ตัวอย่างรวม (GET + params + headers)
import requests

url = "https://api.example.com/users"
params = {"page": 1}
headers = {"Accept": "application/json"}

res = requests.get(url, params=params, headers=headers, timeout=5)

if res.status_code == 200:
    print(res.json())
else:
    print("Error:", res.status_code, res.text)

เช็คลิสต์เวลาหา URL/API จาก Inspect (Network)

เปิด DevTools → Network → Fetch/XHR

กด Preserve log แล้วกด Clear

ทำ action ให้เว็บโหลดข้อมูล (ค้นหา/กดดาวน์โหลด/เปลี่ยนหน้า)

คลิก request ที่สงสัย แล้วดู 3 อย่างนี้:

Request URL (สำคัญสุด)

Response (ถ้าเป็น JSON/CSV คือของจริง)

Status code (200 = ผ่าน)

ถ้าเป็น CKAN ให้จำ pattern นี้

API: /api/3/action/...

ไฟล์ดาวน์โหลด: /resource/<id>/download/...csv

วิธีเร็วสุดให้ได้ “URL ดาวน์โหลดไฟล์”

ใช้ package_show → เข้า result["resources"] → เอา resource["url"] มาใช้
(เหมือนที่คุณทำกับ csv_url)