#!/usr/bin/python

""" arm edge low level language """

import usb.core
import usb.util
import time
from logutil import LOGGER_DEFAULT as logger


# motors

MOTOR_MAP_BITS = {
    5: {'byte': 1, 'bits': [1, 2]},  # Base
    4: {'byte': 0, 'bits': [64, 128]},  # Shoulder Down
    3: {'byte': 0, 'bits': [16, 32]},  # Elbow
    2: {'byte': 0, 'bits': [4, 8]},  # Wrist
    1: {'byte': 0, 'bits': [1, 2]},  # Grab
}

LIGHT_BITS = {'byte': 2, 'bits': [1]}

ACTION_BITS = {
    'GRAB_CLOSE':  [1, 0, 0],  # Grab close
    'GRAB_OPEN':   [2, 0, 0],  # Grab open
    'WRIST_UP':    [4, 0, 0],  # Wrist Up
    'WRIST_DN':    [8, 0, 0],  # Wrist Down
    'ELBOW_UP':    [16, 0, 0],  # Elbow Up
    'ELBOW_DN':    [32, 0, 0],  # Elbow Down
    'SHOULDER_UP': [64, 0, 0],  # Shoulder Up
    'SHOULDER_DN': [128, 0, 0],  # Shoulder Down
    'LIGHT_ON':    [0, 0, 1],  # light on
    'BASE_AC':     [0, 1, 0],  # Rotate Base Anticlockwise
    'BASE_CL':     [0, 2, 0],  # Rotate Base Clockwise
}


def to_bytes(instruction):
    """ converts to bytes for output """
    logger.debug('to_bytes %s %s', type(instruction), instruction)
    motor_bytes = [0, 0, 0]
    motors = instruction.get('M', {})
    for motor in motors:
        vectors = motors[motor]
        logger.debug('to_bytes %s. %s', motor, vectors)
        motor_bits = MOTOR_MAP_BITS[motor]
        byte = motor_bits['byte']
        if vectors['dir'] == -1:
            bit = motor_bits['bits'][1]
        else:
            bit = motor_bits['bits'][0]
        motor_bytes[byte] = motor_bytes[byte] | bit

    if instruction.get('L', False):
        motor_bytes[2] = 1
    return motor_bytes


class EdgeRaw(object):

    """Low level driver for the OWI Edge"""

    def __init__(self):
        """ sets up class; initialises arm instance  """
        # initialise essentials
        self._arm = usb.core.find(idVendor=0x1267, idProduct=0x0000)
        # check this
        if self._arm is None:
            raise ValueError("Arm not found")
        # and check this
        self.stop()

    def stop(self):
        """ stops the arm """
        self._arm.ctrl_transfer(0x40, 6, 0x100, 0, [0, 0, 0], 1000)

    def output(self, duration, motor_bytes):
        """applies output bit set for the duration"""
        logger.debug('output %s for %s', motor_bytes, duration)
        # Start the movement
        self._arm.ctrl_transfer(0x40, 6, 0x100, 0, motor_bytes, 1000)
        time.sleep(duration)
        # Stop the movement after waiting specified duration
        self.stop()

    def drive(self, instruction):
        """applies output motor set for the duration"""
        logger.debug('drive %s', instruction)
        # Start the movement
        # {1: {'dir': 1}, 2: {'dir': -1}, 'D': 1.0}
        motor_bytes = to_bytes(instruction)
        duration = instruction.get('D', 0)
        logger.debug('drive %s for %s', motor_bytes, duration)
        self.output(duration, motor_bytes)
        # Stop the movement after waiting specified duration
        self.stop()
