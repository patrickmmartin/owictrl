#!/usr/bin/python

import sys

# import the USB and Time libraries into Python
import usb.core, usb.util, time

# do we want to track the estimated position?

"""Low level driver for the OWI Edge"""
class EdgeRaw:

   """ sets up class; initialises arm instance  """
   def __init__(self):
      # initialise essentials
      self._arm = usb.core.find(idVendor=0x1267, idProduct=0x0000)
      # check this
      if self._arm is None:
         raise ValueError("Arm not found")
      # and check this
      self.stop()
      
   """ stops the arm """   
   def stop(self):
      self._arm.ctrl_transfer(0x40,6,0x100,0,[0, 0, 0],1000)

   """applies output bit set for the duration"""
   def output(self, duration, motors):
#      print('moving', motors, 'for ', duration)
      # Start the movement
      self._arm.ctrl_transfer(0x40,6,0x100,0,motors,1000)
      time.sleep(duration)
      # Stop the movement after waiting specified duration
      self.stop()

