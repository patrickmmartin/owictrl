#! /usr/bin/python

""" test cases for the mini language """

import os
import unittest
import edgelang


class EdgeLangBaseTestCase(unittest.TestCase):
    def setUp(self):
        pass

class EdgeLangParseTestCase(EdgeLangBaseTestCase):
    def runTest(self):
        instructions = edgelang.to_ll("M1+,M2-,D1.0")

class EdgeLangParseTestResultCase(EdgeLangBaseTestCase):
    def runTest(self):
        instructions = edgelang.to_ll("M1+,M2-,D1.0")
        self.assertEqual(instructions[0], {1: {'dir': 1}, 2: {'dir': -1}, 'D': 1.0})

class EdgeLangParseInvalidTestCase(EdgeLangBaseTestCase):
    @unittest.expectedFailure
    def runTest(self):
        instructions1 = edgelang.to_ll("A1,B2-,C1")

class EdgeLangParseDefaultsTestCase(EdgeLangBaseTestCase):
    def runTest(self):
        instructions1 = edgelang.to_ll("M1,M2-,D1")
        instructions2 = edgelang.to_ll("M1,M2-,D1")
        self.assertEqual(instructions1[0], instructions2[0])

class EdgeLangParseWSpaceDefaultsTestCase(EdgeLangBaseTestCase):
    def runTest(self):
        instructions1 = edgelang.to_ll("M1,M2-,D1")
        instructions2 = edgelang.to_ll(" M1 , M2- , D1 ")
        self.assertEqual(instructions1[0], instructions2[0])

class EdgeLangParseLEDTestCase(EdgeLangBaseTestCase):
    def runTest(self):
        instructions1 = edgelang.to_ll("L1,D1")
        instructions2 = edgelang.to_ll(" L1 , D1 ")
        self.assertEqual(instructions1[0], instructions2[0])


if __name__ == '__main__':
    unittest.main()
