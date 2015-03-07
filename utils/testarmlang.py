#! /usr/bin/python

""" test cases for the mini language """

import unittest
import edgelang




class EdgeLangBaseTestCase(unittest.TestCase):
    """ base class with setUp """
    def setUp(self):
        """ set up the base class """
        pass


class EdgeLangParseTestCase(EdgeLangBaseTestCase):
    """ test class with most basic parse test """
    def runTest(self):
        """ run the test """
        edgelang.to_ll("M1+,M2-,D1.0")



class EdgeLangParseTestResultCase(EdgeLangBaseTestCase):
    """ test for format of returned dict """
    def runTest(self):
        """ run the test """
        instructions = edgelang.to_ll("M1+,M2-,D1.0")
        self.assertEqual(
            instructions[0], {'M': {1: {'dir': 1}, 2: {'dir': -1}}, 'D': 1.0})




class EdgeLangParseInvalidTestCase(EdgeLangBaseTestCase):
    """ test for invalid """
    @unittest.expectedFailure
    def runTest(self):
        """ run the test """
        edgelang.to_ll("A1,B2-,C1")




class EdgeLangParseDefaultsTestCase(EdgeLangBaseTestCase):
    """ test for correct parsing and correct defaults """
    def runTest(self):
        """ run the test """
        instructions1 = edgelang.to_ll("M1+,M2-,D1")
        instructions2 = edgelang.to_ll("M1,M2-,D1")
        self.assertEqual(instructions1[0], instructions2[0])




class EdgeLangParseWSpaceDefaultsTestCase(EdgeLangBaseTestCase):
    """ test for whitespace handling """
    def runTest(self):
        """ run the test """
        instructions1 = edgelang.to_ll("M1,M2-,D1")
        instructions2 = edgelang.to_ll(" M1 , M2- , D1 ")
        self.assertEqual(instructions1[0], instructions2[0])




class EdgeLangParseLEDTestCase(EdgeLangBaseTestCase):
    """ test for setting LED """
    def runTest(self):
        """ run the test """
        instructions1 = edgelang.to_ll("L1,D1")
        instructions2 = edgelang.to_ll(" L1 , D1 ")
        self.assertEqual(instructions1[0], instructions2[0])

if __name__ == '__main__':
    unittest.main()
