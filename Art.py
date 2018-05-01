#  File: Art.py

#  Description: Create recursive art with turtle graphics

#  Student Name: Vaishnavi Kashyap

#  Student UT EID: vmk288

#  Course Name: CS 313E

#  Unique Number: 51340

#  Date Created: 2/27/2018

#  Date Last Modified: 3/1/2018


import os 
import turtle
import random

# draw a line from (x1, y1) to (x2, y2)
def drawLine (ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

# draw a square 
def drawSquare (ttl, color, xneg, yneg, xpos, ypos):
  ttl.color('black', color)
  ttl.penup()
  ttl.goto(xneg, yneg)
  ttl.begin_fill()
  ttl.pendown()
  ttl.goto(xpos, yneg)
  ttl.goto(xpos, ypos)
  ttl.goto(xneg, ypos)
  ttl.goto(xneg, yneg)
  ttl.end_fill()
  ttl.color('black')

def color (ttl, level, xneg, yneg, xpos, ypos):
  color = random.randint(1, 5)
  if color == 1: 
    color = 'purple'
  elif color == 2:
    color = 'red'
  elif color == 3:
    color = 'yellow'
  elif color == 4:
    color = 'blue' 
  elif color == 5:
    color = 'orange'

  drawSquare(ttl, color, xneg, yneg, xpos, ypos)

def way(ttl, level):
  if level == 1:
    choose = random.randint(1, 2)
    return choose
  else:
    num = random.randint(1, 5)
    if level == 2 and num == 1:
        choose = 3
    elif level == 3 and num == 2:
        choose = 3
    elif level == 4 and num == 3:
        choose = 3
    elif level == 5 and num == 4:
        choose = 3
    elif level == 6 and num == 5:
        choose = 3
    else:
      choose = random.randint(1, 2)
  return choose


def recurse(ttl, level, xneg, xpos, yneg, ypos):
  if level == 0:
    return
  else:
    choose = way(ttl, level)
    if choose == 1:
      if (xpos - (25 // level)) - (xneg + (25 // level)) > 0:
        x = random.randint((xneg + (25 // level)), (xpos - (25 // level)))
      else:
        x = (xneg + xpos) // 2
      drawLine(ttl, x, yneg, x, ypos)

      if level == 1:
        color(ttl, level, x, yneg, xpos, ypos)

      recurse(ttl, level - 1, x, xpos, yneg, ypos)
      recurse(ttl, level - 1, xneg, x, yneg, ypos)

    elif choose == 2:
      if (ypos - (25 // level)) - (yneg + (25 // level)) > 0:
        y = random.randint((yneg + (25 // level)), (ypos - (25 // level)))
      else:
        y = (yneg + ypos) // 2
      drawLine(ttl, xneg, y, xpos, y)

      if level == 1:
        color(ttl, level, xneg, y, xpos, ypos)
      recurse(ttl, level - 1, xneg, xpos, y, ypos)
      recurse(ttl, level -1, xneg, xpos, yneg, y)

    else:
      recurse(ttl, level - 1, xneg, xpos, yneg, ypos)


def main():
  # put label on top of page
  turtle.title ('Recursive Art')

  # setup screen size
  turtle.screensize (800, 800)

  # create a turtle object
  ttl = turtle.Turtle()

  print('Recursive Art')
  level = int(input('Enter a level of recurstion between 1 and 6: '))

  turtle.tracer(10000)

  ttl.pensize (6)
  ttl.color('black')

  recurse(ttl, level, -350, 350, -350, 350)

  ttl.penup()
  ttl.goto(-350, -350)
  ttl.pendown()
  ttl.goto(-350, 350)
  ttl.goto(350, 350)
  ttl.goto(350, -350)
  ttl.goto(-350, -350)
  ttl.penup()

  outName = os.path.basename(__file__)[:-2]+'eps'
  turtScrn = turtle.getscreen()
  turtScrn.getcanvas().postscript(file=outName)


main()
