#! /usr/bin/python

""" test cases for the mini language arm driver """


def drive_lang():
    """ loop to drive the arm with the high level language """
    import edgelang            # EdgeLang
    import edgehl              # Edge

    print '#### manual robot arm control program...'

    edge = edgehl.Edge()

    print '#### arm acquired'

    command_listing = ('#### enter command strings to control robot controls \n' +
                       'M5 \tbase \n' +
                       'M4 \tshoulder \n' +
                       'M3 \telbow \n' +
                       'M2 \twrist \n' +
                       'M1 \tgrabber \n' +
                       '\' \tLED on \n' +
                       '<Enter> to quit')

    example_string = ('example string for grabbing an item: \n' +
                      "M3,M4-,D4.5;" +
                      "M1,M3,M4-,D0.5;" +
                      "M5,D5;" +
                      "M1-,M3-,M4,D0.5;" +
                      "M3-,M4,D4.5")

    print command_listing

    print example_string

    str_input = raw_input("enter string\n")
    while not str_input == '':
        try:
            edgelang.to_ll(str_input)  # tests the inputs
            edge.add_moves(str_input)
            edge.move()
            edge.stop()
        except edgelang.EdgeLangError as err:
            print "error in string: " + str(err)

        str_input = raw_input("enter string\n")

    print '#### stopping arm'

    edge.stop()

if __name__ == '__main__':
    drive_lang()
