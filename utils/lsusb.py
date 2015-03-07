#!/usr/bin/python

""" simpler USB devices lister """


def lsusb():
    """ lists the USB devices """
    import sys
    import usb.core
    # find all devices
    dev = usb.core.find(find_all=True)
    # loop through devices
    for cfg in dev:
        sys.stdout.write(repr(cfg) + '\n')

if __name__ == '__main__':
    lsusb()
