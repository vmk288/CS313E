class Matrix (object):
  def __init__ (self, row = 0, col = 0):
    self.matrix = []
    self.row = row
    self.col = col

  # performs matrix addition
  def __add__ (self, other):
    if (self.row != other.row) or (self.col != other.col):
      return None

    new_matrix = Matrix (self.row, self.col)

    for i in range (self.row):
      new_row = []
      for j in range (self.col):
        new_row.append (self.matrix[i][j] + other.matrix[i][j])
      new_matrix.matrix.append (new_row)

    return new_matrix

  # performs matrix multiplication
  def __mul__ (self, other):
    if (self.col != other.row):
      return None

    mat = Matrix (self.row, other.col)

    for i in range (self.row):
      new_row = []
      for j in range (other.col):
        sum_n = 0
        for k in range (other.row):
          sum_n += self.matrix[i][k] * other.matrix[k][j]
        new_row.append (sum_n)
      mat.matrix.append (new_row)

    return mat

  # returns the a string representation of a matrix
  def __str__ (self):
    s = ''
    for i in range (self.row):
      for j in range (self.col):
        s = s + str(self.matrix[i][j]).rjust(3, ' ') + " "
      s = s + "\n"
    return s

def readMatrix (inFile):
  line = inFile.readline ()
  line = line.strip()
  line = line.split()
  row = int (line[0])
  col = int (line[1])

  mat = Matrix (row, col)

  for i in range (row):
    line = inFile.readline ()
    line = line.strip()
    line = line.split()
    for j in range (col):
      line[j] = int (line[j])
    mat.matrix.append(line)

  # do a dummy read
  line = inFile.readline()

  return mat

def main():
  # open file for reading
  inFile = open ("matrix.txt", "r")

  print ("\nTest Matrix Addition")
  # populate the matrices
  matA = readMatrix (inFile)
  print (matA)
  matB = readMatrix (inFile)
  print (matB)

  # add the two matrices
  matC = matA + matB
  print (matC)

  print ("\nTest Matrix Multiplication")
  # populate the matrices
  matP = readMatrix (inFile)
  print (matP)
  matQ = readMatrix (inFile)
  print (matQ)

  # multiply the matrices
  matR = matP * matQ
  print (matR)

  # close the file
  inFile.close()

main()

