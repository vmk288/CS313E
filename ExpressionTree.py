class Stack (object):
  def __init__ (self):
    self.stack = []

  def push (self, item):
    self.stack.append ( item )

  def pop (self):
    return self.stack.pop()

  def peek (self):
    return self.stack[-1]

  def is_empty (self):
    return (len(self.stack) == 0)

  def size (self):
    return (len(self.stack))

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

class Tree (object):
  def __init__ (self):
    self.root = Node(None)

  def createTree (self, expr):
    eq = expr.split()
    parent = Stack()
    current = self.root

    for token in eq:
      if token == '(':
        parent.push(current)
        current.lchild = Node(None)
        current = current.lchild

      elif token in ['+', '-', '*', '/']:
        current.data = token
        parent.push(current)
        current.rchild = Node(None)
        current = current.rchild

      elif token.isdigit() or '.' in token:
        current.data = token
        current = parent.pop()

      elif token == ')':
        if not parent.is_empty():
          current = parent.pop()

        else:
          break

  def evaluate (self, aNode):
    if aNode.data == '+':
      return self.evaluate(aNode.lchild) + self.evaluate(aNode.rchild)

    elif aNode.data == '-':
      return self.evaluate(aNode.lchild) - self.evaluate(aNode.rchild) 

    elif aNode.data == '*':
      return self.evaluate(aNode.lchild) * self.evaluate(aNode.rchild)

    elif aNode.data == '/':
      return self.evaluate(aNode.lchild) / self.evaluate(aNode.rchild)
      
    elif aNode.data.isdigit() or '.' in aNode.data:
      return eval(aNode.data)

  def preOrder (self, aNode):
    if (aNode != None):
      print(aNode.data, end = ' ')
      self.preOrder (aNode.lchild)
      self.preOrder (aNode.rchild)

  def postOrder (self, aNode):
    if (aNode != None):
      self.postOrder (aNode.lchild)
      self.postOrder (aNode.rchild)
      print(aNode.data, end = ' ')

def main():
  inFile = open("expression.txt", "r")
  data = inFile.readline()
  exp_tree = Tree()
  exp_tree.createTree(data)
  print(data, '=', exp_tree.evaluate(exp_tree.root), "\n")
  
  # Print prefix and postfix versions of the expression
  print("Prefix Expression:", end = ' ') 
  exp_tree.preOrder(exp_tree.root)
  print("\n")
  print("Postfix Expression:", end = ' ')
  exp_tree.postOrder(exp_tree.root)
  print()
  
main()
