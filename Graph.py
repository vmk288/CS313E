# File: Graph.py

# Description: Creating a graph from an input data file and adding the following functions to the Graph class

# Student Name: Annie L. Zhang

# Student UT EID: alz373

# Partner's Name: Vaishnavi Kashyap

# Partner's UT EID: vmk288

# Course Name: CS 313E

# Unique Number: 51340

# Date Created: 23 April 2018

# Date Last Modified: 25 April 2018

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if a vertex was visited
  def wasVisited (self):
    return self.visited

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

class Edge (object):
  def __init__ (self, fromVertex, toVertex):
    self.u = fromVertex
    self.v = toVertex

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []
    self.Edge = []

  # check if a vertex already exists in the graph
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # given a label get the index of a vertex
  def getIndex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if ((self.Vertices[i]).label == label):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex(label))

      # add a new column in the adjacency matrix for the new Vertex
      nVert = len(self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)
      
      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # do the depth first search in a graph
  def dfs (self, v):
    # create a Stack
    theStack = Stack()

    # mark vertex v as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices [v])
    theStack.push (v)

    # vist other vertices according to depth
    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1): 
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push(u)
    
    # the stack is empty let us reset the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do breadth first search in a graph
  def bfs (self, v):
    # create a Queue
    theQueue = Queue ()

    # mark the vertex as visited and enqueue
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theQueue.enqueue (v)

    while (not theQueue.isEmpty()):
      # get the vertex at the front
      front = theQueue.dequeue()
      # get an adjacent unvisited vertex
      unvisited = self.getAdjUnvisitedVertex (front)
      while (unvisited != -1):
        (self.Vertices[unvisited]).visited = True
        print (self.Vertices[unvisited])
        theQueue.enqueue (unvisited)
        unvisited = self.getAdjUnvisitedVertex (front)

    # the stack is empty let us reset the flags
    nVert = len (self.Vertices)
    for v in range (nVert):
      (self.Vertices[v]).visited = False

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
    v1 = self.getIndex(fromVertexLabel)
    v2 = self.getIndex(toVertexLabel)
    if (self.adjMat[v1][v2] != 0):
      return self.adjMat[v1][v2]
    return -1

  # get a list of immediate neighbors that you can go to from a vertex
  # return empty list if there are none  
  def getNeighbors (self, vertexLabel):
    nList = []
    index = self.getIndex(vertexLabel)
    for i in range(len(self.adjMat[index])):
      if (self.adjMat[index][i] != 0):
        nList.append(self.Vertices[i])
    return nList

  # get a copy of the list of vertices
  def getVertices (self):
    return self.Vertices[:]

  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    begin = self.getIndex(fromVertexLabel)
    end = self.getIndex(toVertexLabel)
    self.adjMat[begin][end] = 0
    self.adjMat[end][begin] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):
    targetIdx = self.getIndex(vertexLabel)

    if targetIdx >= 0:
      for item in self.Vertices:
        if vertexLabel == item.label:
          self.Vertices.remove(item)   

      for i in range(len(self.adjMat)):
        del self.adjMat[i][targetIdx]      
      del self.adjMat[targetIdx]     
    
    else:
      return
    

def main():
  # create a Graph object
  cities = Graph()

  # open file for reading
  inFile = open ("./graph.txt", "r")

  # read the Vertices
  numVertices = int ((inFile.readline()).strip())
  print (numVertices)
  for i in range (numVertices):
    city = (inFile.readline()).strip()
    print (city)
    cities.addVertex (city)

  # read the edges
  numEdges = int ((inFile.readline()).strip())  
  print (numEdges)
  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.addDirectedEdge (start, finish, weight)

  # print the adjacency matrix
  print ("\nAdjacency Matrix")
  for i in range (numVertices):
    for j in range (numVertices):
      print (cities.adjMat[i][j], end = ' ')
    print ()
  print ()

  # read the starting vertex for dfs and bfs
  startVertex = (inFile.readline()).strip()
  print (startVertex)

  # get the index of the start Vertex
  startIndex = cities.getIndex (startVertex)
  print (startIndex)

  # test depth first search
  print ("\nDepth First Search from " + startVertex)
  cities.dfs (startIndex)
  print()

  # test breadth first search
  print ("BFS from " + startVertex + ':')
  cities.bfs (startIndex)
  print()

  # test deletion of an edge

  toandfrom = (inFile.readline()).strip()
  city1 = toandfrom.split(' ', 1)[0]
  city2 = toandfrom.split(' ', 1)[1]
  print("Delete Edge from:", city1, '-', city2)
  print("New Adjacency Matrix after Edge Deletion:")
  cities.deleteEdge(city1, city2)

  # print the adjacency matrix
  nVert = len (cities.adjMat)
  for i in range (nVert):
    for j in range (nVert):
      print (cities.adjMat[i][j], end = " ")
    print()
  print ()

  # test deletion of a vertex
  lastvertex = (inFile.readline()).strip()
  print("\nDelete Vertex: " + str(lastvertex))
  cities.deleteVertex(lastvertex)
  print("\nNew list of cities:")
  for i in cities.Vertices:
    print(i.label)

  # print the adjacency matrix
  print("\nNew Adjacency Matrix after Vertex Deletion:")
  a = len (cities.adjMat)
  for i in range (a):
    for j in range (a):
      print (cities.adjMat[i][j], end = " ")
    print()
  print ()

  # close file
  inFile.close()
   
main()

