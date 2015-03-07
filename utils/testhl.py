#! /usr/bin/python

""" test cases for the mini language arm driver """

import unittest
import edgehl              # Edge


class EdgeHLBaseTestCase(unittest.TestCase):

    """ base class with setUp """

    def setUp(self):
        """ shared setup """
        self._edge = edgehl.Edge()


class EdgeHLDefaultsTestCase(EdgeHLBaseTestCase):

    """ test for empty list """

    def runTest(self):
        """ run test case """
        self._edge.move()
        self._edge.stop()
        self._edge.pause()
        self._edge.resume()


class EdgeHLEmptyTestCase(EdgeHLBaseTestCase):

    """ test for setting empty list """

    def runTest(self):
        """ run test case """
        self._edge.move()
        self._edge.stop()
        self._edge.pause()
        self._edge.resume()


class EdgeHLAddLEDTestCase(EdgeHLBaseTestCase):

    """ test for setting moves """

    def runTest(self):
        """ run test case """
        self._edge.add_moves("L1,D0.1")
        self._edge.move()
        self._edge.stop()
        self._edge.pause()
        self._edge.resume()


class EdgeHLAddSingleMovesTestCase(EdgeHLBaseTestCase):

    """ test for setting moves """

    def runTest(self):
        """ run test case """
        self._edge.add_moves("M1,D0.1")
        self._edge.add_moves("M1-,D0.1")
        self._edge.add_moves("M2,D0.1")
        self._edge.add_moves("M2-,D0.1")
        self._edge.add_moves("M3,D0.1")
        self._edge.add_moves("M3-,D0.1")
        self._edge.add_moves("M4,D0.1")
        self._edge.add_moves("M4-,D0.1")
        self._edge.add_moves("M5,D0.1")
        self._edge.add_moves("M5-,D0.1")
        self._edge.move()
        self._edge.stop()
        self._edge.pause()
        self._edge.resume()


class EdgeHLAddDoubleMovesTestCase(EdgeHLBaseTestCase):

    """ test for setting moves """

    def runTest(self):
        """ run test case """
        self._edge.add_moves("M3,M4-,D0.5")
        self._edge.add_moves("M3-,M4,D0.5")
        self._edge.add_moves("M2,M4-,D0.5")
        self._edge.add_moves("M2-,M4,D0.5")
        self._edge.move()
        self._edge.stop()
        self._edge.pause()
        self._edge.resume()


class EdgeHLAddTripleMovesTestCase(EdgeHLBaseTestCase):

    """ test for setting moves """

    def runTest(self):
        """ run test case """
        self._edge.add_moves("M5,D5")
        self._edge.add_moves("M3,M4-,D4.5")
        self._edge.add_moves("M1,M3,M4-,D0.5")
        self._edge.add_moves("M5-,D5")
        self._edge.add_moves("M1-,M3-,M4,D0.5")
        self._edge.add_moves("M3-,M4,D4.5")
        self._edge.move()
        self._edge.stop()
        self._edge.pause()
        self._edge.resume()


if __name__ == '__main__':
    unittest.main()
