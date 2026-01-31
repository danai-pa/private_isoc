import os
from dotenv import load_dotenv
from urllib.parse import quote_plus
load_dotenv()
DATABASE = { 
    "ISOC_STAGGING" : {
        "host": os.getenv("ISOC_STAGGING_HOST"),
        "port": os.getenv("ISOC_STAGGING_PORT"),
        "user": os.getenv("ISOC_STAGGING_USER"),
        "password": os.getenv("ISOC_STAGGING_PASS"),
        "database": os.getenv("ISOC_STAGGING_DB"),
    },
    "MAHONLAND_DEV" : {
        "host": os.getenv("MAHONLAND_DEV_HOST"),
        "port": os.getenv("MAHONLAND_DEV_PORT"),
        "user": os.getenv("MAHONLAND_DEV_USER"),
        "password": os.getenv("MAHONLAND_DEV_PASS"),
        "database": os.getenv("MAHONLAND_DEV_DB"),
    },
    "ISOC_SPP02" : {
        "host": os.getenv("ISOC_SPP02_HOST"),
        "port": os.getenv("ISOC_SPP02_PORT"),
        "user": os.getenv("ISOC_SPP02_USER"),
        "password": os.getenv("ISOC_SPP02_PASS"),
        "database": os.getenv("ISOC_SPP02_DB"),
    },
     "ISOC_360" : {
        "host": os.getenv("ISOC_360_HOST"),
        "port": os.getenv("ISOC_360_PORT"),
        "user": os.getenv("ISOC_360_USER"),
        "password": quote_plus(os.getenv("ISOC_360_PASS")),
        "database": os.getenv("ISOC_360_DB"),
    }      
}