#! /usr/bin/python


""" trivial textual representation of arm moves"""


"""  motors """

motor_map_bits = {        
        'M5'  : { 'byte': 1, 'bits': [1,    2]}, # Base
        'M4'  : { 'byte': 0, 'bits': [64, 128]}, # Shoulder Down 
        'M3'  : { 'byte': 0, 'bits': [16,  32]}, # Elbow
        'M2'  : { 'byte': 0, 'bits': [4,    8]}, # Wrist 
        'M1'  : { 'byte': 0, 'bits': [1,    2]}, # Grab
        'L'   : { 'byte': 2, 'bits': [1]      }
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
        print (instruction)
        commands = instruction.split(",")
        for command in commands:
            print("\t%s" % command)
    
    # split on commas

def to_hl(str):
    raise Error("not implemented")


