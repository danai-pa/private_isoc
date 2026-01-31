import requests
import os
from pathlib import Path    
# url = "https://data.ny.gov/api/views/d6yy-54nr/rows.csv?accessType=DOWNLOAD"

# r = requests.get(url, stream=True, timeout=60)
# print("status:", r.status_code)
# print("content-type:", r.headers.get("content-type"))
# print("content-disposition:", r.headers.get("content-disposition"))
# r.raise_for_status()


url = "https://data.bangkok.go.th/dataset/0bf49df9-7baa-480b-b55e-a38881ff5519/resource/3bd7d9f2-61cf-4484-b78c-9573df17fceb/download/bma_school.csv"
r = requests.get(url, stream=True, timeout=60)
print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))
print("content-disposition:", r.headers.get("content-disposition"))
# csv_file_name = r.headers.get("content-disposition").split("filename=")[-1]
# v = r.raise_for_status()
# print("v:", v)
# curPath = Path(__file__).resolve().parent
# save_path = curPath / csv_file_name
# with save_path.open("wb") as f:
#     for chunk in r.iter_content(1024 * 256):
#         if chunk:
#             f.write(chunk)
# print("saved to:", save_path)