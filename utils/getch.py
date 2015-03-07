# from recipe in http://code.activestate.com/recipes/134892-getch-like-unbuffered-character-reading-from-stdin/
# there is a lot more in there, but I need to get that Mac to check it

""" module to read chars live  """

class _Getch(object):

    """Gets a single character from standard input.  Does not echo to the
screen."""

    def __init__(self):
        """ ctor """
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self):
        """ returns result from delegate """
        return self.impl()


class _GetchUnix(object):
    """ **nix style implementation """

    def __call__(self):
        """ invocation of this implementation """
        import sys
        import tty
        import termios
        stdin_h = sys.stdin.fileno()
        old_settings = termios.tcgetattr(stdin_h)
        try:
            tty.setraw(stdin_h)
            char = stdin_h.read(1)
        finally:
            termios.tcsetattr(stdin_h, termios.TCSADRAIN, old_settings)
        return char


class _GetchWindows(object):
    """ windows implementation """
    def __init__(self):
        import msvcrt

    def __call__(self):
        """ invocation of this implementation """
        import msvcrt
        return msvcrt.getch()


GETCH = _Getch()
