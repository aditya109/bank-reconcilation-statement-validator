from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    STATIC_FILE_DIRECTORY = r"D:\Projects\bank-reconcilation-statement-validator\1.3\server\live\static"
    OUTPUT_DIRECTORY = STATIC_FILE_DIRECTORY + r"\output"

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True