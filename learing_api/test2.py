import requests
import os
from dotenv import load_dotenv
from pathlib import Path

url = "https://www.onep.go.th/data/tentative-list.csv"
r = requests.get(url, stream=True, timeout=60)
print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))
print("content-disposition:", r.headers.get("content-disposition"))
print("rows", r.text[:200])
# csv_file_name = r.headers.get("content-disposition").split("filename=")[-1]
v = r.raise_for_status()
print("v:", v)
csv_file_name = "tentative-list.csv"
curPath = Path(__file__).resolve().parent
save_path = curPath / csv_file_name
with save_path.open("wb") as f:
    for chunk in r.iter_content(1024 * 256):
        if chunk:
            f.write(chunk)
print("saved to:", save_path)