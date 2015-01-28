
# the real device
# from edgell import EdgeRaw

# the fake device
# from edgemock import EdgeMock as EdgeRaw

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
      self._arm = EdgeRaw()



    

