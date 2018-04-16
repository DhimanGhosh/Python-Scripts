import turtle
import math
tina = turtle.Turtle()
tina.shape("arrow")

l = input()

def sima(x=0):
  length = int(l) + int(x)
  shift = length/10+length/2
  
  tina.penup()
  tina.left(180)
  tina.forward(length*3)
  tina.right(180)
  tina.pendown()
  
  # S
  tina.forward(length)
  tina.left(90)
  tina.forward(length)
  tina.left(90)
  tina.forward(length)
  tina.right(90)
  tina.forward(length)
  tina.right(90)
  tina.forward(length)
  tina.penup()
  tina.forward(shift)
  tina.right(90)
  
  # I
  tina.pendown()
  tina.forward(length*2)
  tina.left(90)
  tina.penup()
  tina.forward(shift)
  tina.left(90)
  
  # M
  tina.pendown()
  tina.forward(length*2)
  tina.right(135)
  tina.forward(length)
  tina.left(90)
  tina.forward(length)
  tina.right(135)
  tina.forward(length*2)
  tina.left(90)
  tina.penup()
  tina.forward(shift)
  tina.left(90)
  
  # A
  tina.pendown()
  tina.forward(length*2)
  tina.right(135)
  slant = length*2*math.sqrt(2)
  tina.forward(slant)
  tina.backward(slant/2)
  tina.right(135)
  tina.forward(slant/3)
  
  # Turle Away From Screen
  tina.penup()
  tina.forward(length*4.5)

sima(l)
