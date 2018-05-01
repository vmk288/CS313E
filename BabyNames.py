#  File: BabyNames.py 

#  Description: This program stores baby names in a dictionary and outputs information based on menu options 

#  Student Name: Vaishnavi Kashyap

#  Student UT EID: vmk288

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 3/19/2018

#  Date Last Modified: 3/24/2018

import urllib.request

# function to check if name exists in dictionary
def names(name, dict):
  return name in dict
  
# function to return all rankings of a name
def rank(name, dict):
  return dict[name]

# function to return list of all names in a decade 
def all_rank(dict):
  list = []
  for key in dict:
    if 0 not in dict[key]:
      list.append(key)
  list.sort()
  return list

# Returns a list of sorted names that only appear in one decade
def decade_rank(dict, dec):
  list = []
  dec = dec % 1900 // 10
  for key in dict:
    count = 0
    for rank in dict[key]:
      if (rank == 0):
        count += 1
    if (count == 10) and (dict[key][dec] != 0):
      list.append(key)
  list.sort()
  return list

# function to return names of a given rank in a decade
def all_names(dict, decade):
  list = []
  decade = (decade % 1900) // 10
  for name in dict:
    if (dict[name][decade] != 0):
      list.append(name)
  list.sort()
  return list

# function to check if things in list are getting smaller 
def small(a):
  for i in range(len(a)):
    if a[i] == 0:
      a[i] = 1001
  for i in range(1, len(a)):
    if (a[i] >= a[i - 1]):
      return False
  return True

# function to check if things in list are getting larger
def large(a):
  for i in range (len(a)):
    if a[i] == 0:
      a[i] = 1001
  for i in range(1, len(a)):
    if (a[i] <= a[i -1]):
      return False
  return True
  
# function to store popular names (increase in rank)
def popular(dict):
  list = []
  for name in dict:
 
    if small(dict[name]):
      list.append(name)
    
    for i in range(len(dict[name])):
      if (dict[name][i] == 1001):
        dict[name][i] = 0
  list.sort()
  return list
  
# function to store least popular names (decrease in rank)
def least_pop(dict):
  list = []
  for name in dict:
    
    if large(dict[name]):
      list.append(name)
   
    for i in range(len(dict[name])):
      if (dict[name][i] == 1001):
        dict[name][i] = 0
  list.sort()
  return list

# function to return decade of the highest rank for a given name
def high_rank(name, dict):
  highest = 1000
  for rank in dict[name]:
    if (rank < highest) and (rank != 0):
      highest = rank
      index = dict[name].index(rank)
  return 1900 + (index * 10)
      
  
def main():
  '''
  try:
    in_file = urllib.request.urlopen('http://www.cs.utexas.edu/~mitra/csSpring2018/cs313/assgn/names.txt')
    line = str (line, encoding = 'utf8')
  '''
  in_file = open('names.txt', 'r')

  baby_names = {}
  
  for line in in_file:
    name, dec0, dec1, dec2, dec3, dec4, dec5, dec6, dec7, dec8, dec9, dec10 = line.split(' ')
    ranks = [dec0, dec1, dec2, dec3, dec4, dec5, dec6, dec7, dec8, dec9, dec10]
    for i in range(len(ranks)):
      ranks[i] = int(ranks[i])
    baby_names[name] = ranks
  
  in_file.close()

  while True:
    
    print ('Options:')
    print ('Enter 1 to search for names.')
    print ('Enter 2 to display data for one name.')
    print ('Enter 3 to display all names that appear in only one decade.')
    print ('Enter 4 to display all names that appear in all decades.')
    print ('Enter 5 to display all names that are more popular in every decade.')
    print ('Enter 6 to display all names that are less popular in every decade.')
    print ('Enter 7 to quit. \n')
    
    # Option 1
    option = int(input('Enter choice: '))
    if option == 1:
      name = input('Enter a name: ')
      # Output for case where name is not ranked 
      if names(name, baby_names):
        print ('\nThe matches with their highest ranking decade are:')
        print (name, str(high_rank(name, baby_names)))
    
      else:
        print (name, 'does not appear in any decade.')
      print()
    
    # Option 2
    elif option == 2:
      name = input('Enter a name: ')
      if names(name, baby_names):
        ranks = rank(name, baby_names)
        
        print (name + ': ' + ' '.join(str(i) for i in ranks))
        
        index = 0
        for i in range(1900, 2010, 10):
          print (str(i) + ': ' + str(ranks[index]))
          index = index + 1
      else:
        print (name, 'does not appear in any decade.')
      print()
      
    # Option 3      
    elif option == 3:
      dec = int(input('Enter decade: '))
      print('The names are in order of rank:')
      n = decade_rank(baby_names, dec)
      for name in n:
        print (name)
      print()
        
    # Option 4
    elif option == 4:
      n = all_rank(baby_names)
      print(len(n), 'names appear in every decade. The names are:')
      for name in n:
        print (name)
      print()
    
    # Option 5
    elif option == 5:
      n = popular(baby_names)
      print(str(len(n)) + ' names are more popular in every decade.')
      for name in n:
        print (name)
      print()

    # Option 6
    elif option == 6:
      n = least_pop(baby_names)
      print(str(len(n)) + ' names are less popular in every decade.')
      for name in n:
        print (name)
      print()
    
    # Option 7
    elif option == 7:
      print ('\n\nGoodbye.')
      return
main()

