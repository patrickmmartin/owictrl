#! /usr/bin/python

""" runnable test cases for the high level arm language """

import os
import unittest
from edgell import EdgeRaw


class EdgeLLBaseTestCase(unittest.TestCase):
    def setUp(self):
        # check that we are running as root (default requirement for usb writes)
        self.assertEqual(os.geteuid(), 0, "access to the device requires root-ness")
        # ok, good to go
        self.arm = EdgeRaw()

class EdgeLLConstructTestCase(EdgeLLBaseTestCase):
    def runTest(self):
        pass

class EdgeLLLEDTestCase(EdgeLLBaseTestCase):
    def runTest(self):
        print("blinking light.")
        self.arm.output(0.5, [0,  0,  1])

class EdgeLLM5TestCase(EdgeLLBaseTestCase):
    def runTest(self):
        print("moving base.")
        self.arm.output(0.5, [0,  1,  0])
        self.arm.output(0.5, [0,  2,  0])

if __name__ == '__main__':
    unittest.main()

