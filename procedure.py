##  JL Cardenas
##  Author jluis.pcardenas@gmail.com
import scheme
import enviroment

class Procedure:
  Instances = 1
  
  def __init__(self, _id, code, env):
    self.id = _id
    self.code = code
    self.env = env
    self.memoized = False
    Procedure.Instances += 1

  def invoke(self, args, env):
    _vars = scheme.Scheme.va_list(args, env, False)
    nenv = enviroment.Environment(_vars, args, env)
    ret = scheme.Scheme.evaluate(self.code, nenv)
    self.memoized = True

    return ret