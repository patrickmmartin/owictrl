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


def to_bytes(instruction):
    """ converts to bytes for output """
    logger.info('to_bytes %s %s', type(instruction), instruction)
    motor_bytes = [0, 0, 0]
    motors = instruction.get('M', {})
    for motor in motors:
        vectors = motors[motor]
        logger.info('to_bytes %s. %s', motor, vectors)
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
        logger.info('output %s for %s', motor_bytes, duration)
        # Start the movement
        self._arm.ctrl_transfer(0x40, 6, 0x100, 0, motor_bytes, 1000)
        time.sleep(duration)
        # Stop the movement after waiting specified duration
        self.stop()

    def drive(self, instruction):
        """applies output motor set for the duration"""
        logger.info('drive %s', instruction)
        # Start the movement
        # {1: {'dir': 1}, 2: {'dir': -1}, 'D': 1.0}
        motor_bytes = to_bytes(instruction)
        duration = instruction.get('D', 0)
        logger.info('drive %s for %s', motor_bytes, duration)
        self.output(duration, motor_bytes)
        # Stop the movement after waiting specified duration
        self.stop()
