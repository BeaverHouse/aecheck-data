import oracledb
from dotenv import load_dotenv
import os

load_dotenv()

def get_oracle():
    return oracledb.connect(
        user=os.getenv("ORACLE_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        dsn=os.getenv("ORACLE_DSN"),
    )