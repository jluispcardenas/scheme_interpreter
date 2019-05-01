##  JL Cardenas
##  Author jluis.pcardenas@gmail.com
import scheme
import procedure
import pair
import closure
import utils

class Native (procedure.Procedure):

  def __init__(self, id, proc, min, max = -1):
    self.id = id
    self.proc = proc
    self.min = min
    self.max = max
    
  def to_string(self):
    return "#<procedure-%s>" % (self.id)
   
  def invoke(self, args, env):
    if self.min != -1 and (self.max == -1 and len(args) != self.min):
      raise ValueError("error in %s: incorrect number of arguments to procedure." % (self.id))

    if self.proc == None:
      return Native.binary_op(self.id, args, env)

    return self.proc(args, env)

  @staticmethod
  def check_argument_type(m, cl, arg0):
    if isinstance(arg0, cl) == False:
        raise ValueError("error in '%s': expected type '%s', got '%s'" % (m, cl, arg0))

  @staticmethod
  def apply(args, env):
    proc = Native.ARG(args)
    Native.check_argument_type("apply", procedure.Procedure, proc) 
	  
    arg0 = Native.ARG(args)
    Native.check_argument_type("apply", pair.Pair, arg0) 
    
    nargs = scheme.Scheme.va_list(arg0, env, False)

    return proc.invoke(nargs, env)

  @staticmethod
  def ARG(v):
    return v.pop(0)

  @staticmethod
  def car(args, env):
    val = args.pop(0)
    if isinstance(val, pair.Pair) == False:
      raise ValueError("error in car: expected type pair, got '%s'." % (utils.Utils.get_type(val)))
	
    return val.car

  @staticmethod
  def cdr(args, env):
    val = args.pop(0)
    Native.check_argument_type("cdr", pair.Pair, val)
  
    return val.cdr

  @staticmethod
  def cons(args, env):
	  arg0 = Native.ARG(args)
	  arg1 = Native.ARG(args)

	  return pair.Pair(arg0, arg1)

  @staticmethod
  def define(args, env):
    arg0 = Native.ARG(args)
    arg1 = Native.ARG(args)
    
    if isinstance(arg0, str):
      name = arg0
      env.set(name, scheme.Scheme.evaluate(arg1, env))
      return name
    elif isinstance(arg0, pair.Pair):
      name = arg0.car
      lst = [arg0.cdr, arg1]
      env.set(name, Native.call_native("lambda", lst, env))
      return name
    else:
      raise ValueError("error in define: ll-formed special form")

  @staticmethod
  def display(args, env):
    print(utils.Utils.stringtify(args))
    return None

  @staticmethod
  def call_native(method, v, env):
    return scheme.Scheme.vSymbols.get(method).invoke(v, env)

  @staticmethod
  def equal(args, env):
    arg0 = Native.ARG(args)
    arg1 = Native.ARG(args)
  
    if utils.Utils.get_type(arg0) != utils.Utils.get_type(arg1):
      return False
    elif isinstance(arg0, pair.Pair):
      la1 = [arg0]
      la2 = [arg1]

      l =  Native.call_native("length", la1, env)
      l2 = Native.call_native("length", la2, env)

      if l == l2:
        t = arg0
        t2 = arg1
        while t != None and t.car != None:
          la = [t.car, t2.car]
          if Native.call_native("equal?", la, env) == False:
            return False
          t = t.cdr
          t2 = t2.cdr
        
        return True
      else:
        return False
    else:
      return arg0 == arg1
  
    return False

  @staticmethod
  def _if(args, env):
    
    predicate = Native.ARG(args)
    proc1 = Native.ARG(args)
    proc2 = Native.ARG(args)
    
    ret = scheme.Scheme.evaluate(predicate, env)
    
    if ret:
      return scheme.Scheme.evaluate(proc1, env)
    else:
      return scheme.Scheme.evaluate(proc2, env)

  @staticmethod
  def _lambda(args, env):
    arg0 = Native.ARG(args)
    arg1 = Native.ARG(args)
  
    return closure.Closure(arg0, arg1, env)

  @staticmethod
  def load(args, env):
    val = args.pop(0)
    Native.check_argument_type("load", str, val)
    
    path = val
    try:
      with open(path) as f:
        pass
        #Scheme.read_input(f, None, env)
    except:
      raise ValueError("unable to open file %s" % (val))
      
    return None

  @staticmethod
  def length(args, env):
    val = args.pop(0)
    Native.check_argument_type("length", pair.Pair, val)
    
    p = val
    len = 0
    while isinstance(p, pair.Pair) and p.car != None:
      len += 1
      p = p.cdr
      
    return len

  @staticmethod
  def list(args, env):
    p = None
    pt = None
    while len(args) > 0:
      o = Native.ARG(args)
      if p == None:
        p = pair.Pair(o, None)
        pt = p
      else:
        pt.cdr = pair.Pair(o, None)
        pt = pt.cdr
    
    return p

  @staticmethod
  def islist(args, env):
	  return isinstance(args.pop(0), pair.Pair)

  @staticmethod
  def isnull(args, env):
    arg0 = Native.ARG(args)
    if arg0 == None or isinstance(arg0, pair.Pair) and arg0.car == None:
      return True
      
    return False

  @staticmethod
  def quote(args, env):
    return scheme.Scheme.vSymbols.get("list").invoke(args, env)

  @staticmethod
  def binary_op(op, args, env):
    if op[0] == '<' and op[0] == '>' and op[1] == '=':
      n1 = args.pop(0)
      n2 = args.pop(0)
      
      if op == ">":
        return n1 > n2
      elif op == "<":
        return n1 < n2
      elif op == ">=":
        return n1 >= n2
      elif op == "<=":
        return n1 <= n2
      else:
        return n1 == n2
    else:
      n1 = args.pop(0)
      while len(args) > 0:
        n = args.pop(0)

        if op == "+":
          n1 = n1 + n
        elif op == "-":
          n1 = n1 - n
        elif op == "*":
          n1 = n1 * n
        elif op == "/":
          n1 = n1 / n
    
    return n1