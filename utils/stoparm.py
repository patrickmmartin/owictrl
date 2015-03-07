#!/usr/bin/python

""" OWI Edge Emergency Stop """

from logutil import LOGGER_DEFAULT as logger

logger.info('startup')


def stop():
    """ stops the arm """
    import usb.core
    import usb.util
    logger.info('seeking arm')

    arm = usb.core.find(idVendor=0x1267, idProduct=0x0000)
    logger.info('find complete')

    # Check if the arm is detected and warn if not
    if arm is None:
        raise ValueError("Arm not found")

    cmd = [0, 0, 0]

    logger.info('stopping')
    arm.ctrl_transfer(0x40, 6, 0x100, 0, cmd, 1000)

if __name__ == '__main__':
    stop()
