#!/usr/bin/python

from getch import getch
from edgell import Edge

key_map_motors = {        
        'a'  : [0,  1,  0], # Rotate Base Anticlockwise
        's'  : [0,  2,  0], # Rotate Base Clockwise
        'd'  : [128,0,  0], # Shoulder Down 
        'e'  : [64, 0,  0], # Shoulder Up
        'f'  : [32, 0,  0], # Elbow Down
        'r'  : [16, 0,  0], # Elbow Up
        'g'  : [8,  0,  0], # Wrist Down
        't'  : [4,  0,  0], # Wrist Up
        '['  : [2,  0,  0], # Grab open
        ']'  : [1,  0,  0],  # Grab close
        '\'' : [0,  0,  1], # light on
        }

def to_motors(ch):
    return key_map_motors.get(ch, [0, 0, 0])

edge = Edge()

print('waiting for /...')

c = ''
while c != '/':
    c = getch()
    motors = to_motors(c)
    if (motors != [0, 0, 0]):
#        print (c, motors)
        # special case for light
        if (motors == [0, 0,  1]):
            edge.move_raw(0.5, motors)
        else:
            edge.move_raw(0.02, motors)


print('stopping arm')

edge.stop()
