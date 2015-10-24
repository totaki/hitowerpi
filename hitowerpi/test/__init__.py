import unittest


def run_test(module=None, case=None, func=None ):
    if module:
        pass
    elif module and case:
        pass
    elif module and case and func:
        pass
    else:
        run_all_test()


def run_all_test():
    tests = unittest.TestLoader().discover(start_dir=".")
    suite = unittest.defaultTestLoader.suiteClass()
    suite.addTest(tests)
    unittest.TextTestRunner().run(suite)
