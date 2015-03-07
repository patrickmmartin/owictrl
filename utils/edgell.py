#!/usr/bin/python

""" arm edge low level language """

import usb.core
import usb.util
import time
from logutil import logger


# TODO(PMM) do we want to track the estimated position?

# motors

motor_map_bits = {
    5: {'byte': 1, 'bits': [1, 2]},  # Base
    4: {'byte': 0, 'bits': [64, 128]},  # Shoulder Down
    3: {'byte': 0, 'bits': [16, 32]},  # Elbow
    2: {'byte': 0, 'bits': [4, 8]},  # Wrist
    1: {'byte': 0, 'bits': [1, 2]},  # Grab
}

light_bits = {'byte': 2, 'bits': [1]}


def to_bytes(instruction):
    logger.info('to_bytes {0} {1}'.format(type(instruction), instruction))
    motor_bytes = [0, 0, 0]
    M = instruction.get('M', {})
    for motor in M:
        vectors = M[motor]
        logger.info('to_bytes {0}. {1}'.format(motor, vectors))
        # TODO(PMM) map from motor to bytes
        motor_bits = motor_map_bits[motor]
        byte = motor_bits['byte']
        if (vectors['dir'] == -1):
            bit = motor_bits['bits'][1]
        else:
            bit = motor_bits['bits'][0]
        motor_bytes[byte] = motor_bytes[byte] | bit

    if (instruction.get('L', False)):
        motor_bytes[2] = 1
    return motor_bytes

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
        self._arm.ctrl_transfer(0x40, 6, 0x100, 0, [0, 0, 0], 1000)

    """applies output bit set for the duration"""

    def output(self, duration, motor_bytes):
        logger.info('output {0} for {1}'.format(motor_bytes, duration))
        # Start the movement
        self._arm.ctrl_transfer(0x40, 6, 0x100, 0, motor_bytes, 1000)
        time.sleep(duration)
        # Stop the movement after waiting specified duration
        self.stop()

    """applies output motor set for the duration"""

    def drive(self, instruction):
        logger.info('drive {0}'.format(instruction))
        # Start the movement
        # {1: {'dir': 1}, 2: {'dir': -1}, 'D': 1.0}
        # TODO(PMM) map the motor bytes to the output bytes
        motor_bytes = to_bytes(instruction)
        duration = instruction.get('D', 0)
        logger.info('drive {0} for {1}'.format(motor_bytes, duration))
        self.output(duration, motor_bytes)
        # Stop the movement after waiting specified duration
        self.stop()
