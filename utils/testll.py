#! /usr/bin/python

""" test cases for the mini language output """

import unittest
import edgelang
import edgell


class EdgeLangBaseTestCase(unittest.TestCase):

    """ base class with setUp """
    _blank_move = [0, 0, 0]
    _LED_only = [0, 0, 1]

    def setUp(self):
        pass


class EdgeLangLLTestCase(EdgeLangBaseTestCase):

    """ test class with most basic parse test """

    def runTest(self):
        """ implement runTest"""
        instructions = edgelang.to_ll("D1.0")
        edge_bytes = edgell.to_bytes(instructions[0])
        self.assertEqual(edge_bytes, self._blank_move)


class EdgeLangLLTestResultCase(EdgeLangBaseTestCase):

    """ test for format of returned dict """

    def runTest(self):
        """ implement runTest"""
        instructions = edgelang.to_ll("M1+,M2-,D1.0")
        edge_bytes = edgell.to_bytes(instructions[0])
        self.assertEqual(edge_bytes, self._blank_move)


class EdgeLangLLLEDOffTestCase(EdgeLangBaseTestCase):

    """ test for setting LED """

    def runTest(self):
        """ implement runTest"""
        instructions = edgelang.to_ll(" L0 , D1 ")
        edge_bytes = edgell.to_bytes(instructions[0])
        self.assertEqual(edge_bytes, self._blank_move)


class EdgeLangLLLEDOnTestCase(EdgeLangBaseTestCase):

    """ test for setting LED """

    def runTest(self):
        """ implement runTest"""
        instructions = edgelang.to_ll(" L1 , D1 ")
        edge_bytes = edgell.to_bytes(instructions[0])
        self.assertEqual(edge_bytes, self._LED_only)


class EdgeLangInvalidTestCase(EdgeLangBaseTestCase):

    """ reject negative durations """

    @unittest.expectedFailure
    def runTest(self):
        """ implement runTest"""
        instructions = edgelang.to_ll("A1,B1,C1")
        edgell.to_bytes(instructions[0])


class EdgeLangDurationTestCase(EdgeLangBaseTestCase):

    """ reject invalid directives """
    @unittest.expectedFailure
    def runTest(self):
        """ implement runTest"""
        instructions = edgelang.to_ll("M1,D-1")
        edgell.to_bytes(instructions[0])

if __name__ == '__main__':
    unittest.main()
