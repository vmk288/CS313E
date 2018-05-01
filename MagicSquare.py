# File: MagicSquare.py

# Description: To construct magic squares by implementing given algorithm

# Student Name: Annie L. Zhang

# Student UT EID: alz373

#  Partner's Name: Vaishnavi Kashyap

#  Partner's UT EID: vmk288

# Course Name: CS 313E

# Unique Number: 51340

# Date Created: 24 January 2018

# Date Last Modified: 24 January 2018

#Define functions for moving along the square.
def move_correct(x,y):
    return x+1, y+1

def move_xout(x,y):
    return x,0

def move_yout(x,y):
    return 0,y

def move_diagout(x,y):
    return x-2,y-1

# Populate a 2-D list with numbers from 1 to n^2
def make_square (n):
  magic_square = []
  for i in range (0, n): 
    a = []
    for j in range (0, n): 
      a.append(0)
    magic_square.append(a)
  
  a = n-1
  b = (n-1)//2

  magic_square[a][b] = 1

# Move according to the above algorithm.
  for move in range (2, n**2 + 1):

  	a, b = move_correct(a,b)

  	try:
  	  if magic_square[a][b] == 0:
  	    magic_square[a][b] = move
  	  else:
  	    a, b = move_diagout(a,b)
  	    magic_square[a][b] = move

# Use Try-Except to bypass IndexError, and return within the array.
  	except:
  	  if a > (n-1) and b <= (n-1) :
  	  	a, b = move_yout(a,b)
  	  	magic_square[a][b] = move
  	  elif a <= (n-1)  and b > (n-1) :
  	  	a, b = move_xout(a,b)
  	  	magic_square[a][b] = move
  	  else:
  	  	a, b = move_diagout(a,b)
  	  	magic_square[a][b] = move	
  	move += 1
  	continue

  return magic_square

# Print the magic square in a neat format where the numbers
# are right justified
def print_square (magic_square):
  return('\n'.join([''.join(['{:5}'.format(num) for num in row]) 
      for row in magic_square]))


# Check that the 2-D list generated is indeed a magic square
def check_square ( magic_square ):
  # sum the first row
  canon_sum = 0
  for j in range (len(magic_square[0])):
    canon_sum += magic_square[0][j]

  # sum each row and comapre with canon_sum
  for i in range (len(magic_square)):
    sum_n = 0
    for j in range (len(magic_square[i])):
      sum_n += magic_square[i][j]
    if (sum_n != canon_sum):
      return False

  # sum each column and compare with canon_sum
  for j in range (len (magic_square[0])):
    sum_n = 0
    for i in range (len(magic_square)):
      sum_n += magic_square[i][j]
    if (sum_n != canon_sum):
      return False

  # sum the diagonal going left to right
  sum_lr = 0
  for i in range (len(magic_square)):
    sum_lr += magic_square[i][i]
  if (sum_lr != canon_sum):
    return False

  # sum the diagonal going right to left
  sum_rl = 0
  for i in range (len(magic_square)):
    sum_rl += magic_square[i][len(magic_square) - 1 - i]
  if (sum_rl != canon_sum):
    return False

  return canon_sum



def main():
# Prompt the user to enter an odd number 3 or greater
  print("")
  n = int(input("Please enter an odd number 3 or greater: "))

  # Check the user input
  while (n < 3) or (n %2 == 0): 
    n = int(input("Please enter an odd number 3 or greater: "))

  # Create the magic square
  magic_square = make_square(n)
  
  # Print the magic square
  print("")
  print("Here is a " + str(n) + "x" + str(n) + " magic square: ")
  print("")
  a = print_square(magic_square)
  print(a)


  # Verify that it is a magic square
  if check_square(magic_square) == int(n*(n**2 + 1)/ 2):
  	print("")
  	print("Sum of row = ", int(n*(n**2 + 1)/ 2))
  	print("Sum of column = ", int(n*(n**2 + 1)/ 2))
  	print("Sum of diagonal (UL to LR) = ", int(n*(n**2 + 1)/ 2))
  	print("Sum of diagonal (UR to LL) = ", int(n*(n**2 + 1)/ 2))
  else:
  	print("This is not a Magic Square.")


main()



