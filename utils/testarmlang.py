#! /usr/bin/python

""" test cases for the mini language """

import unittest
import edgelang

""" base class with setUp """


class EdgeLangBaseTestCase(unittest.TestCase):

    def setUp(self):
        pass

""" test class with most basic parse test """


class EdgeLangParseTestCase(EdgeLangBaseTestCase):

    def runTest(self):
        edgelang.to_ll("M1+,M2-,D1.0")

""" test for format of returned dict """


class EdgeLangParseTestResultCase(EdgeLangBaseTestCase):

    def runTest(self):
        instructions = edgelang.to_ll("M1+,M2-,D1.0")
        self.assertEqual(
            instructions[0], {'M': {1: {'dir': 1}, 2: {'dir': -1}}, 'D': 1.0})

""" test for invalid """


class EdgeLangParseInvalidTestCase(EdgeLangBaseTestCase):

    @unittest.expectedFailure
    def runTest(self):
        instructions1 = edgelang.to_ll("A1,B2-,C1")

""" test for correct parsing and correct defaults """


class EdgeLangParseDefaultsTestCase(EdgeLangBaseTestCase):

    def runTest(self):
        instructions1 = edgelang.to_ll("M1+,M2-,D1")
        instructions2 = edgelang.to_ll("M1,M2-,D1")
        self.assertEqual(instructions1[0], instructions2[0])

""" test for whitespace handling """


class EdgeLangParseWSpaceDefaultsTestCase(EdgeLangBaseTestCase):

    def runTest(self):
        instructions1 = edgelang.to_ll("M1,M2-,D1")
        instructions2 = edgelang.to_ll(" M1 , M2- , D1 ")
        self.assertEqual(instructions1[0], instructions2[0])

""" test for setting LED """


class EdgeLangParseLEDTestCase(EdgeLangBaseTestCase):

    def runTest(self):
        instructions1 = edgelang.to_ll("L1,D1")
        instructions2 = edgelang.to_ll(" L1 , D1 ")
        self.assertEqual(instructions1[0], instructions2[0])

if __name__ == '__main__':
    unittest.main()
