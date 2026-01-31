from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.config import DATABASE

_engines = {}
_Session = {}

def get_engine(db_key):
    if db_key not in _engines:
        print("Creating new engine for key:", db_key)
        config = DATABASE.get(db_key)
        # print(db_key)
        if not config:
            raise ValueError(f"Not found configuration found for key: {db_key}")
        
        connection_string = (
            f"postgresql://{config['user']}:{config['password']}@"
            f"{config['host']}:{config['port']}/{config['database']}"
        )
        _engines[db_key] = create_engine(connection_string, echo=True)
        # print(f"Engine created for {db_key}")
    return _engines[db_key]

def get_session(db_key):
    if db_key not in _Session:
        print("Creating get session for key:", db_key)
        engine = get_engine(db_key)
        _Session[db_key] = sessionmaker(
            bind=engine,
            autoflush=False,
            autocommit=False)
    return _Session[db_key]()

