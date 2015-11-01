import unittest
import hitowerpi.test.fixtures as fxs
from hitowerpi import config
from hitowerpi.pins import Pins, FakeGPIO


class TestPinMethods(unittest.TestCase):

    def setUp(self):
        FakeGPIO.states = fxs.FIXTURES_STATES
        config.PINS = fxs.FIXTURES_PIN_CONFIG

    def test_get_pin_state(self):
        pin = Pins.get(fxs.PIN1)
        self.assertEqual(pin.state, fxs.PIN1_STATE)

    def test_set_pin_state(self):
        pin = Pins.get(fxs.PIN1)
        pin.state = not fxs.PIN1_STATE
        self.assertEqual(pin.state, not fxs.PIN1_STATE)

    def test_change_pin_state(self):
        pin = Pins.get(fxs.PIN1)
        pin.chg_state()
        self.assertEqual(pin.state, not fxs.PIN1_STATE)
        pin.chg_state()

    def test_get_bad_pin(self):
        with self.assertRaises(ValueError):
            Pins.get(0)

    def test_set_bad_pin(self):
        with self.assertRaises(ValueError):
            Pins.get(fxs.PIN1).state = 10

    def test_set_bad_pin(self):
        with self.assertRaises(AttributeError):
            Pins.get(fxs.PIN2).state = 0


def run_test():
    suite = unittest.defaultTestLoader.suiteClass()
    suite.addTest(unittest.makeSuite(TestPinMethods))
    unittest.TextTestRunner().run(suite)
