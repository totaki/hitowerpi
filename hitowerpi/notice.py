import struct
from hitowerpi.config import *
"""
Notice may be as fourth types:
000 - error
001 - message
010 - action
011 - state
Notice may be as next scopes:
000 - monitor
001 - program
010 - io
"""

class Notice:

    @staticmethod
    def message(self):
        pass

    @staticmethod
    def action(self):
        pass

    @staticmethod
    def state(self):
        pass