import unittest
from hitowerpi import config
from hitowerpi.pins import  Pins, FakeGPIO

PIN1, PIN2, PIN10, PIN16 = (1, 2, 10, 16)
PIN1_STATE, PIN2_STATE, PIN10_STATE, PIN16_STATE = (0, 1, 1, 0)

FIXTURES_PIN_CONFIG = {
    PIN1: {'type': config.INPUT, 'name': 'Pin: %s' % PIN1},
    PIN2: {'type': config.INPUT, 'name': 'Pin: %s' % PIN2},
    PIN10: {'type': config.OUTPUT, 'name': 'Pin: %s' % PIN10},
    PIN16: {'type': config.INPUT, 'name': 'Pin: %s' % PIN16}
}
FIXTURES_STATES = {PIN1: PIN1_STATE, PIN2: PIN2_STATE, PIN10: PIN10_STATE, PIN16: PIN16_STATE }


class TestPinMethods(unittest.TestCase):

    def setUp(self):
        FakeGPIO.states = FIXTURES_STATES
        config.PINS = FIXTURES_PIN_CONFIG

    def test_get_pin_state(self):
        pin = Pins.get(PIN1)
        self.assertEqual(pin.state, PIN1_STATE)

    def test_set_pin_state(self):
        pin = Pins.get(PIN1)
        pin.state = not PIN1_STATE
        self.assertEqual(pin.state, not PIN1_STATE)

    def test_change_pin_state(self):
        pin = Pins.get(PIN1)
        pin.chg_state()
        self.assertEqual(pin.state, not PIN1_STATE)
        pin.chg_state()

    def test_get_bad_pin(self):
        with self.assertRaises(ValueError):
            Pins.get(0)

    def test_set_bad_pin(self):
        with self.assertRaises(ValueError):
            Pins.get(1).state = 10

    def test_set_bad_pin(self):
        with self.assertRaises(AttributeError):
            Pins.get(10).state = 0


class Test2Methods(unittest.TestCase):
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


def run_test():
    suite = unittest.defaultTestLoader.suiteClass()
    suite.addTest(unittest.makeSuite(TestPinMethods))
    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    run_test()
