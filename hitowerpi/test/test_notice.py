import unittest
from hitowerpi.config import *
import hitowerpi.notice as notice


class TestNoticeMethods(unittest.TestCase):

    def test_get_header(self):
        str_ = '0b0010010111111110'
        ntc = notice.Notice(
            ntc_type=MSG_T,
            scope=IO_S,
            meta=255)
        self.assertEqual(ntc._get_header(), str_)

    def test_set_header(self):
        data_type = 0
        meta = 134
        str_ = '0b' + notice.TYPES[MSG_T] + notice.SCOPES[MON_S] + \
               bin(meta)[2:] + str(data_type)
        ntc = notice.Notice()
        ntc._set_header(int(str_, 2))
        self.assertEqual(ntc.type, MSG_T)
        self.assertEqual(ntc.scope, MON_S)
        self.assertEqual(ntc.meta, meta)
        self.assertEqual(ntc.data_type, data_type)

    def test_pack(self):
        msg = notice.Notice(
            ntc_type=MSG_T,
            scope=MON_S,
            meta=134,
            data=145456).pack()
        self.assertEqual(msg, b'\x0c!\x00\x00\x00\x00\x00\x0008\x02\x00\x00\x00\x00\x00')

    def test_unpack(self):
        msg = notice.Notice.unpack(b'\x0c!\x00\x00\x00\x00\x00\x0008\x02\x00\x00\x00\x00\x00')
        self.assertEqual(msg.type, MSG_T)
        self.assertEqual(msg.scope, MON_S)
        self.assertEqual(msg.meta, 134)
        self.assertEqual(msg.data_type, 0)
        self.assertEqual(msg.data, 145456)
