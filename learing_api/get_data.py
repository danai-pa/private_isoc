import os
import requests
from dotenv import load_dotenv

load_dotenv()  # <- ตรงนี้คือให้ python อ่านไฟล์ .env

api_key = os.getenv("DATA_GOTH_API_KEY")
print("has_key:", bool(api_key), "len:", len(api_key) if api_key else 0)

CKAN = "https://opend.data.go.th/get-ckan"
dataset_id = "msk44_05"

headers = {"api-key": api_key}  # <- token ใส่ตรงนี้

resource_id = "bd8c34ce-6237-4b86-ba0e-4e8ae4b4f16d"

r = requests.get(
    f"{CKAN}/datastore_search",
    params={"resource_id": resource_id, "limit": 5, "offset": 0},
    headers=headers,
    timeout=30
)
print("status:", r.status_code)

d = r.json()
print("success:", d.get("success"))

result = d["result"]
print("total:", result.get("total"))
print("records in this call:", len(result.get("records", [])))

first = result.get("records", [None])[0]
print("first record keys:", list(first.keys()) if first else None)
print("first record:", first)
