from os import path
import sys
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

PROJECT_DIRECTORY_CONFIG = {
    "BACKEND_SOURCE_DIRECTORY": basedir,
    "LIVE_DIRECTORY": f"{basedir}\\live",
    "STATIC_DIRECTORY": f"{basedir}\\live\\static",
    "OUTPUT_DIRECTORY": f"{basedir}\\live\\static\\output",
}

