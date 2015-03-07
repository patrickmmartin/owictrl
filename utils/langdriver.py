#! /usr/bin/python

""" test cases for the mini language arm driver """

import edgelang            # EdgeLang
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
      "M5,D5;" +
      "M1-,M3-,M4,D0.5;" +
      "M3-,M4,D4.5")

str_input = raw_input("enter string\n")
while not str_input == '':
    try:
        instructions = edgelang.to_ll(str_input)
        edge.addMoves(str_input)
        edge.move()
        edge.stop()
    except Exception as e:
        print "error in string: " + str(e)

    str_input = raw_input("enter string\n")

print('#### stopping arm')

edge.stop()
