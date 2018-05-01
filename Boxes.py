#  File: Boxes.py

#  Description: To output the largest subset of boxes that nest inside each other starting with the inner most box to the outer most box.

# Student Name: Annie L. Zhang

# Student UT EID: alz373

#  Partner's Name: Vaishnavi Kashyap

#  Partner's UT EID: vmk288

# Course Name: CS 313E

# Unique Number: 51340

# Date Created: 19 February 2018

# Date Last Modified: 21 February 2018


# Determine if box1 can fit into box2
def does_fit(box1, box2):
  return box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]

def fits_all(sub):
  for i in range(0, len(sub) -1):
    if not does_fit(sub[i], sub[i + 1]):
      return False
  return True
  
# Recursion based from given subset code
def subsets (a, b, lo, nest):
  hi = len(a)
  if (lo == hi):
    if fits_all(b):
      nest.append(b)
      return
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, c, lo + 1, nest)
    subsets (a, b, lo + 1, nest)

def main():
  
# Opens boxes.txt file for reading
  in_file = open ('boxes.txt', 'r')

# Read number of boxes
  line = in_file.readline()
  line = line.strip()
  num_boxes = int(line)
  
# Append all boxes to list
  tot_boxes = []
 
 # Create empty list of boxes
  box_list = [] 
  
# Read list of boxes from file
  for i in range (num_boxes):
    line = in_file.readline()
    line = line.strip()
    a, b, c = line.split(" ")
    a, b, c = int(a), int(b), int(c)
    box_dim = [a, b, c]
    box_dim.sort()
    box_list.append(box_dim)

# Close File
  in_file.close()
  
# Sorts boxes
  box_list.sort()

# Empty list to satisfy parameter in of subsets function
  b = []
  subsets(box_list, b, 0, tot_boxes)
  
# Initialize counter
  counter = 2

# Determines maximum size
  for i in tot_boxes:
  	if len(i) > counter:
  	  counter = len(i)

# If not maximum size, get rid of
  no = []
  for i in range(0, len(tot_boxes)):
  	if len(tot_boxes[i]) != counter:
  		no.append(tot_boxes[i])

# Remove subsets that don't nest
  for j in no:
  	tot_boxes.remove(j)
  
# Sort list
  tot_boxes.sort()
  
# Format
  print ("Largest Subset of Nesting Boxes")
  for k in tot_boxes:
    for box in k:
      print (box)
    print('')
      
main()
