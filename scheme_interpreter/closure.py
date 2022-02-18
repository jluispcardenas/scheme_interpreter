from .scheme import *
from .enviroment import Environment
from .procedure import Procedure

class Closure (Procedure):
  Instances = 1

  def __init__(self, _args, code, env):
    self.code = code
    self.env = env
    self.args = _args
    self.id = Closure.Instances
    self.memoized = False
    Closure.Instances += 1

  def invoke(self, args, env):
    _vars = scheme.Scheme.va_list(self.args, env, False)

    if len(_vars) == 1 and len(args) > 1:
      args = args[:1]
    elif len(_vars) != len(args):
      raise ValueError("Incorrect number of arguments for closure")

    nenv = Environment(_vars, args, env)
    ret = scheme.Scheme.evaluate(self.code, nenv)
    self.memoized = True

    return rets
