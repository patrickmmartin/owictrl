"""
   code to model mapping Leap hand objects to robot arms
"""

from  armmodel import ArmModel

def to_arm(hand):
    """
    maps the hand instance to an ArmModel
    """
    # TODO(PMM) map hand properties

    return ArmModel()


def to_ll(target, current):
    """

    generates a set of motor moves from the current ArmModel
    moving to the target ArmModel
    """

    #TODO(PMM) generate binary moves (with small dead zone) for model diffs
    ret = {'D': 0.0}
    for i in range(0, 5):
        if abs(target.motors[i] - current.motors[i]) > 1:
            ret['D'] = 0.1
            ret[i + 1] = {'dir' : 1 if abs(target.motors[i] - current.motors[i]) > 0 else -1}

#    example return {1: {'dir': 1}, 2: {'dir': -1}, 'D': 0.1}
    return ret

