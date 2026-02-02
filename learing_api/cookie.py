import requests
import pandas as pd 
import io
import pathlib

url = 'https://storage.googleapis.com/kagglesdsdata/datasets/9191134/14391756/Chocolate%20Sales%20%282%29.csv?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20260201%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20260201T120120Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=32022ef93ef2139c329526c1500f782aaeb58989679652b02fe5b28dea1c7727eb37ede6e715bf686d886ed84e08c727d40f70a7aa9847053a45e4f92cc3a862379df8934769135bc8e7cf65295758f0245f52ce15534afbb3fe0c3b62786ae7e6d46752da1ea262afe1d1eae43250c93f6303a934cd9323df0b0162b551e8ab9b869e7910c95472ee742fe4c8b6061ecc29f65abb68565124d4db10ea911d4207cc76b4a2006d2633a69a7ab60063f982d3125fcd16809251044cc04423d5c02d96369cd3184842ba184cbf34a458011f9009849c30a690e843594af6c73c672e66fa777c263182d6a425df7da4c4eed73e5ed1bef649536c1bdd93c75b7359'
headers = {"User-Agent": "Mozilla/5.0"}
r = requests.get(url, headers=headers, timeout=60)
# print("status:", r.status_code)
# print("content-type:", r.headers['content-type'])
# print("first_200",r.text[:200])
r.raise_for_status()

curPath = pathlib.Path(__file__).resolve().parent
chiPath = curPath / "download_csv_api"
csv = chiPath / "Chocolate_Sales.csv"
df = pd.read_csv(io.BytesIO(r.content))

print("shape =", df.shape)
print("columns =", list(df.columns))
print(df.head())

print("*"*30)
df.to_csv(csv, index=False, encoding="utf-8-sig", sep=",")
print(f"save to {csv}")