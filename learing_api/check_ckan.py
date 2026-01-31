import requests
import os
from pathlib import Path
print("STEP 1: Call CKAN package_show API")

api_url = "https://catalog-dga.data.go.th/th/api/3/action/package_show"
params = {"id": "9443ffaa-8aa0-4922-93e5-a8c2374eb8d8"}

data = requests.get(api_url, params=params, timeout=60).json()

print("success =", data.get("success"))

result = data.get("result", {})
resources = result.get("resources", [])
print (type(resources))

csv_url = []

for i, r in enumerate(resources, start=1):
    fmt = (r.get("format") or "" ).strip().lower()
    url = (r.get("url") or "").strip().lower()

    if fmt =="csv" or url.lower().endswith(".csv"):
        csv_url.append(url)
print("csv_founds_count =", len(csv_url))
# print("csv_url =", csv_url)

for i , u in enumerate(csv_url, start=1):
    print(i,u)
    
curpath = Path(__file__).resolve().parent
chipath = curpath / "download_csv_api"
print("*"*30, "\nSTEP B: Download each CSV URL")
print("*"*30)

for i , url in enumerate(csv_url, start=1):
    filename = f"{chipath}/file_{i}.csv"
    print(f"\n[{i}] downloading...")
    print("url =", url)
    print("save_to =", filename)

    resp = requests.get(url, stream=True, timeout=60)
    print("status:", resp.status_code)
    resp.raise_for_status()

    with open(filename, "wb") as f:
        f.write(resp.content)
    
    print("saved_bytes =", len(resp.content))

    preview = resp.content[:600].decode("utf-8-sig", errors="replace")
    lines = preview.splitlines()
    print("--- preview first 2 lines ---")
    for line in lines[:2]:
        print(line)