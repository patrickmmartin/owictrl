#! /usr/bin/python

""" test cases for the mini language """

import os
import unittest
import edgelang


class EdgeLangBaseTestCase(unittest.TestCase):
    def setUp(self):
        pass

class EdgeLangSimpleTestCase(EdgeLangBaseTestCase):
    def runTest(self):
        instructions = edgelang.to_ll("M11,M21")


if __name__ == '__main__':
    unittest.main()
