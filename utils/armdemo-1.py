#!/usr/bin/python

""" runnable arm demo #1 """


def armdemo1():
    """ runs the arm demo #1 """
    from logutil import LOGGER_DEFAULT as logger

    logger.info('startup')

    # import the USB and Time libraries into Python
    import usb.core
    import usb.util
    import time

    logger.info('seeking arm')

    arm = usb.core.find(idVendor=0x1267, idProduct=0x0000)

    logger.info('find complete')

    # Check if the arm is detected and warn if not
    if arm is None:
        raise ValueError("Arm not found")

    def move_arm(duration, cmd):
        """ actual arm driver function  """
        # Start the movement
        arm.ctrl_transfer(0x40, 6, 0x100, 0, cmd, 1000)
        # Stop the movement after waiting specified duration
        time.sleep(duration)
        cmd = [0, 0, 0]
        arm.ctrl_transfer(0x40, 6, 0x100, 0, cmd, 1000)

    logger.info('controlling arm')

    # Give the arm some commands
    move_arm(0.5, [0, 1, 0])  # Rotate Base Anticlockwise
    move_arm(0.25, [64, 0, 0])  # Shoulder Up
    move_arm(0.25, [16, 0, 0])  # Elbow Up

    move_arm(0.5, [64 + 32, 0, 0])  # "Back"

if __name__ == '__main__':
    armdemo1()
