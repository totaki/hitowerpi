from hitowerpi import config

PIN1, PIN2, PIN10, PIN16 = (1, 2, 10, 16)
PIN1_STATE, PIN2_STATE, PIN10_STATE, PIN16_STATE = (0, 1, 1, 0)

FIXTURES_PIN_CONFIG = {
    PIN1: {'type': config.INPUT, 'name': 'Pin: %s' % PIN1},
    PIN2: {'type': config.INPUT, 'name': 'Pin: %s' % PIN2},
    PIN10: {'type': config.OUTPUT, 'name': 'Pin: %s' % PIN10},
    PIN16: {'type': config.INPUT, 'name': 'Pin: %s' % PIN16}
}

FIXTURES_STATES = {PIN1: PIN1_STATE, PIN2: PIN2_STATE, PIN10: PIN10_STATE, PIN16: PIN16_STATE }
