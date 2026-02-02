import os
import io
import requests
import pandas as pd
import pathlib 


url = 'https://storage.googleapis.com/kagglesdsdata/datasets/11167/15520/train.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20260201%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20260201T131705Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=80a93a4ba8458fbb00c5c59135c42e74c9147ada39a674b40a5dd6ad4ea8d2d6906283e9c9bdbf1e1c61d4a3598875469a5bdfd2f858e24a9f381b4f35707ec3e7c2e3add25f9e59de65c11d509e02c8363b0f54fdae3df6a94fc0eb2480277a258eb57906734ef0865cdc756d1e5ddb506c05710aa7bef4f837c6c35703ce59eb2aefe0088360e2b0bd8953ab9c12c335ea43f8c13938546dc76211098047894add86239e0b3c5e644e4e6181887d24559a7af33c88fdae5aa3ff9838445976e8a7351535eb3009aed2f482d35a3fe739a28cb323ca1f5949503a2ebc936ee60a40b90860f0874fed62f75e590bbb377ad5665b55ce3a7cfe137d19a835dfeb'
headers = {"User-Agent": "Mozilla/5.0"}

r = requests.get(url, headers=headers, timeout=60)
print("status:",r.status_code)
print("haders:",r.headers)
print("content-type:", r.headers['content-type'])
r.raise_for_status()

df = pd.read_csv(io.BytesIO(r.content))
print(df.shape)
print(df.head())

curPath = parentPath = pathlib.Path(__file__).resolve().parent
chiPath = curPath / "download_csv_api"
csv = chiPath / "mobie_prize.csv"
print("*"*30 , "Now Downloading" , "*"*30)
df.to_csv(csv, index=False, encoding="utf-8-sig", sep=",")
print(f"save to {csv}")