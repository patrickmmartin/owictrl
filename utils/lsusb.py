#!/usr/bin/python

""" simpler USB devices lister """

import sys
import usb.core
# find all devices
dev = usb.core.find(find_all=True)
# loop through devices
for cfg in dev:
    sys.stdout.write(repr(cfg) + '\n')
# TODO(PMM) it would be nice to match the output of lsusb - needs sorting and description
#  sys.stdout.write('ID ' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n')
