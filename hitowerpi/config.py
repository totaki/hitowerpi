import configparser

VERSION = "0.1"

FAKEPI = True
DEBUG = True

INPUT = 0
OUTPUT = 1

PINS = {
    1: {'type': OUTPUT, 'name': 'pin1'},
    2: {'type': INPUT, 'name': 'pin2'},
    10: {'type': OUTPUT, 'name': 'pin3'},
    11: {'type': INPUT, 'name': 'pin4'}
}


class ConfigParser:

    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read()

    @property
    def pins(self):
        pins = {}
        for section in self._config.sections():
            if section.startswitch("PIN"):
                pins[int(self._config[section][3:])] = self._config[section]