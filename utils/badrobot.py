#!/usr/bin/python

""" test cases for the mini language arm driver """

import logging

from logutil import LOGGER_DEFAULT as logger

def drive_lang():
    """ loop to drive the arm with the high level language """
    import edgelang            # EdgeLang
    import edgehl              # Edge

    print '#### manual robot arm control program...'

    logger.setLevel(20)
    
    edge = edgehl.Edge()

    print '#### arm acquired'


    demos  =  "M3,M4-,D4.5;" + \
             "M1,M3,M4-,D0.5;" + \
             "M5,D5;" + \
             "M1-,M3-,M4,D0.5;" + \
             "M3-,M4,D4.5"

    wait1  =  "D1"
    wait2  =  "D2"

    unfurl = "M5,M4-,M3,D5;M4-,M3,M2,D2.5;M2,D2.5"
    furl   = "M5-,M4,M3-,D5;M4,M3-,M2-,D2;M2-,D2"

    # multiply up
    shootR   = ("L1,D0.1;M5,D0.1;" * 40) + "L1,D0"  
    shootL   = ("L1,D0.1;M5-,D0.1;" * 40) + "L1,D0"    
    nod    = "M2,D1;M2-,D1"

    grab  =  "M1,D1"
    drop =  "M1-,D1"
    
    shake =  "M5-,D1;M5,D1"

    # we string together the actions into the "script"
    script = [unfurl, wait2, nod,
              wait2, nod,
              shake, wait2,
              shake, wait2,
              shake, wait2, wait2,
              grab,  wait2, drop,
              shootR, shootL, shootR, shootL, furl]

#    script = [shake, wait2,
#              shake, wait2,
#              shake, wait4,
#              grab,  wait2, drop]
    
    for str_input in script:
        try:
            edgelang.to_ll(str_input)  # tests the inputs
            print("command string: {0}".format(str_input))
            edge.add_moves(str_input)
            edge.move()
            edge.stop()
        except edgelang.EdgeLangError as err:
            print "error in string: " + str(err)

    print '#### stopping arm'

    edge.stop()

if __name__ == '__main__':
    drive_lang()
