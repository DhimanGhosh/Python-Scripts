import turtle
import math
tina = turtle.Turtle()
tina.shape("arrow")

origin=[0,0]

def draw_star(l,shift):
  tina.forward(l)
  goto([origin[0]+shift,origin[1]])
  tina.right(15)

def draw_rect(l,b):
  tina.forward(b)
  tina.right(90)
  tina.forward(l)
  tina.right(90)

def penup():
  tina.penup()

def pendown():
  tina.pendown()

def goto(list1):
  tina.goto(list1[0],list1[1])

# Main
def main():
  screen_shift=20
  s=20
  l=int(s)*5-screen_shift
  b=(int(s)*3)/2-5
  
  penup()
  flag_top_left = [origin[0]-l*2+screen_shift, origin[1]+b*2]
  
  # Flag Mid
  goto(flag_top_left)
  tina.color('#FFF')
  tina.begin_fill()
  pendown()
  for _ in range(2):
    draw_rect(b*4,l*4)
  tina.end_fill()
  penup()
  
  # Flag Circle
  goto([origin[0]+screen_shift,origin[1]])
  pendown()
  tina.color('#000080')
  for _ in range(24):
    draw_star(s,screen_shift)
  goto([origin[0]+screen_shift,origin[1]-int(s)])
  tina.circle(s)
  penup()
  
  # Flag Bottom
  goto([flag_top_left[0],flag_top_left[1]-b*4])
  tina.color('#138808')
  tina.begin_fill()
  pendown()
  for _ in range(2):
    draw_rect(b*4,l*4)
  tina.end_fill()
  penup()
  
  # Flag Top
  goto([flag_top_left[0],flag_top_left[1]+b*4])
  tina.color('#FF9933')
  tina.begin_fill()
  pendown()
  for _ in range(2):
    draw_rect(b*4,l*4)
  tina.end_fill()
  penup()
  
  # Stand
  goto([flag_top_left[0]-2,flag_top_left[1]+b*4])
  tina.color('#A52A2A')
  tina.begin_fill()
  pendown()
  for _ in range(2):
    draw_rect(b*20,2)
  tina.end_fill()
  penup()
  
main()
