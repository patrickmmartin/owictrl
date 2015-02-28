#!/usr/bin/python

""" OWI Edge Emergency Stop """

import sys

print('startup')

import usb.core
import usb.util
import time
print('seeking arm')

RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x0000)
print('find complete')

# Check if the arm is detected and warn if not
if RoboArm is None:
    raise ValueError("Arm not found")

ArmCmd = [0, 0, 0]

print('stopping')
RoboArm.ctrl_transfer(0x40, 6, 0x100, 0, ArmCmd, 1000)
