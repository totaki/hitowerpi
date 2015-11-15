import unittest
from hitowerpi.config import *
from hitowerpi.io import IOs


class TestIOMethods(unittest.TestCase):

    def test_get_ios(self):
        ios = IOs.inputs()
        nums = [1, 5]
        for io in ios:
            self.assertTrue(io.num in nums)
        ios = IOs.outputs()
        nums = [6, 11]
        for io in ios:
            self.assertTrue(io.num in nums)

    def test_get_io_state(self):
        io = IOs.input(1)
        self.assertEqual(io.state, HL)
        io = IOs.output(6)
        self.assertEqual(io.state, LL)

    def test_set_pin_state(self):
        io = IOs.output(6)
        io.up()
        self.assertEqual(io.state, HL)
        io.down()
        self.assertEqual(io.state, LL)
        io.change()
        self.assertEqual(io.state, HL)

    def test_get_bad_io(self):
        with self.assertRaises(ValueError):
            IOs.input(6)
        with self.assertRaises(ValueError):
            IOs.output(1)

    def test_info_io(self):
        io = IOs.input(1)
        self.assertEqual(io.name, 'pin-1')
        self.assertEqual(io.num, 1)
        self.assertEqual(io.type, FAKETYPE)

