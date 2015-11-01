import hitowerpi.config as config
import hitowerpi.server as server
import hitowerpi.test as test

HELP = "\n    This is Hightower application for Raspberry Pi\n" \
       "    Version: %s\n" % (config.VERSION)


class Tester:

    @classmethod
    def run(self, *args):
        test.run_test()


class Server:

    @classmethod
    def start(cls, *args):
        server.run_server()


commands = {
    'test': lambda args: Tester.run(args),
    'server': lambda args: Server.start(args)
}


def run_commands(args):
    try:
        commands[args[0]](args[1:])
    except (KeyError, IndexError):
        print(HELP)

