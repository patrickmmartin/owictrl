#!/usr/bin/python

""" OWI Edge Emergency Stop """

from logutil import logger

logger.info('startup')

def stop():

    import usb.core
    import usb.util
    logger.info('seeking arm')

    RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x0000)
    logger.info('find complete')

    # Check if the arm is detected and warn if not
    if RoboArm is None:
        raise ValueError("Arm not found")

    ArmCmd = [0, 0, 0]

    logger.info('stopping')
    RoboArm.ctrl_transfer(0x40, 6, 0x100, 0, ArmCmd, 1000)

if (__name__ == '__main__'):
    stop()
