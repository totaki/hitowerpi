import configparser
import os

DEBUG = True
VERSION = "0.1"
API_VERSION = "0.1"

HL = 1
LL = 0

INSEC = 'INPUT'
OUTSEC = 'OUTPUT'
INDICT = 'inputs'
OUTDICT = 'outputs'
FAKETYPE = 'fake'
PITYPE = 'pi'
SOCTYPE = 'socket'
IOSTATE = 'state'
PNAMEOPT = 'name'
PTYPEOPT = 'type'
PINITOPT = 'init'
PDESCOPT = 'description'

SRVSEC = 'SERVER'
UNAMEOPT = 'username'
UPASSOPT = 'password'
PORTOPT = 'port'

IOAPP = 'io'

NUMPART = IOAPP
APPPART = 'app'
MSGPART = 'message'
DATAPART = 'data'
ERPART = 'error'

# Notice defaults
# types
MSG_T = 'message'
ACT_T = 'action'
ST_T = 'state'
ERR_T = 'error'
# scopes
MON_S = 'monitor'
PR_S = 'program'
IO_S = IOAPP


SOCKET_CLIENT = '/tmp/htpclient.sock'
SOCKET_SERVER = '/tmp/htpserver.sock'

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
