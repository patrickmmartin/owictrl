#!/usr/bin/python

import sys

# import the USB and Time libraries into Python
import usb.core, usb.util, time

# do we want to track the estimated position?


# motors

motor_map_bits = {        
        '5'  : { 'byte': 1, 'bits': [1,    2]}, # Base
        '4'  : { 'byte': 0, 'bits': [64, 128]}, # Shoulder Down 
        '3'  : { 'byte': 0, 'bits': [16,  32]}, # Elbow
        '2'  : { 'byte': 0, 'bits': [4,    8]}, # Wrist 
        '1'  : { 'byte': 0, 'bits': [1,    2]}, # Grab
        }
light_bits = 
        { 'byte': 2, 'bits': [1] }



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
   def output(self, duration, motor_bytes):
#      print('moving', motor_bytes, 'for ', duration)
      # Start the movement
      self._arm.ctrl_transfer(0x40,6,0x100, 0, motor_bytes, 1000)
      time.sleep(duration)
      # Stop the movement after waiting specified duration
      self.stop()

   """applies output motor set for the duration"""
   def output(self, duration, motors):
#      print('moving', motors, 'for ', duration)
      # Start the movement
      # {1: {'dir': 1}, 2: {'dir': -1}, 'D': 1.0}
      motor_bytes = [0, 0, 0] 
      self._arm.ctrl_transfer(0x40,6,0x100,0,motor_bytes,1000)
      time.sleep(duration)
      # Stop the movement after waiting specified duration
      self.stop()

