#! /usr/bin/python

""" trivial textual representation of arm moves"""


def parse_motor(command, res):
    # Mn[+/-]
    # get motor number
    # get direction
    clen = len(command)
    lengths = set([2, 3])
    if not (set([clen]) & lengths):
        raise Exception(
            'command not correct length {0} (length {1})'.format(
                "[2, 3]",
                clen))
    m = int(command[1])
    d = 1 if ((clen < 3) or (command[2] == '+')) else -1
    res['M'][m] = {'dir': d}


def parse_duration(command, res):
    # Dn.nn
    # get duration
    d = float(command[1:])
    if (d < 0):
        raise Exception('duration must be non-negative')
    res['D'] = d


def parse_light(command, res):
    # L[1/0]
    # get on/off
    res['L'] = command[1:] == "1"

command_map = {
    'M': parse_motor,
    'D': parse_duration,
    'L': parse_light
}

""" semicolon delimited set of comma delimited set of params with a char code and 1-2 params """
""" examples of input """
"""  'M1+,M2-,D1;M1-,M2+,D2' """
"""     M1 forwards, M2 backwards for 1 second, then  """
"""     M1 backwards, M2 forwards for 1 second  """


def to_ll(str):
    result = list()
    instructions = str.split(";")
    for instruction in instructions:
        commands = instruction.split(",")
        ret = {'M': {}}
        for command in commands:
            command = command.strip()
            if (len(command)) == 0:
                raise Exception("command cannot be blank")
            parse_func = command_map.get(command[0])
            if (parse_func is None):
                raise Exception("command unknown {0}".format(command[0]))

            parse_func(command, ret)
            # could enforce that a duration is specified here here
        result.append(ret)

    return result

    # split on commas


def to_hl(str):
    raise Error("not implemented")
