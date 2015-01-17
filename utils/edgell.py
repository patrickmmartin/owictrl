#!/usr/bin/python

import sys

# import the USB and Time libraries into Python
import usb.core, usb.util, time

"""Low level driver for the OWI Edge"""
class Edge:

   def stop(self):
      self._arm.ctrl_transfer(0x40,6,0x100,0,[0, 0, 0],1000)

   def __init__(self):
      # initialise essentials
      self._arm = usb.core.find(idVendor=0x1267, idProduct=0x0000)
      # check this
      if self._arm is None:
         raise ValueError("Arm not found")
      # and check this
      self.stop()
      
   """moves the set of motors for the duration"""
   def move_raw(self, duration, motors):
#      print('moving', motors, 'for ', duration)
      # Start the movement
      self._arm.ctrl_transfer(0x40,6,0x100,0,motors,1000)
      time.sleep(duration)
      # Stop the movement after waiting specified duration
      self.stop()

