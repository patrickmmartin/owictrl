#!/usr/bin/python

""" runnable arm demo #1 """

def armdemo1():
    from logutil import logger

    logger.info('startup')

    # import the USB and Time libraries into Python
    import usb.core
    import usb.util
    import time

    logger.info('seeking arm')

    # Allocate the name 'RoboArm' to the USB device
    RoboArm = usb.core.find(idVendor=0x1267, idProduct=0x0000)

    logger.info('find complete')

    # Check if the arm is detected and warn if not
    if RoboArm is None:
        raise ValueError("Arm not found")

    # Define a procedure to execute each movement


    def MoveArm(Duration, ArmCmd):
        # Start the movement
        RoboArm.ctrl_transfer(0x40, 6, 0x100, 0, ArmCmd, 1000)
        # Stop the movement after waiting specified duration
        time.sleep(Duration)
        ArmCmd = [0, 0, 0]
        RoboArm.ctrl_transfer(0x40, 6, 0x100, 0, ArmCmd, 1000)

    logger.info('controlling arm')

    # Give the arm some commands
    MoveArm(0.5, [0, 1, 0])  # Rotate Base Anticlockwise
    MoveArm(0.25, [64, 0, 0])  # Shoulder Up
    MoveArm(0.25, [16, 0, 0])  # Elbow Up

    MoveArm(0.5, [64 + 32, 0, 0])  # "Back"

if (__name__ == '__main__'):
    armdemo1()
