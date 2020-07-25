import configparser
config = configparser.ConfigParser()
config.read('config.ini')

sections = config.sections()

CONFIG = {
    'PROJECT_DIRECTORY' : {
        'server_source_directory' : None,
        'static_folder_path' : None,
        'output_directory_path': None,
    },
}


def load_config_ini() :

    CONFIG['PROJECT_DIRECTORY']['server_source_directory'] = config['PROJECT_DIRECTORY']['server_source_directory']
    CONFIG['PROJECT_DIRECTORY']['static_folder_path'] = config['PROJECT_DIRECTORY']['static_folder_path']
    CONFIG['PROJECT_DIRECTORY']['output_directory_path'] = config['PROJECT_DIRECTORY']['output_directory_path']

    return CONFIG

