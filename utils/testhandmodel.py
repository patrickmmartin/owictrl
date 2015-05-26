#! /usr/bin/python

""" test cases for the arm model language """

import unittest
from armmodel import ArmModel
import handmodel

class HandModelBaseTestCase(unittest.TestCase):

    """ base class with setUp """

    def setUp(self):
        """ set up the base class """
        pass


class HandModelConstructTestCase(HandModelBaseTestCase):

    """ test class for constructor """

    def runTest(self):
        """ run the test """
        model = ArmModel()
        moves = handmodel.to_ll(model, model)
        self.assertEqual(moves, {'D' : 0.0} )


class HandModelDeltaTestCase(HandModelBaseTestCase):

    """ test class for constructor """

    def runTest(self):
        """ run the test """
        model = ArmModel()
        modeltarget = ArmModel()
        modeltarget.motors = [15.0, 0.0, 0.0, 0.0, 0.0]
        moves = handmodel.to_ll(model, modeltarget)
        self.assertEqual(moves, {1: {'dir': 1}, 'D' : 0.1} )


class HandModelConvergeTestCase(HandModelBaseTestCase):

    """ test class for constructor """

    def runTest(self):
        """ run the test """
        model = ArmModel()
        modeltarget = ArmModel()
        modeltarget.motors = [15.0, 0.0, 0.0, 0.0, 0.0]

    
if __name__ == '__main__':
    unittest.main()
