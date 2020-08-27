import configparser
from os import path
import sys
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

config = configparser.ConfigParser()

config.add_section('PROJECT_DIRECTORY')

 
config['PROJECT_DIRECTORY']['SERVER_SOURCE_DIRECTORY'] = basedir
config['PROJECT_DIRECTORY']['STATIC_FOLDER_PATH'] = f'{basedir}\\resources\\static'
config['PROJECT_DIRECTORY']['OUTPUT_DIRECTORY_PATH'] = f'{basedir}\\resources\\static\\output'

with open('./sample/config.ini', 'w') as configfile:
    config.write(configfile)