#!/usr/bin/python

""" runnable arm demo #1 """


def armdemo2():
    """ runner for the arm demo 2 """
    from logutil import LOGGER_DEFAULT as logger

    logger.info('startup')

    # import the USB and Time libraries into Python
    import usb.core
    import usb.util
    import time

    logger.info('seeking arm')

    # Allocate the name 'arm' to the USB device
    arm = usb.core.find(idVendor=0x1267, idProduct=0x0000)

    logger.info('find complete')

    # Check if the arm is detected and warn if not
    if arm is None:
        raise ValueError("Arm not found")

    # Define a procedure to execute each movement

    def move_arm(duration, cmd):
        """ the actual move function """
        # Start the movement
        arm.ctrl_transfer(0x40, 6, 0x100, 0, cmd, 1000)
        # Stop the movement after waiting specified duration
        time.sleep(duration)
        cmd = [0, 0, 0]
        arm.ctrl_transfer(0x40, 6, 0x100, 0, cmd, 1000)

    logger.info('complete: reversing')

    move_arm(0.5, [0, 2, 0])  # Rotate Base Clockwise
    move_arm(0.25, [128, 0, 0])  # Shoulder Down
    move_arm(0.25, [32, 0, 0])  # Elbow Down

    move_arm(0.5, [128 + 16, 0, 0])  # "Forward"


if __name__ == '__main__':
    armdemo2()
