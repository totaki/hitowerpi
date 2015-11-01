import configparser
import os

VERSION = "0.1"

HL = 1
LL = 0

INSEC = 'INPUT'
OUTSEC = 'OUTPUT'
INDICT = 'inputs'
OUTDICT = 'outputs'
FAKETYPE = 'fake'
PITYPE = 'pi'
SOCTYPE = 'socket'
PNAMEOPT = 'name'
PTYPEOPT = 'type'
PINITOPT = 'init'

SRVSEC = 'SERVER'
UNAMEOPT = 'username'
UPASSOPT = 'password'
PORTOPT = 'port'


class ConfigParser:

    _pins = {INDICT: {}, OUTDICT: {}}
    _config_file = '/'.join([os.getcwd(), 'config.ini'])

    def __init__(self):
        self._config = configparser.ConfigParser()
        self._config.read(self._config_file)
        self._read_pins()

    def _read_pins(self):
        for section in self._config.sections():
            if section.startswith(INSEC):
                self._pins[INDICT][int(
                    section[len(INSEC):])] = self._config[section]

            if section.startswith(OUTSEC):
                self._pins[OUTDICT][int(
                    section[len(OUTSEC):])] = self._config[section]

    @property
    def inputs(self):
        return self._pins[INDICT]

    @property
    def outputs(self):
        return self._pins[OUTDICT]

    @property
    def user(self):
        return {
            UNAMEOPT: self._config[SRVSEC][UNAMEOPT],
            UPASSOPT: self._config[SRVSEC][UPASSOPT]
        }

    @property
    def server(self):
        return {PORTOPT: self._config[SRVSEC][PORTOPT]}


ConfigParser = ConfigParser()
config = ConfigParser
