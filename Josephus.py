
class Link(object):
  def __init__ (self, item, next = None):
    self.item = item
    self.next = next  

class CircularList(object):
  # Constructor
  def __init__ (self):
    self.first = None  

  # Insert an element (value) in the list 
  def insert (self, item):
    new_Link = Link(item, self.first)
    curr = self.first

    if (curr == None):
      self.first = new_Link 
      self.first.next = self.first  
      return 
    while (curr.next != self.first):
      curr = curr.next
    curr.next = new_Link 

  # Find the link with the given key (value)
  def find (self, key):
    curr = self.first

    if (curr.next == None):
      return None 
    while (curr.item != key): #changed data to item 
      curr = curr.next
    return curr 

  # Delete a link with the given key (value)
  def delete (self, key):
    curr = self.first 
    prev = self.first

    while (curr.item != key): #changed data to item 
        prev = curr
        curr = curr.next

    if (curr == self.first):
      self.last_Link() 
      self.first = self.first.next    
    else:
      prev.next = curr.next

    return curr.item # changed data to item   

  # Delete the nth link starting from the Link start
  # Return the next link from the deleted Link 
  def delete_after (self, start, n):
    curr = self.find(start) 
      
    for i in range (0, n-1): 
      curr = curr.next
    
    d = self.delete(curr.item)
    return (d, curr.next.item)    
  
  # Return a string representation of a Circular List
  def __str__ (self):
    string = ''
    curr = self.first.next
    while (curr.next != self.first):
      string += (str(curr.item) + ' ')
      curr = curr.next
    string += (str(curr.data) + ' ')
    return (string)

  # If at last link, have to skip over current_next
  def last_Link(self):  
    curr = self.first
    while(curr.next != self.first):
      curr = curr.next

    curr.next = self.first.next
    return
  
  # Check for whether links were returned properly after deletions
  def size (self):
    counter = 0
    curr = self.first

    while (curr.next != self.first):
      curr = curr.next
      counter += 1 
    return (counter)   


    

def main():

  in_file = open ("josephus.txt", "r")
  
  num_soldiers = in_file.readline()
  num_soldiers = int(num_soldiers.strip())
  begin = in_file.readline()
  begin = int(begin.strip())
  elim = in_file.readline()
  elim = int(elim.strip())
  
  josephus = CircularList() 
  
  for i in range (1, num_soldiers + 1):
    josephus.insert(i)

  string = ''

  for j in range (1, num_soldiers + 1): 
    d, begin = josephus.delete_after(begin, elim)  
    string += (str(d) + ' ') 
  print (string)
main()

