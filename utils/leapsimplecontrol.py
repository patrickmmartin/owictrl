#!/usr/bin/python

"""
  example of simple class with on/off motion controlled via the Leap Motion
  with a dead zone and movement on the extremes 
"""

import Leap
import sys
import thread
import time
from edgell import EdgeRaw


action_bits = {
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

    def on_init(self, controller):
        self.edge = EdgeRaw()
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        # Get hands
        for hand in frame.hands:
            #
            handType = "Left hand" if hand.is_left else "Right hand"

            pinch = hand.pinch_strength

            if (pinch < 0.05):
                self.edge.output(0.02, action_bits['GRAB_OPEN'])

            if (pinch > 0.9):
                self.edge.output(0.02, action_bits['GRAB_CLOSE'])

            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            (pitch, roll, yaw) = (
                direction.pitch * Leap.RAD_TO_DEG,
                normal.roll * Leap.RAD_TO_DEG,
                direction.yaw * Leap.RAD_TO_DEG)

            if (pitch < -5):
                self.edge.output(0.02, action_bits['WRIST_DN'])

            if (pitch > 15):
                self.edge.output(0.02, action_bits['WRIST_UP'])


def main():
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
