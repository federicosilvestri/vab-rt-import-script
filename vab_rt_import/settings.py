import os
from pathlib import Path
from dotenv import load_dotenv

# Root folder
_ENV_FILE = Path(__file__).resolve().parent.parent / '.env'

if not _ENV_FILE.exists() or not _ENV_FILE.is_file():
    msg = "Cannot load environment file .env in {}".format(_ENV_FILE.absolute())
    raise RuntimeError(msg)

# Load
if not load_dotenv(_ENV_FILE):
    msg = "Cannot load variables inside .env in {}".format(_ENV_FILE.absolute())
    raise RuntimeError(msg)

SRC_DB_HOST = os.getenv("SRC_DB_HOST")
SRC_DB_PORT = int(os.getenv("SRC_DB_PORT"))
SRC_DB_USER = os.getenv("SRC_DB_USER")
SRC_DB_PASSWORD = os.getenv("SRC_DB_PASSWORD")
SRC_DB_NAME = os.getenv("SRC_DB_NAME")
SRC_SOCI_DB_TABLE = os.getenv("SRC_DB_SOCI_TABLE")
