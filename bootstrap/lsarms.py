#!/usr/bin/python

""" test for OWI Edge arm connected """


def find_arms():
    """ attempts to locate OWI Edge arms """

    print 'lsarms: \tfind OWI Edge robot arms'

    print 'startup:\timport prerequisites'

    # import the USB and Time libraries into Python
    import usb.core
    import usb.util

    print 'seek:   \tfind arm'
    arm = usb.core.find(idVendor=0x1267, idProduct=0x0000)

    print 'seek:   \tcomplete'
    # Check if the arm is detected and warn if not
    if arm is None:
        print 'seek:    \tno arm found'
        exit(1)
    else:
        print 'seek:    \tarm found'
        exit(0)


if __name__ == '__main__':
    find_arms()
