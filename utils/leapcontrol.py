#!/usr/bin/python

"""
  class to control the robot arm from the Leap Motion
  with proportional control
"""

import Leap
import sys
from edgell import EdgeRaw


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


class EdgeListener(Leap.Listener):

    """
    listener for Leap events to control arm
    """

    def __init__(self):
        """
        construct the class and initialise the Edge arm instance
        """
        self.edge = EdgeRaw()
        Leap.Listener.__init__(self)

    def on_frame(self, controller):
        """
        frame callback from Leap - handle the frame data
        """
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        # Get hands
        for hand in frame.hands:
            pass
            #
            #handType = "Left hand" if hand.is_left else "Right hand"

#            pinch = hand.pinch_strength
#            normal = hand.palm_normal
#            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
#            (pitch, roll, yaw) = (
#                direction.pitch * Leap.RAD_TO_DEG,
#                normal.roll * Leap.RAD_TO_DEG,
#                direction.yaw * Leap.RAD_TO_DEG)

        # TODO(PMM) need to map the positions and orientations to the arm

        # TODO(PMM) need to have a class to track the arm's presumed position


def main():
    """
    creates a listener which handles the frames dispatched to it
    """
    # Create a listener and controller
    listener = EdgeListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
