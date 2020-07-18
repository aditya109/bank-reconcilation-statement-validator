import sys
from live.server import trigger


def setup():
    sys.path.append("/live")
    trigger()


setup()
