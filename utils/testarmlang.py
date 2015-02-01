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

if __name__ == '__main__':
    unittest.main()
