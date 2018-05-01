#  File: Triangle.py

#  Description: To find the greatest path sum starting at the top of the triangle and moving only to adjacent numbers on the row below using four approaches of problem solving

#  Student's Name: Annie Zhang

#  Student's UT EID: alz373

#  Partner's Name: Vaishnavi Kashyap

#  Partner's UT EID: vmk288

# Course Name: CS 313E

# Unique Number: 51340

#  Date Created: 5 March 2018

#  Date Last Modified: 8 March 2018

# returns the greatest path sum using exhaustive search
import time

def exhaustive_search (grid):
  lines = len(grid)
  sol = 2 ** (lines - 1)
  max = 0

  for i in range(sol):
    sub = int(grid[0][0])
    index = 0 
    for j in range(lines - 1):
      index = index + (i >> j & 1)
      sub = sub + int(grid[j + 1][index])
    if sub > max:
      max = sub
  return max

# returns the greatest path sum using greedy approach
def greedy (grid):
  lines = len(grid)
  temp = 0
  total_sum = 0

  for i in range(lines):
    if len(grid[i]) == 1:
      total_sum = total_sum + int(grid[i][0])
    else: 
      if int(grid[i][temp]) > int(grid[i][temp + 1]):
        total_sum = total_sum + int(grid[i][temp])
        temp = temp
      else:
        total_sum = total_sum + int(grid[i][temp + 1])
        temp = temp + 1

  return total_sum

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid, a = 0, b = 0):
  lines = len(grid)

  if a >= lines:
    return 0

  else:
    down = rec_search(grid, a + 1, b)
    diagonal_down = rec_search(grid, a + 1, b + 1)
    final = max(down, diagonal_down) + int(grid[a][b])
  return final

# returns the greatest path sum using dynamic programming
def dynamic_prog (grid):
  lines = len(grid)

  for i in range(lines - 2, -1, -1):
    for j in range(i + 1):
      grid[i][j] = int(grid[i][j]) + max(int(grid[i+1][j]), int(grid[i+1][j+1]))

  return grid[0][0]

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  file = open ("triangle1.txt", "r")
  lines = file.readline()
  lines = lines.strip()
  lines = int(lines)

  triangle = []

  for i in range(lines):
    line = file.readline()
    line = line.strip()
    line = line.split()
    triangle.append(line)
  return triangle

def main ():
  # read triangular grid from file
  triangular_grid = read_file()

  # output greates path from exhaustive search
  start_time = time.time()
  exhaustive_total = exhaustive_search(triangular_grid)
  time_exhaustive = round((time.time() - start_time) * 1000, 3)
  print()
  print("The greatest path sum through exhaustive search is " + str(exhaustive_total) +  ".")
  print("The time taken for exhaustive search is " + str(time_exhaustive) + " milliseconds.")
  print()

  # output greates path from greedy approach
  start_time = time.time()
  greedy_total = greedy(triangular_grid)
  time_greedy = round((time.time() - start_time) * 1000, 3)
  print("The greatest path sum through greedy search is " + str(greedy_total) +  ".")
  print("The time taken for greedy search is " + str(time_greedy) + " milliseconds.")
  print()

  # output greates path from divide-and-conquer approach
  start_time = time.time()
  recursive_total = rec_search(triangular_grid)
  time_recursive = round((time.time() - start_time) * 1000, 3)
  print("The greatest path sum through recursive search is " + str(recursive_total) +  ".")
  print("The time taken for recursive search is " + str(time_recursive) + " milliseconds.")
  print()

  # output greates path from dynamic programming 
  start_time = time.time()
  dynamic_total = dynamic_prog(triangular_grid)
  time_dynamic = round((time.time() - start_time) * 1000, 3)
  print("The greatest path sum through dynamic programming is " + str(dynamic_total) +  ".")
  print("The time taken for dynamic programming is " + str(time_dynamic) + " milliseconds.")
  print()

if __name__ == "__main__":
    main()
