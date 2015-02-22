#!/usr/bin/python

""" mock class for the edge arm """

import sys, time

motor_map_bits = {        
        'a'  : [0,  1,  0], # Rotate Base Anticlockwise
        's'  : [0,  2,  0], # Rotate Base Clockwise
        'd'  : [128,0,  0], # Shoulder Down 
        'e'  : [64, 0,  0], # Shoulder Up
        'f'  : [32, 0,  0], # Elbow Down
        'r'  : [16, 0,  0], # Elbow Up
        'g'  : [8,  0,  0], # Wrist Down
        't'  : [4,  0,  0], # Wrist Up
        '['  : [2,  0,  0], # Grab open
        ']'  : [1,  0,  0],  # Grab close
        '\'' : [0,  0,  1], # light on
        }

def to_unit_vecs(bits):
   result = [0, 0, 0]
   if (bits[0] & 1):
      result[0] = 1
   if (bits[0] & 2):
      result[0] = -1

   if (bits[0] & 128):
      result[0] = 1
   if (bits[0] & 64):
      result[0] = -1

   if (bits[0] & 32):
      result[0] = 1
   if (bits[0] & 16):
      result[0] = -1

   if (bits[0] & 8):
      result[0] = 1
   if (bits[0] & 4):
      result[0] = -1

# it's around 12 degrees per second
AngularVelocity = 12

"""Mock low level driver for the OWI Edge"""
class EdgeMock:

   """ sets up class; initialises arm instance  """
   def __init__(self):
      self.angles = (0, 0, 0) # degrees
      print('__init__')
      
   """ stops the arm """   
   def stop(self):
      print('stop')

   """applies output bit set for the duration"""
   def output(self, duration, motors):
      print('moving', motors, 'for ', duration)
      # time.sleep(duration)
      # update the positions
      unit_vecs = to_unit_vecs(motors)
      for i in range(0,2):
         self.angles[i] = unit_vecs[i] * duration
      self.stop()

