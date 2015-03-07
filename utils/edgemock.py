#!/usr/bin/python

""" mock class for the edge arm """

from logutil import LOGGER_DEFAULT as logger

MOTOR_MAP_BITS = {
    'a': [0, 1, 0],  # Rotate Base Anticlockwise
    's': [0, 2, 0],  # Rotate Base Clockwise
    'd': [128, 0, 0],  # Shoulder Down
    'e': [64, 0, 0],  # Shoulder Up
    'f': [32, 0, 0],  # Elbow Down
    'r': [16, 0, 0],  # Elbow Up
    'g': [8, 0, 0],  # Wrist Down
    't': [4, 0, 0],  # Wrist Up
    '[': [2, 0, 0],  # Grab open
    ']': [1, 0, 0],  # Grab close
    '\'': [0, 0, 1],  # light on
}


def to_unit_vecs(bits):
    """ converts to unit vectors """
    result = [0, 0, 0]
    if bits[0] & 1:
        result[0] = 1
    if bits[0] & 2:
        result[0] = -1

    if bits[0] & 128:
        result[0] = 1
    if bits[0] & 64:
        result[0] = -1

    if bits[0] & 32:
        result[0] = 1
    if bits[0] & 16:
        result[0] = -1

    if bits[0] & 8:
        result[0] = 1
    if bits[0] & 4:
        result[0] = -1

    return result

# it's around 12 degrees per second
ANGULAR_VELOCITY = 12


class EdgeMock(object):

    """Mock low level driver for the OWI Edge"""

    def __init__(self):
        """ sets up class; initialises arm instance  """
        self.angles = (0, 0, 0)  # degrees
        self.speeds = (0, 0, 0)  # degrees / s
        logger.info('__init__')

    def stop(self):
        """ stops the arm """
        logger.info('stop')
        self.speeds = (0, 0, 0)

    def output(self, duration, motors):
        """applies output bit set for the duration"""
        logger.info('moving % for %s', motors, duration)
        # time.sleep(duration)
        # update the positions
        unit_vecs = to_unit_vecs(motors)
        for i in range(0, 2):
            self.angles[i] = unit_vecs[i] * duration
        self.stop()
