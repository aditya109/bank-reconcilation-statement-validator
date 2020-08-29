from os import path
import sys
from dotenv import load_dotenv


def provide_config():
    basedir = path.abspath(path.dirname(__file__))
    load_dotenv(path.join(basedir, ".env"))

    config = dict()

    config['__basedir'] = basedir
    config['__static'] = f'{basedir}\\resources\\static'
    config['__output'] = f'{basedir}\\resources\\static\\output'

    return config
