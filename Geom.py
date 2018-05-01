# File: Geom.py

# Description: To develop several classes fundamental in Geometry. 

# Student Name: Annie L. Zhang

# Student UT EID: alz373

#  Partner's Name: Vaishnavi Kashyap

#  Partner's UT EID: vmk288

# Course Name: CS 313E

# Unique Number: 51340

# Date Created: 31 January 2018

# Date Last Modified: 31 January 2018

import math

class Point (object):
  # constructor 
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  def is_equal (self, other):
    tol = 1.0e-16
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c intersects this circle (non-zero area of overlap)
  def does_intersect (self, c):
    distance = self.center.dist (c.center)
    return distance < (self.radius + c.radius)
   
  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  def circle_circumscribes (self, r):
    x = (r.ul.x + r.lr.x)/2
    y = (r.ul.y + r.lr.y)/2
    center = Point (x, y)
    radius = center.dist(r.ul)

    new_Circle = Circle (radius, x, y)
    return new_Circle


  # string representation of a circle
  def __str__ (self):
    return ('Center: (%.1f, %.1f), Radius: %.1f' %
           (self.center.x, self.center.y, self.radius))
    
  # test for equality of radius
  def is_equal (self, other):
    tol = 1.0e-16
    return ((abs (self.radius - other.radius) < tol))

class Rectangle (object):
  # constructor
    def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point (ul_x, ul_y)
            self.lr = Point (lr_x, lr_y)
        else:
            self.ul = Point (0, 1)
            self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
    def length (self):
        return self.ul.y - self.lr.y

  # determine width of Rectangle (distance along the y axis)
    def width (self):
        return self.lr.x - self.ul.x

  # determine the perimeter
    def perimeter (self):
        return (2 * self.width() + 2 * self.length())
    
  # determine the area
    def area (self):
        return self.width() * self.length()

  # determine if a point is strictly inside the Rectangle
    def point_inside (self, p):
        return p.x > self.ul.x and p.x < self.lr.x and p.y > self.lr.y and p.y < self.ul.y

  # determine if another Rectangle is strictly inside this Rectangle
    def rectangle_inside (self, r):
        if (self.lr.y<r.ul.y<self.ul.y and self.ul.x<r.lr.x<self.lr.x):
            return True
        
  # determine if two Rectangles overlap (non-zero area of overlap)
    def does_intersect (self, other):
        if (other.ul.x > self.lr.x) or (other.lr.x < self.ul.x):
            return False
        elif (other.lr.y > self.ul.y) or (other.ul.y < self.lr.y):
            return False
        else:
            return True

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
    def rect_circumscribe (self, c):
        self.ul.x=c.center.x-c.radius
        self.ul.y=c.center.y+c.radius
        self.lr.x=c.center.x+c.radius
        self.lr.y=c.center.y-c.radius
        smallest_rect=Rectangle(self.ul.x, self.ul.y, self.lr.x, self.lr.y)
        return smallest_rect

  # give string representation of a rectangle
    def __str__ (self):
        return ('UL: (%.1f, %.1f), LR: (%.1f, %.1f)' %
               (self.ul.x, self.ul.y, self.lr.x, self.lr.y))

  # determine if two rectangles have the same length and width
    def is_equal (self, other):
        tol = 1.0e-16
        if (abs(self.length()-other.length())<tol and abs(self.width()-other.width())<tol):
                return True

def main():
  # open the file geom.txt
    file = open("geom.txt",'r')

  # create Point objects P and Q
    p = file.readline().split()
    p1_x= float(p[0])
    p1_y= float(p[1])
    P = Point(p1_x,p1_y)
    q= file.readline().split()
    p2_x= float(q[0])
    p2_y= float(q[1])
    Q = Point(p2_x, p2_y)
  
  # print the coordinates of the points P and Q
    print("Coordinates of P: ", P)
    print("Coordinates of Q: ", Q)

  # find the distance between the points P and Q
    dPQ = round(P.dist(Q), 2)
    print("Distance between P and Q: ", dPQ)
 
  # create two Circle objects C and D
    c = file.readline().split()
    radiusc = float(c[2])
    center_c_x = float(c[0])
    center_c_y = float(c[1])
    circleC = Circle (radiusc, center_c_x, center_c_y)

    d = file.readline().split()
    radiusd = float(d[2])
    center_d_x = float(d[0])
    center_d_y = float(d[1])
    circleD = Circle (radiusd, center_d_x, center_d_y)

  # print C and D
    print("Circle C: ", circleC)
    print("Circle D: ", circleD)

  # compute the circumference of C
    circC = round(circleC.circumference(), 2)
    print("Circumference of C: ", circC)

  # compute the area of D
    areaD = round(circleD.area(), 2)
    print("Area of D: ", areaD)

  # determine if P is strictly inside C
    if circleC.point_inside(P) == True: 
      print("P is inside C.")
    else: 
      print("P is not inside C.")

  # determine if C is strictly inside D
    if circleD.circle_inside(circleC) == True: 
      print("C is inside D.")
    else: 
      print("C is not inside D.")

  # determine if C and D intersect (non zero area of intersection)
    if circleD.does_intersect(circleC) == True: 
      print("C does intersect D.")
    else: 
      print("C does not intersect D.")

  # determine if C and D are equal (have the same radius)
    if circleC.is_equal(circleD) == True: 
      print("C is equal to D.")
    else: 
      print("C is not equal to D.")

  # create two rectangle objects G and H
    g = file.readline().split()
    g_ul_x = float(g[0])
    g_ul_y = float(g[1])
    g_lr_x = float(g[2])
    g_lr_y = float(g[3])
    rectG = Rectangle (g_ul_x, g_ul_y, g_lr_x, g_lr_y)

    h = file.readline().split()
    h_ul_x = float(h[0])
    h_ul_y = float(h[1])
    h_lr_x = float(h[2])
    h_lr_y = float(h[3])
    rectH = Rectangle (h_ul_x, h_ul_y, h_lr_x, h_lr_y)
    

  # print the two rectangles G and H
    print("Rectangle G: ", rectG)
    print("Rectangle H: ", rectH)

  # determine the length of G (distance along x axis)

    lenG = round(rectG.length(), 2)
    print("Length of G: ", lenG)  

  # determine the width of H (distance along y axis)
    widH = round(rectH.width(), 2)
    print("Width of H: ", widH) 

  # determine the perimeter of G
    perG = round(rectG.perimeter(), 2)
    print("Perimeter of G: ", perG) 

  # determine the area of H
    areaH = round(rectH.area(), 2)
    print("Area of H: ", areaH) 

  # determine if point P is strictly inside rectangle G
    if rectG.point_inside(P) == True: 
      print("P is inside G.")
    else: 
      print("P is not inside G.")

  # determine if rectangle G is strictly inside rectangle H
    if rectH.rectangle_inside(rectG) == True: 
      print("G is inside H.")
    else: 
      print("G is not inside H.")

  # determine if rectangles G and H overlap (non-zero area of overlap)
    if rectH.does_intersect(rectG) == True: 
      print("G does overlap H.")
    else: 
      print("G does not overlap H.")

  # find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
    my_Circle = circleC.circle_circumscribes(rectG)
    print("Circle that circumscribes G: ", my_Circle)

  # find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle

    my_Rect = rectG.rect_circumscribe(circleD)
    print("Rectangle that circumscribes D: ", my_Rect)

  # determine if the two rectangles have the same length and width

    if rectG.is_equal(rectH) == True: 
      print("G is equal to H.")
    else: 
      print("G is not equal to H.")

  # close the file geom txt

    file.close()
   

main()





