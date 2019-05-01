##  JL Cardenas
##  Author jluis.pcardenas@gmail.com
import utils

class Environment:
  def __init__(self, _vars, vals, parent):
    self.table = dict()
  
    if len(_vars) > 0 and len(vals) > 0:
      self.extend(_vars, vals)
    
    self.parent = parent

  def lookup(self, key):
    val = self.table.get(key, None)

    if val == None:
      if self.parent != None:
        return self.parent.lookup(key)
      else:
        raise ValueError("the name '%s' does not exist in the current context" % (key))
    else:
      return val
    	
  def set(self, k, val):
    if isinstance(k, str) == False:
      raise ValueError("Error to set symbol: " % utils.Utils.stringtify(k))
	  
    self.table[k] = val
    
  def extend(self, _vars, vals):
    if (len(_vars) != len(vals)):
      raise ValueError("Incorrect number of values for enviroment")

    for i in range(len(_vars)):
      self.set(_vars[i], vals[i])

    return self.table