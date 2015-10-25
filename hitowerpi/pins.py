from hitowerpi import config


class FakeGPIO:
    _states = {}

    @property
    def states(self):
        return self._states

    @states.setter
    def states(self, value):
        """Data must be {int: bool, int: bool}"""
        self._states = value

    def input(self, pin):
        return self._states[pin]

    def output(self, pin, value):
        self._states[pin] = value

FakeGPIO = FakeGPIO()


class Pin:
    GPIO = (lambda: FakeGPIO if config.FAKEPI else False)()

    def __init__(self, pin, info):
        self._pin = pin
        self._info = info

    def _get_state(self):
        return int(self.GPIO.input(self._pin))

    def _set_state(self, value):
        self.GPIO.output(self._pin, bool(value))
        return value

    @property
    def pin(self):
        return self._pin

    @property
    def state(self):
        return self._get_state()

    @state.setter
    def state(self, value):
        if value not in [0, 1]:
            raise ValueError("Bad value - %s" % value)

        if self._info['type'] == config.INPUT:
            raise AttributeError

        try:
            self._set_state(value)
        except Exception:
            pass

    def chg_state(self):
        self.state = not self.state
        return self.state


class Pins:
    _pins = config.PINS

    @classmethod
    def get(cls, pin):
        if pin in cls._pins:
            return Pin(pin, cls._pins[pin])
        else:
            raise ValueError("Pin %s not exist in config" % pin)

    @classmethod
    def all(cls):
        return tuple(Pin(i) for i in cls._pins)


if __name__ == "__main__":
    print("\nThis is module of hitowerpi package. Not executable\n")
