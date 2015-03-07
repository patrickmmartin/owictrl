# the real device

from logutil import logger

""" high level """

# the language
import edgelang

# the real device
from edgell import EdgeRaw

# the fake device
#from edgemock import EdgeMock as EdgeRaw

"""High level driver for the OWI Edge"""


class Edge:

    # TODO needs to have a concept of the current status
    # TODO needs to have a concept of current move plan
    # TODO needs to handle light status appropriately
    # TODO needs to deliver the requested angular change
    # should handle 100% motor moves
    # could handle partial power moves through time slicing

    """ sets up class; initialises   """

    def __init__(self):
        # initialise essentials
        self._moves = list()
        self._moveIndex = 0
        self._paused = False
        self._arm = EdgeRaw()

    """ add the moves """

    def addMoves(self, moves):
        # store moves
        self._moves.append(moves)

    """ clear the moves """

    def clearMoves(self):
        # clear the moves list
        self._moves = list()

    """  stop """

    def stop(self):
        # stop the arm
        self._arm.stop()

    """ start from the currently defined actions """

    def start(self):
        self._moveIndex = 0
        self.resume()

    """ the main loop for moving the arm """

    def move(self):
        # move while actions remain and not paused
        logger.info('move starting')
        while (not self._paused and (self._moveIndex < len(self._moves))):
            move = self._moves[self._moveIndex]
            instructions = edgelang.to_ll(move)
            logger.info('move {0} {1}'.format(move, instructions))
            for instruction in instructions:
                logger.info('move {0}'.format(instruction))
                self._arm.drive(instruction)
            self._moveIndex += 1
            logger.info("finished")
        self.stop()

    """ pause the moves  """

    def pause(self):
        # flag paused
        self._paused = True

    """ resume the motion """

    def resume(self):
        self._paused = False
        if (len(self._moves) > 0):
            self.move()
