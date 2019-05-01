##  JL Cardenas
##  Author jluis.pcardenas@gmail.com
import symbols
from native import Native

class InstallPrim:

  @staticmethod
  def install():
    symbols.Symbols.set("#t", True)
    symbols.Symbols.set("#f", False)
    
    symbols.Symbols.set("apply", Native("apply", Native.apply, 2))
    symbols.Symbols.set("car", Native("car", Native.car, 1))
    symbols.Symbols.set("cdr", Native("cdr", Native.cdr, 1))
    symbols.Symbols.set("cons", Native("cons", Native.cons, 2))
    symbols.Symbols.set("define", Native("define", Native.define, 2))
    symbols.Symbols.set("display", Native("display", Native.display, 1))
    symbols.Symbols.set("equal?", Native("equal?", Native.equal, 2))
    symbols.Symbols.set("if", Native("if", Native._if, 3))
    symbols.Symbols.set("lambda", Native("lambda", Native._lambda, 2))
    symbols.Symbols.set("length", Native("length", Native.length, 1))
    symbols.Symbols.set("list", Native("list", Native.list, -1))
    symbols.Symbols.set("list?", Native("list?", Native.islist, 1))
    symbols.Symbols.set("load", Native("load", Native.load, 1))
    
    symbols.Symbols.set("null?", Native("null?", Native.isnull, 1))
	#symbols.Symbols.set("macro", Native("macro", Native.macro, 2)

    symbols.Symbols.set("quote", Native("quote", Native.quote, -1))

    symbols.Symbols.set("+", Native("+", None, -1))
    symbols.Symbols.set("-", Native("-", None, -1))
    symbols.Symbols.set("*", Native("*", None, -1))
    symbols.Symbols.set("/", Native("/", None, -1))

    symbols.Symbols.set(">", Native(">", None, 2))
    symbols.Symbols.set("<", Native("<", None, 2))
    symbols.Symbols.set(">=", Native(">=", None, 2))
    symbols.Symbols.set("<=", Native("<=", None, 2))
    symbols.Symbols.set("=", Native("=", None, 2))
