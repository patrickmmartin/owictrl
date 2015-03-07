#! /usr/bin/python

""" test cases for the mini language output """

import unittest
import edgelang
import edgell

""" base class with setUp """


class EdgeLangBaseTestCase(unittest.TestCase):
    _blank_move = [0, 0, 0]
    _LED_only = [0, 0, 1]

    def setUp(self):
        pass

""" test class with most basic parse test """


class EdgeLangLLTestCase(EdgeLangBaseTestCase):

    def runTest(self):
        instructions = edgelang.to_ll("D1.0")
        edge_bytes = edgell.to_bytes(instructions[0])
        self.assertEqual(edge_bytes, self._blank_move)

""" test for format of returned dict """


class EdgeLangLLTestResultCase(EdgeLangBaseTestCase):

    def runTest(self):
        instructions = edgelang.to_ll("M1+,M2-,D1.0")
        edge_bytes = edgell.to_bytes(instructions[0])
        self.assertEqual(edge_bytes, self._blank_move)

""" test for setting LED """


class EdgeLangLLLEDOffTestCase(EdgeLangBaseTestCase):

    def runTest(self):
        instructions = edgelang.to_ll(" L0 , D1 ")
        edge_bytes = edgell.to_bytes(instructions[0])
        self.assertEqual(edge_bytes, self._blank_move)

""" test for setting LED """


class EdgeLangLLLEDOnTestCase(EdgeLangBaseTestCase):

    def runTest(self):
        instructions = edgelang.to_ll(" L1 , D1 ")
        edge_bytes = edgell.to_bytes(instructions[0])
        self.assertEqual(edge_bytes, self._LED_only)

""" reject negative durations """


class EdgeLangInvalidTestCase(EdgeLangBaseTestCase):

    @unittest.expectedFailure
    def runTest(self):
        instructions = edgelang.to_ll("A1,B1,C1")
        edge_bytes = edgell.to_bytes(instructions[0])

""" reject invalid directives """


class EdgeLangDurationTestCase(EdgeLangBaseTestCase):

    @unittest.expectedFailure
    def runTest(self):
        instructions = edgelang.to_ll("M1,D-1")
        edge_bytes = edgell.to_bytes(instructions[0])

if __name__ == '__main__':
    unittest.main()
