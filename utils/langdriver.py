#! /usr/bin/python

""" test cases for the mini language arm driver """

import os
import edgelang            # EdgeLang
import edgell              # EdgeLL
import edgehl              # Edge



print('#### manual robot arm control program...')

edge = edgehl.Edge()


print('#### arm acquired')



print('#### enter command strings to control robot controls \n' + 
      'M5 \tbase \n' +
      'M4 \tshoulder \n' +
      'M3 \telbow \n' +
      'M2 \twrist \n' +
      'M1 \tgrabber \n' +
      '\' \tLED on \n' + 
      '<Enter> to quit')

print('example string for grabbing an item: \n' +
"M3,M4-,D4.5;" +
"M1,M3,M4-,D0.5;" +
"M1-,M3-,M4,D0.5;" +
"M3-,M4,D4.5")

str = raw_input("enter string")
while not str == '':
    try:
        instructions = edgelang.to_ll(move) 
        edge.addMoves(str)
        edge.move()
        edge.stop()
    except:
        print "error in string"
        
    str = raw_input("enter string")

print('#### stopping arm')

edge.stop()
