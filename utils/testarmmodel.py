#! /usr/bin/python

""" test cases for the arm model language """

import unittest
from armmodel import ArmModel


class ArmModelBaseTestCase(unittest.TestCase):

    """ base class with setUp """

    def setUp(self):
        """ set up the base class """
        pass


class ArmModelConstructTestCase(ArmModelBaseTestCase):

    """ test class for constructor """

    def runTest(self):
        """ run the test """
        model = ArmModel()
        self.assertEqual(model.motors, [0.0, 0.0, 0.0, 0.0, 0.0])


class ArmModelMotorsTestCase(ArmModelBaseTestCase):

    """ test class for constructor """

    def runTest(self):
        """ run the test """
        model = ArmModel()
        motors = [1.0, 2.0, 3.0, 4.0, 5.0]
        model.motors = motors
        self.assertEqual(model.motors, motors)
        model.reset()
        self.assertEqual(model.motors, [0.0, 0.0, 0.0, 0.0, 0.0])


if __name__ == '__main__':
    unittest.main()
