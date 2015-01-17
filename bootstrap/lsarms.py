#!/usr/bin/python
# test for OWI Edge arm connected
import sys

print('lsarms: \tfind OWI Edge robot arms')

print('startup:\timport prerequisites')

# import the USB and Time libraries into Python
import usb.core, usb.util, time

# TODO(PMM) - sorry, can't currently test for over 2 arms
print('seek:   \tfind arm')
RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x0000)

print('seek:   \tcomplete')
# Check if the arm is detected and warn if not
if RoboArm is None:
   print('seek:\tno arm found')
   exit(1)
else:
   print('seek:    \tarm found')
   exit(0)

