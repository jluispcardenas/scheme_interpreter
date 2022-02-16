from lexer import Lexer
from pair import Pair

class Parse:

  @staticmethod
  def parse(exp):
    tokens = Lexer.tokenize(exp)
    stack = []

    if len(tokens) > 0:
      exp = Parse.sexp(tokens)
      stack.append(exp)
    
    if len(stack) == 1:
      return stack.pop()
    else:
      raise ValueError("Empty stack")

  @staticmethod
  def sexp(tokens):
    o = tokens.pop(0)

    if len(tokens) == 0:
      return None
    elif isinstance(o, str) and o == "\"": #quote
      nx = tokens.pop(0)
      ss = nx
      while len(tokens) > 0 and nx != "\"":
        ss += nx
        nx = tokens.pop(0)
      
      if nx != "\"":
        raise ValueError("Unterminated string constant")
    
      return ss
    elif isinstance(o, str) and o == "(": 
      return Parse.next_list(tokens)
    elif isinstance(o, str) and o == "'": #casiquote
      return Pair("quote", Parse.sexp(tokens))
    else:
      if o.isnumeric() or Parse.is_valid_decimal(o):
        if "." in o:
          return float(o)
        else:
          return int(o)
      
      return o

  @staticmethod
  def is_valid_decimal(s):
    try:
      float(s)
    except ValueError:
      return False
    else:
      return True   

  @staticmethod
  def next_list(tokens):
    cur = Parse.sexp(tokens)
    
    p = None, pt = None
    while len(tokens) > 0 and cur != None and cur != ")":
      if p == None:
        p = Pair(cur, None)
        pt = p
      else:
        pt.cdr = Pair(cur, None)
        pt = pt.cdr
      
      cur = Parse.sexp(tokens)
  
    return p