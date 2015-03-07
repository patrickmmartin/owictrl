""" high level device for the Edge  """

from logutil import LOGGER_DEFAULT as logger


# the language
import edgelang

# the real device
from edgell import EdgeRaw

# the fake device
#from edgemock import EdgeMock as EdgeRaw


class Edge(object):

    """High level driver for the OWI Edge"""

    def __init__(self):
        """ sets up class; initialises """
        self._moves = list()
        self._move_index = 0
        self._paused = False
        self._arm = EdgeRaw()

    def add_moves(self, moves):
        """ add the moves """
        self._moves.append(moves)

    def clear_moves(self):
        """ clear the moves """
        self._moves = list()

    def stop(self):
        """  stop """
        self._arm.stop()

    def start(self):
        """ start from the currently defined actions """
        self._move_index = 0
        self.resume()

    def move(self):
        """ the main loop for moving the arm """
        logger.info('move starting')
        while not self._paused and (self._move_index < len(self._moves)):
            move = self._moves[self._move_index]
            instructions = edgelang.to_ll(move)
            logger.info('move %s %s', move, instructions)
            for instruction in instructions:
                logger.info('move %s', instruction)
                self._arm.drive(instruction)
            self._move_index += 1
            logger.info("finished")
        self.stop()

    def pause(self):
        """ pause the moves  """
        # flag paused
        self._paused = True

    def resume(self):
        """ resume the motion """
        self._paused = False
        if len(self._moves) > 0:
            self.move()
