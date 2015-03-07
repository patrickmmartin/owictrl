""" trivial textual representation of arm moves"""


class EdgeLangError(Exception):

    """Base class for exceptions in this module."""
    pass


def parse_motor(command, res):
    """ parses command string """
    # Mn[+/-]
    # get motor number
    # get direction
    clen = len(command)
    lengths = set([2, 3])
    if not set([clen]) & lengths:
        raise EdgeLangError(
            'command not correct length {0} (length {1})'.format(
                "[2, 3]",
                clen))
    motor = int(command[1])
    duration = 1 if (clen < 3) or (command[2] == '+') else -1
    res['M'][motor] = {'dir': duration}


def parse_duration(command, res):
    """ parses duration string """
    # Dn.nn
    # get duration
    duration = float(command[1:])
    if duration < 0:
        raise EdgeLangError('duration must be non-negative')
    res['D'] = duration


def parse_light(command, res):
    """ parses light string """
    # L[1/0]
    # get on/off
    res['L'] = command[1:] == "1"

COMMAND_MAP = {
    'M': parse_motor,
    'D': parse_duration,
    'L': parse_light
}

#""" semicolon delimited set of comma delimited set of params with a char code and 1-2 params """
#""" examples of input """
#"""  'M1+,M2-,D1;M1-,M2+,D2' """
#"""     M1 forwards, M2 backwards for 1 second, then  """
#"""     M1 backwards, M2 forwards for 1 second  """


def to_ll(commandstr):
    """ parses command string to low level """
    result = list()
    instructions = commandstr.split(";")
    for instruction in instructions:
        commands = instruction.split(",")
        ret = {'M': {}}
        for command in commands:
            command = command.strip()
            if (len(command)) == 0:
                raise EdgeLangError("command cannot be blank")
            parse_func = COMMAND_MAP.get(command[0])
            if parse_func is None:
                raise EdgeLangError("command unknown {0}".format(command[0]))

            parse_func(command, ret)
            # could enforce that a duration is specified here here
        result.append(ret)

    return result

    # split on commas
