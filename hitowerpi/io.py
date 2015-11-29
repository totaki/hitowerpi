from hitowerpi.config import *


class BaseIO:
    pass


class PiIO(BaseIO):
    pass


PiIO = PiIO()


class SocketIO(BaseIO):
    pass


SocketIO = SocketIO()


class FakeIO:
    _states = {}

    def __init__(self):
        self._states = {
            INDICT: self._get_states(config.inputs),
            OUTDICT: self._get_states(config.outputs),
        }

    @staticmethod
    def _get_states(data):
        _dict = {}
        for key in data:
            _dict[key] = int(data[key][PINITOPT])
        return _dict

    def state(self, dct, num):
        return self._states[dct][num]

    def set(self, dct, num, state):
        if dct == OUTDICT:
            self._states[dct][num] = state
            return state
        else:
            raise ValueError('Cannot set state on input: INPUT%s' % num)

FakeIO = FakeIO()

_io_getter = {
    FAKETYPE: FakeIO,
    PITYPE: PiIO,
    SOCTYPE: SocketIO
}


class IO:

    def __init__(self, info, num, io_dct):
        self._io_dct = io_dct
        self._num = num
        self._info = info
        self._io = _io_getter[info[PTYPEOPT]]

    @property
    def name(self):
        return self._info[PNAMEOPT]

    @property
    def num(self):
        return self._num

    @property
    def type(self):
        return self._info[PTYPEOPT]

    @property
    def state(self):
        return self._io.state(self._io_dct, self._num)

    @property
    def description(self):
        try:
            return self._info[PDESCOPT]
        except KeyError:
            return False

    def set(self, state):
        if state not in [HL, LL]:
            raise ValueError("Bad value - %s" % state)
        self._io.set(self._io_dct, self._num, state)
        return "IO {} change state to {}".format(self._num, state)

    def up(self):
        return self.set(HL)

    def down(self):
        return self.set(LL)

    def change(self):
        return self.set(int(not self.state))

    def as_dict(self):
        return {
            PNAMEOPT: self.name,
            PDESCOPT: self.description,
            IOSTATE: self.state
        }


class IOs:

    @classmethod
    def _get(cls, num, dct, io_dct):
        if num in dct:
            return IO(dct[num], num, io_dct)
        else:
            raise ValueError("%s not exist in %s config" % (num, io_dct))

    @classmethod
    def input(cls, num):
        return cls._get(num, config.inputs, INDICT)

    @classmethod
    def output(cls, num):
        return cls._get(num, config.outputs, OUTDICT)

    @classmethod
    def _inputs(cls):
        for i in config.inputs:
            yield cls.input(i)

    @classmethod
    def inputs(cls):
        yield from cls._inputs()

    @classmethod
    def _outputs(cls):
        for i in config.outputs:
            yield cls.output(i)

    @classmethod
    def outputs(cls):
        yield from cls._outputs()

    @classmethod
    def all_as_gen(cls):
        return {INDICT: cls.inputs(), OUTDICT: cls.outputs()}

    @classmethod
    def all_as_dict(cls):
        dct = {}
        ios = cls.all_as_gen()
        for io in ios:
            dct[io] = {}
            for item in ios[io]:
                dct[io][item.num] = item.as_dict()
        return dct


if __name__ == "__main__":
    print("\nThis is module of hitowerpi package. Not executable\n")
