
"""
  class to model the robot arm's position and constraints
"""


class FullInterval(object):

    """
    class to represent constraints on motor moves
    """

    def __init__(self, _start, _end):
        """
        constructor
        """
        if not _start is None:
            self.start = _start
        if not _end is None:
            self.end = _end

    def __div__(self, other):
        """
        implement override for division
        """
        return FullInterval(self.start / other, self.end / other)

    def __repr__(self):
        return "%f, %f" % (self.start, self.end)


class ArmModel(object):

    """
    class to model the presumed position of the OWI edge arm
    """

    constraints = [FullInterval(-135.0, 135.0),
                   FullInterval(-90.0, 90.0),
                   FullInterval(-135.0, 135.0),
                   FullInterval(-60.0, 60.0),
                   FullInterval(-18.0, 18.0)]
    """
      basic constraints
    from basic timings - speeds and ranges
    Base - 270 degrees - 21 seconds for full traverse
    Shoulder - 180 degress or so, but only about 90 usable - 13 seconds
    Elbow" - just under 270 degrees - 18 seconds
    Wrist" - about 120 degrees - 10 seconds
    Grabber - N/A 1.5 seconds to open / close
    """

    traverse_times = [constraints[i] / 12 for i in range(5)]
    """
    estimated traverse times
    """

    def reset(self):
        """
        default initialise the arm data
        """
        self.motors = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.light = False

    def __init__(self, _motors=None, _light=None):
        # initialise the motor positions (degrees)
        self.reset()
        if not _motors is None:
            self.motors = _motors
        if not _light is None:
            self.light = _light

    def applyconstraints(self):
        """
        apply basic contraints
        """
        # TODO(PMM) implement
        pass

    def move(self):
        """
        simulate a moves of the arm
        """
        # TODO(PMM) implement
        pass
