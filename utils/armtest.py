#! /usr/bin/python

""" runnable test cases for the high level arm language """

import os
import unittest
from edgell import EdgeRaw
from logutil import LOGGER_DEFAULT as logger


class EdgeLLBaseTestCase(unittest.TestCase):

    """ base class for tests """

    def setUp(self):
        """ shared setUp """
        # check that we are running as root (default requirement for usb
        # writes)
        self.assertEqual(
            os.geteuid(),
            0,
            "access to the device requires root-ness")
        # ok, good to go
        self.arm = EdgeRaw()


class EdgeLLConstructTestCase(EdgeLLBaseTestCase):

    """ construction test """

    def runTest(self):
        """ run test """
        pass


class EdgeLLLEDTestCase(EdgeLLBaseTestCase):

    """ light test """

    def runTest(self):
        """ run test """
        logger.info("blinking light.")
        self.arm.output(0.5, [0, 0, 1])


class EdgeLLM5TestCase(EdgeLLBaseTestCase):

    """ move test """

    def runTest(self):
        """ run test """
        logger.info("moving base.")
        self.arm.output(0.5, [0, 1, 0])
        self.arm.output(0.5, [0, 2, 0])

if __name__ == '__main__':
    unittest.main()
