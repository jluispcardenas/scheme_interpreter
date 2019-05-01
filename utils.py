##  JL Cardenas
##  Author jluis.pcardenas@gmail.com
import pair

class Utils:

  def __init__(self):
    pass

  @staticmethod
  def is_atom(o):
    return isinstance(o, pair.Pair) == False
  
  @staticmethod
  def get_type(o):
	  if isinstance(o, pair.Pair):
		  return "pair"
	  elif isinstance(o, str):
		  return "atom"
	  elif isinstance(o, str) and (o == '#f' or o == '#t'):
		  return "boolean"
	  else:
		  return "undefined"    

  @staticmethod
  def stringtify(o):
    if o == None:
      return ""
    elif Utils.is_atom(o):
      return str(o)
    elif isinstance(o, pair.Pair):
      p = o
      res = Utils.stringtify(p.car)
      scdr = Utils.string_content(Utils.stringtify(p.cdr), '(', ')')
      if scdr != "":
        res += ", " + scdr

      return "(" + res + ")"
    else:
      return "undefined?"

  @staticmethod
  def string_content(st, lv, rv):
    if st != "":
      if (st[0] == lv):
        st = st[1:]
      if (st[-1] == rv):
        st = st[:-1]
    return st
