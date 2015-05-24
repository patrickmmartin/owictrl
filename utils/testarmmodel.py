#! /usr/bin/python

""" test cases for the arm model language """

import unittest
from armmodel import ArmModel, FullInterval


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


class FullIntervalConstructTestCase(ArmModelBaseTestCase):

    """ test class for constructor """

    def runTest(self):
        """ run the test """
        interval = FullInterval()
        self.assertEqual(str(interval), str(FullInterval()))

class FullIntervalJSONTestCase(ArmModelBaseTestCase):

    """ test class for constructor """

    def runTest(self):
        """ run the test """
        interval = FullInterval()
        interval2 = FullInterval()
        self.assertEqual(str(interval), str(interval2))


class ArmModelStringPickleTestCase(ArmModelBaseTestCase):

    """ test class for constructor """

    def runTest(self):
        """ run the test """
        model = ArmModel()
        pickle_json = model.to_json()
        model_new = ArmModel.from_json(pickle_json)
        self.assertEqual(str(model), str(model))

        #try non default objects
        motors = [1.0, 2.0, 3.0, 4.0, 5.0]
        model.motors = motors
        pickle_json = model.to_json()
        model_new = ArmModel.from_json(pickle_json)
        self.assertEqual(str(model), str(model_new))

class ArmModelFilePickleTestCase(ArmModelBaseTestCase):

    """ test class for constructor """

    def runTest(self):
        """ run the test """
        from StringIO import StringIO
        strio = StringIO()
        model = ArmModel()
        model.to_file(strio)

        strio_new = StringIO()
        model.to_file(strio_new)

        self.assertEqual(strio.getvalue(), strio_new.getvalue())

        strio_new.seek(0)
        model_new = ArmModel.from_file(strio_new)
        self.assertEqual(str(model), str(model_new))


if __name__ == '__main__':
    unittest.main()
