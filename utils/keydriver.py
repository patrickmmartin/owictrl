#!/usr/bin/python

from getch import getch
from edgell import EdgeRaw

key_map_bits = {        
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

def to_bits(ch):
    return key_map_bits.get(ch, [0, 0, 0])

print('#### manual robot arm control program...')

edge = EdgeRaw()

print('#### arm acquired')

print('#### controls \n' + 
      'a/s \tbase \n' +
      'd/e \tshoulder \n' +
      'f/r \telbow \n' +
      'g/t \twrist \n' +
      '[/] \tgrabber \n' +
      '\' \tLED on ')

print('#### waiting for q to quit ...\n>')

c = ''
while c != 'q':
    c = getch()
    bits = to_bits(c)
    if (bits != [0, 0, 0]):
#        print (c, motors)
        # special case for light
        if (bits == [0, 0,  1]):
            edge.output(0.5, bits)
        else:
            edge.output(0.02, bits)

print('stopping arm')

edge.stop()
