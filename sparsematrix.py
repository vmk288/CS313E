
class Link (object):
  def __init__ (self, col = 0, data = 0, next = None):
    self.col = col
    self.data = data
    self.next = next

  def __str__ (self):
    strng = '(' + str(self.col) + ', ' + str(self.data) + ')'
    return strng

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insertLast (self, col, data):
    newLink = Link (col, data)
    curr = self.first

    if (curr == None):
      self.first = newLink
      return

    while (curr.next != None):
      curr = curr.next

    curr.next = newLink

  def __str__ (self):
    curr = self.first
    strng = str(curr)
    curr = curr.next
    while curr != None:
      strng += ', ' + str(curr)
      curr = curr.next
    return strng

class SparseMatrix (object):
  def __init__ (self, row = 0, col = 0):
    self.row = row
    self.col = col
    self.matrix = []
  
  def setElement (self, row, col, data):
    prev = self.matrix[row].first
    curr = self.matrix[row].first
    
    while curr != None:
      if curr.col == col:
        if data == 0:
          if curr.next == None:
            prev.next == None
          if prev == curr:
            self.matrix[row].first = curr.next
          prev.next = curr.next
          return    
        
        curr.data = data
        return
        
      if curr.col > col:
        if data == 0:
          return

        newLink = Link(col, data)
        prev.next = newLink
        newLink.next = curr
        return
        
      prev = curr
      curr = curr.next 

  def __add__ (self, other):
    if self.row != other.row or self.col != other.col:
      return None
      
    add = SparseMatrix(self.row, self.col)
    for i in range(self.row):
      Row1 = LinkedList()
      for j in range(self.col):
        Row1.insertLast(j, self.getRow(i)[j] + other.getRow(i)[j])
      add.matrix.append(Row1)      
      
    return add

  def __mul__ (self, other):
    if self.col != other.row:
      return None
      
    mult = SparseMatrix(self.row, other.col)
    for i in range(self.row):
      Row1 = LinkedList()
      for j in range(other.col):
        sum = 0
        for k in range(self.col):
          sum += self.getRow(i)[k] * other.getCol(j)[k]
        Row1.insertLast(j, sum)
      mult.matrix.append(Row1)
        
    return mult

  def getRow (self, n):
    curr = self.matrix[n].first
    Row1 = self.col * [0]
    
    while curr != None:
      Row1[curr.col] = curr.data
      curr = curr.next
      
    return Row1

  def getCol (self, n):
    Col1 = self.row * [0]
    for i in range(self.row):
      curr = self.matrix[i].first
      
      while curr != None and curr.col <= n:
        if curr.col == n:
          Col1[i] = curr.data
          break
        else:
          curr = curr.next
          
    return Col1

  def __str__ (self):
    strng = ''
    curr = self.matrix
    if (curr == None):
      return strng

    for i in range(self.row):
      curRow = self.getRow(i)
      strng += str(curRow[0]).rjust(2) 
      for j in range(1, self.col):
        strng += str(curRow[j]).rjust(3) 
      strng += '\n'
    return strng

def readMatrix (inFile):
  line = inFile.readline().rstrip("\n").split()
  row = int (line[0])
  col = int (line[1])
  mat = SparseMatrix (row, col)

  for i in range (row):
    line = inFile.readline().rstrip("\n").split()
    Row1 = LinkedList()
    for j in range (col):
      elt = int(line[j])
      if (elt != 0):
        Row1.insertLast (j, elt)
    mat.matrix.append (Row1)
  line = inFile.readline()

  return mat

def main ():
  inFile = open ("matrix.txt", "r")

  print ("\nTest Matrix Addition")
  matA = readMatrix (inFile)
  print (matA)
  matB = readMatrix (inFile)
  print (matB)

  matC = matA + matB
  print (matC)

  print ("Test Matrix Multiplication")
  matP = readMatrix (inFile)
  print (matP)
  matQ = readMatrix (inFile)
  print (matQ)
  
  matR = matP * matQ
  print (matR)

  print ("Test Setting a Zero Element to a Non-Zero Value")
  matA.setElement (1, 1, 5)
  print (matA)
  
  print("Test Setting a Non-zero element to a Zero value:")
  matA.setElement(0, 0, 0)
  print(matA)

  print ("Test Getting a Row")
  row = matP.getRow(1)
  print (row, '\n')

  print ("Test Getting a Column")
  col = matQ.getCol(0)
  print (col, '\n')

  inFile.close()


main()
