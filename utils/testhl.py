#! /usr/bin/python

""" test cases for the mini language arm driver """

import os
import unittest
import edgelang            # EdgeLang
import edgell              # EdgeLL
import edgehl              # Edge

""" base class with setUp """


class EdgeHLBaseTestCase(unittest.TestCase):

    def setUp(self):
        self._edge = edgehl.Edge()

""" test for empty list """


class EdgeHLDefaultsTestCase(EdgeHLBaseTestCase):

    def runTest(self):
        self._edge.move()
        self._edge.stop()
        self._edge.pause()
        self._edge.resume()

""" test for setting empty list """


class EdgeHLEmptyTestCase(EdgeHLBaseTestCase):

    def runTest(self):
        self._edge.move()
        self._edge.stop()
        self._edge.pause()
        self._edge.resume()

""" test for setting moves """


class EdgeHLAddLEDTestCase(EdgeHLBaseTestCase):

    def runTest(self):
        self._edge.addMoves("L1,D0.1")
        self._edge.move()
        self._edge.stop()
        self._edge.pause()
        self._edge.resume()

""" test for setting moves """


class EdgeHLAddSingleMovesTestCase(EdgeHLBaseTestCase):

    def runTest(self):
        self._edge.addMoves("M1,D0.1")
        self._edge.addMoves("M1-,D0.1")
        self._edge.addMoves("M2,D0.1")
        self._edge.addMoves("M2-,D0.1")
        self._edge.addMoves("M3,D0.1")
        self._edge.addMoves("M3-,D0.1")
        self._edge.addMoves("M4,D0.1")
        self._edge.addMoves("M4-,D0.1")
        self._edge.addMoves("M5,D0.1")
        self._edge.addMoves("M5-,D0.1")
        self._edge.move()
        self._edge.stop()
        self._edge.pause()
        self._edge.resume()

""" test for setting moves """


class EdgeHLAddDoubleMovesTestCase(EdgeHLBaseTestCase):

    def runTest(self):
        self._edge.addMoves("M3,M4-,D0.5")
        self._edge.addMoves("M3-,M4,D0.5")
        self._edge.addMoves("M2,M4-,D0.5")
        self._edge.addMoves("M2-,M4,D0.5")
        self._edge.move()
        self._edge.stop()
        self._edge.pause()
        self._edge.resume()

""" test for setting moves """


class EdgeHLAddTripleMovesTestCase(EdgeHLBaseTestCase):

    def runTest(self):
        self._edge.addMoves("M5,D5")
        self._edge.addMoves("M3,M4-,D4.5")
        self._edge.addMoves("M1,M3,M4-,D0.5")
        self._edge.addMoves("M5-,D5")
        self._edge.addMoves("M1-,M3-,M4,D0.5")
        self._edge.addMoves("M3-,M4,D4.5")
        self._edge.move()
        self._edge.stop()
        self._edge.pause()
        self._edge.resume()


if __name__ == '__main__':
    unittest.main()
