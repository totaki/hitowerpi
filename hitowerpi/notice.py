import re
import struct
from hitowerpi.config import *

"""
Message include type - 3, scope - 4, meta - 8, data-type - 1, data - 64 bits.
"""

_bin_to_int = lambda x: int(x, 2)

_val_to_key = lambda dct, val: list(dct.keys())[list(dct.values()).index(val)]

_LENS = (3, 4, 8, 1, 64)

TYPES = {
    ERR_T: '000',
    MSG_T: '001',
    ACT_T: '010',
    ST_T: '011',
}

SCOPES = {
    MON_S: '0000',
    PR_S: '0001',
    IO_S: '0010',
}

_DATA_T = {
    0: 'q',
    1: 'd',
}

_HD_T = 'h'


class Notice:

    _re_header = re.compile(
        r'^([0,1]{%s})([0,1]{%s})([0,1]{%s})([0,1]{%s})$' % _LENS[:-1])
    _sum_header = sum(_LENS[:-1])

    def __init__(self, *args,
                 ntc_type=ERR_T, scope=MON_S, meta=0, data_type=0, data=0):
        self.type = ntc_type
        self.scope = scope
        self.meta = meta
        self.data_type = data_type
        self.data = data

    def _get_header(self):
        return '0b' + TYPES[self.type] + SCOPES[self.scope] + \
               bin(self.meta)[2:] + str(self.data_type)

    def _set_header(self, header):
        header = bin(header)[2:]
        header = '0' * (self._sum_header - len(header)) + header
        try:
            list_ = self._re_header.match(header).groups()
        except AttributeError:
            pass
        else:
            self.type = _val_to_key(TYPES, list_[0])
            self.scope = _val_to_key(SCOPES, list_[1])
            self.meta = _bin_to_int(list_[2])
            self.data_type = _bin_to_int(list_[3])
        finally:
            return

    def pack(self):
        return struct.pack(_HD_T + _DATA_T[self.data_type],
                           _bin_to_int(self._get_header()), self.data)

    @staticmethod
    def unpack(str_):
        notice = Notice()
        header = struct.unpack(_HD_T + _DATA_T[0], str_)[0]
        notice._set_header(header)
        notice.data = struct.unpack(_HD_T + _DATA_T[notice.data_type], str_)[1]
        return notice
