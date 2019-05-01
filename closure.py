##  JL Cardenas
##  Author jluis.pcardenas@gmail.com
import scheme
import enviroment
import procedure

class Closure (procedure.Procedure):
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

    if len(_vars) != len(args):
      raise ValueError("Incorrect number of arguments for closure")

    nenv = enviroment.Environment(_vars, args, env)
    ret = scheme.Scheme.evaluate(self.code, nenv)
    self.memoized = True
    
    return ret