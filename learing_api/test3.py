import requests
from pathlib import Path

url = 'https://opendata.ddc.moph.go.th/dataset/543d7d8c-47f1-4b88-906a-f56f7033ebac/resource/c47d11c8-1ee4-4bee-afda-62839a158097/download/smog_odpc1_2568-01.csv'
r = requests.get(url, stream=True, timeout=60)
print("status:", r.status_code)
print("content-type:", r.headers.get("content-type"))
print("content-disposition:", r.headers.get("content-disposition"))
csv_file_name = 'smog_odpc1_2568-01.csv'
curPath = Path(__file__).resolve().parent
save_path = curPath / csv_file_name
with save_path.open("wb") as f:
    for chunk in r.iter_content(1024 * 256):
        if chunk:
            f.write(chunk)
print("saved to:", save_path)