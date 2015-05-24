#!/usr/bin/python

"""
  class to control the robot arm from the Leap Motion
  with proportional control
"""

import Leap
import sys
from edgell import EdgeRaw, ACTION_BITS


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
