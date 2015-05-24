#!/usr/bin/python

"""
  example of simple class with on/off motion controlled via the Leap Motion
  with a dead zone and movement on the extremes
"""

import Leap
import sys
from edgell import EdgeRaw, ACTION_BITS


class EdgeListener(Leap.Listener):

    """
    Simple listener to provide on/off control for Edge from Leap Motion
    """

    def __init__(self):
        """
        constructor initialised Edge member
        """
        self.edge = EdgeRaw()
        Leap.Listener.__init__(self)

    def on_frame(self, controller):
        """
        handles frame callback from Leap
        """
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        # Get hands
        for hand in frame.hands:
            #
            #handType = "Left hand" if hand.is_left else "Right hand"

            pinch = hand.pinch_strength

            if pinch < 0.05:
                self.edge.output(0.02, ACTION_BITS['GRAB_OPEN'])

            if pinch > 0.9:
                self.edge.output(0.02, ACTION_BITS['GRAB_CLOSE'])

            # Get the hand's normal vector and direction
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            (pitch) = (
                direction.pitch * Leap.RAD_TO_DEG)

#            normal = hand.palm_normal
#            (roll, yaw) = (
#                normal.roll * Leap.RAD_TO_DEG,
#                direction.yaw * Leap.RAD_TO_DEG)

            if pitch < -5:
                self.edge.output(0.02, ACTION_BITS['WRIST_DN'])

            if pitch > 15:
                self.edge.output(0.02, ACTION_BITS['WRIST_UP'])


def main():
    """
    entry point for the application - things happen afte the listener is added in
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
