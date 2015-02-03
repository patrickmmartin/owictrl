#! /usr/bin/python

""" test cases for the mini language """

import os
import unittest
import edgelang
import edgell

""" base class with setUp """
class EdgeLangBaseTestCase(unittest.TestCase):
    def setUp(self):
        pass

""" test class with most basic parse test """
class EdgeLangLLTestCase(EdgeLangBaseTestCase):
    def runTest(self):
        instructions = edgelang.to_ll("D1.0")
        bytes = edgell.to_bytes(instructions[0])
        self.assertEqual(bytes, [0, 0, 0]) # TODO(PMM)

""" test for format of returned dict """
class EdgeLangLLTestResultCase(EdgeLangBaseTestCase):
    def runTest(self):
        instructions = edgelang.to_ll("M1+,M2-,D1.0")
        bytes = edgell.to_bytes(instructions[0])        
        self.assertEqual(bytes, [0, 0, 0]) # TODO(PMM)

""" test for setting LED """
class EdgeLangLLLEDTestCase(EdgeLangBaseTestCase):
    def runTest(self):
        instructions = edgelang.to_ll(" L1 , D1 ")
        bytes = edgell.to_bytes(instructions[0])        
        self.assertEqual(bytes, [0, 0, 1])

# TODO(PMM) combinatorial attack on the motors

if __name__ == '__main__':
    unittest.main()
