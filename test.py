import os
from dotenv import load_dotenv

load_dotenv()

print("DB_HOST =", os.getenv("ISOC_360_HOST"))
print("DB_PORT =", os.getenv("ISOC_360_PORT"))
print("DB_USER =", os.getenv("ISOC_360_USER"))
print("DB_NAME =", os.getenv("ISOC_360_DB"))
print("DB_URL  =", os.getenv("ISOC_360_URL"))
# print("DATABASE_URL =", os.getenv("DATABASE_URL"))

