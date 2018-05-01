# File: TestLinkedList.py

# Description: To write helper methods for the LinkedList Class

# Student Name: Annie L. Zhang

# Student UT EID: alz373

# Partner's Name: Vaishnavi Kashyap

# Partner's UT EID: vmk288

# Course Name: CS 313E

# Unique Number: 51340

# Date Created: 27 March 2018

# Date Last Modified: 29 March 2018

import random

class Link (object):
  def __init__(self, item, next = None):
    self.item = item
    self.next = next

class LinkedList (object):
  def __init__(self):
    self.first = None
    self.num_Links = 0
  
  # get number of links 
  def get_num_links (self):
    return self.num_Links
  
  # add an item at the beginning of the list
  def insert_first (self, item): 
    if self.num_Links == 0:
      self.first = Link(item)

    else:     
      newLink = Link(item)
      newLink.next = self.first
      self.first = newLink

    self.num_Links += 1 

  # add an item at the end of a list
  def insert_last (self, item): 
    if self.num_Links == 0:
      self.first = Link(item)

    else:  
      current = self.first
      while current.next != None:
        current = current.next
      current.next = Link(item)
    
    self.num_Links += 1 

  # add an item in an ordered list in ascending order
  def insert_in_order (self, item): 
    newLink = Link(item)

    current = self.first

    previous = self.first

    if (current == None) or (current.item >= item):
      newLink.next = self.first
      self.first = newLink
      return

    while (current.next != None):
      if (current.item <= item):
        previous = current
        current = current.next
      
      else:
        newLink.next = previous.next
        previous.next = newLink
        return

    if (current.item <= item):
      current.next = newLink

    else:
      newLink.next = previous.next
      previous.next = newLink

    return

  # search in an unordered list, return None if not found
  def find_unordered (self, item): 
    current = self.first
    if current == None:
        return None
    else:
        while (current.item != item):
            if current.next == None:
                return None
            else:
                current = current.next
        return current

  # Search in an ordered list, return None if not found
  def find_ordered (self, item): 
    current = self.first
    if current == None:
        return None
    else:
        while (current.item != item):
            if current.next == None:
                return None
            else:
                if current.next.item > item:
                    return None 
                else:
                    current = current.next
        return current

  # Delete and return Link from an unordered list or None if not found
  def delete_link (self, item):
    current = self.first
    previous = self.first

    if current == None: 
      return None

    while current.item != item: 
      if current.next == None: 
        return None

      else: 
        previous = current
        current = current.next

    if current == self.first: 
      self.first = self.first.next
    else: 
      previous.next = current.next

    return current.item

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    string = ""
    current = self.first
    counter = 0

    while (current != None):
      string += str(current.item) + "  "
      current = current.next
      counter += 1

      if (counter == 10):
        string += "\n"
        counter = 0 

    return string[0:-2]

  # Copy the contents of a list and return new list
  def copy_list (self):

    newList = LinkedList()
    current = self.first
    while current != None:
      newList.insert_last(current.item)
      current = current.next
    return newList

  # Reverse the contents of a list and return new list
  def reverse_list (self): 
    a = []
    newList = LinkedList()
    current = self.first

    while current != None:
      a.append(current.item)
      current = current.next
    
    a = a[::-1]
    for item in a:
      newList.insert_last(item)

    return newList

  # Sort the contents of a list in ascending order and return new list
  def sort_list (self): 

    a = []
    newList = LinkedList()
    current = self.first
    while current != None:
      a.append(current.item)
      current = current.next
    
    a.sort()
    for item in a:
      newList.insert_last(item)

    return newList


  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    current = self.first
    while current.next != None:
      if current.item > current.next.item:
        return False
      current = current.next
    return True 

  # Return True if a list is empty or False otherwise
  def is_empty (self): 
    return self.num_Links == 0

  # Merge two sorted lists and return new list in ascending order
  def merge_list (self, other): 
    newlist = LinkedList()
    current = self.first
    while (current != None):
      newlist.insert_last(current.item)
      current = current.next

    other_current = other.first
    while (other_current != None):
      newlist.insert_last(other_current.item)
      other_current=other_current.next

    newlist = newlist.sort_list()
    return newlist

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    a = []
    newList = LinkedList()
    current = self.first
    while current.next != None:
      a.append(current.item)
      current = current.next
    
    b = []
    current = other.first
    while current.next != None:
      b.append(current.item)
      current = current.next

    return a == b


  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def remove_duplicates (self):
    newlist = LinkedList()
    counter = 0
    a = set([])
    current = self.first
    size = self.get_num_links()

    if size == 0:
      return None     

    while (current != None):

      a.add(current.item)
      counter += 1

      if len(a) == counter:
        newlist.insert_last(current.item)

      else:
        current = current.next
        counter -= 1

    return newlist
    

