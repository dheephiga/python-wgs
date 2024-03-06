import dis
def bar():
  x = 5
  y = 7
  z = x + y
  return z

def main():
  dis.dis(bar) # disassembles `bar`88888