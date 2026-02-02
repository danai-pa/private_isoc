import requests
import os
from pathlib import Path
import pandas as pd
import io
print("STEP 1: Call CKAN package_show API")

api_url = "https://catalog-dga.data.go.th/th/api/3/action/package_show"
params = {"id": "9443ffaa-8aa0-4922-93e5-a8c2374eb8d8"}

data = requests.get(api_url, params=params, timeout=60).json()

print("success =", data.get("success"))

result = data.get("result", {})
resources = result.get("resources", [])
# for i , r in enumerate(resources, start=1):
    # print(i, r) 
    # break
print (type(resources))

csv_url = []
name = ['รายการข้อมูลที่_1',"รายการข้อมูลที่_2"]
for i, r in enumerate(resources, start=1):
    name = (r.get("name") or "").strip().lower()
    # print(f"name = {name}")
    id = (r.get("id") or "").strip().lower()
    # print(f"id = {id}")
    fmt = (r.get("format") or "" ).strip().lower()
    # print(f"fmt = {fmt}")
    url = (r.get("url") or "").strip().lower()

    if fmt =="csv" or url.lower().endswith(".csv"):
        csv_url.append(url)
print("csv_founds_count =", len(csv_url))
# print("csv_url =", csv_url)

# for i , u in enumerate(csv_url, start=1):
#     print(i,u)
csv2 = csv_url[1]
curpath = Path(__file__).resolve().parent
chipath = curpath / "download_csv_api"
print("*"*30, "\nSTEP B: Download each CSV URL")
print("*"*30)

# url_csv = csv_url[0]
# print(url_csv)
headers = {"User-Agent": "Mozilla/5.0"}
dfs = []

r = requests.get(csv2 ,headers=headers, timeout=60)
r.raise_for_status()

text = r.content.decode("utf-8-sig",errors="replace")
df2 = pd.read_csv(
    io.StringIO(text),
    dtype=str,          # กัน pandas เดา type จนเพี้ยน
    low_memory=False,
    on_bad_lines="skip" # ถ้ามีบรรทัดเสีย/คอลัมน์เกิน ให้ข้าม (กัน crash)
)

print("shape =", df2.shape)
print("columns =", list(df2.columns))
print(df2.head(3))

# for i , url in enumerate(csv_url , start=1):
#     print("\n=================")
#     print("FILE",i)
#     print("URL",url)

#     r = requests.get(url ,headers=headers, timeout=60)
#     print("status",r.status_code)
#     r.raise_for_status()

#     df = pd.read_csv(io.BytesIO(r.content),encoding="utf-8-sig")
#     print("shape",df.shape)
#     print("first column : ", list(df.columns)[:8])
#     print(df.head(2))

#     dfs.append(df)

# print(dfs)
# for i , url in enumerate(csv_url, start=1):
#     print(f"\n[{i}] downloading...")
#     print("url =", url)

#     df = pd.read_csv(url ,encoding='utf-8-sig')
#     print("df.shape =", df.shape)
#     print("columns =", list(df.columns))
#     print("head:")
#     print(df.head(5))
# for i , url in enumerate(csv_url, start=1):
    
#     filename = f"{chipath}/file_{i}.csv"
#     print(filename)
#     print(f"\n[{i}] downloading...")
#     print("url =", url)
    # print("save_to =", filename)

    # resp = requests.get(url, stream=True, timeout=60)
    # print("status:", resp.status_code)
    # resp.raise_for_status()

    # with open(filename, "wb") as f:
    #     f.write(resp.content)
    
    # print("saved_bytes =", len(resp.content))

    # preview = resp.content[:600].decode("utf-8-sig", errors="replace")
    # lines = preview.splitlines()
    # print("--- preview first 2 lines ---")
    # for line in lines[:2]:
    #     print(line)