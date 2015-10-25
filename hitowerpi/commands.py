import hitowerpi.test as test
from hitowerpi import config

HELP = "\n    This is Hightower application for Raspberry Pi\n" \
       "    Version: %s\n" % (config.VERSION)


class TestCommands:

    def __init__(self, *args):
        test.run_test()


class ServerCommands:

    def __init__(self, *args):
        print(*args)


commands = {
    'test': lambda args: TestCommands(args),
    'server': lambda args: ServerCommands(args)
}


def run_commands(args):
    try:
        commands[args[0]](args[1:])
    except (KeyError, IndexError):
        print(HELP)

