import unittest
from hitowerpi.config import *

FAKEGPIO = 'fakegpio'

_excpected_inputs_dict = {
    1: {PNAMEOPT: 'pin-1', PTYPEOPT: FAKEGPIO},
    5: {PNAMEOPT: 'pin-5', PTYPEOPT: FAKEGPIO}
}

_excpected_outputs_dict = {
    6: {PNAMEOPT: 'pin-6', PTYPEOPT: FAKEGPIO},
    11: {PNAMEOPT: 'pin-11', PTYPEOPT: FAKEGPIO}
}

_excpected_user_dict = {
    UNAMEOPT: 'admin',
    UPASSOPT: 'admin'
}

_excpected_srv_dict = {
    PORTOPT: '9999',
}


class TestConfig(unittest.TestCase):

    def test_normal_config_read(self):
        self.assertEqual(config.inputs, _excpected_inputs_dict)
        self.assertEqual(config.outputs, _excpected_outputs_dict)
        self.assertEqual(config.user, _excpected_user_dict)
        self.assertEqual(config.server, _excpected_srv_dict)
