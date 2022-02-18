
class Lexer:

  @staticmethod
  def tokenize(exp):
    delimiters = [' ', '(', ')', '[', ']', '[', ']', '"', ',', '\'', '`', ';']
    buff = ""
    tokens = []
    opens = 0
    sz = len(exp)

    for i in range(sz):
      c = exp[i]
      if c in delimiters:
        if len(buff) > 0:
          tokens.append(buff)
          buff = ""

        if c != ' ':
          tokens.append(c)

        if c == '(':
          opens += 1
        if c == ')':
          opens -= 1
      else:
        buff += c

    if (opens != 0):
      raise ValueError("Unbalanced parens")

    return tokens
