##  JL Cardenas
##  Author jluis.pcardenas@gmail.com
from enviroment import Environment
from procedure import Procedure
from utils import Utils
from parse import Parse
from pair import Pair
from closure import Closure
from installPrim import InstallPrim
import symbols

class Scheme:
  vSymbols = symbols.Symbols()
  
  @staticmethod
  def evaluate(exp, env):
    if Utils.is_atom(exp):
      if (isinstance(exp, str) == False):
        return exp
      #if exp == None or isinstance(exp, str): #constant
      #  return exp
      elif Scheme.vSymbols.get(exp) != None: # symbol
        return Scheme.vSymbols.get(exp)
      else:
        return env.lookup(exp)
    elif isinstance(exp, Pair): # application
      return Scheme.apply(exp.car, exp.cdr, env)
    else:
      raise ValueError("Unknown expression type -- %s." % (exp))

  @staticmethod
  def apply(method, arguments, env):
    if Scheme.vSymbols.get(method) != None and isinstance(Scheme.vSymbols.get(method), Procedure):
      specials = ["if", "define", "cond", "macro", "quote", "lambda"] 
      args = Scheme.va_list(arguments, env, method not in specials)
      
      return Scheme.vSymbols.get(method).invoke(args, env)

    elif isinstance(env.lookup(method), Closure):
      proc = env.lookup(method)
      args = Scheme.va_list(arguments, env, True)
      
      return proc.invoke(args, env)
    else:
      raise ValueError("unknown procedure type -- %s" % (method))

  @staticmethod
  def va_list(args, env, _eval):
    if args == None:
      return []
    
    if _eval:
      car = Scheme.evaluate(args.car, env)
    else:
      car = args.car
    
    lst = []
    lst.append(car)

    cdrs = Scheme.va_list(args.cdr, env, _eval)
    while len(cdrs) > 0:
      o = cdrs.pop(0)
      lst.append(o)

    return lst

  @staticmethod
  def read_input(env):
    exp = ""

    while True:
      prefix = "> "
      if len(exp) > 0:
        prefix = "..."
      
      exp += input(prefix)
 
      lp = exp.count('(')
      rp = exp.count(')')
      qn = exp.count('"')

      if len(exp) == 0:
        print("Empty expression")
      elif lp == rp and (qn % 2) == 0:
        try:
          parsed = Parse.parse(exp)
          
          result = Scheme.evaluate(parsed, env)

          if result != None:
            print(">> " + Utils.stringtify(result) + "\r\n")
        except ValueError as e:
          print(str(e))
        finally:
          exp = ""
  
  @staticmethod
  def main():
    env = Environment([], [], None)

    InstallPrim.install()

    print("Scheme interpreter 0.010 by JLPC")

    Scheme.read_input(env)

    return 1