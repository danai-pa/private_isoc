import pathlib 
import pandas as pd

curPath = pathlib.Path(__file__).resolve().parents[2]
cd_cur = curPath / "learning_api" / "download_csv_api"
csv = cd_cur / "mobie_prize.csv"
print("Current path:", csv)

df = pd.read_csv(csv)
print(df.head())