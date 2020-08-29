# TODO write a proper setup please !!!
from sample.server import trigger
from config import provide_config

if __name__ == "__main__":
    config = provide_config()
    trigger(configuration=config)
