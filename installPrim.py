##  JL Cardenas
##  Author jluis.pcardenas@gmail.com
from symbols import Symbols
from native import Native

class InstallPrim:

  @staticmethod
  def install():
    Symbols.set("#t", True)
    Symbols.set("#f", False)
    
    Symbols.set("apply", Native("apply", Native.apply, 2))
    Symbols.set("car", Native("car", Native.car, 1))
    Symbols.set("cdr", Native("cdr", Native.cdr, 1))
    Symbols.set("cons", Native("cons", Native.cons, 2))
    Symbols.set("define", Native("define", Native.define, 2))
    Symbols.set("display", Native("display", Native.display, 1))
    Symbols.set("equal?", Native("equal?", Native.equal, 2))
    Symbols.set("if", Native("if", Native._if, 3))
    Symbols.set("lambda", Native("lambda", Native._lambda, 2))
    Symbols.set("length", Native("length", Native.length, 1))
    Symbols.set("list", Native("list", Native.list, -1))
    Symbols.set("list?", Native("list?", Native.islist, 1))
    Symbols.set("load", Native("load", Native.load, 1))
    
    Symbols.set("null?", Native("null?", Native.isnull, 1))
	#Symbols.set("macro", Native("macro", Native.macro, 2)

    Symbols.set("quote", Native("quote", Native.quote, -1))

    Symbols.set("+", Native("+", None, -1))
    Symbols.set("-", Native("-", None, -1))
    Symbols.set("*", Native("*", None, -1))
    Symbols.set("/", Native("/", None, -1))

    Symbols.set(">", Native(">", None, 2))
    Symbols.set("<", Native("<", None, 2))
    Symbols.set(">=", Native(">=", None, 2))
    Symbols.set("<=", Native("<=", None, 2))
    Symbols.set("=", Native("=", None, 2))
