import random

def main():
  
  # Create three trees - two are the same and the third is different

  # Tree_A, Tree_B are same, Tree_C different
  tree_A = Tree()
  tree_A.insert(11)
  tree_A.insert(7)
  tree_A.insert(77)
  tree_A.insert(15)
  tree_A.insert(87)
  tree_A.insert(92)
  tree_A.insert(1)
  tree_A.insert(93)
  tree_A.insert(45)
  tree_A.insert(37)
  tree_A.insert(12)
  tree_A.insert(99)
  tree_A.insert(4)
  tree_A.insert(10)
  tree_A.insert(51)
  
  tree_B = Tree()
  tree_B.insert(11)
  tree_B.insert(7)
  tree_B.insert(77)
  tree_B.insert(15)
  tree_B.insert(87)
  tree_B.insert(92)
  tree_B.insert(1)
  tree_B.insert(93)
  tree_B.insert(45)
  tree_B.insert(37)
  tree_B.insert(12)
  tree_B.insert(99)
  tree_B.insert(4)
  tree_B.insert(10)
  tree_B.insert(51)
  
  
  tree_C = Tree()
  num_nodes = random.randint(16, 30)
  for i in range(num_nodes):  
    tree_C.insert(random.randint(1,99))
  
  # Test your method is_similar()
  print("\ntree_A and tree_B are similar: ", tree_A.is_similar(tree_B))
  print("tree_B and tree_C are similar: ", tree_B.is_similar(tree_C))
  
  
  # Print the various levels of two of the trees that are different
  print("\nThe levels of tree_A are:")
  for a in range(1, 16):
    tree_A.print_level(a)
    
  print("\nThe levels of tree_C are:")
  for c in range(1,tree_C.get_height()+1):
    tree_C.print_level(c)
    
  # Get the height of the two trees that are different
  print("\nThe height of tree_A is: ", tree_A.get_height())

  # If heights are not diff, adds node to tree C
  while(tree_A.get_height() == tree_C.get_height()): 
      tree_C.insert(random.randint(1,99))

  print("The height of tree_C is: ", tree_C.get_height())
    
  # Get the number of nodes in the left and right subtree
  print("The number of nodes in tree_B is: ", tree_B.num_nodes())
  print("The number of nodes in tree_C is: ", tree_C.num_nodes())

class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # Inserts a node in the tree
  def insert (self, value):
    new_node = Node (value)

    if (self.root == None):
      self.root = new_node
    else:
      curr = self.root
      par = self.root
      while (curr != None):
        par = curr
        if (value < curr.data):
          curr = curr.lChild
        else:
          curr = curr.rChild

      if (value < par.data):
        par.lChild = new_node
      else:
        par.rChild = new_node

   # Returns true if two binary trees are similar
  def is_similar(self, pNode):
    node1 = self.root
    node2 = pNode.root
    return self.compare(node1, node2)
  
  # Helper function for isSimiliar
  def compare(self, node1, node2):
    if node1 == None and node2 == None:
      return True
      
    if node1 == None and node2 != None:
      return False

    elif node1 != None and node2 == None:
      return False

    elif node1.data != node2.data:
      return False

    else:
      return self.compare(node1.lChild, node2.lChild) and self.compare(node1.rChild, node2.rChild)
    
  # Prints out all nodes at the given level
  def print_level(self, level):
    n = []
    self.print_helper(level, 1, n, self.root)
    if len(n) == 0:
      return 
    else:
      print(n)
    
  # print_level helper 
  def print_helper(self, level, curr_level, nodes, first):
    if curr_level > level:
      return
    
    if first == None:
      return

    else:
      if curr_level == level:
        nodes.append(first.data)
      else:
        self.print_helper(level, curr_level + 1, nodes, first.lChild)
        self.print_helper(level, curr_level + 1, nodes, first.rChild)
    

  # Returns the height of the tree
  def get_height(self):
    height = [0]
    self.count(self.root, 0, height)
    height.sort()
    return height[-1]   
    
  # finds length of all paths from root to leaf - helper for get_height
  def count(self, first, size, height):
    if first == None:
      height.append(size)
    else:
      size += 1
      self.count(first.lChild, size, height)
      self.count(first.rChild, size, height)
          
  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root 
  def num_nodes(self):
    nodes = self.count_nodes(self.root)
    return nodes
    
  # counter for number of nodes - helper for num_nodes
  def count_nodes(self, first):
    if first == None:
      return 0
    else:
      return 1 + self.count_nodes(first.lChild) + self.count_nodes(first.rChild)
       
main()