def main():

  linkedlist = LinkedList()

  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.

  for i in range (15): 
    a =  random.randint(0, 100)
    linkedlist.insert_first(a)

  print("")
  print("Test Insert_First and __str__()")
  print(linkedlist)

  # Test method insert_last()
  linkedlist = LinkedList()
  for i in range (10): 
    a =  random.randint(0, 100)
    linkedlist.insert_last(a)

  print("")
  print("Test Insert_Last")
  print(linkedlist)

  # Test method insert_in_order()
  linkedlist = LinkedList()
  for i in range (15): 
    a =  random.randint(0, 100)
    linkedlist.insert_in_order(a)

  print("")
  print("Test Insert_In_Order")
  print(linkedlist)

  # Test method get_num_links()
  linkedlist = LinkedList()
  linkedlist.insert_last(2)
  linkedlist.insert_last(1)
  linkedlist.insert_last(3)
  linkedlist.insert_last(5)
  linkedlist.insert_last(4)
  linkedlist.insert_last(6)
  linkedlist.insert_last(7)
  linkedlist.insert_last(9)
  linkedlist.insert_last(8)
  linkedlist.insert_last(10)
  print("")
  print("Test Get_Num_Links")
  print("Number of Links: " + str(linkedlist.get_num_links()))

  # Test method find_unordered() 
  # Consider two cases - item is there, item is not there
  print("")
  print("Test Find_Unordered")

  #If Item is There
  print(linkedlist.find_unordered(11) != None)

  #If Item is Not There
  print(linkedlist.find_unordered(11) == None)

  # Test method find_ordered() 
  # Consider two cases - item is there, item is not there 
  linkedlist = LinkedList()
  linkedlist.insert_last(1)
  linkedlist.insert_last(2)
  linkedlist.insert_last(3)
  linkedlist.insert_last(4)
  linkedlist.insert_last(5)
  linkedlist.insert_last(6)
  linkedlist.insert_last(7)
  linkedlist.insert_last(8)
  linkedlist.insert_last(9)
  linkedlist.insert_last(10)
  print("")
  print("Test Find_Ordered")

  #If Item is There
  print(linkedlist.find_ordered(11) != None)

  #If Item is Not There
  print(linkedlist.find_ordered(11) == None)

  # Test method delete_link()
  # Consider two cases - item is there, item is not there
  print("")
  print("Test Delete_Link")

  #Item present
  print(linkedlist.delete_link(7))

  #Item not present
  print(linkedlist.delete_link(11))
  print("The New Deleted List: " + str(linkedlist))

  # Test method copy_list()
  print("")
  print("Test Copy_List")
  print("Linked List: " + str(linkedlist))
  print("Copied List: " + str(linkedlist.copy_list()))

  # Test method reverse_list()
  print("")
  print("Test Reverse_List")
  print("Linked List: " + str(linkedlist))
  print("Reverse List: " + str(linkedlist.reverse_list()))

  # Test method sort_list()
  linkedlist = LinkedList()
  linkedlist.insert_last(2)
  linkedlist.insert_last(1)
  linkedlist.insert_last(3)
  linkedlist.insert_last(5)
  linkedlist.insert_last(4)
  linkedlist.insert_last(6)
  linkedlist.insert_last(7)
  linkedlist.insert_last(9)
  linkedlist.insert_last(8)
  linkedlist.insert_last(10)
  print("")
  print("Test Sort_List")
  print("Linked List: " + str(linkedlist))
  print("Sorted List: " + str(linkedlist.sort_list()))

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print("")
  print("Test Is_Sort_List")
  print("Sorted?: " + str(linkedlist.sort_list().is_sorted()))
  print("Sorted?: " + str(linkedlist.is_sorted()))

  # Test method is_empty()
  print("")
  print("Test Is_Empty")
  print("Empty?: " + str(linkedlist.is_empty()))
  linkedlist = LinkedList()
  print("Empty?: " + str(linkedlist.is_empty()))

  # Test method merge_list()
  linkedlist1 = LinkedList()
  linkedlist1.insert_last(2)
  linkedlist1.insert_last(5)
  linkedlist1.insert_last(4)
  linkedlist1.insert_last(9)

  linkedlist2 = LinkedList()
  linkedlist2.insert_last(6)
  linkedlist2.insert_last(3)
  linkedlist2.insert_last(7)
  linkedlist2.insert_last(8)
  linkedlist2.insert_last(10)
  print("")
  print("Test Merge_List")
  print(linkedlist1.merge_list(linkedlist2))

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  print("")
  print("Test Is_Equal")
  print(linkedlist1.is_equal(linkedlist2))
  linkedlist2 = LinkedList()
  linkedlist2.insert_last(2)
  linkedlist2.insert_last(5)
  linkedlist2.insert_last(4)
  linkedlist2.insert_last(9)
  print(linkedlist1.is_equal(linkedlist2))

  # Test remove_duplicates()
  print("")
  print("Test Remove_Duplicates")
  linkedlist = LinkedList()
  linkedlist.insert_last(2)
  linkedlist.insert_last(5)
  linkedlist.insert_last(5)
  linkedlist.insert_last(9)
  print(linkedlist)
  print(linkedlist.remove_duplicates())

if __name__ == "__main__":
  main()

