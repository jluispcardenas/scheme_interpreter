
class Symbols:
  _table = dict()

  @staticmethod
  def get(k):
    return Symbols._table.get(k, None)

  @staticmethod
  def set(k, v):
    Symbols._table[k] = v
