import requests
import io
import pandas as pd
import pathlib


headers={"User-Agent": "Mozilla/5.0"}
url = 'https://storage.googleapis.com/kagglesdsdata/datasets/9235577/14465228/full_dataset_thesis%20-%201.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20260201%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20260201T123113Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=171c30e546f4d742a58bd763c71e62e07d2e1ea5aea1cccc812a6dff6b7c25ef58276f879adabe6935bf08fb479a84981dea16f127533d91d4a3f5c950ec45746dd41834193d04a18cb4a7e1299d3bd6d543e70b57657037240d53664afa0fac610129821d09634017b6a376c69333f2f96137912b6b5ff7cc6ff9239233c76c12bd9b626d113209ad6c316160e79a1a5324debd7d85df0374656cdca957ff8ff9157603398c848af605f10fffb246c2c37c16e6cb2af839290937cccd8a17f0ade69404dfda6f06e15c894161cc1f7aecf2d03a7ef95b007344088190b3da9600d7a599986bff6a815de28b8b78bb3e42961134d28a8211912c6a011704c2f7'
r = requests.get(url, headers=headers, timeout=60)
print("status:", r.status_code)
print("content-type:", r.headers['content-type'])
# print("content", r.content)
print("first_200",r.text[:200])
r.raise_for_status()

df = pd.read_csv(io.BytesIO(r.content))
print(df.shape)
print(df.head())

curPath = pathlib.Path(__file__).resolve().parent
chiPath = curPath / "download_csv_api"
csv = chiPath / "european_football.csv"
print("*"*30 , "Now Downloading" , "*"*30)
df.to_csv(csv, index=False, encoding="utf-8-sig", sep=",")
print(f"save to {csv}")
# print("shape =", df.shape)
# print("columns =", list(df.columns))
# print(df.head()