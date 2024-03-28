def hello():
    print("Dis assembler")

#to see how the disassembler works inside python
import dis
dis(hello)

def bar():
  x = 5
  y = 7
  z = x + y
  return z

def main():
  dis.dis(bar) # disassembles `bar`