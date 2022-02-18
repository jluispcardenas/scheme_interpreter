from .utils import *

class Pair:
    def __init__(self, car, cdr):
	    self.car = car
	    self.cdr = cdr

    def to_string(self):
      utils.Utils.stringtify(self)
